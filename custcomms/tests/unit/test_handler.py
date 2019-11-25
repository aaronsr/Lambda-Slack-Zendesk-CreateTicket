'''from .testFixtures import apigw_event
from .testFixtures import return_slack_message_parse_data as parsed_data
from .testFixtures import return_slack_message_return_message as returned_data
from custcomms import app


def test_lambda_handler(apigw_event):

    assert app.lambda_handler(apigw_event, "") == "200 OK"


def test_post_fast_response(apigw_event):

    assert app.post_fast_response(apigw_event) == "post_fast_response has successfully sent a message"


def test_post_slack_message(parsed_data, returned_data):

    assert app.post_slack_message(parsed_data, returned_data) == "post_slack_message has successfully sent a message"


def test_slack_message_verification(apigw_event):

    data = apigw_event["body"]
    assert app.slack_message_verification(data) == "slack_message_verification has completed successfully"


def test_parse_slack_data(apigw_event):
    data = apigw_event["body"]
    print(app.parse_slack_data(data))
    # Test for slack_event, and that it provides the correct slack message
    assert (app.parse_slack_data(data)[0]["text"]) == 'Create Notification Test'

    # Test for slack_user_data
    assert (app.parse_slack_data(data)[1]["ok"]) is True


def test_parse_slack_comment():


'''