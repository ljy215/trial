import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import socket
import socks
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7890)  # 修改为你的代理地址
socket.socket = socks.socksocket
def get_google_credentials():
    print("[DEBUG] 正在尝试通过 Gmail 发送邮件...")
    creds = None
    token_path = "token.json"

    if os.path.exists(token_path):
        with open(token_path, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # ✅ 改成命令行授权，不再监听本地端口
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, "wb") as token:
            pickle.dump(creds, token)

    return creds
