from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json, re
import codecs
import unicodedata
# import queries

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = 'lyrics'

# Creating index if not manually created
# def createIndex():
#     index = Index(INDEX, using=client)
#     res = index.create()
#     print(res)

def read_all_songs():
    with open('corpus/lyrics_2019.json', 'r', encoding='utf-8-sig') as f:
        all_songs = json.loads("[" +
                          f.read().replace("}\n{", "},\n{") +"]")
        # all_songs = json.loads(f.read())
        res_list = [i for n, i in enumerate(all_songs) if i not in all_songs[n + 1:]]
        return res_list

def genData(song_array):
    for song in song_array:
        # Fields-capturing
        # print(song)
        title = song.get("பாடல்", None)
        movie = song.get("திரைப்படம்",None)
        lyricist = song.get("பாடலாசிரியர்", None)
        composer = song.get("இசையமைப்பாளர்", None)
        singers = song.get("பாடியவர்கள்", None)
        year = song.get("வருடம்", None)
        genre = song.get("வகை", None)
        lyrics = song.get("பாடல்வரிகள்", None)
        rating = song.get("மதிப்பீடு",None)
        views = song.get('நுகர்ச்சி', None)

        yield {
            "_index": "tamilsonglyrics",
            "_source": {
                "பாடல்": title,
                "திரைப்படம்": movie,
                "பாடலாசிரியர்": lyricist,
                "இசையமைப்பாளர்": composer,
                "பாடியவர்கள்": singers,
                "வருடம்": year,
                "வகை": genre,
                "பாடல்வரிகள்": lyrics,
                "மதிப்பீடு": rating,
                "நுகர்ச்சி": views
            },
        }

# createIndex()
all_songs = read_all_songs()
helpers.bulk(client,genData(all_songs))
