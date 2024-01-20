provider "aws" {
  access_key = "your-aws-access-key"
  secret_key = "your-aws-secret-key"
  region     = "your-aws-region"
}

resource "aws_instance" "k3s_node" {
  count         = 3
  ami           = "ami-xxxxxxxxxxxxxxxxx"  # Replace with the appropriate AMI for your region and OS
  instance_type = "t3.micro"  # Adjust the instance type as needed
  key_name      = "your-ssh-key-name"
}

variable "k3s_server_ips" {
  default = aws_instance.k3s_node[*].public_ip
}

# Prometheus configuration
resource "aws_instance" "prometheus" {
  ami           = "ami-xxxxxxxxxxxxxxxxx"  # Replace with the appropriate Prometheus AMI
  instance_type = "t3.micro"  # Adjust the instance type as needed
  key_name      = "your-ssh-key-name"

  user_data = <<-EOF
              #!/bin/bash
              docker run -d -p 9090:9090 prom/prometheus
              EOF
}

# Grafana configuration
resource "aws_instance" "grafana" {
  ami           = "ami-xxxxxxxxxxxxxxxxx"  # Replace with the appropriate Grafana AMI
  instance_type = "t3.micro"  # Adjust the instance type as needed
  key_name      = "your-ssh-key-name"

  user_data = <<-EOF
              #!/bin/bash
              docker run -d -p 3000:3000 grafana/grafana
              EOF
}

# Alertmanager configuration
resource "aws_instance" "alertmanager" {
  ami           = "ami-xxxxxxxxxxxxxxxxx"  # Replace with the appropriate Alertmanager AMI
  instance_type = "t3.micro"  # Adjust the instance type as needed
  key_name      = "your-ssh-key-name"

  user_data = <<-EOF
              #!/bin/bash
              docker run -d -p 9093:9093 prom/alertmanager
              EOF
}
