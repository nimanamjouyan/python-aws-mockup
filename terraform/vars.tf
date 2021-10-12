variable "AWS_ACCESS_KEY" {}
variable "AWS_SECRET_KEY" {}
variable "AWS_REGION" {
    default = "ap-southeast-2"
}
variable "AMI" {
    default = "ami-0567f647e75c7bc05"   # The AMI for the Ubuntu Server 20.04
}

variable "INSTANCE_TYPE" {
    default = "t2.micro"   # The AMI for the Ubuntu Server 20.04
}
variable "PATH_TO_PRIVATE_KEY" {
    default = "nima_key"
}

variable "PATH_TO_PUBLIC_KEY" {
    default = "../mykey.pub"
}