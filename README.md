# ResearchPaperRecommendation

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
Follow the commands to create a environemnt "env" and activate it
```
$mkdir env
$python3 -m venv env
$source ./env/bin/activate 
```
To deactivate,
```
$deactivate
```
