import json
from fastapi import FastAPI,Request, APIRouter
from scrobble import scrobble_track,send_now_playing
from pprint import pprint
import sys

app = FastAPI()

@app.get("/")
def read_root():
    return {"Created by Damian Rene '27"}


@app.post("/scrobble")
async def scrobble_item(request: Request):
    #pprint(await request.json())
    response = await request.json()

    title = response["now_playing"]["song"]["title"]
    artist = response["now_playing"]["song"]["artist"]
    duration = response["now_playing"]["duration"]

    # Validate
    if len(artist) == 0 and len(title) == 0:
        print("Error: Artist and track are blank")
        return "error"
    if len(artist) == 0:
        print("Error: Artist is blank")
        return "error"
    if len(title) == 0:
        print("Error: Track is blank")
        return "error"

    scrobble_track(artist,title)
    send_now_playing(artist, title, duration)

    return "Success"


'''
Current AzuraCast Post request info

title = ["now_playing"]["song"]["title"]
artist = ["now_playing"]["song"]["artist"]


[
  {
    "station": {
      "id": 1,
      "name": "AzuraTest Radio",
      "shortcode": "azuratest_radio",
      "description": "An AzuraCast station!",
      "frontend": "shoutcast2",
      "backend": "liquidsoap",
      "timezone": "America/Chicago",
      "listen_url": "http://localhost:8000/radio.mp3",
      "url": "https://example.com/",
      "public_player_url": "https://example.com/public/example_station",
      "playlist_pls_url": "https://example.com/public/example_station/playlist.pls",
      "playlist_m3u_url": "https://example.com/public/example_station/playlist.m3u",
      "is_public": true,
      "mounts": [
        {
          "id": 1,
          "name": "/radio.mp3",
          "url": "http://localhost:8000/radio.mp3",
          "bitrate": 128,
          "format": "mp3",
          "listeners": {
            "total": 20,
            "unique": 15,
            "current": 20
          },
          "path": "/radio.mp3",
          "is_default": true
        }
      ],
      "remotes": [
        {
          "id": 1,
          "name": "/radio.mp3",
          "url": "http://localhost:8000/radio.mp3",
          "bitrate": 128,
          "format": "mp3",
          "listeners": {
            "total": 20,
            "unique": 15,
            "current": 20
          }
        }
      ],
      "hls_enabled": true,
      "hls_is_default": true,
      "hls_url": "https://example.com/hls/azuratest_radio/live.m3u8",
      "hls_listeners": 1
    },
    "listeners": {
      "total": 20,
      "unique": 15,
      "current": 20
    },
    "live": {
      "is_live": false,
      "streamer_name": "DJ Jazzy Jeff",
      "broadcast_start": 1591548318,
      "art": "https://picsum.photos/1200/1200"
    },
    "now_playing": {
      "sh_id": 0,
      "played_at": 1609480800,
      "duration": 180,
      "playlist": "Top 100",
      "streamer": "Test DJ",
      "is_request": true,
      "song": {
        "text": "Chet Porter - Aluko River",
        "artist": "Chet Porter",
        "title": "Aluko River",
        "album": "Moving Castle",
        "genre": "Rock",
        "isrc": "US28E1600021",
        "lyrics": "",
        "id": "9f33bbc912c19603e51be8e0987d076b",
        "art": "https://picsum.photos/1200/1200",
        "custom_fields": [
          "custom_field_value"
        ]
      },
      "elapsed": 25,
      "remaining": 155
    },
    "playing_next": {
      "cued_at": 1609480800,
      "played_at": 1609480800,
      "duration": 180,
      "playlist": "Top 100",
      "is_request": true,
      "song": {
        "text": "Chet Porter - Aluko River",
        "artist": "Chet Porter",
        "title": "Aluko River",
        "album": "Moving Castle",
        "genre": "Rock",
        "isrc": "US28E1600021",
        "lyrics": "",
        "id": "9f33bbc912c19603e51be8e0987d076b",
        "art": "https://picsum.photos/1200/1200",
        "custom_fields": [
          "custom_field_value"
        ]
      }
    },
    "song_history": [
      {
        "sh_id": 0,
        "played_at": 1609480800,
        "duration": 180,
        "playlist": "Top 100",
        "streamer": "Test DJ",
        "is_request": true,
        "song": {
          "text": "Chet Porter - Aluko River",
          "artist": "Chet Porter",
          "title": "Aluko River",
          "album": "Moving Castle",
          "genre": "Rock",
          "isrc": "US28E1600021",
          "lyrics": "",
          "id": "9f33bbc912c19603e51be8e0987d076b",
          "art": "https://picsum.photos/1200/1200",
          "custom_fields": [
            "custom_field_value"
          ]
        }
      }
    ],
    "is_online": true,
    "cache": "hit"
  }
]'''