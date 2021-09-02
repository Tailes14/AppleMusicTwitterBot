from TwitterAPI import TwitterAPI
import requests
import configT




def main():
    api = TwitterAPI(configT.consumerKey, configT.consumerSecret, configT.accessToken, configT.accessSecret)

    r = api.request('statuses/update', {'status':'This is a tweet!'})
    print(r.status_code)

if __name__ == '__main__':
    main()