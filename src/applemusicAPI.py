from spotifyAPI import GET_CURRENT_TRACK_URL
import configAM
from pprint import pprint
import requests
import time
from TwitterAPI import TwitterAPI
import configT

# might not need use for song link https://developer.apple.com/documentation/applemusicapi/get_a_catalog_song
# use for getting song https://developer.apple.com/documentation/applemusicapi/get_recently_played_tracks
# use for getting keys https://developer.apple.com/documentation/applemusicapi/getting_keys_and_creating_tokens?changes=latest_major
# using requests https://docs.python-requests.org/en/master/user/quickstart/


GET_CURRENT_TRACK_URL = 'https://api.music.apple.com/v1/me/recent/played/tracks?limit=1?types=songs'



def tweet(api, info):
    formatted = 'Currently listening to:\n{}\n{}\n{}'.format(info['artists'], info['name'], info['link'])
    r = api.request('statuses/update', {'status': formatted})
    print(r.status_code)

def main():
    pass

if __name__ == '__main__':
    main()
