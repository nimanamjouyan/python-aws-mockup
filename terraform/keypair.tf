resource "aws_key_pair" "mykey" {
    for_each = {for i in var.INSTANCES: i.name => i}
    
    key_name = each.value.name
    public_key = "${file("${each.value.path_to_public_key}")}"
}