def process_status(status):
    status_messages = {
        'active': 'Active',
        'inactive': 'Inactive'
    }
    print(status_messages.get(status, 'Unknown'))

data = {'status': 'active'}
process_status(data['status'])
