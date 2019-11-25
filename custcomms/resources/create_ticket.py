from resources.utilities import post_api_object
import json
zendesk_user_id = str


def notifications(*args):
    #  logging.info('Function: notifications')
    subject = 'Notification: MyCompany to {}'.format(args[0][0])
    body = '{}'.format(args[0][0]) + '\n' 'Please be aware that we are notifying you of important information ' \
                                     'regarding your account'
    ticket_type = 'incident'
    ticket_priority = 'normal'
    assignee_id = zendesk_user_id[0]
    custom_fields = args[0][1]
    email_ccs = args[0][2]
    requester = args[0][3]
    data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'requester': requester, 'email_ccs': email_ccs,
                       'custom_fields': custom_fields, 'assignee_id': assignee_id, 'type': ticket_type,
                       'priority': ticket_priority}}
    payload = json.dumps(data)
    return payload


def create_ticket(customer):
    function_url = '/api/v2/tickets.json'
    try:
        if customer == 'customer1':
            custom_fields = [{"id": 360015337231, "value": "Customer1"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer1.com'}, {'user_email': 'email@customer1.com'}]
            requester = 'email@customer1.com'
            data = 'customer1', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer2':
            custom_fields = [{"id": 360015337231, "value": "customer2"}]  # Impacted Customer Field
            email_ccs = [{'user_email': 'email@customer1.com'}, {'user_email': 'email@customer1.com'}]
            requester = 'email@customer1.com'
            data = 'customer2', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer3':
            custom_fields = [{"id": 360015337231, "value": "customer3"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer1.com'}]
            requester = 'email@customer1.com'
            data = 'customer3', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer4':
            custom_fields = [{"id": 360015337231, "value": "customer4"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer4.com'}, {'user_email': 'email@customer4.com'},
                         {'user_email': 'email@customer4.com'}, {'user_email': 'email@customer1.com'}]
            requester = 'email@customer1.com'
            data = 'customer4', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer5':
            custom_fields = [{"id": 360015337231, "value": "customer5"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer1.com'}]
            requester = 'email@customer1.com'
            data = 'customer5', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer6':
            custom_fields = [{"id": 360015337231, "value": "customer6"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer6.com'}, {'user_email': 'email@customer6.com'},
                         {'user_email': 'email@customer6.com'}]
            requester = 'email@customer6.com'
            data = 'customer6', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer7':
            custom_fields = [{"id": 360015337231, "value": "customer7"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer7.com'}, {'user_email': 'email@customer7.com'},
                         {'user_email': 'email@customer7.com'}, {'user_email': 'email@customer7.com'},
                         {'user_email': 'email@customer7.com'}, {'user_email': 'email@customer7.com'}]
            requester = 'email@customer7.com'
            data = 'customer7', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer8':
            custom_fields = [{"id": 360015337231, "value": "customer8"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer1.com'},
                         {"user_email": 'email@customer1.com'},
                         {"user_email": 'email@customer1.com'}, {"user_email": 'email@customer1.com'}]
            requester = 'email@customer1.com'

            data = 'customer8', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer9':
            custom_fields = [{"id": 360015337231, "value": "customer9"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer1.com'},
                         {"user_email": 'email@customer1.com'}]
            requester = 'email@customer1.com'
            #  logging.info('customer3 specific ticket information')
            data = 'customer9', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer10':
            custom_fields = [{"id": 360015337231, "value": "customer10"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer1.com'}, {"user_email": 'email@customer1.com'},
                         {"user_email": 'email@customer1.com'}, {"user_email": 'email@customer1.com'},
                         {"user_email": 'email@customer1.com'}]
            requester = 'email@customer1.com'
            #  logging.info('customer3 specific ticket information')
            data = 'customer10', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'customer11':
            custom_fields = [{"id": 360015337231, "value": "customer11"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'doc@customer11.com'}, {"user_email": 'email@customer1.com'},
                         {"user_email": 'email@customer1.com'}, {"user_email": 'email@customer1.com'}]
            requester = 'email@customer1.com'

            data = 'customer11', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
        elif customer == 'test':
            custom_fields = [{"id": 360015337231, "value": "MyCompany"}]  # Impacted Customer Field
            email_ccs = [{"user_email": 'email@customer1.com'}]
            requester = "email@customer1.com"
            data = 'Test', custom_fields, email_ccs, requester

            response = post_api_object(function_url, notifications(data))
            return response
    except Exception as err:
        raise err
    else:
        return 'The customer is not in the DataBase'

