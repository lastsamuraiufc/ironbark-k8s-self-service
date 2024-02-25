terraform {
  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "2.12.1"
    }
  }
}

provider "kubernetes" {
  config_path    = "~/.kube/gu-tailscale.yaml"
  config_context = "gu-tailscale"
}

provider "helm" {
  kubernetes {
    config_path    = "~/.kube/gu-tailscale.yaml"
    config_context = "gu-tailscale"
  }
}
