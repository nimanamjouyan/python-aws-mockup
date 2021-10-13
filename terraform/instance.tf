resource "aws_instance" "my_instance" {
    for_each = {for i in var.INSTANCES: i.name => i}

    ami = each.value.ami
    instance_type = each.value.type

    # The public SSH key
    key_name = "${aws_key_pair.mykey[each.key].key_name}"

    # The security group
    vpc_security_group_ids = ["${aws_security_group.allow-ssh.id}"]

    # User data
    user_data = "${data.template_cloudinit_config.docker-cloudinit.rendered}"

    tags = {
        Name = each.value.name
    }
  
}