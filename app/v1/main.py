from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from app.config import V
from app.v1.routers import countries


app = FastAPI(
    title="NWB Countries",
    description="New Wave Biotech Countries Task",
    version=f"{V}",
    contact={
        "name": "Valerio Santucci",
        "email": "valerio.santucci@outlook.it",
    },
)

app.include_router(countries.router, tags=["Countries"])
app = VersionedFastAPI(app, version_format=f"{V}", prefix_format=f"/v{V}")
