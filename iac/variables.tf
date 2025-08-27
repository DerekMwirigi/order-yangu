variable "gcp_project_id" {
  description = "Google Cloud project ID."
  type        = string
  default = "order-yangu-470223"
}

variable "gcp_region" {
  description = "Google Cloud region to deploy resources in."
  type        = string
  default     = "us-central1"
}

variable "order_service_tag" {
  type        = string
  description = "The Docker image tag for the Order Service."
  default     = "latest" // TODO: Apply a tagged imaged so we can monitor image health
}

variable "payment_service_tag" {
  type        = string
  description = "The Docker image tag for the Payment Service."
  default     = "latest" // TODO: Apply a tagged imaged so we can monitor image health
}