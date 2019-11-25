from resources.environment_variables import bot_token, verification_token, api_Base_URL, api_UserName, api_Token
from botocore.vendored import requests
import urllib
import logging
import sys

zendesk_user_id = str
SLACK_URL = 'https://slack.com/api/chat.postMessage'


def post_fast_response(data):
    # Respond back to Slack within the 3 second retry parameter
    try:
        print('Function post_fast_response')
        header = {'content-type': 'application/json'}
        my_data = (
            ("token", bot_token),
            ("channel", data['body']['event']['channel'])
        )
        requests.post(SLACK_URL, data=my_data, headers=header)
        return "post_fast_response has successfully sent a message"
    except Exception as error:
        return_message = "Error in post_fast_response function: {}".format(error)
        return return_message


def post_slack_message(parse_data, return_message):
    try:
        print("This is post_slack_message function (parse_data)", parse_data)
        print("This is post_slack_message function (return_message)", return_message)
        data = urllib.parse.urlencode(
            (
                ("token", bot_token),
                ("channel", parse_data[0]['channel']),
                ("text", return_message)
            )
        )
        data = data.encode("ascii")
        print(data)

        request = urllib.request.Request(
            SLACK_URL,
            data=data,
            method="POST"
        )
        # Add a header mentioning that the text is URL-encoded.
        request.add_header(
            "Content-Type",
            "application/x-www-form-urlencoded"
        )

        # Fire off the request!
        urllib.request.urlopen(request).read()
        return "post_slack_message has successfully sent a message"
    except Exception as error:
        return_message = "Error in post_slack_message function: {}".format(error)
        return return_message


def slack_message_verification(data):
    # Verify slack message via Verification Token
    try:
        if data['token'] == verification_token:
            return "slack_message_verification has completed successfully"
    except Exception as error:
        return_message = "Error in post_slack_message function: {}".format(error)
        return return_message


def get_slack_data(data):
    slack_event_data = data['event']
    print('function: get_slack_data: \n', slack_event_data)
    if 'subtype' in slack_event_data:
        logging.warning('Subtype is true in the get_slack_data function, ending.')
        sys.exit()
    else:
        return slack_event_data


def get_slack_user(user_id):
    #  logging.info('Get slack user function')
    url = 'https://slack.com/api/users.info'
    header = {'content-type': 'application/json'}
    data = {'user': user_id,
            'token': bot_token}
    response = requests.get(url, headers=header, params=data)
    data = response.json()
    print('data variable in Function:get_slack_user ', data)
    return data


def find_zendesk_user(email):
    #  logging.info('Find Zendesk user function')
    function_url = '/api/v2/users/search.json?query={}'.format(email)
    response = get_api_object(function_url)
    data = (response['users'][0])
    #  logging.info('this is the data from Zendesk user function', data)
    return data


def post_api_object(function_url, data):
    #  logging.info('Function: post_api_object')
    header = {'content-type': 'application/json'}
    response = requests.post(api_Base_URL + function_url, data=data,
                             auth=(api_UserName, api_Token), headers=header)
    if response.status_code != 201:
        raise Exception('Zendesk Error', 'Status:', response.status_code, 'Problem with the request. Exiting.',
                        response.json())
    else:
        ticket_data = response.json()
        return ticket_data


def get_api_object(function_url):
    #  logging.info('Function: get_api_object')
    response = requests.get(api_Base_URL + function_url, auth=(api_UserName, api_Token))

    if response.status_code != 200:
        return 'Something went wrong, here is the error code - ' + response.status_code
    else:
        ticket_data = response.json()
        return ticket_data

