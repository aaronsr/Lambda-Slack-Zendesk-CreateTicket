# Project Title

One Paragraph of project description goes here

# Layout
```
.
├── README.md                   <-- Instructions file
├── cust-comms                  <-- Source code for a lambda function
│   ├── __init__.py
│   ├── app.py                  <-- Main function code
│   ├── requirements.txt        <-- Requirements code
├── template.yaml               <-- SAM Template
├── resources                   <-- Resource function files
|   └── __init__.py
|   ├── create_ticket.py
|   ├── environment_variables.py
|   ├── parse_data.py
|   ├── utilities.py
|__ tests                       <-- Unit tests
   └── unit
       ├── __init__.py
       ├── test_handler.py
       ├── testFixtures.py
```


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)
* [AWS CLI configured](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html)

My company used the azure AD to provide SSO with AWS, so I also followed this guide:
```
https://github.com/dtjohnson/aws-azure-login#docker
```

### Installing for Pycharm

I followed the guide [here](https://camillovisini.com/deploy-serverless-python-functions-aws-lambda-pycharm/) to setup the local environment:
```
https://camillovisini.com/deploy-serverless-python-functions-aws-lambda-pycharm/
    Some Specific SAM configuration info:
    RunTime: Python 3.7
    Handler = app.lambda_handler
    Environment Variables:
        (slack)BOT_TOKEN=
        (slack)VERIFICATION_TOKEN=
        ZENDESK_API_TOKEN=
        ZENDESK_API_USERNAME=
```
Basic text for the event template (Pycharm) & event.json
```
{
    "body": {
      "token": "Slack Token here",
      "team_id": "Slack Team ID",
      "api_app_id": "Your Slack App API ID",
      "event": {
        "client_msg_id": "7be085f6-d527-4015-a165-a75ae24ed7d9",
        "type": "message",
        "text": "Create Notification Test",
        "user": "Slack User ID",
        "ts": "1567180526.034200",
        "team": "Slack Team ID",
        "channel": "Slack Channel ID",
        "event_ts": "1567180526.034200",
        "channel_type": "im"
      },
      "type": "event_callback",
      "event_id": "Slack Event ID",
      "event_time": 1567180526,
      "authed_users": [
        "ULHD2RDJA"
      ]
},
    "headers": {
      "Accept": "*/*",
      "Accept-Encoding": "gzip,deflate",
      "CloudFront-Forwarded-Proto": "https",
      "CloudFront-Is-Desktop-Viewer": "true",
      "CloudFront-Is-Mobile-Viewer": "false",
      "CloudFront-Is-SmartTV-Viewer": "false",
      "CloudFront-Is-Tablet-Viewer": "false",
      "CloudFront-Viewer-Country": "US",
      "Content-Type": "application/json",
      "Host": "uij4hvd209.execute-api.us-west-2.amazonaws.com",
      "User-Agent": "Slackbot 1.0 (+https://api.slack.com/robots)",
      "Via": "1.1 ade18dc841d2e1cc8ef49611c5d4c93e.cloudfront.net (CloudFront)",
      "X-Amz-Cf-Id": "sahQqO9KtqtOHSAQC67wNMYxKMrVGHsbuj1PMz2Jd0B_d9vifBESNw==",
      "X-Amzn-Trace-Id": "Root=1-5d6946ee-4ecf6c8afbdb4f661468c93a",
      "X-Forwarded-For": "54.158.77.65, 70.132.60.89",
      "X-Forwarded-Port": "443",
      "X-Forwarded-Proto": "https",
      "X-Slack-Request-Timestamp": "1567180526",
      "X-Slack-Signature": "v0=355ea209964ab407d2fe99ea6ce3389889f8238aebe3c660a79d30f3bb1a9a5d"
    }
  }
```


### Local development
**Invoke function locally, with pycharm**
```
In Pycharm, click Run -> Run'[Local] app.lambda_handler**
```
**Invoking function locally using a local sample payload**

```bash
sam build -> Only necessary once
sam local invoke custCommsFunction --event event.json
```



## Testing
Next, we install test dependencies and we run `pytest` against our `tests` folder to run our initial unit tests:

```bash
pip install pytest pytest-mock --user
python -m pytest tests/ -v
```

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* AWS Serverless Application Model
* AWS Lambda
* AWS API Gateway

## Authors

* **Aaron LeMoine**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Camillo Visini via https://camillovisini.com
* Dave T. Johnson via https://github.com/dtjohnson/aws-azure-login
