
resource "helm_release" "docker-registry" {
  chart = "docker-registry"
  name  = "docker-registry"
  repository = "https://helm.twun.io"
  namespace = data.kubernetes_namespace_v1.kube-system.metadata[0].name

  set {
    name  = "service.nodePort"
    value = 30005
  }

  set {
    name  = "service.type"
    value = "NodePort"
  }

}
