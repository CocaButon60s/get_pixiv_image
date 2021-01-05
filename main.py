import eel, os, pickle
from pathlib import Path
from pixivapi import Size, Client
from pixivapi.errors import LoginError

client = Client()
USER_INFO_PATH = str(Path.home())+"/.config/get_pixiv_image/conf.pickle"

def store_user_info(id, pswd):
    folder = os.path.dirname(USER_INFO_PATH)
    if not os.path.exists(folder): os.makedirs(folder)
    with open(USER_INFO_PATH, "wb") as f: pickle.dump([id, pswd], f)

@eel.expose
def login(id, pswd):
    try:
        client.login(id, pswd)
        store_user_info(id, pswd)
        return "SUCCESS"
    except Exception as e: return "ERR:LOGIN" if type(e) == LoginError else "ERR"

@eel.expose
def load_user_info():
    if not os.path.exists(USER_INFO_PATH): return ["", ""]
    with open(USER_INFO_PATH, "rb") as f: info = pickle.load(f)
    return info

@eel.expose
def get_image(id):
    folder = Path.cwd() / "images" / id
    if not os.path.exists(folder): os.makedirs(folder)
    try:
        res = client.fetch_user_illustrations(id)
        while True:
            for illust in res['illustrations']: illust.download(directory=folder, size=Size.ORIGINAL)
            if not res['next']: break
            res = client.fetch_user_illustrations(id, offset=res['next'])
        return "SUCCESS"
    except Exception as e:
        os.rmdir(folder)
        return "ERR"

def main():
    eel.init("web/dist")
    eel.start("index.html")

if __name__ == "__main__":
    try:main()
    except Exception as e: print(e)