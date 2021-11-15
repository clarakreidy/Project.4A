# Task Planning

## Treat the data
- [x] Unify the data structure and format
- [ ] Add timestamps to the sheets
- [ ] Create a script that cleans the data

## Getting the infrastructure up and running
- [x] Set up the elasticsearch container
- [x] Set up the kibana container
- [x] Connect kibana and elasticsearch via docker
- [ ] Set up Logstash container
- [ ] Create config file for logstash to read the excels
- [ ] Create a startup script for logstash to read all excels on docker startup


## Generating a dashboard
- [ ] Generate indexes for the data
- [ ] Create a dashboard and add charts to represent the data in kibana
- [ ] Create a config file that recreates the dashboard
- [ ] Add dashboard config file to kibana docker and load it on startup


## Create elasticsearch queries
> Not everything might be doable, this section will change as I work
- [ ] Create a search and filter bar to the dashboard with _search engine like_ implementation
- [ ] Call queries from a small web app (outside kibana dashboard)
	- [ ] search query
	- [ ] filter query
	- [ ] IF STILL I HAVE TIME: advanced search
- [ ] IF STILL I HAVE TIME: Display query results in the web app