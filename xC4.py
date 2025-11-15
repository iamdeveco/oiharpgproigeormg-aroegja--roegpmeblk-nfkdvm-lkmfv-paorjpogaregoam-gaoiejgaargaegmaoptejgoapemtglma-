# By AbdeeLkarim Thug

import binascii
import os
import random
import re
import socket
import threading
import time
import urllib3
from datetime import datetime

import base64
import json
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from google.protobuf.timestamp_pb2 import Timestamp
from protobuf_decoder.protobuf_decoder import Parser
from byte import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Key, Iv = (
    bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56]),
    bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37]),
)



def EnC_AEs(HeX):
    cipher = AES.new(Key, AES.MODE_CBC, Iv)
    return cipher.encrypt(pad(bytes.fromhex(HeX), AES.block_size)).hex()


def DEc_AEs(HeX):
    cipher = AES.new(Key, AES.MODE_CBC, Iv)
    return unpad(cipher.decrypt(bytes.fromhex(HeX)), AES.block_size).hex()


def EnC_PacKeT(HeX, K, V):
    return AES.new(K, AES.MODE_CBC, V).encrypt(pad(bytes.fromhex(HeX), 16)).hex()


def DEc_PacKeT(HeX, K, V):
    return unpad(AES.new(K, AES.MODE_CBC, V).decrypt(bytes.fromhex(HeX)), 16).hex()


def EnC_Uid(H, Tp):
    e, H = [], int(H)
    while H:
        e.append((H & 0x7F) | (0x80 if H > 0x7F else 0))
        H >>= 7
    return bytes(e).hex() if Tp == 'Uid' else None


def EnC_Vr(N):
    if N < 0:
        ''
    H = []
    while True:
        Thug = N & 0x7F
        N >>= 7
        if N:
            Thug |= 0x80
        H.append(Thug)
        if not N:
            break
    return bytes(H)


def DEc_Uid(H):
    n = s = 0
    for b in bytes.fromhex(H):
        n |= (b & 0x7F) << s
        if not b & 0x80:
            break
        s += 7
    return n


def CrEaTe_VarianT(field_number, value):
    field_header = (field_number << 3) | 0
    return EnC_Vr(field_header) + EnC_Vr(value)


def CrEaTe_LenGTh(field_number, value):
    field_header = (field_number << 3) | 2
    encoded_value = value.encode() if isinstance(value, str) else value
    return EnC_Vr(field_header) + EnC_Vr(len(encoded_value)) + encoded_value


def CrEaTe_ProTo(fields):
    packet = bytearray()
    for field, value in fields.items():
        if isinstance(value, dict):
            nested_packet = CrEaTe_ProTo(value)
            packet.extend(CrEaTe_LenGTh(field, nested_packet))
        elif isinstance(value, int):
            packet.extend(CrEaTe_VarianT(field, value))
        elif isinstance(value, str) or isinstance(value, bytes):
            packet.extend(CrEaTe_LenGTh(field, value))
    return packet


def DecodE_HeX(H):
    R = hex(H)
    F = str(R)[2:]
    if len(F) == 1:
        F = '0' + F
        return F
    else:
        return F


def Fix_PackEt(parsed_results):
    result_dict = {}
    for result in parsed_results:
        field_data = {}
        field_data['wire_type'] = result.wire_type
        if result.wire_type == 'varint':
            field_data['data'] = result.data
        if result.wire_type == 'string':
            field_data['data'] = result.data
        if result.wire_type == 'bytes':
            field_data['data'] = result.data
        elif result.wire_type == 'length_delimited':
            field_data['data'] = Fix_PackEt(result.data.results)
        result_dict[result.field] = field_data
    return result_dict


def DeCode_PackEt(input_text):
    try:
        parsed_results = Parser().parse(input_text)
        parsed_results_objects = parsed_results
        parsed_results_dict = Fix_PackEt(parsed_results_objects)
        json_data = json.dumps(parsed_results_dict)
        return json_data
    except Exception as e:
        print(f"error {e}")
        return None


def xMsGFixinG(n):
    return '🗿'.join(str(n)[i:i + 3] for i in range(0, len(str(n)), 3))


def ArA_CoLor():
    Tp = [
        '32CD32', '00BFFF', '00FA9A', '90EE90', 'FF4500', 'FF6347', 'FF69B4', 'FF8C00',
        'FF6347', 'FFD700', 'FFDAB9', 'F0F0F0', 'F0E68C', 'D3D3D3', 'A9A9A9', 'D2691E',
        'CD853F', 'BC8F8F', '6A5ACD', '483D8B', '4682B4', '9370DB', 'C71585', 'FF8C00',
        'FFA07A',
    ]
    return random.choice(Tp)


def xBunnEr():
    bN = [
        902000306, 902000305, 902000003, 902000016, 902000017, 902000019, 902000020,
        902000021, 902000023, 902000070, 902000087, 902000108, 902000011, 902049020,
        902049018, 902049017, 902049016, 902049015, 902049003, 902033016, 902033017,
        902033018, 902048018, 902000306, 902000305,
    ]
    return random.choice(bN)

async def xSEndMsgsQ(Msg, uid, K, V):
    fields = {
        1: uid,
        2: uid,
        4: Msg,
        5: 1756580149,
        7: 2,
        8: 904990072,
        9: {
            1: "@thug4ff",
            2: await xBunnEr(),
            4: 330,
            5: 827001005,
            8: "@thug4ff",
            10: 1,
            11: 1,
            13: {1: 2},
            14: {
                1: 1158053040,
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0015\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            }
        },
        10: "en",
        13: {2: 2, 3: 1}
    }

    Pk = (await CrEaTe_ProTo(fields)).hex()
    Pk = "080112" + await EnC_Uid(len(Pk) // 2, Tp='Uid') + Pk
    return await GeneRaTePk(Pk, '1201', K, V)
  

async def AutH_Chat(T , uid, code , K, V):
    fields = {
  1: T,
  2: {
    1: uid,
    3: "en",
    4: str(code)
  }
}
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '1215' , K , V)

def xSEndMsg(Msg , Tp , Tp2 , id , K , V):
    feilds = {1: id,
              2: Tp2,
              3: Tp,
              4: Msg ,
              5: 1735129800,
              7: 2,
              9: {1: "xBesTo - C4­",
                        2: xBunnEr(), 3: 901048018,
                        4: 330, 5: 910000001,
                        8: "xBesTo - C4",
                        10: 1, 11: 1},
              10: "en",
              13: {
                   2: 1,
                   3: 1
                   },
              14: {}}
    Pk = str(CrEaTe_ProTo(feilds).hex())
    Pk = "080112" + EnC_Uid(len(Pk) // 2 , Tp = 'Uid') + Pk
    return GeneRaTePk(str(Pk) , '1215' , K , V)


def OpEnSq(K, V):
    fields = {
        1: 1,
        2: {2: '\u0001',
            3: 1,
            4: 1,
            5: 'en',
            9: 1,
            11: 1,
            13: 1,
            14:
                {
                    2: 5756,
                    6: 11,
                    8: '1.111.5',
                    9: 2,
                    10: 4
                }},
    }
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0515', K, V)


def cHSq(Nu, Uid, K, V):
    fields = {1: 17,
              2: {1: int(Uid),
                  2: 1,
                  3: int(Nu - 1),
                  4: 62,
                  5: '\u001a',
                  8: 5,
                  13: 329}}
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0515', K, V)


def SEnd_InV(Nu, Uid, region, K, V):
    fields = {
        1: 2,
        2: {
            1: int(Uid),
            2: region,
            4: int(Nu)}}
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0515', K, V)


def leave_s(K, V):
    fields = {1: 7,
              2: {1: 00000000}}
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0515', K, V)


def leave_room(idroom, K, V):
    fields = {1: 6,
              2: {1: int(idroom)}}
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0515', K, V)


def start_autooo(K, V):
    fields = {1: 9,
              2: {1: 00000000}}
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0515', K, V)


def AuthClan(CLan_Uid, AuTh, K, V):
    fields = {
        1: 3,
        2: {1: int(CLan_Uid),
            2: 1,
            4: str(AuTh)}
        }
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '1201', K, V)


def GeT_Status(PLayer_Uid, K, V):
    PLayer_Uid = EnC_Uid(PLayer_Uid, Tp='Uid')
    if len(PLayer_Uid) == 8:
        Pk = f'080112080a04{PLayer_Uid}1005'
    elif len(PLayer_Uid) == 10:
        Pk = f"080112090a05{PLayer_Uid}1005"
    return GeneRaTePk(Pk, '0f15', K, V)


def SPam_Room(Uid, Rm, Nm, K, V):
    fields = {
        1: 78,
        2: {
            1: int(Rm),
            2: f"[{ArA_CoLor()}]{Nm}",
            3: {2: 1, 3: 1},
            4: 330,
            5: 1,
            6: 201,
            10: xBunnEr(),
            11: int(Uid),
            12: 1,
        },
    }
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0e15', K, V)


def Join_Room(room_id, region, K, V):
    fields = {
        1: 3,
        2: {
            1: int(room_id),
            8: {1: 'IDC1', 2: 3000, 3: region},
            9: "\x01\t\n\x12\x19 ",
            10: 1,
            12: b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01",
            13: 3,
            14: 3,
            16: region,
        },
    }
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0e10', K, V)


def SPamSq(Uid, region, K, V):
    fields = {
        1: 33,
        2: {
            1: int(Uid),
            2: region,
            3: 1,
            4: 1,
            7: 330,
            8: 19459,
            9: 100,
            12: 1,
            16: 1,
            17: {2: 94, 6: 11, 8: '1.111.5', 9: 3, 10: 2},
            18: 201,
            23: {2: 1, 3: 1},
            24: xBunnEr(),
            26: {},
            28: {},
        },
    }
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0515', K, V)


def AccEpT(PLayer_Uid, AuTh_CodE_Sq, K, V):
    fields = {
        1: 4,
        2: {
            1: int(PLayer_Uid),
            3: int(PLayer_Uid),
            4: "\u0001\u0007\t\n\u0012\u0019\u001a ",
            8: 1,
            9: {2: 1393, 4: 'wW_T', 6: 11, 8: '1.111.5', 9: 3, 10: 2},
            10: AuTh_CodE_Sq,
            12: 1,
            13: 'en',
            16: 'OR',
        },
    }
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0515', K, V)


def Huh(PLayer_Uid, AuTh_CodE_Sq, K, V):
    fields = {
        1: 61,
        2: {
            1: 474731042,
            2: {
                1: 474731042,
                2: 11037044965,
                3: "[b][c][00ff00]C4:[ff0000]RIZAKYI",
                5: 17472,
                6: 15,
                7: 1,
                8: {2: 1, 3: 1},
                9: 3,
            },
            3: '1742773572995511270_6hi4ayshuh',
        },
    }
    return GeneRaTePk(str(CrEaTe_ProTo(fields).hex()), '0515', K, V)


def GeneRaTePk(Pk, N, K, V):
    PkEnc = EnC_PacKeT(Pk, K, V)
    _ = DecodE_HeX(int(len(PkEnc) // 2))
    if len(_) == 2:
        HeadEr = N + '000000'
    elif len(_) == 3:
        HeadEr = N + '00000'
    elif len(_) == 4:
        HeadEr = N + '0000'
    elif len(_) == 5:
        HeadEr = N + '000'
    return bytes.fromhex(HeadEr + _ + PkEnc)


def GuiLd_AccEss(Tg, Nm, Uid, BLk, OwN, AprV):
    return Tg in Nm and Uid not in BLk and Uid in (OwN | AprV)


def ChEck_Commande(id):
    return '<' not in id and '>' not in id and '[' not in id and ']' not in id


def L_DaTa():
    load = lambda f: json.load(open(f)) if os.path.exists(f) else {}
    return map(load, [
        'Thug_CLan_LiKes.json',
        'Thug_RemaininG_LiKes.json',
        'Thug_RemaininG_Room.json',
    ])



def ChEck_Limit_CLan(Uid, STaTus):
    data, max_use, file = (like_data_clan, 10, 'Thug_CLan_LiKes.json') if STaTus == 'like' else ''
    t, limit = time.time(), 86400
    u = data.get(str(Uid), {'count': 0, 'start_time': t})
    if t - u['start_time'] >= limit:
        u = {'count': 0, 'start_time': t}
    if u['count'] < max_use:
        u['count'] += 1
        data[str(Uid)] = u
        json.dump(data, open(file, 'w'))
        return f"{max_use - u['count']}", datetime.fromtimestamp(u['start_time'] + limit).strftime(
            '%I:%M %p - %d/%m/%y')
    return False, datetime.fromtimestamp(u['start_time'] + limit).strftime('%I:%M %p - %d/%m/%y')


def ChEck_Limit(Uid, STaTus):
    data, max_use, file = (
        (like_data, 10, 'Thug_RemaininG_LiKes.json') if STaTus == 'like' else (
        room_data, 10, 'Thug_RemaininG_Room.json')
    )
    t, limit = time.time(), 86400
    u = data.get(str(Uid), {'count': 0, 'start_time': t})
    if t - u['start_time'] >= limit:
        u = {'count': 0, 'start_time': t}
    if u['count'] < max_use:
        u['count'] += 1
        data[str(Uid)] = u
        json.dump(data, open(file, 'w'))
        return f"{max_use - u['count']}", datetime.fromtimestamp(u['start_time'] + limit).strftime(
            '%I:%M %p - %d/%m/%y')
    return False, datetime.fromtimestamp(u['start_time'] + limit).strftime('%I:%M %p - %d/%m/%y')

def nmnmmmmn(plain_text, key, iv):
    plain_text = bytes.fromhex(plain_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()

def join_teamcode(room_id, key, iv):
    room_id_hex = ''.join(format(ord(c), 'x') for c in room_id)
    packet = f"080412b705220701090a0b1219202a07{room_id_hex}300640014ae9040a8001303946454133424438453839323231443032303331423031313131313030303230303239303030323030323530303032353442383542303530393030303033423431373232393134323230313034303631343034376462626236636163626536363734373436356530303030303066663037303930353065313262636665363810dd011abf03755154571b08004d000c0950090c560c0b0857015a0f020f5d5009085657570c0b075d0f04080809120208440b0c0000080b5101060f0f060e5c010d0d5406560c0b0b0a5b005b0d0505000d1b020a445e5b0f026270697b636b5c606d4e5e437470517d5900665b5a04010e1a094f7c575b4a5178697f480878760e50606b585259697b077e5b605c4e0d12020a446b5e08610b4f465651546b465208740a7b436940780d7d4b561d610413094f684e54574a516a75547660484172750f5a7a416547540a6c4453080f1b08084d014e4c457c41066a1649485f08490413705b7e4f7a567f5e5c590005110b455e5e79760d0a775246005f52024751745148407c096f5d69794b750e1b0a4e6c747840625c7f415e6c1d6d5f081e02007f477f7d640e7e56567e041b50575654515e1f43564a5b5c565e5d484d595e5d5854525a5c534c584c57037a015571555b545267095c6b6001017504794d6273524e765c051b0b4460037b0b4161764108487151694972606b426b75440a7c415b045205100d44540e4d6a697a4a55747c41730b6f5f487a61597d68537369745d520e1a0c4f505d037d7a7203410c77716a69536c7f755363746b667c736860600d22047c575755300b3a091d6d647370687a1d144208312e3130382e3134480350015a0c0a044944433110761a024d455a0d0a04494443321084011a024d455a0d0a044944433310d7011a024d456a02656e8201024f52"
    encrypted_packet = nmnmmmmn(packet, key, iv)
    header_length = len(encrypted_packet) // 2

    header_length_hex = dec_to_hex(header_length)

    if len(header_length_hex) == 2:
        final_packet = "0515000000" + header_length_hex + encrypted_packet
    elif len(header_length_hex) == 3:
        final_packet = "051500000" + header_length_hex + encrypted_packet
    elif len(header_length_hex) == 4:
        final_packet = "05150000" + header_length_hex + encrypted_packet
    elif len(header_length_hex) == 5:
        final_packet = "05150000" + header_length_hex + encrypted_packet
    else:
        raise ValueError("eororr 505 🐜")

    return bytes.fromhex(final_packet)


import json
import os
from pprint import pprint

f = 'blacklist.json'
approvee = 'approved.json'
black, approve = [], []


def load_json(filename):
    """Charge la liste depuis un fichier JSON, ou retourne une liste vide si le fichier n'existe pas."""
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # pprint(data)
                if isinstance(data, list):
                    return data
        except json.JSONDecodeError:
            pass
    # Si le fichier est vide ou invalide, retourne une liste vide
    return []


def save_json(filename, data):
    """Sauvegarde une liste dans un fichier JSON."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erreur en sauvegardant {filename}: {e}")


def load_blacklist():
    """Charge la blacklist depuis le fichier JSON."""
    global black
    black = load_json(f)


def load_approve():
    """Charge la liste des approuvés depuis le fichier JSON."""
    global approve
    approve = load_json(approvee)


def Add_Uid(user_id):
    """Ajoute un UID dans la blacklist (en clair)."""
    data = load_json(f)
    user_id = str(user_id)
    if user_id not in data:
        data.append(user_id)
        save_json(f, data)


def Remove_Uid(player_uid):
    """Supprime un UID de la blacklist (en clair)."""
    data = load_json(f)
    player_uid = str(player_uid)
    if player_uid in data:
        data.remove(player_uid)
        save_json(f, data)
        return True
    return False


def A(user_id):
    """Ajoute un UID dans la liste des approuvés."""
    data = load_json(approvee)
    user_id = str(user_id)
    if user_id not in data:
        data.append(user_id)
        save_json(approvee, data)


def D(player_uid):
    """Supprime un UID de la liste des approuvés."""
    data = load_json(approvee)
    player_uid = str(player_uid)
    if player_uid in data:
        data.remove(player_uid)
        save_json(approvee, data)
        return True
    return False


def Clear():
    """Vide complètement la blacklist."""
    global black
    black.clear()
    save_json(f, black)
    return True


def Add_Black(user_id):
    """Ajoute un UID dans la blacklist sans chiffrement."""
    user_id = str(user_id)
    data = load_json(f)
    if user_id not in data:
        data.append(user_id)
        save_json(f, data)
        black.append(user_id)
        return True
    return False


def Rem_Black(user_id):
    """Supprime un UID de la blacklist sans chiffrement."""
    user_id = str(user_id)
    if user_id in black:
        black.remove(user_id)
    if Remove_Uid(user_id):
        return True
    return False


def Show_Uids():
    """Retourne la liste des UIDs blacklistés, ou False si vide."""
    try:
        data = load_json(f)
        return "\n".join(sorted(data, key=int)) if data else False
    except (ValueError, FileNotFoundError):
        return False


def Approved(user_id):
    """Ajoute un UID dans la liste des approuvés sans chiffrement."""
    user_id = str(user_id)
    data = load_json(approvee)
    if user_id not in data:
        data.append(user_id)
        save_json(approvee, data)
        approve.append(user_id)
        return True
    return False


def DeApproved(user_id):
    """Supprime un UID de la liste des approuvés sans chiffrement."""
    user_id = str(user_id)
    if user_id in approve:
        approve.remove(user_id)
    if D(user_id):
        return True
    return False


def Show_Approvs():
    """Retourne la liste des UIDs approuvés, ou False si vide."""
    try:
        data = load_json(approvee)
        return "\n".join(sorted(data, key=int)) if data else False
    except (ValueError, FileNotFoundError):
        return False


def Clear_Approvs():
    """Vide complètement la liste des approuvés."""
    global approve
    approve.clear()
    save_json(approvee, approve)
    return True


# --- Initialisation au démarrage ---
load_blacklist()
# encrypt_uids()
load_approve()
# encrypt_uids2()
like_data_clan, like_data, room_data = L_DaTa()


def get_available_room(input_text):
    try:
        parsed_results = Parser().parse(input_text)
        parsed_results_objects = parsed_results
        parsed_results_dict = parse_results(parsed_results_objects)
        json_data = json.dumps(parsed_results_dict)
        return json_data
    except Exception as e:
        print(f"error {e}")
        return None
def parse_results(parsed_results):
    result_dict = {}
    for result in parsed_results:
        field_data = {}
        field_data["wire_type"] = result.wire_type
        if result.wire_type == "varint":
            field_data["data"] = result.data
        if result.wire_type == "string":
            field_data["data"] = result.data
        if result.wire_type == "bytes":
            field_data["data"] = result.data
        elif result.wire_type == "length_delimited":
            field_data["data"] = parse_results(result.data.results)
        result_dict[result.field] = field_data
    return result_dict


def Emote_k(TarGeT , idT, K, V,region):
    fields = {
        1: 21,
        2: {
            1: 804266360,
            2: 909000001,
            5: {
                1: TarGeT,
                3: idT,
            }
        }
    }
    if region.lower() == "ind":
        packet = '0514'
    elif region.lower() == "bd":
        packet = "0519"
    else:
        packet = "0515"
    return  GeneRaTePk(( CrEaTe_ProTo(fields)).hex() , packet , K , V)