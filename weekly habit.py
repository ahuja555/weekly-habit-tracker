habit_info = ("Reading", True, 7, 20.5)
weekly_habits = (1, 0, 1, 1, 0, 1, 1)

day_1_status = weekly_habits
day_4_status = weekly_habits

first_three_days = weekly_habits[0:3]
weekend_days = weekly_habits[5:7]

weekly_habits = weekly_habits + (1,)

done = 0
not_done = 0
for i in range(0, len(weekly_habits)):
    if weekly_habits[i] == 1:
        done += 1
    else:
        not_done += 1

print("===== WEEKLY HABIT TRACKER =====")
print(f"Habit Name:      {habit_info[0]}")
print(f"Daily Target:    {habit_info[3]} minutes")
print(f"Weekly Record:   {weekly_habits}")
print(f"Total Completed: {done} days")
print(f"Total Missed:    {not_done} days")
print("--------------------------------")

if done > not_done:
    print("Great habit progress!")
else:
    print("Try to be more consistent!")
print("================================")
