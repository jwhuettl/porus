# porus

porus is a GTFS-based web application that looks at longterm data from transit sources. It is built with Flask and Postgres, it also uses Docker for ease of development and hosting modularity. 

## Features

- [ ] realtime tracking of transit
- [ ] import of historical data

## Why

I like transit and think this is an interesting project. Fun fact the name, porus, is a greek mythological figure that is the personfication of expediency. 

## API

The main API will be the [Metro Transit API](https://svc.metrotransit.org/swagger/index.html) but I hope that much of the tooling can be used to add other APIs from other places as GTFS seems to be the structure of the API as well as the data it returns.