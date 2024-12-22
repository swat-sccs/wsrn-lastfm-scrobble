#!/usr/bin/env python3
#Taken and modified from pylast lastfm-tools repo
#https://github.com/hugovk/lastfm-tools/blob/main/scrobble.py

import datetime
import time
from mylast import lastfm_network, split_artist_track


def scrobble_track(artist, track):

    unix_timestamp = int(time.mktime(datetime.datetime.now().timetuple()))
    print("Timestamp:\t" + str(unix_timestamp))

    lastfm_network.scrobble(artist=artist, title=track, timestamp=unix_timestamp)

def send_now_playing(artist, title, duration):
    lastfm_network.update_now_playing(artist=artist, title=title, duration=duration)


# End of file