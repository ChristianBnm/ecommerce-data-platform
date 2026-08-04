from fastapi import FastAPI

app = FastAPI(
    title="Ecommerce Data Platform API",
    description="API principal de la plataforma SaaS de inteligencia de negocio",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "application": "Ecommerce Data Platform",
        "status": "running"
    }