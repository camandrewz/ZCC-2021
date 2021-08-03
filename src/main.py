from api import API_CLIENT
from Ticket import Ticket
import pandas as pd
import copy


def main():

    client = API_CLIENT()

    while True:
        input_cmd = input("Enter your command: ")

        if input_cmd == "help":
            print("Try \"get tickets\" to retrieve all tickets\n")

        elif input_cmd == "get tickets":

            tix_table = get_tix_table(client)

            print(tix_table)

            break


def get_tix_table(client):

    tickets = client.get_all_tickets()

    all_tickets = [Ticket(tix['url'], tix['id'], tix['external_id'], tix['created_at'], tix['updated_at'], tix['type'], tix['subject'], tix['description'], tix['priority'], tix['status'],
                          tix['recipient'], tix['requester_id'], tix['submitter_id'], tix['assignee_id'], tix['organization_id'], tix['group_id'], tix['tags'], tix['ticket_form_id'], tix['brand_id']) for tix in tickets]

    tix_table = pd.DataFrame(
        columns=['Ticket ID', 'Subject', 'Priority', 'Tags', 'Date Created'])

    for ticket in all_tickets:
        tix_table.loc[len(tix_table.index)] = [
            ticket.id, ticket.subject, ticket.priority, ticket.tags, ticket.created_at]

    return tix_table


if __name__ == "__main__":
    main()
