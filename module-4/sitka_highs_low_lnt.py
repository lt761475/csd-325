import csv, sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], [] #added lows list
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        
        #new change, append to lows list
        low = int(row[6])
        lows.append(low)


while True:
    #display instructions and get user choice
    print("Enter 'highs' to view daily high temperatures")
    print("Enter 'lows' to view daily low temperatures")
    print("Enter 'exit' to close")
    userChoice = input("Enter choice: ")
    
    if userChoice.lower() == "highs":
        # Plot the high temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format highs plo with red.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
        
    elif userChoice.lower() == "lows":
        # Plot the low temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format lows plot with blue.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
        
    elif userChoice.lower() == "exit":
        print("Thanks for visiting!")
        sys.exit()
        
    else:
        print("\n\nPlease enter below options.\n")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    