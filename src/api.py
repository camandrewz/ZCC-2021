import requests
import json


class API_CLIENT():

    def __init__(self, subdomain, email, api_key) -> None:
        self.domain = 'https://zccandrewscam.zendesk.com'
        self.email = 'cameron.andrews@gmail.com/token'
        self.api_key = 'PTUSr1lfqJXapEFDMcRDRcmfyfOk9ItN3KiJuNQP'
        self.session = requests.Session()
        self.session.auth = self.email, self.api_key

    def get_ticket_count(self):

        conn_str = f'{self.domain}/api/v2/tickets/count.json'

        # JSON returns dict, and the true ticket count lies in ['count']['value]'
        ticket_count = self.session.get(conn_str).json()['count']['value']

        return ticket_count

    def get_all_tickets(self):

        conn_str = f'{self.domain}/api/v2/tickets.json?page[size]=25'

        tickets = self.session.get(conn_str).json()['tickets']

        return tickets
