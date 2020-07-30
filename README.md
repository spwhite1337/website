# Stack Overflow problem

- The nginx server successfully hosts the vue-app but fails to receive requests from the flask app. 
- I can port the flask app itself and it works just fine, it is only a communication issue.
- My goals is to have the vue-app interface with the flask backend through axios requests.

To reproduce this error:
- Clone this branch
- `docker-compose up --build`
- go to `http://localhost` and click the button to see the 404 error.
