import os

from flask import Flask, redirect
from PayGmailScraper import authorize, oauth2callback

from zaim_pay_importer import ZaimPayImporter

app = Flask(__name__)
app.secret_key = "your-secret-key"

# 開発環境で HTTPS を使用しない場合の設定
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# credentials_web.jsonのパスを指定　指定しない場合は環境変数から取得
CREDENTIALS_PATH = "credentials_web.json"


@app.route("/")
def index():
    try:
        CONSUMER_ID = "xxxxxxxxxxx"
        CONSUMER_SECRET = "xxxxxxxxxx"
        ACCESS_TOKEN = "xxxxxxxxxx"
        ACCESS_TOKEN_SECRET = "xxxxxxxxxx"
        EXCLUDE_SET = {"amazon", "チャージ", "チヤージ", "charge", "jr east mobile suica"}

        client = ZaimPayImporter(
            CONSUMER_ID,
            CONSUMER_SECRET,
            ACCESS_TOKEN,
            ACCESS_TOKEN_SECRET,
            EXCLUDE_SET,
            "web",
        )
        client.import_ana_pay()
        client.import_rakuten_pay()
        return "インポート完了"
    except Exception as e:
        print(f"Error: {e}")
        return redirect("/authorize")


@app.route("/authorize")
def authorize_route():
    return authorize(CREDENTIALS_PATH)


@app.route("/oauth2callback")
def oauth2callback_route():
    return oauth2callback()


if __name__ == "__main__":
    app.run()
