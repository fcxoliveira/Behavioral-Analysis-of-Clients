import serial
import time
ser = serial.Serial('COM3', 115200, timeout=0)

def creatNewTxt(arqName):
    try:
        arq = open(arqName+'.txt', 'r')

    except:
        arq = open(arqName+'.txt', 'w')
        arq.close()

    return arqName+'.txt'

def readSerial():

    response  = ser.read(115200)
    try:
        responseDecode = response.decode()
        print(responseDecode)
        return (responseDecode, 'OK')

    except UnicodeDecodeError:
        return (response, 'ERROR')


arqName = creatNewTxt('Livraria Cultura' +str(time.time()))
#arqErrorName = creatNewTxt('Error - probListLog')
#timeStamp = time.time()
error = True
while True:

    time.sleep(1)
    response, status = readSerial()

    if error :
        timeStamp = time.time()
        text = '@timeStamp '+str(timeStamp)+'@\n'
        arq = open(arqName, 'a')
        arq.write(text)
        arq.close()
        print(text)
        error = False

    if status == 'OK':
        arq = open(arqName, 'a')
        text = response
        print(status)
        print(text)
        arq.write(text)
        arq.close()
    elif status == 'ERROR':
        print(status)
        #arq = open(arqErrorName, 'a')
        #arq.write('@timeStamp '+str(timeStamp)+'#\n')
        #arq.write(response)
        #arq.write('\n')
        #arq.close()
        error = True
        continue
