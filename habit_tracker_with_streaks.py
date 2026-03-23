import datetime

FILE_NAME = "habits.txt"
print("Welcome to Habit Tracker system !")
# -------- LOAD DATA --------
def load_data():
    data = {}
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, dates = line.strip().split("|")
                data[name] = dates.split(",") if dates else []
    except:
        pass
    return data

# -------- SAVE DATA --------
def save_data(data):
    with open(FILE_NAME, "w") as f:
        for habit, dates in data.items():
            line = habit + "|" + ",".join(dates)
            f.write(line + "\n")

# -------- ADD HABIT --------
def add_habit(data):
    name = input("Enter habit name: ")

    if name in data:
        print("Habit already exists!")
    else:
        data[name] = []
        print("Habit added!")

# -------- MARK DONE --------
def mark_done(data):
    name = input("Enter habit name: ")

    if name not in data:
        print("Habit not found!")
        return

    today = str(datetime.date.today())

    if today in data[name]:
        print("Already marked today!")
    else:
        data[name].append(today)
        print("Marked as done!")

# -------- CURRENT STREAK --------
def current_streak(dates):
    if not dates:
        return 0

    dates = sorted(dates)
    streak = 0
    today = datetime.date.today()

    for i in range(len(dates)-1, -1, -1):
        d = datetime.datetime.strptime(dates[i], "%Y-%m-%d").date()

        if d == today - datetime.timedelta(days=streak):
            streak += 1
        else:
            break

    return streak

# -------- LONGEST STREAK --------
def longest_streak(dates):
    if not dates:
        return 0

    dates = sorted([datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in dates])

    max_streak = 1
    current = 1

    for i in range(1, len(dates)):
        if dates[i] == dates[i-1] + datetime.timedelta(days=1):
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 1

    return max_streak

# -------- SHOW --------
def show(data):
    if not data:
        print("No habits found!")
        return

    for habit, dates in data.items():
        print(f"\nHabit: {habit}")
        print("Current Streak:", current_streak(dates))
        print("Longest Streak:", longest_streak(dates))

# -------- MAIN --------
habits = load_data()

while True:
    print("\n==== HABIT TRACKER ====")
    print("1. Add Habit")
    print("2. Mark as Done")
    print("3. Show Streaks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_habit(habits)

    elif choice == '2':
        mark_done(habits)

    elif choice == '3':
        show(habits)

    elif choice == '4':
        save_data(habits)
        print("Data saved. Bye!")
        break

    else:
        print("Invalid choice!")