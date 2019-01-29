import time
from slackclient import SlackClient
import json


BOT_TOKEN = "xoxb-530519613028-530688557810-r1lR42CuYoeLJ5kY074Rputc"
CHANNEL_NAME = "twitbot"


def main():
    # Create the slackclient instance
    sc = SlackClient(BOT_TOKEN)

    # Connect to slack
    if sc.rtm_connect():
        a =open("hurriyet.json","r", encoding="utf-8")

        count = 0
        for line in a:
                _json = json.loads(line)

                count += 1
                message = "HÜRRİYET-----------#"+str(count)+"\nTweet :" + _json.get("tweet") + "\nTakipçi Sayısı : " + str(_json.get("followers_count"))+"\nBeğeni : " + str(_json.get("favorite")) +"\nRetweet :" + str(_json.get("retweet"))

                sc.rtm_send_message(channel=CHANNEL_NAME, message=message)

                # Sleep for half a second
                time.sleep(0.5)
                print(message)



        b = open("cnn.json", "r", encoding="utf-8")

        count = 0
        for line in b:
                _json = json.loads(line)
                count += 1
                message ="CNN-----------#"+str(count)+"\nTweet :" + _json.get("tweet") + "\nTakipçi Sayısı : " + str(
                    _json.get("followers_count")) + "\nBeğeni : " + str(_json.get("favorite")) + "\nRetweet :" + str(
                    _json.get("retweet"))

                sc.rtm_send_message(channel=CHANNEL_NAME, message=message)
                # Sleep for half a second
                time.sleep(0.5)
                print(message)

        c = open("kanald.json", "r", encoding="utf-8")

        count = 0
        for line in c:
                _json = json.loads(line)
                count += 1
                message ="KANALD-----------#"+str(count)+"\nTweet :" + _json.get("tweet") + "\nTakipçi Sayısı : " + str(
                    _json.get("followers_count")) + "\nBeğeni : " + str(_json.get("favorite")) + "\nRetweet :" + str(
                    _json.get("retweet"))

                sc.rtm_send_message(channel=CHANNEL_NAME, message=message)
                # Sleep for half a second
                time.sleep(0.5)
                print(message)

        d = open("milliyet.json", "r", encoding="utf-8")

        count = 0
        for line in d:
                _json = json.loads(line)
                count += 1
                message ="MİLLİYET-----------#"+str(count)+"\nTweet :" + _json.get("tweet") + "\nTakipçi Sayısı : " + str(
                    _json.get("followers_count")) + "\nBeğeni : " + str(_json.get("favorite")) + "\nRetweet :" + str(
                    _json.get("retweet"))

                sc.rtm_send_message(channel=CHANNEL_NAME, message=message)
                # Sleep for half a second
                time.sleep(0.5)
                print(message)

    

if __name__ == '__main__':

 main()
