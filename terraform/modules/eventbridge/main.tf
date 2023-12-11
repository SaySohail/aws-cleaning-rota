resource "aws_cloudwatch_event_rule" "every_monday_and_thursday" {
  name                = "every_monday_and_thursday"
  description         = "Fires every Monday and Thursday at 9am in 2023"
  schedule_expression = "cron(0 9 ? * MON,THU 2023)"
}

resource "aws_cloudwatch_event_target" "invoke_lambda" {
  rule      = aws_cloudwatch_event_rule.every_monday_and_thursday.name
  target_id = "invoke_lambda"
  arn       = var.lambda_function_arn
}

resource "aws_cloudwatch_event_rule" "every_monday_and_thursday_2024" {
  name                = "every_monday_and_thursday_2024"
  description         = "Fires every Monday and Thursday at 9am in 2024"
  schedule_expression = "cron(0 9 ? 1,2 MON,THU *)"
}

resource "aws_cloudwatch_event_target" "invoke_lambda_2024" {
  rule      = aws_cloudwatch_event_rule.every_monday_and_thursday_2024.name
  target_id = "invoke_lambda_2024"
  arn       = var.lambda_function_arn
}