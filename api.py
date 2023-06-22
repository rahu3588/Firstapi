from fastapi import FastAPI

app = FastAPI()

@app.get('/TXF')
def cybar_programer():
    return 'ok'

