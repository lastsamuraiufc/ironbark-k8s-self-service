# ironbark-k8s-self-service
Self service portal for provisioning k8s namespaces 

The goal here is to create a simple web interface where a user can provision a k8s namespace on a k8s cluster.

This should include these high-level goals:
* The namespace should be locked down using some kind of permissions system
* The k8s cluster should use OPA and istio
* There is automation around setting up the k8s cluster and deploying the application ( Terraform / helm )
* Users should not be able to see all namespaces or other namespaces ( utilizing the security restrictions of the k8s namespace system )
* Provisioned namespaces can be tracked in a database or some other system - even terraform

# Skills we're aiming to gain

* Abilitty to secure and harden a k8s cluster using Terraform
* Code review process ( PR and push with git )
* Utilizing github runners with k8s permissions and roles
* k8s security things: roles, rolebindings, istio, and OPA
* k8s operators
* Terraform automation and security hardening - including how to use open source tools to further validate compliance

# Additional bonus goals

* Web interface showing provisioned namespaces and real-time security compliance reports

# Dev goals

* Use something like k3s to fire up a dev environment for POC testing.
* Use tailscale for network meshing - developers can connect to dev instances using this
* Create web interface to allow users to provision namespaces on k8s cluster
