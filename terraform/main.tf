module "lambda" {
  source = "./modules/lambda"

  function_name = var.function_name
  handler       = var.handler
  runtime       = var.runtime
  filename      = var.filename
}