from resources.utilities import post_fast_response, post_slack_message, slack_message_verification
from resources.parse_data import parse_slack_data, parse_slack_comment


import logging
import sys

zendesk_user_id = str
logging.getLogger().setLevel(logging.INFO)


def lambda_handler(data, context):
    """
    Handle an incoming HTTP request from a Slack chat-bot.
    """
    try:
        # logging data
        print('This is the value of data: ', data)

        # Sends fast response, and ignores Slacks auto-retry
        if "X-Slack-Retry-Reason" in data['headers']:
            sys.exit()
        else:
            post_fast_response(data)

        # Simple conversation of data to remove header information
        data = data['body']

        # Check for one time challenge from Slack
        if "challenge" in data:
            return data["challenge"]

        # Ignore bot events, only respond to non-bot events
        if "bot_id" in data['event']:
            logging.warning("Ignore bot event")
            sys.exit()
        elif "subtype" in data['event']:
            logging.warning("Ignore subtype bot event")
            sys.exit()
        else:
            # Authenticate message
            slack_message_verification(data)

            parse_data = parse_slack_data(data)

            text = data["event"]["text"].lower().split()

            return_message = parse_slack_comment(text)

            post_slack_message(parse_data, return_message)
    except Exception as error:
        return_message = "Error in lambda_handler function: {}".format(error)
        return return_message

    return "200 OK"























