import os
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from routers import user, project
import datetime

app = FastAPI()

# Configura las rutas del enrutador
app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(project.router, prefix="/api/projects", tags=["projects"])

origins = [
    "https://music-app-frontend-pc8g.vercel.app",
    "https://music-app-frontend-pc8g-5x5jpup4y-omars-projects-b5a3697e.vercel.app",
    "https://music-gen-demo-omars-projects-b5a3697e.vercel.app"
    # Agrega aquí cualquier otra variación necesaria
]

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir los orígenes especificados
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS", "PATCH", "DELETE", "POST", "PUT"],
    allow_headers=[
        "X-CSRF-Token", "X-Requested-With", "Accept", "Accept-Version", "Content-Length",
        "Content-MD5", "Content-Type", "Date", "X-Api-Version"
    ],
)

# Middleware para agregar encabezados CORS a las respuestas
def add_cors_headers_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,OPTIONS,PATCH,DELETE,POST,PUT"
    response.headers["Access-Control-Allow-Headers"] = "X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version"
    return response

app.middleware('http')(add_cors_headers_middleware)

# Handler para devolver la fecha y hora actual
@app.api_route("/", methods=["GET", "OPTIONS", "PATCH", "DELETE", "POST", "PUT"])
async def handler(request: Request):
    if request.method == "OPTIONS":
        return Response(status_code=200)
    
    # Devuelve la fecha y hora actual
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return Response(content=current_date)

# Ejemplo de cómo consumirlo en el frontend
# JavaScript (fetch API)
# 
# async function getCurrentDate() {
#     try {
#         const response = await fetch('http://localhost:8000/', {
#             method: 'GET',
#             headers: {
#                 'Accept': 'application/json',
#             },
#             credentials: 'include'
#         });
#         if (response.ok) {
#             const data = await response.text();
#             console.log('Fecha y hora actual:', data);
#         } else {
#             console.error('Error en la solicitud:', response.status);
#         }
#     } catch (error) {
#         console.error('Error en la solicitud:', error);
#     }
# }
# 
# getCurrentDate();
