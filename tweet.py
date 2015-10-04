import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "agvZ0kTe9Se820jwrk3J2EfMu",
    "consumer_secret"     : "5aYEdm1QUoiGh4K6QaJUdqjsHbbqXsI0F4LlqbL0IH55E3qXBi",
    "access_token"        : "3862358111-bKBdQtb80BUAqFJz0Le3MZbgYq1zVTTaaBvkBXx",
    "access_token_secret" : "kG3yWxBBT7Tx6DytUD0Shlz5mXI1nBjdEgh2UwuW88Xnh" 
    }

  api = get_api(cfg)
  tweet = "@" + name + " failed to stop the alarm!\n Now " + filename + "will be DELETED!!!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
