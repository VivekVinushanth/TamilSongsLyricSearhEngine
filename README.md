# TamilSongsLyricSearhEngine

This Repository includes the frontend,backend implementaion for a search query.
After configruing the elasticsearch, the sample seach engine is used to try the query searches.

Corpus obtained from my previous work :  https://github.com/VivekVinushanth/TamilSongsLyricsCorpus


Directory Structure
---
```
 ├── analyzers : Custom filters (Stemmers/stoppingwords,synonyms)
 ├── corpus : Modified data from the pre-processed data from actual (corpus) 
 ├── templates : The resultpage for UI (of Flask)
 ├── app.py : Flask backend to have transaction with ElasticSearch APIs
 ├── bulkdata.py : Python file that converts JSON to a bulkdata and uploads to ElasticSearch Bulk API
 ├── query.py : ElasticSearch search queries inclusive of advanced queries, aggreagtions and textmining
 ├── rules.py : Simple rules to pre-process query data and choose relevant queries to fit
 ├── search.py : Search API call
```

Demo
---
* Install ElasticSearch and Run
* Run 'bulkdata.py' to add index(uncomment indexing part if not manually added) and add data
* Add the UI part to htdocs folder
* Go to http://localhost/LyricsSearch/
* Search for Lyrics (Only works gfor bsaic queries at the moment with this UI)
* For advanced queries try the postman queries colelction from postman or browser



