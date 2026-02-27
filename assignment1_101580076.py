"""
Author: Luis Tello
Assignment: 01
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"  # String
preferred_weight_kg = 20.5   # Float
highest_rep = 25             # Integer
membership_active = True     # Boolean

print(f"Gym Member: {gym_member}")
print(f"Preferred Weight: {preferred_weight_kg} kg")
print(f"Highest Rep: {highest_rep}")
print(f"Membership Active: {membership_active}")

# Step c: Create a dictionary named workout_stats
# workout_stats is a dictionary mapping names of friends (Strings) to activity workout in minutes (Tuples)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 50, 35),   # yoga, running and weightlifting
    "Tyler": (20, 25, 15)
}

print("\nWorkout Stats Dictionary:")
print(workout_stats)

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    yoga, running, weights = minutes
    total_minutes = yoga + running + weights
    workout_stats[f"{friend}_Total"] = total_minutes

print("\nUpdated Workout Stats Dictionary with Totals:")
print(workout_stats)

# Step e: Create a 2D nested list called workout_list
workout_list = []
friend_names = []

for friend, minutes in workout_stats.items():
    if not friend.endswith("_Total"):
        workout_list.append(list(minutes))
        friend_names.append(friend)

print(f"\nWorkout List (2D): {workout_list}")
print(f"Friend Names: {friend_names}")

# Step f: Slice the workout_list
# Yoga and running minutes for all friends
print("\nYoga and running minutes for all friends:")
for row in workout_list:
    print(row[:2])

# Weightlifting minutes for the last two friends
print("\nWeightlifting minutes for the last two friends:")
for row in workout_list[-2:]:
    print(row[2])

# Step g: Check if any friend's total >= 120
print("\nActivity Check:")
for friend in friend_names:
    total = workout_stats[f"{friend}_Total"]
    if total >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
friend_input = input("\nEnter a friend's name: ")

if friend_input in friend_names:
    yoga, running, weights = workout_stats[friend_input]
    total = workout_stats[f"{friend_input}_Total"]
    print(f"\nWorkout stats for {friend_input}:")
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {running} minutes")
    print(f"Weightlifting: {weights} minutes")
    print(f"Total workout minutes: {total}")
else:
    print(f"\nFriend '{friend_input}' not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
highest_friend = None
highest_total = None
lowest_friend = None
lowest_total = None

for friend in friend_names:
    total = workout_stats[f"{friend}_Total"]
    if highest_total is None or total > highest_total:
        highest_total = total
        highest_friend = friend
    if lowest_total is None or total < lowest_total:
        lowest_total = total
        lowest_friend = friend

print("\nSummary:")
print(f"Friend with highest total workout minutes: {highest_friend} ({highest_total} minutes)")
print(f"Friend with lowest total workout minutes: {lowest_friend} ({lowest_total} minutes)")
