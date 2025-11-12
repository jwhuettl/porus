# porus

> **NOTE :: This project is a work in progress and not to be used until there is a working release**




porus is a GTFS-based web application that looks at longterm data from transit sources. It is built with Flask and Postgres, it also uses Docker for ease of development and hosting modularity. 

## Main Features

- [ ] realtime tracking of transit
- [ ] import of historical data
- [ ] statistical analysis of returned and historical data
- [ ] tooling for adding new apis
- [ ] packaging api backend

## Why

I like transit and think this is an interesting project. It was brought to me by my cousin, who is also a software developer, but in a very different career path as something he wanted to do, but lacked the time. As someone with a bit too much time and a very strong interest in public works and open source software, I thought it would be a worthy endevour. 

Fun fact, the name, porus, is a greek mythological figure who is the personfication of expediency (when I can't think of a name for something, I turn to greek mythological figures, its how all my computers and various technology are named). 

## API

The main API will be the [Metro Transit API](https://svc.metrotransit.org/swagger/index.html) but I hope that much of the tooling can be used to add other APIs from other places as GTFS seems to be determine both the URLs of the API and the data it returns, with some exceptions for extensions to the GTFS standard which the Metro Transit API does have, which is noted in the documentation. 

## GTFS

I think that the [GTFS](https://gtfs.org/) project is really cool and honestly a wonderful public, open source service. As someone who loves both public services and open source software, it really is a match made. I also think that their centering of the rider is really important as this focus on those that actively rely on public transit is very much indicative of a good faith interaction with a public good. 

## Background

As I have a background in Full Stack Development, some of this project is very familiar yet most of the experience is in other languages and frameworks, this project offers the opportunity to really expand my skills and see how some of the concepts might apply outside of the language I learned them in. Additionally, this is the first time I am building a codebase from scratch without external input and without any help. 

## Inner Workings

Most of the code in this app will probably be orchestrating the background jobs such as pulling data or updating existing data or doing some of the mathematics or statistics to provide insight. There is going to be a lot of background jobs, because this is more of a reporting platform instead of an interactive one. 

### Jobs

I think there are two categories of jobs that need to be run, daily and constant. Daily jobs will be run once daily those would be schedule updates, stops, and routes. The constant jobs are larger share which include data on routes, alerts, and more realtime data. 

## Dependencies

Nearly all of the dependencies can be found in `requirements.txt` file, there are some specific ones that need to be highlighted and explained. Additionally, there are some core pieces that do not appear in this file, such as Docker and Docker Compose, also bear some necessity to explain or elaboration. 


### Docker

Both [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) are the backbone of this project as they allow for deployment and possible platform agnosticism that this project is designed to have. It also simplies the building and database integration of the project especially when expanding the scope of this project. 


## Misc

logo -> lily script one 
background color -> #AAFb
