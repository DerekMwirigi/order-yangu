resource "google_cloud_run_v2_service" "payment_service" {
  project  = var.gcp_project_id
  name     = "payment-service"
  location = var.gcp_region

  template {
    containers {
      image = "us-central1-docker.pkg.dev/order-yangu-470223/order-yangu/payment-service-app:${var.order_service_tag}"
      ports {
        container_port = 8080
      }
    }
  }
}

resource "google_cloud_run_domain_mapping" "payment_service_domain" {
  location = var.gcp_region
  name     = "payments.orderyangu.top"

  metadata {
    namespace = var.gcp_project_id
  }
  
  spec {
    route_name = google_cloud_run_v2_service.payment_service.name
  }
}
