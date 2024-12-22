import os
import sys
import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account for Last.fm

try:
    API_KEY = os.environ["LASTFM_API_KEY"]
    API_SECRET = os.environ["LASTFM_API_SECRET"]
except KeyError:
    print("API Key Not Provided, Check .env")

try:
    lastfm_username = os.environ["LASTFM_USERNAME"]
    lastfm_password_hash = pylast.md5(os.environ["LASTFM_PASSWORD"])
except KeyError:
    print("Something went wrong")


lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=lastfm_username,
    password_hash=lastfm_password_hash,
)


def track_and_timestamp(track):
    return f"{track.playback_date}\t{track.track}"


def print_track(track):
    print(track_and_timestamp(track))


TRACK_SEPARATOR = " - "


def split_artist_track(artist_track):
    artist_track = artist_track.replace(" – ", " - ")
    artist_track = artist_track.replace("“", '"')
    artist_track = artist_track.replace("”", '"')

    (artist, track) = artist_track.split(TRACK_SEPARATOR)
    artist = artist.strip()
    track = track.strip()
    print("Artist:\t\t'" + artist + "'")
    print("Track:\t\t'" + track + "'")

    # Validate
    if len(artist) == 0 and len(track) == 0:
        sys.exit("Error: Artist and track are blank")
    if len(artist) == 0:
        sys.exit("Error: Artist is blank")
    if len(track) == 0:
        sys.exit("Error: Track is blank")

    return (artist, track)


# End of file