from pandas.core.frame import DataFrame
from api import API_CLIENT
from Ticket import Ticket
import pandas as pd
import os


def main():

    client = API_CLIENT()

    while True:

        print("\n")

        input_cmd = input("Enter your command (\"help\" lists all commands): ")

        if input_cmd == "help":
            print("\n")
            print("1) List Tickets (Pages of 25)\n")
            print("2) View a specific ticket\n")
            print("3) Exit\n")

        elif input_cmd == "1":

            clearConsole()
            print("\n\n\n\n")

            tix_table = get_tix_table(client, None)

            print("\n")
            print(tix_table)
            print("\nType \"next\" to go to the next page.")
            print("Type \"back\" to go to the previous page.\n")

        elif input_cmd == "next":

            tix_table = get_tix_table(client, "next")

            if not tix_table.empty:
                clearConsole()
                print("\n\n\n\n")
                print("\n")
                print(tix_table)
                print("\nType \"next\" to go to the next page.")
                print("Type \"back\" to go to the previous page.\n")

        elif input_cmd == "back":

            tix_table = get_tix_table(client, "prev")

            if not tix_table.empty:
                clearConsole()
                print("\n\n\n\n")
                print("\n")
                print(tix_table)
                print("\nType \"next\" to go to the next page.")
                print("Type \"back\" to go to the previous page.\n")

        elif input_cmd == "2":

            print("\n")

            id = input("Enter the Ticket ID: ")

            clearConsole()

            ticket = client.get_ticket(id)

            if ticket == {}:
                print("Uh Oh! The Ticket ID entered does not exist. Try Again!")
                continue
            else:

                print("\n\n\n\n")

                for key in ticket["ticket"]:

                    if key == "description":
                        print(str(key).upper() + ": \n" +
                              str(ticket["ticket"][key]) + "\n")

                    else:
                        print(str(key).upper() + ": " +
                              str(ticket["ticket"][key]) + "\n")

        elif input_cmd == "3":

            print("Goodbye!")
            quit()

        else:

            print("Sorry. Command not recognized.")


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def get_tix_table(client, next_or_prev):

    tickets = client.get_all_tickets(next_or_prev)

    if tickets == -1:
        print("\nYou cannot move to that page.")
        return DataFrame()

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
