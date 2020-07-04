
# Getting started 

1. clone this repository 
2. Install docker 
3. install docker compose 
4. install minikube(if required)
5. install Postman to test


# Scripts 

to start the elasticsearch cluster
```
docker-compose up -d
```

```
use index.json to add mapping 
```

```
use test.py to add data to your current mapping in elastic search 
```

If everything is fine youll be able to see in your ES UI 

to now search stuff 

```
{
   "query": { "prefix": { "name.keyword": "El" } } // this is to use it as autocomplete
}
```
```
{
     "query": {
         "bool": {
             "must": {
                 "match": {
                     "title": "bayou" // this is similar to select * from table where title="value"
                 }
             }
         }
     }
}
```

# To explore 

1. add a new dataset.
2. add a new index and mapping 
3. add relevent search 
