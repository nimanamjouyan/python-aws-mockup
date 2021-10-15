from typing import List
import logging
from fastapi import Depends, FastAPI, UploadFile, File, HTTPException, Query
from model import InstanceParams, Secrets
from python_terraform import *
from modules import params_to_list

logger = logging.getLogger()

description = """
FastApi meets Terraform 💪
####
Making terraform API available through FastAPI which allows for spinning up EC2 instances provided a JSON of relevant parameters.
"""

app = FastAPI(
    title="AWS Monster", description=description, version="0.0.1", docs_url="/"
)

tf = Terraform(working_dir="./terraform")
tf.init()


@app.post("/main", tags=["Main"])
async def main(
    instance_names: List[str] = Query(None),
    public_keys: List[UploadFile] = File(...),
    secrets: Secrets = Depends(),
    instance_params: InstanceParams = Depends(),
):
    if len(instance_names) != len(public_keys):
        raise HTTPException(
            status_code=404,
            detail="The length of instance names must be equal to the number of keys supplied!!",
        )
    # TODO: Use the paths variable to remove/unlink all the temp paths eventually.
    (params, paths) = params_to_list(public_keys, instance_names, instance_params)

    return_code, stdout, stderr = tf.apply(
        refresh=False,
        skip_plan=True,
        capture_output=False,
        var={
            "AWS_ACCESS_KEY": secrets.aws_access_key_id.get_secret_value(),
            "AWS_SECRET_KEY": secrets.aws_secret_key_id.get_secret_value(),
            "AWS_REGION": instance_params.region_name,
            "INSTANCES": params,
        },
    )
    # TODO: See if the instance id or public ip can be returned rather than what is below. id and ip are more useful things!!
    return {"return_code": return_code, "stdout": stdout, "stderr": stderr}
    # print(return_code, "\n", stdout, "\n", stderr)
    # print(save_upload_file_tmp("/home/morph/mykey.pub"))
    # data = json.load(file.file)
    # print(data)
    # print(save_upload_file_tmp(file))
    # return {"instance_ids": create_instance(model, key_names)}
