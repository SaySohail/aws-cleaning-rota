
resource "aws_lambda_function" "example" {
  function_name = var.function_name
  handler       = var.handler
  role          = aws_iam_role.lambda_role.arn
  runtime       = var.runtime
  depends_on    = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]

  filename = var.filename       # "${path.module}/python/hello-python.zip"
  source_code_hash = filebase64sha256(var.filename)
}

# data "archive_file" "zip_the_python_code" {
# type        = "zip"
# source_dir  = "${path.module}/python/"
# output_path = "${path.module}/python/rota-python.zip"
# }