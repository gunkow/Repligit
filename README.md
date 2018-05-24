# Repligit

This app's only purpose is to replicate(fork) it's github repo to the user's GitHub profile

## Run
To run it you should have **python2.7** and **flask** installed on your host machine
And register it as OAUTH app in GitHub. 
It means that GitHub provides you with **client_id** and **secret_id** .
And you should provide GitHub with your Repligit's **callback path** .
Then go repo's root and run in your shell the following:
```
 export FLASK_APP="repligit.py"
 export SECRET= **your secret_id**
 export CLIENT_ID= **your client_id**
 export CALLBACK= **callback**
 flask run --host="0.0.0.0"
```
The Repligit's workflow is:

* user goes to Repligit's url (e.g. "0.0.0.0:5000/" (first view) )
* user clicks the "Fork" button
* user is redirected to GitHub to authorize
* user is redirected back to Repligit's **'callback'** page by GitHub with a temporary code in a code parameter(2nd view)
* Repligit exchanges this code for an access token with GitHub
* Repligit forks the repo via GitHub API asyncroniously

Then user may check GitHub whether the request is complete
