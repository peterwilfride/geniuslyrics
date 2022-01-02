#!/home/cyber/dev/geniuslyrics/venv/bin/python

import os
import json
import dotenv
from termcolor import colored
from lyricsgenius import Genius
from lyricsgenius.api.public_methods import artist

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

#_name = input('Name: ')
#_artist = input('Artist: ')

song_name = os.system('mpc -f %title% current')
song_artist = os.system('mpc -f %artist% current')

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
