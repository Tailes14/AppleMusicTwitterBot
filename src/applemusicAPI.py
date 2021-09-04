import configAM
from pprint import pprint
import requests
import time
from TwitterAPI import TwitterAPI
import configT
import StoreKit
from applepymusic import AppleMusicClient


# might not need use for song link https://developer.apple.com/documentation/applemusicapi/get_a_catalog_song
# use for getting song https://developer.apple.com/documentation/applemusicapi/get_recently_played_tracks
# use for getting keys https://developer.apple.com/documentation/applemusicapi/getting_keys_and_creating_tokens?changes=latest_major
# using requests https://docs.python-requests.org/en/master/user/quickstart/
# maybe useful https://www.appcoda.com/musickit-music-player-swiftui/
#https://github.com/ronaldoussoren/pyobjc/blob/master/pyobjc-framework-StoreKit/PyObjCTest/test_skcloudservicecontroller.py
#https://github.com/ronaldoussoren/pyobjc/blob/master/pyobjc-framework-StoreKit/Lib/StoreKit/_metadata.py

#GET_CURRENT_TRACK_URL = 'https://api.music.apple.com/v1/me/recent/played/tracks?limit=1?types=songs'

#https://www.youtube.com/watch?v=FNeZsxb4UDY

def tweet(api, info):
    formatted = 'Currently listening to:\n{}\n{}\n{}'.format(info['artists'], info['name'], info['link'])
    r = api.request('statuses/update', {'status': formatted})
    print(r.status_code)

def main():
    client = AppleMusicClient(
        configAM.teamID, configAM.key, configAM.privatev2
    )

    # getting the user token
    client._get_auth_headers()

    played = client.user_heavy_rotation(limit=10)


if __name__ == '__main__':
    main()
