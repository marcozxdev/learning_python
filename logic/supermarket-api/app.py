# main.py
from fastapi import FastAPI
from apis import productos

app = FastAPI()

# Rutas
# app.include_router(productos.router)
# 