# Instructions

## .env file structure
```
PULUMITOKEN = 
PULUMIPROJECTNAME = 
PULUMIORG = 
```

## Copy public key from your own computer
- mac: `pbcopy < ~/.ssh/id_rsa.pub` 

## To run locally and expose to web: 
- install ngrok 
- run app, `flask app` 
- run ngrok, `ngrok http 5000` on whatever port you are exposing 