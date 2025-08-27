
# Domain DNS is configured at Cloudflare and needs TXT DNS record to verify ownership
# Mapping a custom domain to the order-service
resource "google_cloud_run_domain_mapping" "order_service_domain" {
  location = var.gcp_region
  name     = "orders.orderyangu.top"
  spec {
    route_name = google_cloud_run_v2_service.order_service.name
  }
}

# Mapping a custom domain to the payment-service
resource "google_cloud_run_domain_mapping" "payment_service_domain" {
  location = var.gcp_region
  name     = "payments.orderyangu.top"
  spec {
    route_name = google_cloud_run_v2_service.payment_service.name
  }
}
