import requests
from bs4 import BeautifulSoup
import os
import time
def listthesubjectsoftests(linkler):
    num = 0
    for link in linkler:

        if(link['href'].startswith("https://cdn.eba.gov.tr/yardimcikaynaklar/2022/01/odsgm/kt/"+grade+"kt/")):
           
           
            num+=1
            if num >=2:
                
                print(str(num-1)+". "+link.text.strip())    
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def findtitle(subject):
    url = "https://odsgm.meb.gov.tr/www/11-sinif-tarih-kazanim-testleri/icerik/"+str(subject)
    response = requests.get(url)
    htmlcd = response.content
    soup = BeautifulSoup(htmlcd,"html.parser")
    listindex = soup.find("div",{"class":"outline-info"})
    return listindex.text.strip()
def showsubjects(grade):
    if grade== 5:
         print("""
656 5. Sınıf Matematik Kazanım Testleri
657 5. Sınıf Fen Bilimleri Kazanım Testleri
658 5. Sınıf Sosyal Bilgiler Kazanım Testleri
659 5. Sınıf Din Kültürü ve Ahlak Bilgisi Kazanım Testleri
660 5. Sınıf İngilizce Kazanım Testleri
        """)
    elif grade== 6:
         print("""
661 6. Sınıf İngilizce Kazanım Testleri
662 6. Sınıf Din Kültürü ve Ahlak Bilgisi Kazanım Testleri
663 6. Sınıf Sosyal Bilgiler Kazanım Testleri
664 6. Sınıf Fen Bilimleri Kazanım Testleri
665 6. Sınıf Matematik Kazanım Testleri
666 6. Sınıf Türkçe Kazanım Testleri
        """)
    elif grade == 7:
         print("""
667 7. Sınıf İngilizce Kazanım Testleri
668 7. Sınıf Din Kültürü ve Ahlak Bilgisi Kazanım Testleri
669 7. Sınıf Sosyal Bilgiler Kazanım Testleri
670 7. Sınıf Fen Bilimleri Kazanım Testleri
671 7. Sınıf Matematik Kazanım Testleri
672 7. Sınıf Türkçe Kazanım Testleri
        """)
    elif grade == 8:
         print("""
673 8. Sınıf İngilizce Kazanım Testleri
674 8. Sınıf Din Kültürü ve Ahlak Bilgisi Kazanım Testleri
675 8. Sınıf T.C. İnkılap Tarihi ve Atatürkçülük Kazanım Testleri
676 8. Sınıf Fen Bilimleri Kazanım Testleri
677 8. Sınıf Matematik Kazanım Testleri
678 8. Sınıf Türkçe Kazanım Testleri
        """)
    elif grade == 9:
         print("""
679 9. Sınıf İngilizce Kazanım Testleri
680 9. Sınıf Din Kültürü ve Ahlak Bilgisi Kazanım Testleri
681 9. Sınıf Coğrafya Kazanım Testleri
682 9. Sınıf Tarih Kazanım Testleri
683 9. Sınıf Biyoloji Kazanım Testleri
684 9. Sınıf Kimya Kazanım Testleri
685 9. Sınıf Fizik Kazanım Testleri
686 9. Sınıf Matematik Kazanım Testleri
687 9. Sınıf Türk Dili ve Edebiyatı Kazanım Testleri
        """)
    elif grade == 10:
         print("""
688 10. Sınıf Felsefe Kazanım Testleri
689 10. Sınıf İngilizce Kazanım Testleri
690 10. Sınıf Din Kültürü ve Ahlak Bilgisi Kazanım Testleri
691 10. Sınıf Coğrafya Kazanım Testleri
692 10. Sınıf Tarih Kazanım Testleri
693 10. Sınıf Biyoloji Kazanım Testleri
694 10. Sınıf Kimya Kazanım Testleri
695 10. Sınıf Fizik Kazanım Testleri
        """)
    elif grade == 11:
         print("""
698 11. Sınıf İngilizce Kazanım Testleri
699 11. Sınıf Din Kültürü ve Ahlak Bilgisi Kazanım Testleri
700 11. Sınıf Sosyoloji Kazanım Testleri
701 11. Sınıf Psikoloji Kazanım Testleri
702 11. Sınıf Felsefe Kazanım Testleri
703 11. Sınıf Coğrafya Kazanım Testleri
704 11. Sınıf Tarih Kazanım Testleri
705 11. Sınıf Biyoloji Kazanım Testleri
706 11. Sınıf Kimya Kazanım Testleri
707 11. Sınıf Fizik Kazanım Testleri
708 11. Sınıf Matematik (İleri Düzey) Kazanım Testleri
709 11. Sınıf Matematik (Temel Düzey) Kazanım Testleri
710 11. Sınıf Türk Dili ve Edebiyatı Kazanım Testleri        
        """)
    elif grade== 12:
         print("""
711 12. Sınıf İngilizce Kazanım Testleri
712 12. Sınıf Din Kültürü ve Ahlak Bilgisi Kazanım Testleri
713 12. Sınıf Mantık Kazanım Testleri
714 12. Sınıf Coğrafya Kazanım Testleri
715 12. Sınıf Tarih Kazanım Testleri
716 12. Sınıf Biyoloji Kazanım Testleri
717 12. Sınıf Kimya Kazanım Testleri
718 12. Sınıf Fizik Kazanım Testleri
719 12. Sınıf Matematik (İleri Düzey) Kazanım Testleri
720 12. Sınıf Matematik (Temel Düzey) Kazanım Testleri
721 12. Sınıf Türk Dili ve Edebiyatı Kazanım Testleri
        """)
    elif grade == 1:
         print("""
722 Mezun İngilizce Kazanım Testleri
723 Mezun Felsefe Grubu Kazanım Testleri
724 Mezun Din Kültürü ve Ahlak Bilgisi Kazanım Testleri
725 Mezun Coğrafya Kazanım Testleri
726 Mezun Tarih Kazanım Testleri
727 Mezun Biyoloji Kazanım Testleri        
        """)
        
      
initial_path= os.getcwd()
currentpath=initial_path
if not os.path.exists("logs"):
    os.mkdir("logs")    
while True:
    mustwrite = []
    print(
    """
    ---------------------------------------------------------------------------
    Test Numarası ----------> kaçıncı teste kadar indirmek istediğiniz örn: 11 
    ---------------------------------------------------------------------------
    Sınıf bilgisi ------------------> 5,6,7,8,9,10,11,12(mezun için 1 yazın)
    ---------------------------------------------------------------------------
    Konulara sınıfınızı girdiğinizde ulaşacaksınız.
    ---------------------------------------------------------------------------
    İstediğiniz testleri virgülle ayırarak yazınız örneğin 2.testten 6.teste kadar istiyorsanız 2,6 yazınız.
    """)
    
    grade = input("Kaçıncı sınıfsınız : ")
    showsubjects(int(grade))
    subject = input("Hangi dersi istiyorsunuz : ")
    
    title = findtitle(subject)
    url = "https://odsgm.meb.gov.tr/www/"+grade+"-sinif-fizik-kazanim-testleri/icerik/"+subject
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,"html.parser")
    linkler = soup.find_all("a",href=True)
    num = -1
    maxtestnum=0
    listthesubjectsoftests(linkler)
    testnum = input("Test sayısı : ")
    listus = testnum.split(",")
    firsttest = int(listus[0])
    lasttest=int(listus[1])
    
    
    if not os.path.exists(title):
        os.mkdir(title)
    os.chdir(os.path.join(currentpath,title))

    for link in linkler:
        if(link['href'].startswith("https://cdn.eba.gov.tr/yardimcikaynaklar/2022/01/odsgm/kt/"+grade+"kt/")):
            num+=1
            if num<=int(lasttest) and num>=int(firsttest):
                a = link['href']
                dl =requests.get(a,allow_redirects=True)
                open(str(num)+link.text.strip()+".pdf",'wb').write(dl.content)
                written= link.text.strip()+ os.getcwd() +" adresine indirildi.\n"
                print(link.text.strip()+ os.getcwd() +" adresine indirildi.")
                mustwrite.append(written)
    url = "https://odsgm.meb.gov.tr/www/"+grade+"sinif-tarih-kazanim-testleri/icerik/"+subject
    response = requests.get(url)
    htmlcd = response.content
    soup = BeautifulSoup(htmlcd,"html.parser")
    listindex = soup.find_all("p",{"class":"MsoNormal"})
    for link in listindex:
        amogus =link.find("a")
        if amogus["href"].startswith("/kurslar/pdf/cvp/kt"):
            a="https://odsgm.meb.gov.tr"+amogus['href'] 
            dl = requests.get(a,allow_redirects=True)
            open("Cevap Anahtarı.pdf","wb").write(dl.content)  
    os.chdir(initial_path)
    # os.chdir("/logs")
    # with open("dosyakonumu.txt","a",encoding="utf-8") as file:
    #     file.writelines(mustwrite)
    os.chdir(initial_path)
    time.sleep(3)
    clearConsole()
            