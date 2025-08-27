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

resource "google_cloud_run_domain_mapping" "order_service_domain" {
  location = var.gcp_region
  name     = "orders.orderyangu.top"
  spec {
    route_name = google_cloud_run_v2_service.order_service.name
  }
}
