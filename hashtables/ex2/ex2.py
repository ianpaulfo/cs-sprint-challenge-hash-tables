#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

def hash_tickets(tickets, length):
    # Initialize an empty hash table with python dictionary
    dict = {}
    # iterate through tickets and hash as key value pair
    for i in range(length):
        ticket = tickets[i]
        source = ticket.get_source()
        destination = ticket.get_destination()
        dict[source] = destination
    return dict


def reconstruct_trip(tickets, length):
    routes = hash_tickets(tickets, length)
    dict = [routes["NONE"]] * length

    for i in range(1, len(dict)):
        dict[i] = routes[dict[i - 1]]


    return dict
