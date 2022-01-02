#!/home/cyber/dev/geniuslyrics/venv/bin/python

import os
import json
import sys
import dotenv
from termcolor import colored
from lyricsgenius import Genius
from lyricsgenius.api.public_methods import artist

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

if len(sys.argv) == 1: # default
    song_name = os.popen('mpc -f %title% current').read()
    song_artist = os.popen('mpc -f %artist% current').read()
elif sys.argv[2] == '-i' or sys.argv[2] == '--i': # interactive mode
    song_name = input('Song ame: ')
    song_artist = input('Name artist: ')
elif sys.argv[2] == '-h' or sys.argv[2] == '--help': # help
    print("""   
          Usage: lyrics
                 Shows in the terminal the lyrics of the song that is 
                 playing through the mpc or playerctl.

          Options:
            -i, --i     Interactive mode. prompts the user to name and 
                        artist the song that wants to see the lyrics.
            -h, --help  Help.

          """)

TOKEN = os.environ.get("TOKEN")
genius = Genius(TOKEN)

song = genius.search_song(song_name, artist=song_artist)

_ = song.save_lyrics('tmp_lyrics.json')

f = open('tmp_lyrics.json')

data = json.load(f)
data_list = data["lyrics"].split('\n')
len_data_list = len(data_list)

for word in data_list[:len_data_list-2]:
    if word.startswith('[') and word.endswith(']'):
        word = colored(word, 'blue')
        print(word)
    else:
        print(word)

f.close()
os.remove('tmp_lyrics.json')
