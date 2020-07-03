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
* Install ElasticSearch 
* Add 'analyze' folder in config of Elasticsaeach and add files from analyzers
* Run ElasticSearch
* Run 'bulkdata.py' to add index(uncomment indexing part if not manually added) and add data
* Add the UI part to htdocs folder
* Go to http://localhost/LyricsSearch/
* Search for Lyrics (Only works for basic queries at the moment with this UI)
* For advanced queries try the postman queries colelction from postman or browser 9Samples below)

SampleQueries
---
* Can search for lyrics if you just know movie/year/singer/lyricist/genre.
 * E.g.- "யுகபாரதி"
```
{
    "query": {
        "query_string": {
            "query":"யுகபாரதி"
        }
    }
}
```

* Can search specifying the field when you just know movie/year/singer/lyricist/genre.
 * E.g.- "பாடலாசிரியர் யுகபாரதி"
```
{
     "query" : {
          "match" : {
             "பாடலாசிரியர்" : "யுகபாரதி"
         }
     }
 }
```
* Can search with WildCard when not so sure of spell
 * E.g.- "யுக*" for "யுகபாரதி"
 ```{
     "query" : {
          "match" : {
             "பாடலாசிரியர்" : "யுக*"
         }
     }
 }
 ```
* Can search when you think one term might show up in multiple fields
 * E.g.- "அனிருத்"
```
{
      "query" : {
         "multi_match" : {
             "query" : "அனிருத்",
             "fields": ["பாடியவர்கள்","இசையமைப்பாளர்"]
         }
     }
}
```
* Can search for Top-20 songs of particular nature(Genre/singers/music directors) where Top is marked on "மதிப்பீடு" (rating)
 * E.g. - மிகச்சிறந்த 20 குத்துபாடல்
```{
   "size":20,
   "sort" : [
       { "மதிப்பீடு" : {"order" : "desc"}}
   ],
   "query": {
       "multi_match": {
           "fields":["வகை"],
           "query" : "குத்துபாடல்",
           "fuzziness": "AUTO"
       }
   }
}
```

* Can search for Famous songs (of music directors/gneres/singers) where 'famous' is marked upon "நுகர்ச்சி" (views)
 * E.g. - பிரபல்யமான 15 ஹரிஷ் ஜெயராஜ் பாடல்கள்
```{
   "size":15,
   "sort" : [
       { "நுகர்ச்சி" : {"order" : "desc"}}
   ],
   "query": {
       "multi_match": {
           "fields":["இசையமைப்பாளர்"],
           "query" : "ஹரிஷ் ஜெயராஜ்",
           "fuzziness": "AUTO"
       }
   }
}
```
* Can search with query spanning multiplefields
 * E.g.  இமான் 2019 பாடல்வரிகள் 
```
{
 "query": {
   "bool": {
         "must": [
             { "match": { "இசையமைப்பாளர்": "இமான்" }},
             { "match": { "வருடம்": "2019" }}
         ]
       }
     }
   
}
```
* Can seach for latest songs (Range Query) where latest is based on year
 * E.g.- இமான் சமீபத்திய பாடல்கள் 
```{
  "query": {
    "bool": {
      "must": [{
          "match": {
            "இசையமைப்பாளர்": "இமான்"
          }
        },
        {
          "range": {
            "வருடம்" : {
                "gte" : "2019"
            }
          }
        }
      ]
    }
  }
}
```
* Can search for Latest songs (Filtered query)
 * E.g. - சமீபத்திய பாடல்கள் 
```
{
  "query": {
    "bool": {
      "must": [{
          "match": {
            "வருடம்": "2019"
          }
        },
        {
          "range": {
            "வருடம்" : {
                "gte" : "2019"
            }
          }
        }
      ]
    }
  }
}
```
* Can get only prefered fields searching with other field
E.g.- Latest குத்துபாடல் திரைப்படம்/இசையமைப்பாளர்
 * 
 ```
 {
    "_source":{
        "includes":["திரைப்படம்","இசையமைப்பாளர்"]
    },
    "size":10,
    "sort" : [
        { "மதிப்பீடு" : {"order" : "desc"}}
    ],
    "query": {
        "multi_match": {
            "fields":["வகை"],
            "query" : "குத்துபாடல்",
            "fuzziness": "AUTO"
        }
    }
}
```
* Can search for details only with lyrics ( Text Mining)
```
{
    "query":{
       "more_like_this":{
          "fields":[
             "பாடல்வரிகள்"
          ],
          "like":"நெஞ்சில் மாமழை நெஞ்சில் மாமழை தந்து வானம் கூத்தாட கொஞ்சும் தாமரை கொஞ்சும் தாமரை வந்து எங்கும் பூத்தாட    எத்தனை நாள் எத்தனை நாள் பார்ப்பது எட்டி நின்று எட்டி நின்று காய்வது கள்ள குரல் பாடல் உள்ளே ஓடுது கண்மூடி கண்மூடி காதோரம் பாடுது    நெஞ்சில் மாமழை நெஞ்சில் மாமழை தந்து வானம் கூத்தாட கொஞ்சும் தாமரை கொஞ்சும் தாமரை வந்து எங்கும் பூத்தாட   வாரத்தில் எத்தனை நாள் பார்ப்பது அன்றாடம் வந்து பார்க்க ஏங்குது வராமல் போகும் நாட்கள் வீண் என வம்பாக சண்டை போட வைக்குது   சொல்ல போனால் என் நாட்களை வண்ணம் பூசி .",
          "min_term_freq":1,
          "max_query_terms":20
       }
    }
  }
  ```
 
 * Can do aggregated bucket querying with terms
 
 ```{
  "aggs": {
    "ratings": {
      "terms": { "field": "வகை" }
    }
  }
}
```


