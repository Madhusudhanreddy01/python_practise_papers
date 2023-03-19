'''18. Write a python program where for every two hours it prints the pattern without using 
sleep function 
            * * * * * 
            * * * *
            * * *
            * *
            *
'''


import datetime

# Take user input for the number of rows
rows = int(input("Enter the number of rows: "))


# Set the delay time to 2 hours using the datetime.timedelta object
delay = datetime.timedelta(minutes=1)

# Run the loop continuously
while True:
    # Record the current time before printing the pattern
    start_time = datetime.datetime.now()
    
    # Print the pattern with decreasing number of stars in each row
    for i in range(rows, 0, -1):
        for j in range(0, i):
            print("* ", end="")
        print()

    # Record the current time after printing the pattern
    end_time = datetime.datetime.now()

    # Calculate the time elapsed by subtracting the start time from the end time
    time_elapsed = end_time - start_time

    # Use a busy-wait loop to delay the program until the desired delay time has passed
    while time_elapsed < delay:
        # Record the current time to update the time elapsed
        end_time = datetime.datetime.now()
        time_elapsed = end_time - start_time
