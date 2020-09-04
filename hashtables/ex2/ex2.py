class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    locations = {}

    for ticket in tickets:
        locations[ticket.source] = ticket.destination

    current_location = locations["NONE"]
    route = []

    while current_location != "NONE":
        route.append(current_location)
        # go to next location
        current_location = locations[current_location]

    route.append("NONE")
    
    return route
