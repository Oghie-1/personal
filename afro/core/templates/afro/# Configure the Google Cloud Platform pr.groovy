# Configure the Google Cloud Platform provider ----453
provider "google" {
  credentials = file("service-account.json")
  project     = "my-project"
  region      = "us-central1"
}

# Create a GKE cluster
resource "google_container_cluster" "cluster" {
  name               = "my-cluster"
  initial_node_count = 3
  node_config {
    machine_type = "n1-standard-1"
  }
}

# Create a Deployment and a Service in the cluster
resource "kubernetes_deployment" "deployment" {
  metadata {
    name = "my-deployment"
  }
  spec {
    replicas = 3
    selector {
      match_labels = {
        app = "my-app"
      }
    }
    template {
      metadata {
        labels = {
          app = "my-app"
        }
      }
      spec {
        container {
          name  = "my-container"
          image = "gcr.io/my-project/my-image:latest"
        }
      }
    }
  }
}

resource "kubernetes_service" "service" {
  metadata {
    name = "my-service"
  }
  spec {
    selector {
      app = "my-app"
    }
    type     = "LoadBalancer"
    port {
      port        = 80
      target_port = 80
    }
  }
}
