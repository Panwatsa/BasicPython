#temperture.py

from urllib.request import urlopen #urllib เป็น built in libraries
from bs4 import BeautifulSoup
import csv
from datetime import datetime



def writetocsv(data):
    
    date = datetime.now().strftime('%Y-%m-%d')
    
    with open('data-temperature-{}.csv'.format(date),'a',newline='',encoding='utf-8') as file: #'a' ทำการส่งออกและเพิ่มค่าลงไปในไฟล์
        filewriter = csv.writer(file)
        filewriter.writerow(data)


alldata = {}

def checktemp(ID):
    url = 'https://www.tmd.go.th/province.php?id=' + str(ID)

    webopen = urlopen(url) #เปิดเว็บโดยไม่ต้องเปิด chrome
    html_page = webopen.read() #อ่านข้อมูลในเว็บ
    

    data = BeautifulSoup(html_page,'html.parser') #แปลงโค้ดให้ bs4 ช่วยแปล

    try:
        temp = data.find('td',{'class':'strokeme'})
        title = data.find('span',{'class':'title'})

        city = title.text.strip()
        temp = temp.text
        # print(city, temp)
        alldata[city] = temp
    except:
        pass

for i in range(1,101):
    checktemp(i)
    
for k,v in alldata.items():
    data = [k,v]
    writetocsv(data)

print('saved')