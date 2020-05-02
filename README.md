# ResearchPaperRecommendation - FindIt

FindIt is a software project designed to recommend research papers and articles based upon a given query.The system currently uses tfidf algorithm to extract the best score papers from the database.

## Prerequisites :
- [mongodb](https://docs.mongodb.com/manual/administration/install-community/)

## Creating the database :
1.Go to the directory where mongoDB is installed and start the mongoDB service to open the mongo shell
```
$cd /path/to/mongodb
$sudo systemctl start mongo
$mongo
```
2.Create a new database "recom" 
```
$use recom
```
3.Quit the terminal and import the datasets into your database
```
$quit()
$mongoimport --type csv -d recom -c papers1 --headerline --drop ..path/to/dataset/1_sorted.csv
$mongoimport --type csv -d recom -c papers2 --headerline --drop ..path/to/dataset/nlp3.csv
$mongoimport --type csv -d recom -c papers1 --headerline --drop ..path/to/dataset/nlp2.csv
```
4.To close the mongodb server,use the following command
```
$sudo systemctl stop mongo
```
## Setting Up virtual Python3 environment
1.Follow the commands to create a environemnt "env" and activate it
```
$mkdir env
$python3 -m venv env
$source ./env/bin/activate 
```
2.To deactivate,use
```
$deactivate
```
## Searching papers on the basis of string matching
Make sure the mongo server is active.Also activate the virtual environment and run the following command,
```
$python web_nlp.py
```
Follow the local url displayed.A FindIt website will be hosted.Create an account if you do not have one.User need to signnIn to go to the search query page.Option is also provided to make changes in profile settings including uploading a profile picture and changing profession and workplace.

A list of papers is displayed.You can add more papers into your database and make it extensive.
A Url search option is provided which enables to open the desired paper by typing its Url in the search bar.

## Future Work

1.Currently the system does not take into account the previous searches of the current user and those of other users.MThe algorithm will be further updated to take this into account

2.Optimisation of existing algorithm will be done to improve upon the searching speed.

3.More features will be added to make the system user-friendly.
