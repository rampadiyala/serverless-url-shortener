# Serverless URL Shortener

An API that creates short codes and redirects to the original links, written for AWS.

## Features

- URL validation
- Redirects
- Unit tests with a mock table

## Tech stack

Python, AWS Lambda, API Gateway, DynamoDB, AWS SAM

## How to run

Test: `python -m unittest discover tests`

Deploy: `sam build`, then `sam deploy --guided`. POST `{"url":"https://example.com"}` to `/links`, then open `/CODE`.

## Project files

- `app.py` - Lambda handler
- `template.yaml` - AWS resources
- `tests/` - unit tests

## Notes

The public API has no authentication. AWS may charge for usage. Delete test resources with `sam delete`.

## License

MIT. See [LICENSE](LICENSE).
