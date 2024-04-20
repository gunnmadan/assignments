class EventAttendance: 
    def __init__(self, event_name,capacity):
        self.event_name = event_name
        self.capacity = capacity
        self.attendees = []

    def add_attendee(self, name):
        if len(self.attendees) < (self.capacity):
            self.attendees.append(name)
        else: 
            raise ValueError("Event at full capacity")
        
    def get_attendee_count(self):
        return len(self.attendees)
    
    def __str__(self):
        attendees_str = '\n'.join(self.attendees)
        return (f"Event Name: {self.event_name}, Capacity: {self.capacity}, List of Attendees: {self.attendees}")
    
if __name__ == "__main__":
    try:
        event1 = EventAttendance("AI Bootcamp", 4)
        event1.add_attendee('Ethan')
        event1.add_attendee('Chelsey')
        event1.add_attendee('Maria')
        event1.add_attendee('Maya')
        print(event1)
    except ValueError as e:
        print(e)

    try:
        event2 = EventAttendance("Business Exhibition", 3)
        event2.add_attendee('Michael')
        event2.add_attendee('Ruby')
        event2.add_attendee('Ethan')
        print(event2)
    except ValueError as e:
        print(e)






