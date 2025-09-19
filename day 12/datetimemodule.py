from datetime import datetime

# Current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Only date
print("Today's Date:", now.date())

# Only time
print("Current Time:", now.time())