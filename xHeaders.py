import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , xKEys , base64 , datetime , re ,socket , threading
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from byte import *
# from config import KEY,API_URL
from config.settings import KEY,API_URL
import requests
import binascii
import json
import traceback
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
from pprint import pprint




def DeLet_Uid(uid , Token):
    print(f' Done FuckinG > {id} ')
    url = 'https://clientbp.ggblueshark.com/RemoveFriend'
    headers = {
            "Authorization": f"Bearer {Token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB51",
            "Content-Type": "application/octet-stream",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI)",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "close"
        }
    payload_hex = "08" + Encrypt_ID(str(uid)) + "1801"
    data = bytes.fromhex(encrypt_api(payload_hex))
    ResPonse = requests.post(url , headers=headers , data=data , verify=False)    
    if ResPonse.status_code == 400 and 'BR_FRIEND_NOT_SAME_REGION' in ResPonse.text:
        return f'[b][c]Id : {xMsGFixinG(id)} Not In Same Region !'
    elif ResPonse.status_code == 200:
        return f'[b][c]Good Response Done Delete Id : {xMsGFixinG(id)} !'
    else:
        return f'[b][c]Erorr !'

def GeT_PLayer_InFo(uid, Token):
    try:
        # --- Construction du payload ---
        payload_hex = "08" + Encrypt_ID(str(uid)) + "1801"
        data = bytes.fromhex(encrypt_api(payload_hex))

        url = "https://clientbp.ggwhitehawk.com/GetPlayerPersonalShow"
        print(url,uid)
        headers = {
            "Authorization": f"Bearer {Token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB51",
            "Content-Type": "application/octet-stream",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI)",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "close"
        }

        response = requests.post(url, headers=headers, data=data, verify=False)
        if response.status_code != 200:
            return '\n[b][c][FFD700]FaiLEd GeTinG PLayer InFo !\n'

        # --- Décodage de la réponse ---
        packet = binascii.hexlify(response.content).decode('utf-8')
        decoded = DeCode_PackEt(packet)
        Thug_data = json.loads(decoded)

        # --- Extraction sécurisée des infos joueur ---
        player_data = Thug_data.get("1", {}).get("data", {})
        a1 = str(player_data.get("1", {}).get("data", "Unknown UID"))
        a2 = player_data.get("21", {}).get("data", "0")
        a3 = player_data.get("3", {}).get("data", "Unknown Name")
        player_server = player_data.get("5", {}).get("data", "Unknown Server")
        player_bio = Thug_data.get("9", {}).get("data", {}).get("9", {}).get("data", "")
        player_level = player_data.get("6", {}).get("data", "0")

        # --- Dates ---
        try:
            account_date = datetime.fromtimestamp(
                player_data.get("44", {}).get("data", 0)
            ).strftime("%I:%M %p - %d/%m/%y")
        except Exception:
            account_date = "Unknown"

        try:
            last_login = datetime.fromtimestamp(
                player_data.get("24", {}).get("data", 0)
            ).strftime("%I:%M %p - %d/%m/%y")
        except Exception:
            last_login = "Unknown"

        # --- Infos de clan ---
        clan_id = clan_name = clan_leader = clan_level = clan_members_num = clan_leader_name = None
        clan_data = Thug_data.get("6", {}).get("data", {})

        if isinstance(clan_data, dict):
            clan_id = clan_data.get("1", {}).get("data")
            clan_name = clan_data.get("2", {}).get("data")
            clan_leader = clan_data.get("3", {}).get("data")
            clan_level = clan_data.get("4", {}).get("data")
            clan_members_num = clan_data.get("6", {}).get("data")
            clan_leader_name = Thug_data.get("7", {}).get("data", {}).get("3", {}).get("data")

        # --- Formatage final ---
        info = f"""
[b][c][90EE90]    Get Player Info

[FFFF00][1] - ProFile InFo :
[ffffff]    
 Name : {a3}
 Uid : {xMsGFixinG(a1)}
 Likes : {xMsGFixinG(a2)}
 LeveL : {player_level}
 Server : {player_server}
 Bio : {player_bio}
 Creating : {account_date}
 LasT LoGin : {last_login}
"""

        if clan_name:
            info += f"""
[b][c][FFFF00][2] - Guild InFo :
[ffffff]
 Guild Name : {clan_name}
 Guild Uid : {xMsGFixinG(clan_id)}
 Guild LeveL : {clan_level}
 Guild Members : {clan_members_num}
 Leader s'Uid : {xMsGFixinG(clan_leader)}
 Leader s'Name : {clan_leader_name}
"""
        else:
            info += "\n[FFFF00]No clan found.\n"

        info += """\n
[C][B][00FFFF]━━━━━━━━━━
[FFB300]    DEVELOPED BY @iamdeveco
[C][B][00FFFF]━━━━━━━━━━"""

        return info.replace('[i]', '')

    except Exception:
        return '\n[b][c][FFD700]FaiLEd GeTinG PLayer InFo (fatal) !\n'

