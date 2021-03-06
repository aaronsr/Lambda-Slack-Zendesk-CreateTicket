import pytest


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": {
          "token": "Token",
          "team_id": "TeamID",
          "api_app_id": "AL3RKF63V",
          "event": {
            "client_msg_id": "7be085f6-d527-4015-a165-a75ae24ed7d9",
            "type": "message",
            "text": "Create Notification Test",
            "user": "UserID",
            "ts": "1567180526.034200",
            "team": "TeamID",
            "channel": "ChannelID",
            "event_ts": "1567180526.034200",
            "channel_type": "im"
          },
          "type": "event_callback",
          "event_id": "",
          "event_time": "",
          "authed_users": [
            ""
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
          "X-Forwarded-For": "",
          "X-Forwarded-Port": "443",
          "X-Forwarded-Proto": "https",
          "X-Slack-Request-Timestamp": "",
          "X-Slack-Signature": ""
        }
      }


@pytest.fixture()
def return_slack_message_parse_data():
    return ({
        'client_msg_id': '7be085f6-d527-4015-a165-a75ae24ed7d9',
        'type': 'message',
        'text': 'Create Notification Test',
        'user': '',
        'ts': '1567180526.034200',
        'team': '',
        'channel': '',
        'event_ts': '1567180526.034200',
        'channel_type': 'im'
      },
      {
        'ok': True,
        'user': {
          'id': '',
          'team_id': '',
          'name': '',
          'deleted': False,
          'color': 'db3150',
          'real_name': '',
          'tz': '',
          'tz_label': '',
          'tz_offset': -25200,
          'profile': {
            'title': '',
            'phone': '',
            'skype': '',
            'real_name': '',
            'real_name_normalized': '',
            'display_name': '',
            'display_name_normalized': '',
            'status_text': '',
            'status_emoji': '',
            'status_expiration': 0,
            'avatar_hash': 'f372b9fd917a',
            'image_original': 'https://avatars.slack-edge.com/2019-04-01/595736632548_f372b9fd917afaa1424f_original.jpg',
            'email': '',
            'first_name': '',
            'last_name': '',
            'image_24': 'https://avatars.slack-edge.com/2019-04-01/595736632548_f372b9fd917afaa1424f_24.jpg',
            'image_32': 'https://avatars.slack-edge.com/2019-04-01/595736632548_f372b9fd917afaa1424f_32.jpg',
            'image_48': 'https://avatars.slack-edge.com/2019-04-01/595736632548_f372b9fd917afaa1424f_48.jpg',
            'image_72': 'https://avatars.slack-edge.com/2019-04-01/595736632548_f372b9fd917afaa1424f_72.jpg',
            'image_192': 'https://avatars.slack-edge.com/2019-04-01/595736632548_f372b9fd917afaa1424f_192.jpg',
            'image_512': 'https://avatars.slack-edge.com/2019-04-01/595736632548_f372b9fd917afaa1424f_512.jpg',
            'image_1024': 'https://avatars.slack-edge.com/2019-04-01/595736632548_f372b9fd917afaa1424f_1024.jpg',
            'status_text_canonical': '',
            'team': 'T0BEPSLJV',
            'is_custom_image': True
          },
          'is_admin': False,
          'is_owner': False,
          'is_primary_owner': False,
          'is_restricted': False,
          'is_ultra_restricted': False,
          'is_bot': False,
          'is_app_user': False,
          'updated': 1567525379
        }
      },
      '**EMailAddress',
      [
        'create',
        'notification',
        'test'
      ],
      '')


@pytest.fixture()
def return_slack_message_return_message():
    return "Hello World"

