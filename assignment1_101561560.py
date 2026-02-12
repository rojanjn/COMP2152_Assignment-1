"""
Author: ROJAN JAFARNEZHAD
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5  # float
highest_reps = 25           # int
membership_active = True    # bool

# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex": (20, 30, 50),
    "Jamie": (15, 30, 90),
    "Taylor": (20, 45, 20),
    "John": (33, 10, 30)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for people, minutes in list(workout_stats.items()):
    total = sum(minutes)
    workout_stats[people + "_Total"] = total

print("\nWorkout Stats: ", workout_stats)

# Step e: Create a 2D nested list called workout_list
workout_list = []

for friend, value in workout_stats.items():
    if type(value) == tuple:
        workout_list.append(list(value))
# output (data type: 2D list containing int workout minutes)
print("\nWorkout List: ", workout_list)

# Step f: Slice the workout_list
yoga_run_mins = [row[0:2] for row in workout_list]
print("\nYoga and Running Minutes: ", yoga_run_mins)

weight_mins = [row[2] for row in workout_list[-2:]]
print("\nWeightlifting Minutes for the Last 2 Friends: ", weight_mins)

# Step g: Check if any friend's total >= 120
for key, value in workout_stats.items():
    if key.endswith("_Total") and value >= 120:
        friend_name = key.replace("_Total", "")
        print(f"\nGreat job staying active, {friend_name}!")

# Step h: User input to look up a friend
input_name = input("\nEnter friend's name to see their stats: ").strip().title()

if input_name in workout_stats:
    print(f"\nWorkout details for {input_name}: ")

    activities = ["Yoga", "Running", "Weightlifting"]
    minutes_tuple = workout_stats[input_name]

    # iterate through activities and minutes
    for activity, minutes in zip(activities, minutes_tuple):
        print(f"- {activity}: {minutes} Minutes")
        
    # print total workout minutes
    total_key = input_name + "_Total"
    print(f"--- Total Workout Minutes: {workout_stats[total_key]}")

else:
    print(f"\nFriend {input_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {}

# collecting totals only
for key, value in workout_stats.items():
    if key.endswith("_Total"):
        friend = key.replace("_Total", "")
        totals[friend] = value

# find highest and lowest
highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print(f"\nFriend with the HIGHEST total workout minutes: {highest} ({totals[highest]})")
print(f"Friend with the LOWEST total workout minutes: {lowest} ({totals[lowest]})")
