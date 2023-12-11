variable "function_name" {
  description = "The name of the Lambda function"
  type        = string
  default     = "rota_tf"
}

variable "handler" {
  description = "The handler for the Lambda function"
  type        = string
  default     = "lambda_function.lambda_handler"
}

variable "runtime" {
  description = "The runtime for the Lambda function"
  type        = string
  default     = "python3.9"
}

variable "filename" {
  description = "The path to the function's deployment package within the local filesystem"
  type        = string
  default     = "../../my_deployment_package.zip"
}