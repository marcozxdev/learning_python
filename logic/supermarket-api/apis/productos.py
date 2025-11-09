# apis/productos.py
from fastapi import APIRouter
from pydantic import BaseModel
import json
from typing import List

router = APIRouter()

DATA_FILE = "data/productos.json"

# -------- MODELOS --------
class Producto(BaseModel):
    id: int
    nombre: str
    precio: int
    stock: int

class ProductoNuevo(BaseModel):
    nombre: str
    precio: int
    stock: int

class ItemCompra(BaseModel):
    id: int
    cantidad: int

class Compra(BaseModel):
    items: List[ItemCompra]

# -------- FUNCIONES --------
def cargar_productos():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def guardar_productos(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# -------- RUTAS --------
@router.get("/productos")
def obtener_productos():
    return cargar_productos()

@router.post("/productos")
def agregar_producto(producto: ProductoNuevo):
    productos = cargar_productos()
    nuevo_id = max(p["id"] for p in productos) + 1 if productos else 1
    nuevo = {"id": nuevo_id, **producto.dict()}
    productos.append(nuevo)
    guardar_productos(productos)
    return nuevo

@router.post("/comprar")
def comprar(compra: Compra):
    productos = cargar_productos()
    total = 0
    for item in compra.items:
        for p in productos:
            if p["id"] == item.id:
                if p["stock"] >= item.cantidad:
                    total += p["precio"] * item.cantidad
                    p["stock"] -= item.cantidad
                else:
                    return {"error": f"Stock insuficiente para {p['nombre']}"}
    guardar_productos(productos)
    return {"total": total, "mensaje": "Gracias por tu compra"}
