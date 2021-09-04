import configS
from pprint import pprint
import requests
import time
from TwitterAPI import TwitterAPI
import configT

# youtube video followed for spotify 
# https://www.youtube.com/watch?v=yKz38ThJWqE

SPOTIFY_ACCESS_TOKEN = configS.OAuthToken
GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def get_current_track(access_token):
    response = requests.get(GET_CURRENT_TRACK_URL, 
    headers={"Authorization": f"Bearer {access_token}"})


    try:
        resp_json = response.json()
    except:
        return

    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_name = ', '.join([artist['name'] for artist in artists])
    link = resp_json['item']['external_urls']['spotify']


    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists" : artists_name,
        "link" : link
    }
    return current_track_info

def tweet(api, info):
    formatted = 'Currently listening to:\n{}\n{}\n{}'.format(info['artists'], info['name'], info['link'])
    r = api.request('statuses/update', {'status': formatted})
    print(r.status_code)


def main():
    # running once to get the current song being played
    current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
    if current_track_info == None:
        print("No music being played, waiting...")
        time.sleep(3)
        main()
    currName = current_track_info['name']
    pprint(current_track_info, indent=4)

    api = TwitterAPI(configT.consumerKey, configT.consumerSecret, configT.accessToken, configT.accessSecret)
    tweet(api, current_track_info)


    # then looping and checking for a new song name being played
    while True:
        current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
        if current_track_info == None:
            print("No music being played, waiting...")
            main()
        if current_track_info['name'] != currName:
            pprint(current_track_info, indent=4)
            currName = current_track_info['name']
            tweet(api, current_track_info)
        


if __name__ == '__main__':
    main()