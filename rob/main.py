import fastapi
import uvicorn

api=fastapi.FastAPI()

@api.get('/api/calculate')
def calculate():
    return 2 + 3

uvicorn.run(api)