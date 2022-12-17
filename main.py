from fastapi import FastAPI

app = FastAPI()


@app.get("/") #decorator turns root() to a path operation 
def root_path():    
    return {"message": "Welcome to my API!!"}
