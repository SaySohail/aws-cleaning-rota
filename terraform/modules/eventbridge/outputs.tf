output "eventbridge_rule_arn" {
  description = "The ARN of the EventBridge rule"
  value       = aws_cloudwatch_event_rule.every_monday_and_thursday.arn
}
output "eventbridge_rule_arn_2024" {
  description = "The ARN of the EventBridge rule for 2024"
  value       = aws_cloudwatch_event_rule.every_monday_and_thursday_2024.arn
}