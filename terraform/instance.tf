resource "aws_instance" "my_instance" {
    ami = var.AMI
    instance_type = "t2.micro"
    key_name = "${aws_key_pair.mykey.key_name}"
  
}