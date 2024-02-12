total_strikes = 0
required_strikes = 15

for hour in range(1, required_strikes+1):
    total_strikes += hour

print("Total number of clock strikes from 0 to " + str(required_strikes) + " hours is: " + str(total_strikes))