variable "AWS_ACCESS_KEY" {}
variable "AWS_SECRET_KEY" {}
variable "AWS_REGION" {
    default = "ap-southeast-2"
}
variable "INSTANCES" {
    default = [
        {
            "name" = "Nima"
            "ami" = "ami-0567f647e75c7bc05" 
            "region" = "ap-southeast-2"
            "type" = "t2.micro"
            "path_to_public_key" = "../mykey.pub"
        },
        {
            "name" = "George"
            "ami" = "ami-0567f647e75c7bc05" 
            "region" = "ap-southeast-2"
            "type" = "t2.micro"
            "path_to_public_key" = "../mykey.pub"
        }
    ]
  
}