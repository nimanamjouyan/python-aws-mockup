import logging
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import UploadFile


from model import Model

logger = logging.getLogger()


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path

def save_file_tmp(file_path: str) -> Path:
    # try:
    fsrc = open(file_path, "r")
    suffix = Path(file_path).suffix
    return suffix
    #     with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
    #         shutil.copyfileobj(upload_file.file, tmp)
    #         tmp_path = Path(tmp.name)
    # finally:
    #     upload_file.file.close()
    # return tmp_path