import uvicorn
from fastapi import FastAPI

from app.config import V
from app.v1.main import app

nwb = FastAPI(
    title="NWB Countries",
    description="New Wave Biotech Countries Task",
    version=f"{V}",
    contact={
        "name": "Valerio Santucci",
        "email": "valerio.santucci@outlook.it",
    },
)
nwb.mount("", app)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
