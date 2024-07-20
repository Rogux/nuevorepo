from fastapi import FastAPI

app= FastAPI()

@app.get('/inicio')
async def ruta():
    return "Hola desde aca"