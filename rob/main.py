import fastapi
import uvicorn

api=fastapi.FastAPI()

@api.get('/api/calculate')
def calculate():
    value = 2 + 2

    return {
        'Value' : value
    }

uvicorn.run(api, port=8000, host='127.0.0.1')