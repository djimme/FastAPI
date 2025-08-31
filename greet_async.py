from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

@app.get("/hi")
async def greet():
    await asyncio.sleep(10)
    return "Hello, async!"

@app.get("/hi2")
def greet2():
    return "Hello, greet2!"

if __name__ == "__main__":
    uvicorn.run("greet_async:app", reload=True)