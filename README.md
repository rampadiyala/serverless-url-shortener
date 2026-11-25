# Serverless URL Shortener

Lambda, HTTP API and DynamoDB, defined with AWS SAM. The public API has no authentication, so delete the stack after testing (sam delete).

## How to run

Tests: python -m unittest discover tests. Deploy: sam build, then sam deploy --guided. Create a link: POST {"url":"https://example.com"} to /links. Open /CODE to redirect.
