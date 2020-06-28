from elasticsearch import Elasticsearch

from query import basic_search

INDEX = 'tamilsonglyrics'
client = Elasticsearch(HOST="http://localhost",PORT=9200)

def search(query):
    query_body = basic_search(query)
    print('Making Basic Search ')
    res = client.search(index=INDEX, body=query_body)
    return res
