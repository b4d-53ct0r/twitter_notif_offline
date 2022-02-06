import vonage
import tweepy 
import json
from datetime import datetime
#start config file
cf = "config.json"
pnf  = "number.json"
#end config file

#start target
target = '1337FIL'
#end target 
def get_json(filename,value):
    f = open(filename)
    APIs = json.load(f)
    return APIs[value]
def get_last_tweet(api,user):
    tweet_list = api.user_timeline(screen_name=target,count=1, tweet_mode='extended')
    tweet= tweet_list[0]
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return user.name+' : '+tweet.full_text+' time: '+current_time+' '
def get_n_tweets(user):
    return int(user.statuses_count)
def action(msg):
    print("ACTION HERE")
    client = vonage.Client(key="", secret="")
    sms = vonage.Sms(client)
    #phone 0
    #API_KeY
    #
    #API_SECRET
    #
    responseData = sms.send_message(
        {
            "from": "1337MED",
            "to": "",
            "text": msg,
        }
    )
    # phone 1  
    #API_KEY
    #
    #API_SECRET
    #
    client0 = vonage.Client(key="", secret="")
    sms0 = vonage.Sms(client0)
    responseData0 = sms0.send_message(
        {
            "from": "1337MED",
            "to": "",
            "text": msg,
        }
    )
    if responseData["messages"][0]["status"] == "0" and responseData["messages"][0]["status"] == "0" :
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        print(f"Message failed with error: {responseData0['messages'][0]['error-text']}")
def main():
    #start configuration 
    consumer_key = get_json(cf,"API_KEY")
    access_token = get_json(cf,"AT")
    access_token_secret = get_json(cf,"ATS")
    consumer_secret = get_json(cf,"API_KEY_S")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #end configuration
    
    #start number of normal tweets
    fn = open(pnf)
    n = json.load(fn)
    fn.close()
    #end number of normal tweets
    
    #loop to find if there is new tweet
    while True:
        try:
            while True:
                #start setting target

                user = api.get_user(screen_name=target)
     
                #end setting target
         
                #start check
                if n["n"] != get_n_tweets(user):
                    msg = get_last_tweet(api,user)
                    print(msg)
                    action(msg)
                    n["n"]= get_n_tweets(user)
                    fn = open(pnf,"w")
                    json.dump(n,fn)
                    fn.close()
                    fn = open(pnf)
                    n = json.load(fn)
                    print("updated")
                #end check
                #sleep time to prevent Error 88
                __import__('time').sleep(30)
        except:
            print("[!] Shiiit")

            
    
if __name__ == "__main__":
    main()
