from elasticsearch import Elasticsearch

from query import basic_search, standard_analyzer
# from rules import process

INDEX = 'tamilsonglyrics'
client = Elasticsearch(HOST="http://localhost",PORT=9200)

def search(query):
    # result = client. (index=INDEX,body=standard_analyzer(query))
    # keywords = result ['tokens']['token']
    # print(keywords)

    # query_body= process(query)
    query_body = basic_search(query)
    print('Making Basic Search ')
    res = client.search(index=INDEX, body=query_body)
    return res
