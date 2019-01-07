import time
from slackclient import SlackClient
import json

from uygulama.app import slack_client

BOT_TOKEN = "xoxb-372215092436-492081733540-iskEWWZ41fo9woiBs1mN4I3Ue"
CHANNEL_NAME = "twitter-bottest"


def main():
    # Create the slackclient instance
    sc = SlackClient(BOT_TOKEN)

    # Connect to slack
    if sc.rtm_connect():
        dosya =open("hurriyet.json","r", encoding="utf-8")

        while True:
            for line in dosya:
                _json = json.loads(line)

                message = "Tweet :" + _json.get("tweet") + "\nTakipçi Sayısı : " + str(_json.get("followers_count"))

                sc.rtm_send_message(channel=CHANNEL_NAME, message=message)
                # Sleep for half a second
                time.sleep(0.5)
                print(message)
               



if __name__ == '__main__':
    main()
