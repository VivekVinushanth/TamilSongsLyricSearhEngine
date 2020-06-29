# import json
#
# from query import agg_multi_match_and_sort_q
#
# flags = [0, 0, 0, 0, 0, 0, 0]
# flagedValue = {}
# # flag_pointer -1 => numeric
# # flag_pointer -2 => lyrics
# # flag_pointer -3 => lyricist
# # flag_pointer -4 => musicComposer
# # flag_pointer -5 => singers
# # flag_pointer -6 => genre
# # flag_pointer -7 => year
#
# years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
# genre = ["குத்துபாடல்", "மெல்லிசைபாடல்", "காதல்பாடல்", "கானாபாடல்", "தத்துவபாடல்"]
#
#
# def check_for_year(num):
#     if num in years:
#         return True
#
#
# def get_all_musicComposers():
#     with open('corpus/musicdirectors.json', 'r', encoding='utf-8-sig') as t:
#         music_directors = json.loads(t.read())
#         return music_directors.values()
#
#
# def get_all_singers():
#     with open('corpus/singers.json', 'r', encoding='utf-8-sig') as t:
#         all_artists = json.loads(t.read())
#         return all_artists.values()
#
# def get_all_lyricists():
#     with open('corpus/lyricist.json', 'r', encoding='utf-8-sig') as t:
#         all_lyricists = json.loads(t.read())
#         return all_lyricists.values()
#
#
# singers = get_all_singers()
# lyricist = get_all_lyricists()
# musicdirectors = get_all_musicComposers()
# all_lists = [None, None, lyricist, musicdirectors, singers, genre]
#
#
# def process(query):
#     tokens = query.split
#     for terms in tokens:
#         if terms.isdigit():
#             flags[0] = 1
#             num = int(terms)
#             print('Identified a number', num)
#             if (check_for_year(num)):
#                 flags[6] = 1
#                 flagedValue['வருடம்'] = num
#             else:
#                 flagedValue['size'] = num
#
#         for i in range(2, 5):
#             # check for list of inputs
#             if terms in all_lists[i]:
#                 flags[i] = 1
#                 if (i == 2):
#                     key = "பாடலாசிரியர்"
#                 if (i == 3):
#                     key = "இசையமைப்பாளர்"
#                 if (i == 4):
#                     key = "பாடியவர்கள்"
#                 if (i == 5):
#                     key = "வகை"
#                 flagedValue[key] = terms
#
#     fields = []
#     if 'size' in flagedValue:
#         size = flagedValue['size']
#
#     if 'பாடலாசிரியர்' in flagedValue:
#         fields.append('பாடலாசிரியர்')
#
#     if 'இசையமைப்பாளர்' in flagedValue:
#         fields.append('இசையமைப்பாளர்')
#
#     if 'பாடியவர்கள்' in flagedValue:
#         fields.append('பாடியவர்கள்')
#
#     if 'வருடம்' in flagedValue:
#         fields.append('வருடம்')
#
#     if 'வகை' in flagedValue:
#         fields.append('வகை')
#
#     fields.append('பாடல்வரிகள்')
#     fields.append('பாடல்')
#
#     return agg_multi_match_and_sort_q(query, fields, sort_num=size)