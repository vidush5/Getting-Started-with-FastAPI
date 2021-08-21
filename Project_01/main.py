from fastapi import FastAPI

app = FastAPI()

#basic function
@app.get("/hello")
async def hello():
    return "welcome"

#parsing arguments
@app.get("/hi/{name}")
async def hello(name):
    return f"welcome {name}"

#retrieve data

cricketers = {
    'indian' : ["'Sachin", "Dhoni"],
    'srilanka' : ["'Sangakarra", "Mahela"],
    'pakistan' : ["Malik", "Afridi"]
} 

@app.get("/get_cricketers/{players}")
async def get_cricketers(players):
    return cricketers.get(players)