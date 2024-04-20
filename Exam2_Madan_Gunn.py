def manage_event_schedule(schedule, **changes):
    for key, value in changes.items(): 
        if value is not None:
            schedule[key] = value
        else: 
            del schedule[key] 
        
    #for previous_dict remove all entries that have value None
    # schedule = {k: v for k, v in schedule.items() if v is not None}

    return schedule 

def main():
    schedule = {'Keynote': '09:00',
                'Machine_Learning_101': '10:00', 'Networking': '11:00' }
    updated_schedule = manage_event_schedule(
        schedule, Cybersecurity = "14:00", Networking = '11:30')
    updated_schedule = manage_event_schedule(
        updated_schedule, Machine_Learning_101 = None)
    
    print(updated_schedule)

if __name__ == "__main__":
    main()
        

    
    
    
        