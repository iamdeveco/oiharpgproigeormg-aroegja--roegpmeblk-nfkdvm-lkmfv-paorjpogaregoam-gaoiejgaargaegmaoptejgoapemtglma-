import requests, os, psutil, sys, jwt, pickle, json, binascii, time, urllib3, xKEys, base64, datetime, re, socket, threading
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from threading import Thread
from datetime import datetime , timedelta
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from utils import process_token 
from pprint import pprint
from external_apis import *
from app.utils.encryption_utils import encrypt_api
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def auto():
    time.sleep(6 * 60 * 60)
    print('\n - AuTo ResTartinG The BoT ... ! ')
    p = psutil.Process(os.getpid())
    for handler in p.open_files():
        try:
            os.close(handler.fd)
        except Exception as e:
            print(f" - Error CLose Files : {e}")
    for conn in p.net_connections():
        try:
            if hasattr(conn, 'fd'):
                os.close(conn.fd)
        except Exception as e:
            print(f" - Error CLose Connection : {e}")
    sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])))
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def restart_program():
    print('\n - ResTartinG The BoT ... ! ')
    p = psutil.Process(os.getpid())
    for handler in p.open_files():
        try:
            os.close(handler.fd)
        except Exception as e:
            print(f" - Error CLose Files : {e}")
    for conn in p.net_connections():
        try:
            if hasattr(conn, 'fd'):
                os.close(conn.fd)
        except Exception as e:
            print(f" - Error CLose Connection : {e}")
    sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])))
    python = sys.executable
    os.execl(python, python, *sys.argv)    
        
ownerr = [
    
    '12917534573',
  
  ]
owner = [EnC_Uid(uid , Tp = 'uid') for uid in ownerr]


Thread(target=auto, daemon=True).start()    

class FF_CLient():

    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.region = None
        self.Get_FiNal_ToKen_0115()

    def Connect_SerVer_OnLine(self , Token , tok , host , port , key , iv , host2 , port2):
            global CLients2 , data2 , AutH
            try:
                self.AutH_ToKen_0115 = tok    
                self.CLients2 = socket.create_connection((host2 , int(port2)))
                self.CLients2.send(bytes.fromhex(self.AutH_ToKen_0115))                  
            except:pass        
            while True:
                try:
                    self.data2 = self.CLients2.recv(99999)
                    if '0500' in self.data2.hex()[0:4] and len(self.data2.hex()) > 30:	         	    	    
                            self.packet = json.loads(DeCode_PackEt(f'08{self.data2.hex().split("08", 1)[1]}'))
                            self.AutH = self.packet['5']['data']['7']['data']
                            #print(self.AutH)    		      	
                except:pass    	
                               
    def Connect_SerVer(self , Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code): 
        self.CLients = socket.create_connection((host , int(port)))
        self.CLients.send(bytes.fromhex(tok))                  
        data = self.CLients.recv(1024)       
        self.CLients.send(AuthClan(Guild_Uid , Auth_Code , key , iv))
        threading.Thread(target=self.Connect_SerVer_OnLine, args=(Token , tok , host , port , key , iv , host2 , port2)).start()
        self.Exemple = xMsGFixinG('1007238727')
        while True:
            try:
                data = self.CLients.recv(1024)        	
                if len(data) == 0:
                    try:            		    
                        self.CLients.close() ; self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code)
                    except:
                        try:
                            self.CLients.close() ; self.CLients2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code)          
                        except:
                            self.CLients.close() ; self.CLients2.close()
                            restart_program()

                if '1200' in data.hex()[0:4] and 900 > len(data.hex()) > 100:
                    if b"***" in data:data = data.replace(b"***",b"106")
                    self.thug4ff_data = json.loads(DeCode_PackEt(data.hex()[10:]))                        
                    try:            	       
                       self.InputMsg = 'thug_love' if '8' in self.thug4ff_data["5"]["data"] else self.thug4ff_data["5"]["data"]["4"]["data"] 
                       self.name = self.thug4ff_data["5"]["data"]["9"]["data"]["1"]["data"]
                       
                    except:self.InputMsg = "None"   
                    self.DeCode_CliEnt_Uid = self.thug4ff_data["5"]["data"]["1"]["data"]
                    client_id = EnC_Uid(self.DeCode_CliEnt_Uid , Tp = '1007238727')

                if 'thug_love' in self.InputMsg[:10]:
                    if  client_id not in black :
                        self.CLients.send(xSEndMsg(r'''
                        [b][c][FFD3EF] > Welcome to ECO friend bot <

                        [ffffff] To get the list of commands

                        simply send /start or /help !

                        For Arabic list => ar

                        Enjoy using the bot with new features and better speed

                        Don't forget to follow me on [Youtube] and Discord !\kn
                        User => iamdeveco

                        [FFD3EF] Powered by: The official ECO team !
                        ''',  1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.3)
                        self.CLients.close() ; self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

                if b'/start' in data or b'/help' in data or 'ar' in self.InputMsg[:2]:
                    json_result = get_available_room(data.hex()[10:])
                    # print(data.hex())
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    if 'D̶S̶' in self.name and client_id not in black or client_id in owner and client_id not in black or client_id in approve:
                        self.CLients.send(xSEndMsg(f'''	[b][c][FF0000]TCP BOT RUNING GOOD ! 
                                                
[ffffff]CHANGE SQUAD MODE: [90EE90]
 /6
 /5
 /3

[ffffff]SEND SQUAD TO A FRIEND: [90EE90]
 /c6/id
 /c5/id
 /c3/id

[ffffff]ADD A PLAYER TO THE SQUAD: [90EE90]
 /get/id

[ffffff]ADD 100 DAILY LIKES: [FFFF00]
 /like id
 
[ffffff]GET PLAYEUR INFO : [FFFF00]
 ++ id
 
[ffffff]CHECK IF A PLAYER IS BANNED: [FFFF00]
 /check id

[ffffff]SEND FRIEND REQUEST SPAM: [FFFF00]
 /spam id

[ffffff]SEND VISITS: [FFFF00]
 /visits id

[ffffff]TALK WITH AI: [90EE90]
 /q [your text here]

[ffffff]SEND SQUAD-JOIN SPAM: [90EE90]
 /pp/id

[ffffff]SEND ROOM SPAM TO A PLAYER: [90EE90]
 /sp/id
 
[ffffff]LAG + FORCE START [ATTACK]:[FF9000]
 /str [teamcode]

[ffffff] JOIN TEAMCODE :[FF9000]
 /join [teamcode]

[ffffff] LAG IN TEAMCODE :[FF9000]
 /lag [teamcode]

[ffffff]Follow me on [808000]TikTok [ffffff]and [FF0000]Youtube: \n[FF9000]@iamdeveco \n''', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))

                        time.sleep(0.5)
                        self.CLients.close() ; self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

# /////////////////////////////////////////////////
                # --- /like command ---
                elif '/like' in self.InputMsg[:5]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    id = self.InputMsg[6:]
                    self.Zx = ChEck_Commande(id)
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /like but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] SendinG LiKes To {xMsGFixinG(id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.2)
                        mssg = send_likes(id)
                        self.CLients.send(xSEndMsg(mssg,  1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.5)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /spam command ---
                elif '/spam' in self.InputMsg[:5]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    id = self.InputMsg[6:]
                    self.Zx = ChEck_Commande(id)
                    client_id = str(uid)

                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /spam but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] Sending request to {xMsGFixinG(id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.2)
                        mssg = spam_requests(id, self.region)
                        self.CLients.send(xSEndMsg(mssg,  1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.5)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /q command ---
                elif '/q' in self.InputMsg[:2]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    question = self.InputMsg[2:]
                    client_id = str(uid)

                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /q but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] Question sending in ai "{xMsGFixinG(question)}"\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.2)
                        mssg = talk_with_ai(question)
                        self.CLients.send(xSEndMsg(mssg,  1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.5)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /check command ---
                elif self.InputMsg.startswith('/check'):
                    parts = self.InputMsg.split(maxsplit=1)
                    if len(parts) < 2:
                        self.CLients.send(
                            xSEndMsg("[c][FF0000]⚠️  Please enter an ID after /check.", 1, uid, self.AccounT_Uid, key,
                                     iv))
                        return

                    id = parts[1].strip()
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    self.Zx = ChEck_Commande(id)
                    client_id = str(uid)

                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /check but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] Check account {xMsGFixinG(id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.2)
                        mssg = check_banned_status(id)
                        self.CLients.send(xSEndMsg(mssg,  1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.5)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /visit command ---
                elif self.InputMsg.startswith('/visits'):
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    id = self.InputMsg[7:]
                    self.Zx = ChEck_Commande(id)
                    client_id = str(uid)

                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /visit but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] SendinG Visits To {xMsGFixinG(id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.2)
                        mssg = visits(id, self.region)
                        self.CLients.send(xSEndMsg(mssg,  1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.5)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- ++ command ---
                elif '++' in self.InputMsg[:2]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    id = self.InputMsg[3:]
                    self.Zx = ChEck_Commande(id)
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried ++ but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[{ArA_CoLor()}] GeTinG InFo FoR {xMsGFixinG(id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.5)
                        self.CLients.send(xSEndMsg(GeT_PLayer_InFo(id, Token),  1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.5)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /5 command ---
                if self.InputMsg.startswith('/5'):
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /5 but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][90EE90]GeneRaTinG 5 in SQuid\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.3)
                        self.CLients2.send(OpEnSq(key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(cHSq(5, self.DeCode_CliEnt_Uid, key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(SEnd_InV(2, self.DeCode_CliEnt_Uid, self.region, key, iv))
                        time.sleep(3)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /6 command ---
                if self.InputMsg.startswith('/6'):
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /6 but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}]GeneRaTinG 6 in SQuid\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.3)
                        self.CLients2.send(OpEnSq(key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(cHSq(6, self.DeCode_CliEnt_Uid, key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(SEnd_InV(2, self.DeCode_CliEnt_Uid, self.region, key, iv))
                        time.sleep(4)
                        self.CLients.close();
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /3 command ---
                if self.InputMsg.startswith('/3'):

                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /3 but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}]GeneRaTinG 3 in SQuid\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.3)
                        self.CLients2.send(OpEnSq(key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(cHSq(3, self.DeCode_CliEnt_Uid, key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(SEnd_InV(2, self.DeCode_CliEnt_Uid, self.region, key, iv))
                        time.sleep(3)
                        self.CLients2.send(leave_s(key, iv))
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /c5/ command ---
                elif '/c5/' in self.InputMsg[:4]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    id = self.InputMsg[4:]
                    self.Zx = ChEck_Commande(id)
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /c5/ but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] 5 in SQuid To {xMsGFixinG(id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.3)
                        self.CLients2.send(OpEnSq(key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(cHSq(5, self.DeCode_CliEnt_Uid, key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(SEnd_InV(2, id, self.region, key, iv))
                        time.sleep(4)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /c6/ command ---
                elif '/c6/' in self.InputMsg[:4]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    id = self.InputMsg[4:]
                    self.Zx = ChEck_Commande(id)
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /c6/ but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] 6 in SQuid To {xMsGFixinG(id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))

                        time.sleep(0.3)
                        self.CLients2.send(OpEnSq(key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(cHSq(6, self.DeCode_CliEnt_Uid, key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(SEnd_InV(2, id, self.region, key, iv))
                        time.sleep(4)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /c3/ command ---
                elif '/c3/' in self.InputMsg[:4]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    id = self.InputMsg[4:]
                    self.Zx = ChEck_Commande(id)
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /c3/ but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] 3 in SQuid To {xMsGFixinG(id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.3)
                        self.CLients2.send(OpEnSq(key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(cHSq(3, self.DeCode_CliEnt_Uid, key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(SEnd_InV(2, id, self.region, key, iv))
                        time.sleep(4)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /get/ command ---
                elif '/get/' in self.InputMsg[:5]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    id = self.InputMsg[5:]
                    self.Zx = ChEck_Commande(id)
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /get/ but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] GeTinG PLayer {xMsGFixinG(id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.3)
                        self.CLients2.send(OpEnSq(key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(cHSq(5, self.DeCode_CliEnt_Uid, key, iv))
                        time.sleep(0.3)
                        self.CLients2.send(SEnd_InV(1, id, self.region, key, iv))
                        time.sleep(0.1)
                        self.CLients2.send(SEnd_InV(1, self.DeCode_CliEnt_Uid, self.region, key, iv))
                        time.sleep(4)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 


                # --- /pp command ---
                elif '/pp/' in self.InputMsg[:4]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    self.id = self.InputMsg[4:]
                    self.Zx = ChEck_Commande(self.id)
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /pp but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] SenDinG Spam To {xMsGFixinG(self.id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.1)
                        for i in range(99):
                            threading.Thread(
                                target=lambda: self.CLients2.send(SPamSq(self.id, self.region, key, iv))).start()
                            time.sleep(0.1)
                        time.sleep(0.1)
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][90EE90]SuccEss SendinG SPam\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # --- /sp command ---
                elif '/sp/' in self.InputMsg[:4]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    self.id, self.nm = (
                        self.InputMsg[4:].split(" ", 1) if " " in self.InputMsg[4:] else [self.InputMsg[4:], "THUG4FF"])
                    self.Zx = ChEck_Commande(self.id)
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /sp but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] Spam Room To {xMsGFixinG(self.id)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        try:
                            self.CLients2.send(GeT_Status(self.id, key, iv))
                            time.sleep(0.3)
                        except:
                            pass

                        if '0f00' in self.data2.hex()[:4]:
                            try:
                                packet = self.data2.hex()[10:]
                                self.thug4ff_data = json.loads(DeCode_PackEt(packet))
                                self.room_uid = self.thug4ff_data['5']['data']['1']['data']['15']['data']
                                for i in range(100):
                                    threading.Thread(target=lambda: self.CLients2.send(
                                        SPam_Room(self.id, self.room_uid, self.nm, key, iv))).start()
                                time.sleep(0.1)
                                self.CLients.send(xSEndMsg(
                                    f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][90EE90]SuccEss SEndinG SPam Room\n''',
                                     1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                                ))
                                time.sleep(0.1)
                                self.CLients.close()
                                self.CLients2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                            except:
                                pass

                # --- /st command ---
                if '/str' in self.InputMsg[:4]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    self.teamcode = self.InputMsg[5:]
                    self.Zx = ChEck_Commande(self.teamcode)
                    client_id = str(uid)

                    # Vérification blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /st but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # Vérification permissions
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] A join attack has started on Team Code {xMsGFixinG(self.teamcode)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.1)

                        attack_start_time = time.time()
                        while time.time() - attack_start_time < 30:
                            threading.Thread(
                                target=lambda: self.CLients2.send(join_teamcode(self.teamcode, key, iv))).start()
                            self.CLients2.send(start_autooo(key, iv))
                            self.CLients2.send(leave_s(key, iv))
                            time.sleep(0.15)

                        time.sleep(0.1)
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][90EE90]SuccEss Attack {xMsGFixinG(self.teamcode)} \n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # /////////////////////////////////////////////////

                if self.InputMsg.startswith('/join'):
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)
                    self.teamcode = self.InputMsg[6:]
                    self.Zx = ChEck_Commande(self.teamcode)

                    # 🚫 Vérifie d'abord si l'utilisateur est dans la blacklist
                    client_id = str(uid)
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /join but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

                    # ✅ Si le joueur est autorisé
                    else:
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][{ArA_CoLor()}] Joined Team Code {xMsGFixinG(self.teamcode)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.1)

                        self.CLients2.send(join_teamcode(self.teamcode, key, iv))
                        time.sleep(0.1)

                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][90EE90] Successfully joined {xMsGFixinG(self.teamcode)} \n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.1)


                # 🌀 Commande /lag
                if self.InputMsg.startswith('/lag'):
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)

                    self.teamcode = self.InputMsg[5:]
                    repeat_count = 1
                    self.Zx = ChEck_Commande(self.teamcode)

                    # 🚫 Vérifie la blacklist
                    if client_id in black:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][FF0000] Access Denied!\n\nUser {xMsGFixinG(self.name)} is in the Blacklist.\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        print(f"[BLOCKED] UID {client_id} tried /lag but is blacklisted.")
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                        return

         
                    else :
                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n
                [b][c][{ArA_CoLor()}] [B][32CD32]Starting lag in {xMsGFixinG(self.teamcode)}\n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))
                        time.sleep(0.1)

                        if repeat_count > 3:
                            repeat_count = 3

                        for i in range(repeat_count):
                            if repeat_count > 1:
                                self.CLients.send(xSEndMsg(
                                    f'''\n[C][B][FFA500]Running batch {i + 1} of {repeat_count}...\n''',
                                     1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                                ))

                            for _ in range(33333):
                                self.CLients2.send(join_teamcode(self.teamcode, key, iv))
                                time.sleep(0.0001)
                                self.CLients2.send(leave_s(key, iv))
                                time.sleep(0.0001)

                            if repeat_count > 1 and i < repeat_count - 1:
                                time.sleep(0.1)

                            time.sleep(0.1)

                        self.CLients.send(xSEndMsg(
                            f'''\n[b][c][FFD3EF] User : {xMsGFixinG(self.name)}\n\n[b][c][90EE90] Successfully lagged {xMsGFixinG(self.teamcode)} \n''',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv
                        ))

                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 
                                                         
                elif '/all' in self.InputMsg[:4]:
                        json_result = get_available_room(data.hex()[10:])
                        # print(data.hex())
                        parsed_data = json.loads(json_result)
                        uid = parsed_data["5"]["data"]["1"]["data"]
                        msg = self.InputMsg[5:]
                        if client_id in owner:
                            for i in range(5):
                                self.CLients.send(xSEndMsg(f'[b][c][{ArA_CoLor()}]{msg}', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.5)
                            time.sleep(0.3)
                            self.CLients.close() ; self.CLients2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )
                        else:
                                self.CLients.send(xSEndMsg(f'[b][c]\nOnly the leader can use this feature!\n', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.1)
                                self.CLients.close() ; self.CLients2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

                elif '/owner' in self.InputMsg[:6]:
                    json_result = get_available_room(data.hex()[10:])
                        # print(data.hex())
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)
                    if client_id in ownerr:
                        self.CLients.send(xSEndMsg(f'''[b][c]
     [ffffff]   Welcome, Leader\n\n => {self.name} <=

     [FFD700]  First, we have the Blacklist commands:
                             
     [90EE90]Add ID to the blacklist\n\n[ffffff]=> /add id	 
          
     [90EE90]Remove ID from the blacklist\n\n[ffffff]=> /delete id	 
     
     [90EE90]Show IDs in the list\n\n[ffffff]=> /show
     
     [90EE90]Delete all IDs in the list\n\n[ffffff]=> /clear\n''', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.5)
     #                    self.CLients.send(xSEndMsg(f'''[b][c]
     # [FFD700]  Second, we have commands to approve a member to use the bot even if they don't have the tag:
     #
     # [90EE90]Approve user to use the bot\n\n[ffffff]=> /approve id
     #
     # [90EE90]De-approve user without tag\n\n[ffffff]=> /deapprove id
     #
     # [90EE90]Show IDs in the list\n\n[ffffff]=> /list
     #
     # [90EE90]Delete all IDs in the list\n\n[ffffff]=> /clr/approvs\n''', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.5)
                        self.CLients.send(xSEndMsg(f'''[b][c]
     [FFD700]  Third, we only have two secondary commands:
                             
     [90EE90]Repeat your message for an announcement\n\n[ffffff]=> /all msg	 
          
     [90EE90]Shut down the bot for a specific duration \n\n[ffffff]=> /shotdown (1h/1min/etc...)	 
     
    [FFD700]  Devloper : @iamdeveco\n''', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.3)
                        self.CLients.close() ; self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )
                    else:
                        self.CLients.send(xSEndMsg(f'[b][c]\nOnly the leader can use this feature!\n', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.1)
                        self.CLients.close() ; self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

                elif '/add' in self.InputMsg[:4]:
                        json_result = get_available_room(data.hex()[10:])
                        # print(data.hex())
                        parsed_data = json.loads(json_result)
                        uid = parsed_data["5"]["data"]["1"]["data"]
                        client_id = str(uid)
                        id = self.InputMsg[5:]
                        Req = Add_Black(int(id))
                        if client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and True == Req:
                            self.CLients.send(xSEndMsg(f'\n[b][c][90EE90] [SuccEssFuLLy] AddinG !\n\n[{ArA_CoLor()}] Uid : {xMsGFixinG(id)}\n\n To BLack LisTe !\n\n[ffffff] By Owner : {self.name}\n', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.1)
                            self.CLients.close() ; self.CLients2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

                        if client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and False == Req:
                            self.CLients.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] [Error] AddinG becausse you are not the owner  !\n\n Uid : {xMsGFixinG(id)}\n', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                            time.sleep(0.1)
                            self.CLients.close() ; self.CLients2.close()
                            self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

                        elif client_id not in ownerr:

                                self.CLients.send(xSEndMsg(f'[b][c]\nOnly the leader can use this feature!\n', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                                time.sleep(0.1)
                                self.CLients.close() ; self.CLients2.close()
                                self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

                elif '/show' in self.InputMsg[:5]:
                    json_result = get_available_room(data.hex()[10:])
                        # print(data.hex())
                    parsed_data = json.loads(json_result)
                    # pprint(parsed_data)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    Req = Show_Uids()
                    client_id = str(uid)
                    print(client_id)
                    if client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner:
                        self.CLients.send(xSEndMsg(f'\n[b][c] Uids In BLack LisTe :\n\n{xMsGFixinG(Req)}\n', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

                    elif client_id in ownerr and False == Req:
                        self.CLients.send(xSEndMsg(f'\n[b][c][{ArA_CoLor()}] Uids In BLack Liste NoT Found !\n', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

                    elif client_id not in ownerr:
                        self.CLients.send(xSEndMsg(f'[b][c]\nOnly the Owner can use this feature!\n', 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.1)
                        self.CLients.close()
                        self.CLients2.close()
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )

                elif '/delete' in self.InputMsg[:7]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)
                    id = self.InputMsg[8:]
                    Req = Rem_Black(id)

                    if client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][90EE90][SuccEssFuLLy] RemovinG !\n\n[{ArA_CoLor()}] Uid : {xMsGFixinG(id)}\n\nFrom BLack LisTe !\n\n[ffffff]By Owner : {self.name}\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    elif client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and not Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][{ArA_CoLor()}] Uid : {xMsGFixinG(id)} NoT Found In BLack LisTe!\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    else:
                        self.CLients.send(xSEndMsg(
                            f'[b][c]\nOnly the Owner can use this feature!\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))

                    time.sleep(0.1)
                    self.CLients.close()
                    self.CLients2.close()
                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                elif '/clear' in self.InputMsg[:6]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)
                    Req = Clear()

                    if client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][90EE90][SuccEssFuLLy] - CLearinG !\n\n[{ArA_CoLor()}] BLack LisTe CleareD !\n\n[ffffff]By Owner : {self.name}\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    elif client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and not Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][{ArA_CoLor()}] BLack LisTe Already Empty !\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    else:
                        self.CLients.send(xSEndMsg(
                            f'[b][c]\nOnly the Owner can use this feature!\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))

                    time.sleep(0.1)
                    self.CLients.close()
                    self.CLients2.close()
                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                elif '/approve' in self.InputMsg[:8]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)
                    id = self.InputMsg[9:]
                    Req = Approved(id)

                    if client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][90EE90][SuccEssFuLLy] AddinG !\n\n[{ArA_CoLor()}] Uid : {xMsGFixinG(id)}\n\nTo ApproVEd LisT !\n\n[ffffff]By Owner : {self.name}\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    elif client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and not Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][{ArA_CoLor()}] [Error] AddinG !\n\n Uid : {xMsGFixinG(id)} Already ApproVEd!\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    else:
                        self.CLients.send(xSEndMsg(
                            f'[b][c]\nOnly the Owner can use this feature!\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))

                    time.sleep(0.1)
                    self.CLients.close()
                    self.CLients2.close()
                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                elif '/deapprove' in self.InputMsg[:10]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)
                    id = self.InputMsg[11:]
                    Req = DeApproved(id)

                    if client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][90EE90][SuccEssFuLLy] RemovinG !\n\n[{ArA_CoLor()}] Uid : {xMsGFixinG(id)}\n\nFrom ApproVEd LisT !\n\n[ffffff]By Owner : {self.name}\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    elif client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and not Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][{ArA_CoLor()}] Uid : {xMsGFixinG(id)} NoT Found In ApproVEd LisT!\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    else:
                        self.CLients.send(xSEndMsg(
                            f'[b][c]\nOnly the Owner can use this feature!\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))

                    time.sleep(0.1)
                    self.CLients.close()
                    self.CLients2.close()
                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                elif '/list' in self.InputMsg[:5]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)
                    Req = Show_Approvs()

                    if client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c] Uids In ApproVEd LisT :\n\n{xMsGFixinG(Req)}\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    elif client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and not Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][{ArA_CoLor()}] Uids In ApproVEd LisT NoT Found !\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    else:
                        self.CLients.send(xSEndMsg(
                            f'[b][c]\nOnly the Owner can use this feature!\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))

                    time.sleep(0.1)
                    self.CLients.close()
                    self.CLients2.close()
                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                elif '/clr/approvs' in self.InputMsg[:12]:
                    json_result = get_available_room(data.hex()[10:])
                    parsed_data = json.loads(json_result)
                    uid = parsed_data["5"]["data"]["1"]["data"]
                    client_id = str(uid)
                    Req = Clear_Approvs()

                    if client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][90EE90][SuccEssFuLLy] - CLearinG !\n\n[{ArA_CoLor()}] ApproVEd LisT CleareD !\n\n[ffffff]By Owner : {self.name}\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    elif client_id in ownerr or EnC_Uid(client_id, Tp='Uid') in owner and not Req:
                        self.CLients.send(xSEndMsg(
                            f'\n[b][c][{ArA_CoLor()}] ApproVEd LisT Already Empty !\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                    else:
                        self.CLients.send(xSEndMsg(
                            f'[b][c]\nOnly the Owner can use this feature!\n',
                             1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))

                    time.sleep(0.1)
                    self.CLients.close()
                    self.CLients2.close()
                    self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) 

                # Original: elif '/shotdown' in self.InputMsg[:9]:
                elif '/shotdown' in self.InputMsg[:9]:
                        json_result = get_available_room(data.hex()[10:])
                            # print(data.hex())
                        parsed_data = json.loads(json_result)
                        uid = parsed_data["5"]["data"]["1"]["data"]

                        self.time = self.InputMsg[10:]
                        if 'h' in self.time:
                                hours = int(self.time.replace('h', ''))
                                sleep_time = timedelta(hours=hours)
                        elif 'min' in self.time:
                            minutes = int(self.time.replace('min', ''))
                            sleep_time = timedelta(minutes=minutes)
                        else:
                            print("Invalid time format.")
                        end_time = datetime.now() + sleep_time
                        end_time = end_time.strftime('%d/%m/%y - %I:%M%p')
                        self.CLients.send(xSEndMsg(f"\n[b][c][90EE90][SuccEssFuLLy] ShoT Down ! \n\n[{ArA_CoLor()}] For : {self.time}\n\n ResTartinG At :\n\n  {xMsGFixinG(end_time)}\n\n[ffffff] By Owner : {self.name} ! \n", 1 , Guild_Uid , self.DeCode_CliEnt_Uid , key , iv))
                        time.sleep(0.3)
                        self.CLients.close() , self.CLients2.close()
                        time.sleep(sleep_time.total_seconds())
                        self.Connect_SerVer(Token , tok , host , port , key , iv , host2 , port2 , Guild_Uid , Auth_Code) (Token , tok , host , port , key , iv , host2 , port2 )
                        time.sleep(0.3)
                        restart_program()
            except Exception as e:
                pass




    def GeT_Key_Iv(self, serialized_data):
        """Extrait le timestamp, la clé et l'IV d'un message Protobuf."""
        my_message = xKEys.MyMessage()
        my_message.ParseFromString(serialized_data)

        timestamp, key, iv = my_message.field21, my_message.field22, my_message.field23
        timestamp_obj = Timestamp()
        timestamp_obj.FromNanoseconds(timestamp)
        timestamp_seconds = timestamp_obj.seconds
        timestamp_nanos = timestamp_obj.nanos
        combined_timestamp = timestamp_seconds * 1_000_000_000 + timestamp_nanos

        return combined_timestamp, key, iv

    def Guest_GeneRaTe(self, uid, password):
        """Génère un jeton invité Garena."""
        self.url = "https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant"
        self.headers = {
            "Host": "ffmconnect.live.gop.garenanow.com",
            "User-Agent": "GarenaMSDK/4.0.19P4(G011A; Android 9; en; US;)",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "close"
        }

        self.dataa = {
            "uid": f"{uid}",
            "password": f"{password}",
            "response_type": "token",
            "client_type": "2",
            "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
            "client_id": "100067",
        }

        try:
            self.response = requests.post(self.url, headers=self.headers, data=self.dataa)

            # log status
            if self.response.status_code == 200:
                print("[SUCCESS] Guest_GeneRaTe → status 200")
            else:
                print(f"[ERROR] Guest_GeneRaTe → status {self.response.status_code}")

            self.response.raise_for_status()
            self.response = self.response.json()

            self.Access_ToKen = self.response['access_token']
            self.Access_Uid = self.response['open_id']

            # print(self.Access_ToKen, self.Access_Uid)
            time.sleep(0.2)

            return self.ToKen_GeneRaTe(self.Access_ToKen, self.Access_Uid)

        except Exception as e:
            print(f"[ERROR] Guest_GeneRaTe: {e}")
            restart_program()


    def GeT_LoGin_PorTs(self, JwT_ToKen, PayLoad):
        """Récupère les IP et ports de connexion."""

        self.UrL = 'https://clientbp.ggwhitehawk.com/GetLoginData'
        self.HeadErs = {
            'Expect': '100-continue',
            'Authorization': f'Bearer {JwT_ToKen}',
            'X-Unity-Version': '2018.4.11f1',
            'X-GA': 'v1 1',
            'ReleaseVersion': 'OB51',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)',
            'Host': 'clientbp.ggblueshark.com',
            'Connection': 'close',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        try:
            self.Res = requests.post(self.UrL, headers=self.HeadErs, data=PayLoad, verify=False)

            if self.Res.status_code == 200:
                print("[SUCCESS] GeT_LoGin_PorTs → status 200")
            else:
                print(f"[ERROR] GeT_LoGin_PorTs → status {self.Res.status_code}")

            self.thug4ff_data = json.loads(DeCode_PackEt(self.Res.content.hex()))
            #pprint(self.thug4ff_data)  
            # something brute

            address, address2 = self.thug4ff_data['32']['data'], self.thug4ff_data['14']['data']
            ip, ip2 = address[:-6], address2[:-6]
            port, port2 = address[-5:], address2[-5:]

            try:
                self.Guild_Uid, self.Auth_Code = self.thug4ff_data['20']['data'], self.thug4ff_data['55']['data']
            except:
                self.Guild_Uid, self.Auth_Code = None, None

            return ip, port, ip2, port2

        except requests.RequestException:
            print(" - Bad Requests !")
        except Exception as e:
            print(f" - Failed To GeT PorTs ! ({e})")

        return None, None, None, None

    def Get_playload_by_data(self, JWT_TOKEN, NEW_ACCESS_TOKEN, date):
        """Génère le payload chiffré pour la requête login."""
        try:
            import base64
            token_payload_base64 = JWT_TOKEN.split('.')[1]
            token_payload_base64 += '=' * ((4 - len(token_payload_base64) % 4) % 4)
            decoded_payload = json.loads(base64.urlsafe_b64decode(token_payload_base64).decode('utf-8'))

            NEW_EXTERNAL_ID = decoded_payload['external_id']
            SIGNATURE_MD5 = decoded_payload['signature_md5']
            now = str(datetime.now())[:19]

            PAYLOAD = b':\x071.111.2\xaa\x01\x02ar\xb2\x01 55ed759fcf94f85813e57b2ec8492f5c\xba\x01\x014\xea\x01@6fb7fdef8658fd03174ed551e82b71b21db8187fa0612c8eaf1b63aa687f1eae\x9a\x06\x014\xa2\x06\x014'
            PAYLOAD = PAYLOAD.replace(b"2023-12-24 04:21:34", now.encode())
            PAYLOAD = PAYLOAD.replace(b"15f5ba1de5234a2e73cc65b6f34ce4b299db1af616dd1dd8a6f31b147230e5b6", NEW_ACCESS_TOKEN.encode())
            PAYLOAD = PAYLOAD.replace(b"4666ecda0003f1809655a7a8698573d0", NEW_EXTERNAL_ID.encode())
            PAYLOAD = PAYLOAD.replace(b"7428b253defc164018c604a1ebbfebdf", SIGNATURE_MD5.encode())

            PAYLOAD = PAYLOAD.hex()
            PAYLOAD = encrypt_api(PAYLOAD)
            PAYLOAD = bytes.fromhex(PAYLOAD)

            return PAYLOAD

        except Exception as e:
            print(f"Error in Get_playload_by_data: {e}")
            return None

    def ToKen_GeneRaTe(self, Access_ToKen, Access_Uid):
        """Génère un JWT Token complet avec les clés et ports."""
        self.UrL = "https://loginbp.ggwhitehawk.com/MajorLogin"
        self.HeadErs = {
            'X-Unity-Version': '2018.4.11f1',
            'ReleaseVersion': 'OB51',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-GA': 'v1 1',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
            'Host': 'https://loginbp.ggwhitehawk.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }

        self.ResPonse, self.PaYload = process_token(Access_ToKen, Access_Uid)

        if self.ResPonse.status_code == 200 and len(self.ResPonse.text) > 10:
            print("[SUCCESS] ToKen_GeneRaTe → status 200")
            self.thug4ff_data = json.loads(DeCode_PackEt(self.ResPonse.content.hex()))
            self.JwT_ToKen = self.thug4ff_data['8']['data']
            self.combined_timestamp, self.key, self.iv = self.GeT_Key_Iv(self.ResPonse.content)

            self.PLALOADD = self.Get_playload_by_data(self.JwT_ToKen, Access_ToKen, 1)


            ip, port, ip2, port2 = self.GeT_LoGin_PorTs(self.JwT_ToKen, self.PLALOADD)
            return self.JwT_ToKen, self.key, self.iv, self.combined_timestamp, ip, port, ip2, port2
        else:
            print(f"[ERROR] ToKen_GeneRaTe → status {self.ResPonse.status_code}")
            sys.exit()

    def Get_FiNal_ToKen_0115(self):
        token , key , iv , Timestamp , ip , port , ip2 , port2 = self.Guest_GeneRaTe(self.id, self.password)
        self.JwT_ToKen = token              
        try:
            self.AfTer_DeC_JwT = jwt.decode(token, options={"verify_signature": False})
            self.AccounT_Uid = self.AfTer_DeC_JwT.get('account_id')
            self.EncoDed_AccounT = hex(self.AccounT_Uid)[2:]
            self.HeX_VaLue = DecodE_HeX(Timestamp)
            self.TimE_HEx = self.HeX_VaLue
            self.JwT_ToKen_ = token.encode().hex()


            account_id = self.AfTer_DeC_JwT.get('account_id')
            nickname = self.AfTer_DeC_JwT.get('nickname')
            region = self.AfTer_DeC_JwT.get('lock_region')
            self.region =region
            client_version = self.AfTer_DeC_JwT.get('client_version')
            print("Retrieving client data...")
            print(f"""
Client Data Retrieved Successfully:

Client ID      : {account_id}
Nickname       : {nickname}
Guild ID       : {self.Guild_Uid}
Guild Auth     : {self.Auth_Code}
Region         : {region}
Client Version : {client_version}
""") 

        except Exception as e:
            print(f"- Error In ToKen : {e}")
            return
        try:
            self.Header = hex(len(EnC_PacKeT(self.JwT_ToKen_ , key , iv)) // 2)[2:]
            length = len(self.EncoDed_AccounT)
            self.__ = '00000000'
            if length == 9: self.__ = '0000000'
            elif length == 8: self.__ = '00000000'
            elif length == 10: self.__ = '000000'
            elif length == 7: self.__ = '000000000'
            else:
                print('Unexpected length encountered')                
            self.Header = f'0115{self.__}{self.EncoDed_AccounT}{self.TimE_HEx}00000{self.Header}'
            self.FiNal_ToKen_0115 = self.Header + EnC_PacKeT(self.JwT_ToKen_ , key , iv)
        except Exception as e:
            print(f" - Erorr In Final Token : {e}")
        self.AutH_ToKen = self.FiNal_ToKen_0115

        self.Connect_SerVer(self.JwT_ToKen , self.AutH_ToKen , ip , port , key , iv , ip2 , port2 , self.Guild_Uid , self.Auth_Code)       
        return self.AutH_ToKen , key , iv