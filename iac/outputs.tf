output "order_service_url" {
  description = "Order service URL."
  value       = google_cloud_run_v2_service.order_service.uri
}

output "payment_service_url" {
  description = "Payment service URL."
  value       = google_cloud_run_v2_service.payment_service.uri
}

output "order_service_custom_domain" {
  description = "Order service domain."
  value       = google_cloud_run_domain_mapping.order_service_domain.name
}

output "payment_service_custom_domain" {
  description = "Payment service domain."
  value       = google_cloud_run_domain_mapping.payment_service_domain.name
}
