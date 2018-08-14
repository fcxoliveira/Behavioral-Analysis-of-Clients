import sys
import paho.mqtt.client as mqtt
import json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from mqtt import MQTTUtils
from libSpark import *
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: mqtt_wordcount.py <broker url> <topic>"
        exit(-1)

    sc = SparkContext(appName="PythonStreamingMQTTWordCount")
    ssc = StreamingContext(sc, 30)
    def on_log(client, userdata, level, buf):
        print("log: " + buf)
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conexao Boa")
        else:
            print("Conexao Ruim")
    def on_disconnect(client, userdata, flags, rc=0):
        print("Desconectado por " + str(rc))
    def on_message(client, userdata, msg):
        topic = msg.topic
        m_decode = str(msg.payload.decode("utf-8", "ignored"))
        print("Messagem recebida" + m_decode)
    host = "172.16.206.29"
    port = 1883
    topicTh = "v1/devices/me/telemetry"
    username = "oPTXx7haUuv1vwJKnXWN"
    password = ""
    client = mqtt.Client("Gerente")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_log = on_log
    if (username != ""):
        client.username_pw_set(username, password)
    print("Conectando ao host: ", host)
    client.connect(host, port)
    def sendData(tupla):
        chave = str(tupla[0])
        valor = str(tupla[1])
        data = {}
        data[chave] = valor
        data_out = json.dumps(data)
        return "OK"

    brokerUrl = "tcp://localhost:1883"
    topic = "coleta"

    lines = MQTTUtils.createStream(ssc, brokerUrl, topic)
    #lines.split(" ")[6].pprint()
    linhas = lines.flatMap(lambda line: line.split("\n"))\
                .map(getLine)\
                .reduceByKey(lambda a, b: getAppend(a, b))

    result = linhas.map(getOrganize)
    result.pprint()
    resutArv = result.map(getResultTree)
    resutArv.pprint()
    def extract(rdd):
        c = rdd.collect()
        for record in c:
            data = {}
            key = str(record[0])
            value = str(record[1])
            data[key] = value
            print(data)
            data_out = json.dumps(data)
            client.publish("v1/devices/me/telemetry",data_out, 0)
    consult = resutArv.foreachRDD(extract)
    (extract)
    ssc.start()
    ssc.awaitTermination()