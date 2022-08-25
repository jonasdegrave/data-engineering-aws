terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-central-1"
}

resource "aws_key_pair" "server-key" {
  key_name   = "server-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDJbKOEuSvvkUPYgzCVcfaPNf34z9au0VN6/o0B4dJp+bc2wAm0N2a+/BjG2HdhpEvfSdXp/FEeh+o5c6QqEz3eXCow+U6cvoJuFOZKXhkUwf/dIOguM+6/N/UbJUTzzxocuxwFs3ozkZKCmiKNozA1oEJmkycXuUniJolMxWMnrS4B68MPEFLCECX3IEZ3+fGcnmMUsVE1qOiRjq7sy4I/udv1V/SSIrLfaovtH4iE5ZPeXmtRby/cWuTex04leiprRUMaq0QfPqGj9tVz1jRHXOApCyKE17JzuYLrWxc6NjRoxn1OoHq7ydJy+RDcsMFyiu+J9IB+pcWDfMDp2f1Uyc4UgzZyCz42au0G/ep1AKAYdLYk4I/zQxHqbcCYOd3GJyA57Mekx+zXoCpeZMNCc9jMokBVCg3PQciY3soVl71usA6PWUAgswb9dYnvKhZbbGixWNgZ1foifw1hp1TTcGzCkpz/NpqGCnynRzfCIzccYmi350ri8hMQev7KSQM= jonas@MOTHERSHIP"
}

resource "aws_instance" "api_server" {
  ami           = "ami-065deacbcaac64cf2"
  instance_type = "t2.micro"
  key_name      = "server-key"
  subnet_id      = aws_subnet.public-1-eu-central-1a.id
  associate_public_ip_address = true
  security_groups = [ aws_security_group.allow_ssh.id, aws_security_group.allow_http.id ]

  tags = {
    Name = "api_server"
  }
}


