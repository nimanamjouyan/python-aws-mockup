from typing import List

from fastapi import Depends, FastAPI, Query, UploadFile, File
from python_terraform import *
from modules import save_upload_file_tmp, save_file_tmp
import json

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

t = Terraform()

@app.post("/main", tags=["Main"])
async def main(file: UploadFile = File(...)):

    print(dir(file.file))
    print(file.file.__dict__)
    # print(save_upload_file_tmp("/home/morph/mykey.pub"))
    # data = json.load(file.file)
    # print(data)
    # print(save_upload_file_tmp(file))
    # return {"instance_ids": create_instance(model, key_names)}