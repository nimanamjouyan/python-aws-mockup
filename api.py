from typing import List

from fastapi import Depends, FastAPI, Query

from model import Model
from modules import create_instance


description = """
FastApi meets Terraform 💪
####
Making terraform API available through FastAPI which allows for spinning up EC2 instances provided a JSON of relevant parameters.
"""

app = FastAPI(
    title="AWS Monster",
    description=description,
    version="0.0.1",
    docs_url="/"
    )


@app.get("/main", tags=["Main"])
def main(
    model: Model = Depends(),
    key_names: List[str] = Query(None, title="List of private keys", description="Place one private key per field."),
):
    return {"instance_ids": create_instance(model, key_names)}