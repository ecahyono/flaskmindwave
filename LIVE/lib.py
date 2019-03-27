import mindwave, time ,json
import datetime
headset = mindwave.Headset('COM3','1425')
#time.sleep(1)

data = [] #menampung data sementara json baru
def connect():
        #headset.connect()#
        #print "Connecting..."
        while headset.status != 'connected':
                time.sleep(1)
                if headset.status == 'standby':
                        headset.connect()
                        print "Retrying connect.."
        print " Connected."
        return

def getData(raw):
        time.sleep(0.3)                         #pause n seconds
        f = open('tmp','w')                     #Buka file tmp dengan mode write
        f.write(str(raw))                       #write raw value dari headset ke file tmp  
        #print "Auttention: %s, meditation: %s" % (headset.attention, headset.meditation)
        #print headset.serial_open()
        #print headset.raw_value#"raw_value: %s" % (headset.raw_value)
        return

now = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
def saveData(raw):                                              #setiap berjalan akan menyimpan raw value ke file baru
        time.sleep(0.3)
        data.append(raw)
        file = "data/"+now+".json"
        f = open(file,'w+')                                     #buka file tmp dengan mode 
        f.write(json.dumps(data,ensure_ascii=False))
        return


 
def disconnect():
        if headset.status == 'connected':
                headset.disconnect() 
                print "Disconnected"
        return
        
connect()
while True:
        raw = headset.raw_value 
        getData(raw)
        saveData(raw)
#disconnect()