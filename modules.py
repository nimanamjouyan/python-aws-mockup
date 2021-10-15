import logging
import shutil
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List, Callable, Dict
from model import InstanceParams

from fastapi import UploadFile


logger = logging.getLogger()


def save_upload_file_tmp(upload_files: List[UploadFile]) -> Path:
    tmp_paths = []
    for file in upload_files:
        try:
            suffix = Path(file.filename).suffix
            with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                shutil.copyfileobj(file.file, tmp)
                tmp_path = Path(tmp.name)
                tmp_paths += [tmp_path]
        finally:
            file.file.close()
    return tmp_paths


def params_to_list(
    upload_files: List[UploadFile],
    instance_names: List[str],
    instance_params: InstanceParams,
) -> List[Dict]:
    params_list = []
    tmp_paths = save_upload_file_tmp(upload_files)
    try:
        for tmp_path, instance_name in zip(tmp_paths, instance_names):
            params_list += [
                {
                    "name": instance_name,
                    "ami": instance_params.ami_id,
                    "region": instance_params.region_name,
                    "type": instance_params.instance_type,
                    "path_to_public_key": str(tmp_path),
                    # "path_to_public_key": os.path.join(
                    #     "..", *str(tmp_path).split(os.sep)
                    # ),
                }
            ]
    except Exception as exc:
        logger.error(exc, exc_info=True)

    return params_list, tmp_paths
