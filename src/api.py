import requests
from secrets import Secrets

class API_CLIENT():

    def __init__(self) -> None:
        self.domain = 'https://zccandrewscam.zendesk.com'
        self.email = Secrets.email
        self.api_key = Secrets.api_key
        self.session = requests.Session()
        self.session.auth = self.email, self.api_key
        self.curr_prev_link = None
        self.curr_next_link = None

    def get_ticket_count(self):

        conn_str = f'{self.domain}/api/v2/tickets/count.json'

        # JSON returns dict, and the true ticket count lies in ['count']['value]'
        ticket_count = self.session.get(conn_str).json()['count']['value']

        return ticket_count

    def get_all_tickets(self, prev_or_next):

        if prev_or_next == None:

            conn_str = f'{self.domain}/api/v2/tickets.json?page[size]=25'

            tickets = self.session.get(conn_str).json()

            self.curr_prev_link = tickets["links"]["prev"]
            self.curr_next_link = tickets["links"]["next"]

            if len(tickets["tickets"]) == 0:
                return -1
            else:
                return tickets['tickets']

        elif prev_or_next == "prev":

            conn_str = self.curr_prev_link

            tickets = self.session.get(conn_str).json()

            if tickets["links"]["prev"] != None:
                self.curr_prev_link = tickets["links"]["prev"]
                self.curr_next_link = tickets["links"]["next"]

            if len(tickets["tickets"]) == 0:
                return -1
            else:
                return tickets['tickets']

        elif prev_or_next == "next":

            conn_str = self.curr_next_link

            tickets = self.session.get(conn_str).json()

            if tickets["links"]["next"] != None:
                self.curr_prev_link = tickets["links"]["prev"]
                self.curr_next_link = tickets["links"]["next"]

            if len(tickets["tickets"]) == 0:
                return -1
            else:
                return tickets['tickets']

    def get_ticket(self, id):

        conn_str = f'{self.domain}/api/v2/tickets/{id}'

        ticket = self.session.get(conn_str).json()

        if "error" in ticket:
            return {}
        else:
            return ticket
