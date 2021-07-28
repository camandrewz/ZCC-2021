from api import API_CLIENT
from Ticket import Ticket
import pandas as pd
from flask import Flask, render_template, request


def main():

    client = API_CLIENT('zccandrewscam', 'cameron.andrews@gmail.com',
                        'PTUSr1lfqJXapEFDMcRDRcmfyfOk9ItN3KiJuNQP')

    ticket_count = client.get_ticket_count()
    tickets = client.get_all_tickets()

    all_tickets = [Ticket(tix['url'], tix['id'], tix['external_id'], tix['created_at'], tix['updated_at'], tix['type'], tix['subject'], tix['description'], tix['priority'], tix['status'],
                          tix['recipient'], tix['requester_id'], tix['submitter_id'], tix['assignee_id'], tix['organization_id'], tix['group_id'], tix['tags'], tix['ticket_form_id'], tix['brand_id']) for tix in tickets]

    tix_table = pd.DataFrame(
        columns=['Ticket ID', 'Subject', 'Date Created', 'Priority', 'Tags'])

    for ticket in all_tickets:
        tix_table.loc[len(tix_table.index)] = [
            ticket.id, ticket.subject, ticket.created_at, ticket.priority, ticket.tags]

    # print(tix_table)

    app = Flask(__name__)

    @app.route('/')
    def home():
        app.route('/')
        
        if 'Next' in request.form:
            print("Next test")
        elif 'Back' in request.form:
            print("Back Test")

        return render_template("home.html", tables=[tix_table.to_html(classes='data', index=False)])

    app.run(debug=True)


if __name__ == "__main__":
    main()
