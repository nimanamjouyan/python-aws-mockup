import os
from fastapi import FastAPI, Form, Depends, Query
from typing import List
from model import Model
from modules import create_instance

app = FastAPI(docs_url="/")

with open("VERSION", "r") as f:
    VERSION = f.read()


@app.get("/main")
def main(
    model: Model = Depends(),
    key_names: List[str] = Query(
        None,
        title="List of private keys",
        description="Place one private key per field."
        ),
):
    return {"instance_ids":create_instance(model, key_names)}


@app.get("/version")
def version():
    return VERSION
