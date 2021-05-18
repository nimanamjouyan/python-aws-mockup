from pydantic import BaseModel, Field

class Model(BaseModel):
    ami_id: str = Field(..., title="The ami id of the instance")
    aws_access_key_id: str = Field(..., title="The aws access key id")
    aws_secret_access_key: str = Field(..., title="The aws secret key")
    region_name: str = Field(..., title="The region name of the instance")
    num_instances:  int = Field(..., title="The number of the instances (not more than 5 at a time)", le=5)
    instance_type: str = Field(default="t2.micro", title="The region name of the instance")
