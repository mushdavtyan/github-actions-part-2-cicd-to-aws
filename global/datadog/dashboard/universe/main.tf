resource "null_resource" "package_lambda" {
  provisioner "local-exec" {
    command = <<-EOF
      ls -la
      pwd
      uname -a
    EOF
  }
}
