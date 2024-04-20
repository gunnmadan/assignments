class NegativeValueError(Exception):
    """Custom exception for negative step count."""
    pass

def steps_to_miles(steps):
    """Convert steps to miles."""
    try:
        steps = int(steps)
    except ValueError:
        raise ValueError ("Exception: Non-numeric Value Entered.")
    
    if steps < 0:
        raise NegativeValueError("Exception: Negative Step Count Entered.")
    
    return steps / 2000 

def main():
    while True:
        try:
            steps = input("Enter number of steps: ")
            if steps.lower() == 'quit':
                break 
            miles = steps_to_miles(steps)
            print(f"{miles:.2f} miles")
        except (ValueError , NegativeValueError) as e:
            print(e)

if __name__ == "__main__":
    main()
