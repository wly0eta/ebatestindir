import requests
from bs4 import BeautifulSoup
print(
"""
------------------------------------
Test Numarası ----------> kaçıncı teste kadar indirmek istediğiniz örn: 11 
------------------------------------
5. sınıftan mezuna kadar var 656 to 727
""")
testnum = input("Test sayısı : ")


url = "https://odsgm.meb.gov.tr/www/11-sinif-fizik-kazanim-testleri/icerik/704"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,"html.parser")
linkler = soup.find_all("a",href=True)
num = 0
for link in linkler:
    if(link['href'].startswith("/destekmateryal/pdf/11kt/") and num < int(testnum)):
        a ="https://odsgm.meb.gov.tr"+link['href']
        num+=1
        dl =requests.get(a,allow_redirects=True)
        open('tarih'+str(num)+".pdf",'wb').write(dl.content)
        
