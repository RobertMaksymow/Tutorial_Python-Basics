missions = [] #list to store mission names
mission_details = {'Red Rock': {'Destination': 'Mars', 'Launch Date': '23.23.2333', 'Crew': 'John Rambo, Robin Hood'}, 'To The Moon': {'Destination': 'Earth Moon', 'Launch Date': '12.21.2321', 'Crew': 'John Rambo, Barrack Obama, Donald Trump'}} #dictionary to store details of each mission

print(missions)
print( mission_details)

def add_mission(missions, mission_details, name, details):
    missions.append(name)
    mission_details[name] = details


    print(missions)
    print(mission_details)
    print(f"Mission {name} added successfully.")
    pass

def update_mission(mission_details, name, key, value):
    # TODO: Implement this function
    pass

def display_missions(missions, mission_details):
    print(missions)
    print(mission_details)
    pass

def list_astronauts(mission_details):
    set_names = {}
    for mission in mission_details.values():
        for astronaut in mission["Crew"].split(", "):
            set_names[astronaut] = True
    return set_names
   

# Main menu loop
while True:
    print("\nSpace Mission Management System")
    print("1. Add Mission")
    print("2. Update Mission")
    print("3. Display Missions")
    print("4. List Astronauts")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        name = input("Enter mission name: ")
        destination = input("Enter destination: ")
        launch_date = input("Enter launch date: ")
        crew = input("Enter crew members (comma-separated): ")
        details = {
            "Destination": destination,
            "Launch Date": launch_date,
            "Crew": crew
        }
        add_mission(missions, mission_details, name, details)

    elif choice == '2':
        name = input("Enter mission name to update: ")
        key = input("Enter detail to update (Destination/Launch Date/Crew): ")
        value = input(f"Enter new value for {key}: ")
        update_mission(mission_details, name, key, value)

    elif choice == '3':
        display_missions(missions, mission_details)

    elif choice == '4':
        astronauts = list_astronauts(mission_details)
        print("\nAll Astronauts:")
        for astronaut in astronauts:
            print(f"- {astronaut}")

    elif choice == '5':
        print("Exiting Space Mission Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")




# Understand Data Structure: mission_details should be a nested dictionary. The mission name should be the key, and another dictionary containing the mission info (Destination, Launch Date, Crew) should be the value.
# Example structure: {'Mission Name': {'Destination': 'Mars', ...}}
# Add Mission Logic: Inside your add_mission function, when you add a new mission to mission_details, ensure you are using the name as the key and assigning the details dictionary to it.
# Display Logic: Currently, your display_missions might be printing the whole dictionary structure. Try iterating through the missions (the list of names), and for each name, look up the info in the mission_details dictionary.