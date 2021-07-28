class Ticket():

    def __init__(self, url, id, exteral_id, created_at, updated_at, type, subject, description, priority, status, recipient, 
                       requester_id, submitter_id, assignee_id, organization_id, group_id, tags, ticket_form_id, brand_id):

        self.url = url
        self.id = id
        self.external_id = exteral_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.type = type
        self.subject = subject
        self.description = description
        self.priority = priority
        self.status = status
        self.recipient = recipient
        self.requester_id = requester_id
        self.submitter_id = submitter_id
        self.assignee_id = assignee_id
        self.organization_id = organization_id
        self.group_id = group_id
        self.tags = tags
        self.ticket_form_id = ticket_form_id
        self.brand_id = brand_id

    def to_string(self):
        print("Ticket ID:", self.id)
        print("Subject:", self.subject)
        print("\n")