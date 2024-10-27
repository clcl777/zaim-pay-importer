from zaim_pay_importer import ZaimPayImporter

if __name__ == "__main__":
    CONSUMER_ID = "xxxxxxxxxxx"
    CONSUMER_SECRET = "xxxxxxxxxx"
    ACCESS_TOKEN = "xxxxxxxxxx"
    ACCESS_TOKEN_SECRET = "xxxxxxxxxx"
    CREDENTIALS_PATH = "credentials.json"
    EXCLUDE_SET = {"amazon", "チャージ", "チヤージ", "charge", "jr east mobile suica"}

    client = ZaimPayImporter(
        CONSUMER_ID,
        CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET,
        CREDENTIALS_PATH,
        EXCLUDE_SET,
        "token.json",
        "desktop",
    )
    client.import_ana_pay()
    client.import_rakuten_pay()
