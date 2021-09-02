import configS
from pprint import pprint
import requests
import time



SPOTIFY_ACCESS_TOKEN = configS.OAuthToken
GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def get_current_track(access_token):
    response = requests.get(GET_CURRENT_TRACK_URL, 
    headers={"Authorization": f"Bearer {access_token}"})

    resp_json = response.json()

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




def main():
    # running once to get the current song being played
    current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
    currName = current_track_info['name']
    pprint(current_track_info, indent=4)

    # then looping and checking for a new song name being played
    while True:
        current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
        if current_track_info['name'] != currName:
            pprint(current_track_info, indent=4)
            currName = current_track_info['name']
        


if __name__ == '__main__':
    main()