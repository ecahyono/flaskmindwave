import serial

ser = serial.Serial("COM3", 9600)
temp =''
while 1:
    data=ser.readline()
    print data
    i = int(data, 16)
    data=data.script()
    print(data)
    if data[:1]=="[":
        print "\a"
        #trimadata = data.replace(" "," ")
        #thedata = urlEncode16(trimadata)
        #url = config.keyuri+'%input%ktp'+trimadata
        #thedata = urlEndcode16(uri)
        #webbrowser.open_new(config.host+thedata)