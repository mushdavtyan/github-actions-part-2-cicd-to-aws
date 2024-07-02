terraform {
  required_version = "~> 1"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5"
    }
  }

  # backend "s3" {
  #   bucket = "life360-main-terraform"
  #   key    = "tfstate/us-east-1-dev/terraform.tfstate"
  #   region = "us-east-1"
  # }
}

resource "null_resource" "noop" {
  # This is a no-op resource
}
