import logging
from typing import List


from model import Model

logger = logging.getLogger()


def create_instance(model: Model, key_names: List[str]) -> List[str]:
    """Create ec2 instances based on supplied parameters.

    Args:
        model (Model): pydantic model used for supplying parameters to the function.
        key_names (List[str]): name of private keys supplied.

    Returns:
        List[str]: List of created ec2 instances.
    """

    logger.info("Creating instance...")

    try:
        instance_ids = []
        with open("./docker_install.sh", "r") as file:
            userdata = file.read()

        ec2_res = boto3.client(
            service_name="ec2",
            aws_access_key_id=model.aws_access_key_id,
            aws_secret_access_key=model.aws_secret_access_key,
            region_name=model.region_name,
        )
        for private_key in key_names:
            new_instance = ec2_res.run_instances(
                ImageId=model.ami_id,
                MinCount=model.num_instances,
                MaxCount=model.num_instances,
                UserData=userdata,
                InstanceType=model.instance_type,
                KeyName=private_key,
                # TagSpecifications=[{'ResourceType': 'instance','Tags': [{'Key': 'Name','Value': instance_name}]}],    # For adding instance name
            )

            logger.info("Instance created with ID: " + str(new_instance["Instances"][0]["InstanceId"]))
            instance_ids.append(new_instance["Instances"][0]["InstanceId"])

        return instance_ids
    except Exception as e:
        logger.error("Failed creating the instance: " + str(e))
