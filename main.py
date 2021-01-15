import eel, os, pickle, sys
from pathlib import Path
from pixivapi import Size, Client
from pixivapi.errors import LoginError

client = Client()
USER_INFO_PATH = str(Path.home())+"/.config/get_pixiv_image/conf.pickle"
STORAGE = ""
ID = ""
OFFSET = None
IS_CANCELED = False
CNT = 0

def store_user_info(id, pswd):
    folder = os.path.dirname(USER_INFO_PATH)
    if not os.path.exists(folder): os.makedirs(folder)
    with open(USER_INFO_PATH, "wb") as f: pickle.dump([id, pswd], f)

@eel.expose
def py_login(id, pswd):
    try:
        client.login(id, pswd)
        store_user_info(id, pswd)
        return "SUCCESS"
    except Exception as e: return "ERR:LOGIN" if type(e) == LoginError else "ERR"

@eel.expose
def py_load_user_info():
    if not os.path.exists(USER_INFO_PATH): return ["", ""]
    with open(USER_INFO_PATH, "rb") as f: info = pickle.load(f)
    return info

@eel.expose
def py_set_target(id):
    global STORAGE
    global ID
    global OFFSET
    global IS_CANCELED
    global CNT

    ID = id
    STORAGE = Path.cwd() / "images" / ID
    if not os.path.exists(STORAGE): os.makedirs(STORAGE)
    OFFSET = None
    IS_CANCELED = False
    CNT = 0

@eel.expose
def py_cancel():
    global IS_CANCELED

    IS_CANCELED = True

@eel.expose
def py_get_image():
    global OFFSET
    global CNT

    try:
        if IS_CANCELED: return "CANCEL"
        if OFFSET is not None: res = client.fetch_user_illustrations(ID, offset=OFFSET)
        else: res = client.fetch_user_illustrations(ID)
        for illust in res['illustrations']: illust.download(directory=STORAGE, size=Size.ORIGINAL)
        if res['next'] is None: return "SUCCESS"
        OFFSET = res['next']
        CNT = CNT + 1
        return CNT
    except Exception as e:
        os.rmdir(STORAGE)
        return "ERR"

def onCloseWindow(page, sockets):
    print(sockets)
    print(page + 'が閉じられました。プログラムを終了します')
    sys.exit()

def main():
    eel.init("web/dist")
    eel.start("index.html", close_callback=onCloseWindow)

if __name__ == "__main__":
    try:main()
    except Exception as e: print(e)