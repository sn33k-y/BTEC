import time

def get_team_details():
    team_name = input("Enter Team Name: ")
    players = [input(f"Enter Player {i+1} Name: ") for i in range(5)]
    num_events = int(input("Enter number of events: "))
    return team_name, players, num_events

def get_individual_details():
    player_name = input("Enter Player Name: ")
    num_events = int(input("Enter number of events: "))
    return player_name, num_events

def start_timer():
    return time.time()

def stop_timer(start_time):
    return time.time() - start_time

def calculate_points(time_taken):
    return max(100 - int(time_taken*1.5), 10)  # Example point system

def team_competition():
    print("Starting TEAMS Competition...")
    for _ in range(4):
        print("Event Started!")
        start_time = start_timer()
        input("Press Enter when correct answer is chosen...")
        time_taken = stop_timer(start_time)
        points = calculate_points(time_taken)
        print(f"Time Taken: {time_taken:.2f} seconds, Points: {points}")
        

def individual_competition():
    print("Starting INDIVIDUAL Competition...")
    for _ in range(20):
        print("Event Started!")
        start_time = start_timer()
        input("Press Enter when correct answer is chosen...")
        time_taken = stop_timer(start_time)
        points = calculate_points(time_taken)
        print(f"Time Taken: {time_taken:.2f} seconds, Points: {points}\n")

def main():
    print("Display main menu")
    user_type = input("Are you competing as a TEAM or INDIVIDUAL? ").strip().upper()
    
    if user_type == "TEAM":
        team_details = get_team_details()
        print("Team Registered: ", team_details)
        team_competition()
    elif user_type == "INDIVIDUAL":
        individual_details = get_individual_details()
        print("Individual Registered: ", individual_details)
        individual_competition()
    else:
        print("Invalid selection! Please restart.")

if __name__ == "__main__":
    main()
