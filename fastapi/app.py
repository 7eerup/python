from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def Hello():
    return "Hello Python"