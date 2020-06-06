# Quarantine Notes
Notes from people on quarantine around the globe -> A serverless app

## Local development

## Requirements
- Python 3.6
- NodeJS > 10
- Yarn
- pipenv (`pip install pipenv`)
- serverless (`npm i -g serverless`)
- Java (for the local DynamoDB server)

## API
### Installing the dependencies

Install the Python dependencies:

```
pipenv install --dev
```

Install the NodeJS dependencies:

```
yarn install
```

Install DynamoDB locally:

```
sls dynamodb install
```

### Running the API

Run this command:


```
pipenv run honcho start
```

And access the API on http://localhost:5000


## Web
### Installing the dependencies

Enter in the frontend folder:

```
cd frontend
```


Install the NodeJS dependencies:

```
yarn install
```


### Running the Web interface

Make sure you're in the frontend folder and run this command:

```
yarn run serve
```

And access the Web interface on http://localhost:8080


## TODO
  * [x] add link to personal website
  * [ ] create "view note" page
  * [ ] display linebreaks (currently \n entered have no effect)
  * [x] allow replies on notes
  * [x] show number of replies on Inbox cards
  * [ ] integrate with watson to identify which language the note was written in
  * [ ] add filter by language
  * [ ] add filter by country
  * [x] add spinner while waiting for Inbox component to get notes from aws
  * [ ] write frontend tests


## Running tests

## API

Start the DynamoDB server:

```
yarn run test-db
```

Run the tests:

```
pipenv run pytest --ignore=vuemail-dark
```

## Contributors

- [Eric Magalhães](https://emagalha.es)