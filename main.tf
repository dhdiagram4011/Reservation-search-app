# Copies the file as the root user using SSH
provisioner "file" {
  source      = "Reservation-search-app/*"
  destination = "/var/www/html"

  connection {
    type     = "ssh"
    user     = "root"
    password = "${var.root_password}"
    host     = "${var.host}"
  }
}


