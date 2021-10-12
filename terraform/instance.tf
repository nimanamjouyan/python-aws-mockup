resource "aws_instance" "my_instance" {
    ami = var.AMI
    instance_type = var.INSTANCE_TYPE

    # The public SSH key
    key_name = "${aws_key_pair.mykey.key_name}"

    # The security group
    vpc_security_group_ids = ["${aws_security_group.allow-ssh.id}"]
  
}