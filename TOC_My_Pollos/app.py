import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "eat", 'drink',"big", "small", 'thank', 'show_fsm'],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "drink",
            "conditions": "is_going_to_drink",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "show_fsm",
            "conditions": "is_going_to_show_fsm",
        },
        {
            "trigger": "advance",
            "source": "eat", 
            "dest": "small",
            "conditions": "is_going_to_small",
        },
        {
            "trigger": "advance",
            "source": "eat", 
            "dest": "big",
            "conditions": "is_going_to_big",
        },
        {
            "trigger": "advance",
            "source": "small", 
            "dest": "thank",
            "conditions": "is_going_to_thank",
        },
        {
            "trigger": "advance",
            "source": "big", 
            "dest": "thank",
            "conditions": "is_going_to_thank",
        },
        {
            "trigger": "advance",
            "source": "drink", 
            "dest": "thank",
            "conditions": "is_going_to_thank",
        },
        {
            "trigger": "advance",
            "source": "thank", 
            "dest": "user",
            "conditions": "is_going_to_user",
        },
        {
            "trigger": "advance",
            "source": "show_fsm", 
            "dest": "user",
            "conditions": "is_going_to_user",
        },
        {"trigger": "go_back", "source": ["eat", "drink", "big", "small", 'thank', 'show_fsm'], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str): 
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            # send_text_message(event.reply_token, "請確認輸入")
            if event.message.text == '重新開始':
                send_text_message(event.reply_token, '讓My Pollos來幫您解決惱人的選擇障礙!\n輸入包含「餓」的訊息來開始選擇您的餐點\n輸入包含「渴」的訊息來直接選擇您的飲料\n輸入「fsm」取得fsm結構圖\n隨時打「重新開始」即可從頭開始')
                machine.go_back()
            else:
                 send_text_message(event.reply_token, '輸入格式有誤') 
    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
