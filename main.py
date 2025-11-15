import threading
import jwt
import random
import json
import requests
import socket
import os
import sys
import time
import logging
import urllib3
from time import sleep
from client import FF_CLient
from pathlib import Path
from typing import Dict, List, Tuple
from cfonts import render, say
# Allow local imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
ACCOUNTS_FILE = Path(__file__).parent / "accounts.json"
START_DELAY = 0.5      # délai entre démarrages de threads (s)
MAX_THREADS = 100      # nombre max de threads simultanés
RESTART_ON_CRASH = True

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def load_accounts() -> List[Tuple[str, str]]:
    """Charge accounts.json qui peut être:
       - un objet dictionnaire { "id": "password", ... }
       - une liste d'objets [ {"uid": "...", "password": "..."}, ... ]
       Retourne une liste de tuples (id, password)
    """
    try:
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)

        accounts: List[Tuple[str, str]] = []

        if isinstance(raw, dict):
            # format: { "id": "password", ... }
            for k, v in raw.items():
                uid = str(k).strip()
                pwd = str(v).strip()
                if uid and pwd:
                    accounts.append((uid, pwd))

        elif isinstance(raw, list):
            # format: [ {"uid":..., "password":...}, ... ]
            for entry in raw:
                if not isinstance(entry, dict):
                    continue
                # case-insensitive keys
                uid = None
                pwd = None
                for kk, vv in entry.items():
                    if kk.lower() == "uid" or kk.lower() == "id":
                        uid = str(vv).strip()
                    elif kk.lower() == "password" or kk.lower() == "pwd":
                        pwd = str(vv).strip()
                if uid and pwd:
                    accounts.append((uid, pwd))

        else:
            logging.error("Format JSON inconnu dans accounts.json")
            return []

        # dédoublonner en gardant le premier
        seen = set()
        deduped: List[Tuple[str, str]] = []
        for uid, pwd in accounts:
            if uid in seen:
                logging.warning(f"Doublon ignoré pour UID: {uid}")
                continue
            seen.add(uid)
            deduped.append((uid, pwd))

        return deduped

    except FileNotFoundError:
        logging.error(f"Fichier introuvable: {ACCOUNTS_FILE}")
        return []
    except Exception as e:
        logging.exception(f"Erreur lors du chargement des comptes: {e}")
        return []


def run_client(uid: str, password: str):
    """Crée et lance une instance FF_CLient pour un compte.
       On suppose que FF_CLient prend (uid, password) et expose une méthode start().
    """
    logging.info(f"Lancement client -> UID: {uid}")
    try:
        client = FF_CLient(uid, password)
        # si votre client expose une méthode run() ou connect(), modifiez ici
        if hasattr(client, "start"):
            client.start()
        elif hasattr(client, "run"):
            client.run()
        else:
            # fallback: tenter d'appeler la callable si l'objet est callable
            if callable(client):
                client()
            else:
                logging.error(f"FF_CLient pour {uid} n'a pas de méthode start() ni run().")
    except Exception as e:
        logging.exception(f"Erreur lors du démarrage du client {uid}: {e}")


def start_all(max_threads: int = MAX_THREADS, start_delay: float = START_DELAY):
    accounts = load_accounts()
    if not accounts:
        logging.error("Aucun compte chargé. Vérifie accounts.json")
        return

    logging.info(f"{len(accounts)} compte(s) chargé(s). Lancement avec max_threads={max_threads}...")
    # print(render('THUG4FF', colors=['red', 'blue'], align='center'))
    threads: List[threading.Thread] = []

    for idx, (uid, pwd) in enumerate(accounts):
        # contrôle simple du nombre de threads actifs (moins le thread principal)
        while threading.active_count() - 1 >= max_threads:
            time.sleep(0.1)

        t = threading.Thread(target=run_client, args=(uid, pwd), daemon=False, name=f"FF-{uid}")
        threads.append(t)
        t.start()
        time.sleep(start_delay)

    # attendre la fin de tous les threads
    for t in threads:
        t.join()

    logging.info("Tous les clients ont terminé.")


def restart_program():
    logging.info("Redémarrage du programme...")
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    try:
        start_all()
    except Exception:
        logging.exception("Erreur non gérée dans main")
        if RESTART_ON_CRASH:
            restart_program()
        else:
            raise
