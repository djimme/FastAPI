from fastapi import FastAPI, Body, Header

app = FastAPI()

@app.get("/hi")
def greet(who):
    return f"Hello, {who}!"

@app.post("/hipost/")
def greet_post(who: str = Body(embed=True)):
    return f"Hello again, {who}!!"

@app.get("/hiheader")
def greet_header(who: str = Header()):
    return f"Hello from header ,{who}!!!"

@app.get("/user-agent")
def get_useragent(user_agent: str = Header()):
    print('call this')
    return user_agent

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)