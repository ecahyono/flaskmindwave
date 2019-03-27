from flask import Flask, render_template, make_response, send_file, url_for
import json, time
import Tkinter
import tkMessageBox
import atexit
from time import clock
import request
import os


app = Flask(__name__)


#
# 
# 
# 
#     

def img():
        PEOPLE_FOLDER = os.path.join('static', 'img')
        app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER        

@app.route('/')
def show_index():
        img()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'EEG.jpg') #nampilin gambar     
        return render_template("index.html", user_image = full_filename )

def popup():
        tkMessageBox.showinfo("Information","Created in Python.") 
   
@app.route('/live')                                                     #dekorator flask, hubungan antara url)
def live(): 
        popup()
        img()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'pict.jpg')                
        return render_template('live.html', user = full_filename )                             #fungsi untuk merender file html didalam templates yang nanti akan dipanggil ke browsr

dataset = []                            #menampung data sementara

def myline():
    f = open('tmp','r+')                #buka file tmp dengan mode read
    line = f.readlines()                #baca file per line
    for x in line:                      #loping data perline
        dataset.insert(0,x)             
        return
 
def fromDataset():
        for x in dataset:
                return int(x)           #return dataset (convert to integer)
        
@app.route('/live-data')
def live_data():                                        #fungsi livedata
    myline()                                            #fungsi myline dipanggil agar data refresh per/detik
    data = [time.time() * 500, fromDataset()]           #waktu runing nampilin data yang di ambil  
    print time.ctime(time.time())
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/live-tmp', methods=['GET'])    
def livetmp():
    f = open('tmp','r')                                 #buka file tmp dengan mode read
    line = f.readlines()                                #baca file per line
    for x in line:                                      #loping data perline
        response = make_response(json.dumps(x))                 
        response.content_type = 'application/json'      
        return response                                 
 
@app.route('/data', defaults={'req_path':''}, methods=['GET'])
@app.route('/<path:req_path>')
def simpanjson(req_path):
    BASE_DIR = '/Users/PC 10/Zroyek/example2/LIVE/data'
    data_path = os.path.join(BASE_DIR, req_path)                # menyambungkan base dir dan path yang di request

    if os.path.isfile(data_path):                               # check path dan mengembalikan data
        return send_file(data_path)
    files = os.listdir(data_path)
   
    return render_template('files.html', files=files)           # menampilkan konten dari direktori

#
#
#
#
#
#


def secondsToStr(t):#fungsi waktu
    return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:], [(t*1000,),1000,60,60])          #ngubah supaya formatnya  H:MM:SS.SSS    
            
def sapa(nama): 
    """Fungsi ini untuk menyapa seseorang sesuai nama yang dimasukkan sebagai parameter""" 
    print("Hi, " + nama + ". Apa kabar?") 
sapa('teman')                                                  

line = "="*40
def log(s, elapsed=None):                       #menghitung waktu yang berlalu
    print line
    print secondsToStr(clock()), '-', s         # nampilin waktu yg berlalu
    if elapsed:
        print "Elapsed time:", elapsed 
    print line
    print
   
def date(): 
        date =time.time
        print time.ctime(time.time())
      

def endlog():
    end = clock()
    elapsed = end-start #ngitung waktu awal sampai akhir           
    log("End Program", secondsToStr(elapsed))   #nampilkn waktu akhir saat program di hentikan
    date() 
    print ('Proyek dua')

def now():
    return secondsToStr(clock())


start = clock()
atexit.register(endlog)
log("Start Program")                            #nmpilin waktu awal bngt

def print_info( nama, Npm ): 
    print ("Nama: ", nama) 
    print ("Npm: ", Npm) 
print_info( Npm=1164035, nama = "Eko Cahyono Putro" )
print_info( Npm=1164049, nama = "Nur Arkhamia Batubara" )



 #
 #
 #
 #
 #
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)    #url untuk masuk browser
