resource "google_cloud_run_v2_service" "order_service" {
  project  = var.gcp_project_id
  name     = "order-service"
  location = var.gcp_region

  template {
    containers {
      image = "ghcr.io/derekmwirigi/order-yangu/orders-service-app:${var.order_service_tag}"
      ports {
        container_port = 8080
      }
    }
  }
}