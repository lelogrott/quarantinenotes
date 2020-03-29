# quarantinenotes
Notes from people on quarantine around the globe.


TODO
  * [x] add link to personal website
  * [ ] create "view note" page
  * [ ] display linebreaks (currently \n entered have no effect)
  * [ ] allow replies on notes
  * [ ] integrate with watson to identify which language the note was written in
  * [ ] add filter by language
  * [ ] add filter by country
  * [ ] add spinner while waiting for Inbox component to get notes from aws


TO run locally
- clone the repository and `cd quarantinenotes`
- run `yarn install && yarn --cwd ./vuemail-dark install`
- run `pipenv install`
- run `sls wsgi serve` on `./` to run the API locally.
- run `yarn --cwd ./vuemail-dark serve` to run the site locally
