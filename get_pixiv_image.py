from pathlib import Path
from pixivapi import Size
from pixivapi import Client
from config import *
import os

def main():
    client = Client()
    client.login(ID, PSWD)
    artistID = str(input("artistID:"))
    folder = Path.cwd() / "images" / artistID
    if not os.path.exists(folder): os.makedirs(folder)
    res = client.fetch_user_illustrations(artistID)
    while True:
        for illust in res['illustrations']: illust.download(directory=folder, size=Size.ORIGINAL)
        if not res['next']: break
        res = client.fetch_user_illustrations(artistID, offset=res['next'])

if __name__ == "__main__":
    try: main()
    except Exception as e: print(e)