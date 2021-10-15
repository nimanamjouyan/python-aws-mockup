from pydantic import BaseModel, Field, SecretStr


class Secrets(BaseModel):
    aws_access_key_id: SecretStr = Field(..., title="The aws access key id")
    aws_secret_key_id: SecretStr = Field(..., title="The aws secret key")


class InstanceParams(BaseModel):
    ami_id: str = Field(
        default="ami-0567f647e75c7bc05", title="The ami id of the instance"
    )
    region_name: str = Field(
        default="ap-southeast-2", title="The region name of the instance"
    )
    instance_type: str = Field(
        default="t2.micro", title="The region name of the instance"
    )
