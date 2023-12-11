module "lambda" {
  source = "./modules/lambda"

  function_name = var.function_name
  handler       = var.handler
  runtime       = var.runtime
  filename      = var.filename
}

module "eventbridge"{
  source = "./modules/eventbridge"
  lambda_function_arn = module.lambda.lambda_function_arn
}