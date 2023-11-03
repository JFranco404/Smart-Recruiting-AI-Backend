from fastapi import FastAPI

app = FastAPI()
app.include_router(user.router, tags=["User"])

@app.get("/", tags=["Main"])
def main():
    return {"message": "Hello World"}


