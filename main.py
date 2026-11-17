from fastapi import FastAPI

from database import Base, engine
from routers.alerts import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Intelligence Layer -- Alert Explainer API")
app.include_router(router)


@app.get("/")
def root():
    return {"status": "Alert Explainer API is running"}