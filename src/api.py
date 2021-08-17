import requests
import gc
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
        response = self.session.get(conn_str).json()

        if "error" in response:

            print("\nERROR: " + response["error"])

            if response["error"] == "Couldn't authenticate you":
                print(
                    "There is likely an error with your \"secrets.py\" file. Validate your entered credentials and Try Again.")

                quit()

        else:

            ticket_count = response['count']['value']
            return ticket_count

    def get_all_tickets(self, prev_or_next):

        if prev_or_next == None:

            conn_str = f'{self.domain}/api/v2/tickets.json?page[size]=25'

            tickets = self.session.get(conn_str).json()

            if "error" in tickets:
                print("\nERROR: " + str(tickets))

                if tickets["error"] == "Couldn't authenticate you":
                    print(
                        "There is likely an error with your \"secrets.py\" file. Validate your entered credentials and Try Again.")

                quit()

            self.curr_prev_link = tickets["links"]["prev"]
            self.curr_next_link = tickets["links"]["next"]

            if len(tickets["tickets"]) == 0:
                return -1
            else:
                return tickets['tickets']

        elif prev_or_next == "prev":

            conn_str = self.curr_prev_link

            tickets = self.session.get(conn_str).json()

            if "error" in tickets:
                print("\nERROR: " + str(tickets))

                if tickets["error"] == "Couldn't authenticate you":
                    print(
                        "There is likely an error with your \"secrets.py\" file. Validate your entered credentials and Try Again.")

                quit()

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

            if "error" in tickets:
                print("\nERROR: " + tickets["error"])

                if tickets["error"] == "Couldn't authenticate you":
                    print(
                        "There is likely an error with your \"secrets.py\" file. Validate your entered credentials and Try Again.")

                quit()

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
            print("\nERROR: " + ticket["error"])

            if ticket["error"] == "Couldn't authenticate you":
                print(
                    "There is likely an error with your \"secrets.py\" file. Validate your entered credentials and Try Again.")

                quit()

            elif ticket["error"] == "RecordNotFound":
                print(
                    "The ticket you requested could not be found. Try again using a different Ticket ID.")

                return {}

        if "error" in ticket:
            return {}
        else:
            return ticket

    def close(self):
        self.session.close()
        gc.collect()
