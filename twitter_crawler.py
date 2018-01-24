import twitter

api = twitter.Api(consumer_key='xITCo7ggiRehaEiWP1Oy23Sfl',
                  consumer_secret='GjCsrgTbPKPeWXUIwFzHvrdXrCLur3en67awxHbHVBD5u4f0XP',
                  access_token_key='2369848692-kcMAn9RySj6eeJ21dVgEN7Ul94nvo5Y6Wf1AVdI',
                  access_token_secret='gxVuPmIWgY26Dkl3JT6l5bdWob8l3HSMZAKCdCjsddrSI')

results = api.GetSearch(raw_query="q=CHINA%20&result_type=recent&count=100")