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

## GTFS

I think that the [GTFS](https://gtfs.org/) project is really cool and honestly a wonderful public, open source service. As someone who loves both public services and open source software, it really is a match made. I also think that their centering of the rider is really important as this focus on those that actively rely on public transit is very much indicative of a good faith interaction with a public good. 

### Feeds

The GTFS specification defines a couple of feeds that report data, and will be the core of the statistical analysis of transit. Outside of the realtime data, both schedule and archive will require file operations and dealing with compressed files that are stored as psuedo-'csv's.
 

