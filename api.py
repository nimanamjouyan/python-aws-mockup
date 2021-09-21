from typing import List

from fastapi import Depends, FastAPI, Query

from model import Model
from modules import create_instance

app = FastAPI(docs_url="/")


@app.get("/main")
def main(
    model: Model = Depends(),
    key_names: List[str] = Query(None, title="List of private keys", description="Place one private key per field."),
):
    return {"instance_ids": create_instance(model, key_names)}