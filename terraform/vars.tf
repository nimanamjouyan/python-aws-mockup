variable "AWS_ACCESS_KEY" {}
variable "AWS_SECRET_KEY" {}
variable "AWS_REGION" {
    defualt = "ap-southeast-2"
}
variable "AMI" {
    default = "ami-0567f647e75c7bc05"   # The AMI for the Ubuntu Server 20.04
}