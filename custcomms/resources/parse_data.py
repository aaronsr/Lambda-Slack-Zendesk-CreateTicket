from resources.utilities import get_slack_data, get_slack_user, find_zendesk_user
from resources.create_ticket import create_ticket
zendesk_user_id = str


def parse_slack_data(data):
    try:
        slack_event = get_slack_data(data)
        slack_user_data = (get_slack_user(slack_event['user']))
        email = slack_user_data['user']['profile']['email']
        global zendesk_user_id
        zendesk_user_id = find_zendesk_user(email)
        text = slack_event["text"].lower().split()
        channel_id = slack_event["channel"]

        print('\n'"Slack Event: ", slack_event)
        print('\n'"Slack User Data: ", slack_user_data)
        print('\n'"email: ", email)
        print('\n'"text: ", text)
        print('\n'"channel ID: ", channel_id)

        return slack_event, slack_user_data, email, text, channel_id
    except Exception as error:
        return_message = "Error in parse_slack_data function: {}".format(error)
        return return_message


def parse_slack_comment(text):
    try:
        print('This is the var text, in the parse_slack_comment function', type(text), text)
        if 'help' in text:
            #  logging.info('The help command has been triggered')
            return_message = '*The command to use is: * `create notification <customer>`' \
                            '\n\n*Description:* This is a bot that will create a customer notification ticket. ' \
                            '\n```1. This only creates one ticket at a time' \
                            '\n2. This only creates the initial ticket. You still need to send the customer' \
                            ' a follow up message containing all of the details of the issue' \
                            '\n3. If you want to test, you can substitute the customer with Test ```' \
                            '\n\n*The customer list is:* ' \
                            '\n`customer1`, `Customer2`, `Customer3`, `Customer4`, `Customer5`, `Customer6`, `Customer7`, `Customer8`, `Customer9`, `Customer10` ' \
                            'and `Customer11`  '
            return return_message

        elif text == ['create', 'notification', 'Customer1']:
            #  logging.info('parse_slack_comment = Customer1')
            response = create_ticket('Customer1')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'Customer2']:
            #  logging.info('parse_slack_comment = Customer2')
            response = create_ticket('Customer2')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'Customer3']:
            #  logging.info('parse_slack_comment = Customer3')
            response = create_ticket('Customer3')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'Customer4']:
            #  logging.info('parse_slack_comment: Customer11')
            response = create_ticket('Customer4')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'Customer5']:
            #  logging.info('parse_slack_comment: Customer11')
            response = create_ticket('Customer5')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'Customer6']:
            #  logging.info('parse_slack_comment: Customer11')
            response = create_ticket('Customer6')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'Customer7']:
            #  logging.info('parse_slack_comment: Customer11')
            response = create_ticket('Customer7')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'Customer8']:
            #  logging.info('parse_slack_comment: Customer8')
            response = create_ticket('Customer8')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'Customer9']:
            #  logging.info('parse_slack_comment: Customer9')
            response = create_ticket('Customer9')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'customer10']:
            #  logging.info('parse_slack_comment: customer10')
            response = create_ticket('customer10')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'Customer11']:
            #  logging.info('parse_slack_comment: Customer11')
            response = create_ticket('Customer11')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}'.format(response['ticket']['id'])
            return return_message

        elif text == ['create', 'notification', 'test']:
            return_message = 'Hello World'
            '''response = create_ticket('test')
            return_message = 'Your ticket has been created successfully, here is the link: ' \
                             'https://<MyCompany>.zendesk.com/agent/tickets/{}' \
                .format(response['ticket']['id'])'''
            return return_message

        else:
            return_message = "Ticket creation failed please type help for assistance"
            return return_message

    except Exception as error:
        return_message = "Error in parse_slack_comment function: {}".format(error)
        return return_message

