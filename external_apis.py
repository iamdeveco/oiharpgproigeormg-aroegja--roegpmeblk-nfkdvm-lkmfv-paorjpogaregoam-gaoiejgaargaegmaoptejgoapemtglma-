import requests
import json
from datetime import datetime
import requests
from pprint import pprint
# from config import KEY,API_URL
from config.settings import KEY,API_URL
def talk_with_ai(question):
    url = f"https://princeaiapi.vercel.app/prince/api/v1/ask?key=prince&ask={question}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        msg = data["message"]["content"]
        print(msg)
        return msg
    else:
        return "Something went wrong."


def send_likes(uid):
    try: 
        url = f"{API_URL["like_api"]}/like?uid={uid}&region=AG&key={KEY}"
        safe_url = url.replace(KEY, "****")
        print(safe_url)
        likes_api_response = requests.get(url)
        

        # Message par défaut si la requête échoue
        message = """
[fd8da3] Like request failed. Please check your UID and try again later.
"""
        # pprint(likes_api_response.json())
        if likes_api_response.status_code == 200:
            api_json_response = likes_api_response.json()
            status = api_json_response.get("status")

            if status == 1:  # ✅ Succès
                player = api_json_response.get("player", {})
                likes = api_json_response.get("likes", {})

                player_name = player.get("nickname", "Unknown")
                likes_before = likes.get("before", 0)
                likes_after = likes.get("after", 0)
                likes_added = likes.get("added_by_api", 0)

                message = f"""
[b][c][90EE90] Likes Sent Successfully!
[808000]
Nickname : {player_name}
Previous Count : {likes_before} 
Given Likes : +{likes_added}   
Updated Count : {likes_after}   


[C][B][00FFFF]━━━━━━━━━━
[FFB300]    DEVELOPED BY @iamdeveco
[C][B][00FFFF]━━━━━━━━━━

                """

            elif status == 2:  # ⛔ Limite atteinte
                message = """
[b][c][FF0000] You have reached your daily limit of likes. Try again in 24 hours.
"""

            else:  # ❌ Autre erreur
                message = f"""
[b][c][FF0000] Like request failed. Status code from API: {status}
"""     
        #print(message)
        return message
    except Exception as e:
        return f"Error Extern: {str(e)}"
    
    
def check_banned_status(uid):
    try:
        url = f"{API_URL["raw_api"]}/check_ban/{uid}"
        print(url)
        ban_api_response = requests.get(url
            
        )

        # Message par défaut si la requête échoue
        message = """
[b][c] [90EE90] Ban check failed. Please check your UID and try again later.
"""

        if ban_api_response.status_code == 200:
            api_json_response = ban_api_response.json()
            data = api_json_response.get("data", {})

            nickname = data.get("nickname", "Unknown")
            region = data.get("region", "Unknown")
            is_banned = data.get("is_banned", 0)
            period = data.get("period", 0)
            last_login = data.get("last_login", 0)

            # Conversion du timestamp en date lisible
            last_login_str = "Unknown"
            if last_login:
                dt_object = datetime.fromtimestamp(last_login)
                last_login_str = dt_object.strftime("%d[c]-%m[c]-%Y [c]%Hh%M")

            if is_banned == 0:  # ✅ Pas banni
                message = f"""
[b][c][90EE90]  Player is NOT banned.
[808000]
Nickname   : {nickname}  
Region     : {region} 
Last login :  {last_login_str}
[C][B][00FFFF]━━━━━━━━━━
[FFB300]    DEVELOPED BY @iamdeveco
[C][B][00FFFF]━━━━━━━━━━
"""
            elif is_banned == 1:  # ❌ Banni
                message = f"""

[b][c][FF0000]  Player is BANNED!
[808000]
Nickname   : {nickname}  
Region     : {region}  
Period     : more than {period} months
Last login :  {last_login_str}
[C][B][00FFFF]━━━━━━━━━━
[FFB300]    DEVELOPED BY @iamdeveco
[C][B][00FFFF]━━━━━━━━━━
"""
        
        return message

    except Exception as e:
        return f"Error: {str(e)}"


def spam_requests(uid,region):
    try:
        url = f"{API_URL["spam_api"]}/send_requests?uid={uid}&region={region}"
        print(url)
        spam_requests_api = requests.get(
           url
        )

        # Message par défaut si la requête échoue
        message = """
[fd8da3] Send  request friend failed. Please check your UID and try again later.
"""

        if spam_requests_api.status_code == 200:
            result = spam_requests_api.json()
            

            message = f"""
✅ Friend Request Sent !

Nickname : {result.get('nickname', 'Unknown')}
Region : {result.get('region', 'Unknown')}     
Level:{result.get('level', 'Unknown')}
Success:{result.get('success', 'Unknown')}
Failed:{result.get('fail', 'Unknown')}
[C][B][00FFFF]━━━━━━━━━━
[FFB300]    DEVELOPED BY @iamdeveco
[C][B][00FFFF]━━━━━━━━━━

                """
        #print(message)
        return message
    except Exception as e:
        return f"Error Extern: {str(e)}"
    

def visits(uid,region):
    try:
        url =f"{API_URL["visits_api"]}/visits?uid={uid}&region={region}"
        print(url)
        visits_api = requests.get(
            url
        )

        # Message par défaut si la requête échoue
        message = f"""
[fd8da3] Visits  profile {uid} is failed. Please check your UID and try again later.
"""

        if visits_api.status_code == 200:
            result = visits_api.json()
            

            message = f"""
✅ Visit Statistics !
Nickname : {result.get('nickname', 'Unknown')}
Region : {result.get('region', 'Unknown')}     
Level:{result.get('level', 'Unknown')}
Success:{result.get('success', 'Unknown')}
Failed:{result.get('fail', 'Unknown')}
[C][B][00FFFF]━━━━━━━━━━
[FFB300]    DEVELOPED BY @iamdeveco
[C][B][00FFFF]━━━━━━━━━━
                """
        #print(message)
        return message
    except Exception as e:
        return f"Error Extern: {str(e)}"
    
