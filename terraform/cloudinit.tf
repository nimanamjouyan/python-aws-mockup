provider "cloudinit" {}

data "template_file" "init-script" {
    template = "${file("init.cfg")}"
    vars = {
        region = "${var.AWS_REGION}"
    }
}

data "template_cloudinit_config" "docker-cloudinit" {
    gzip = false
    base64_encode = false

    part {
        filename = "init.cfg"
        content_type = "text/cloud-config"
        content = data.template_file.init-script.rendered
    }
}
