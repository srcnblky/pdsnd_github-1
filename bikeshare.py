import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


months = ["january", "february", "march", "april", "may", "june", "all"]
#define  the months to the program from this section. All letters are introduced in lower case so that there is no problem when the program compares.
days = [ "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "Saturday",  "all"]
#define  the days to the program from this section. All letters are introduced in lower case so that there is no problem when the program compares.
cities = ["chicago", "new york city", "washington"]
#define  the cities to the program from this section. All letters are introduced in lower case so that there is no problem when the program compares.

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ""
    global cities 
    while city not in cities:
        city = input("Which city do you want to analyze Chicago ,New york city or Washington ?  ").lower()

        if city in cities:
            print(" OK ")
        else:
            print("Invalid entry! city do you want to analyze chicago, new york city or washington")

    # TO DO: get user input for month (all, january, february, ... , june)

    month = ""
    global months
    while month not in months:
        month = input("Which month? January, February, March, April, May, June or you can type \"all\" : ").lower()

        if month in months:
            print(" OK ")
        if month == "all":
            print(" OK ")
        if month not in months:
            print("Invalid entry ! Which month? January, February, March, April, May, June or you can type \"all\" : ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day=""
    global days
    while day not in days:
        day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or you can type \"all\" : ").lower()

        if day in days:
            print(" OK ")
        if day == "all":
            print(" OK ")
        if day not in days:
            print("Invalid entry ! Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or you can type \"all\" :")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()


    if month != "all":
        month = months.index(month) + 1
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    time_beginning = time.time()

    # TO DO : display the most common month
    print("The most common month is : ")
    print(df["month"].value_counts().idxmax())

    # TO DO : display the most common day of week
    print("The most common day of week is : ")
    print(df["day_of_week"].value_counts().idxmax())

    # TO DO : display the most common start hour
    print("The most common start hour is : ")
    print(df["Start Time"].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - time_beginning))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    time_beginning = time.time()
	# TO DO : display most commonly used start station
    print("The most commonly used start station : ", )
    print(df["Start Station"].value_counts().idxmax())


    # TO DO : display most commonly used end station
    print("The most commonly used end station :")
    print(df["End Station"].value_counts().idxmax())


    # TO DO : display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip : {}, {}".format(df["End Station"].value_counts().idxmax(), df["Start Station"].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - time_beginning))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    time_beginning = time.time()


    # TO DO : display total travel time
    print("Total travel time : ")
    print(df["Trip Duration"].sum())


    # TO DO : display mean travel time
    print(df["Trip Duration"].mean())
    print("Mean travel time : ")

    print("\nThis took %s seconds." % (time.time() - time_beginning))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    time_beginning = time.time()

    # TO DO : Display counts of user types
    print("Counts of user types: \n")
    print(df["User Type"].value_counts())


    # TO DO : Display counts of gender
    if "Gender" in df.columns:
        print("\nCounts of gender: \n")
        print(df["Gender"].value_counts())

    # TO DO : Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:

        birth_year = df["Birth Year"]
        print("\nThe most common birth year: ")
        print(int(birth_year.value_counts().idxmax()))

        print("\nThe most recent birth year: ")
        print(int(birth_year.value_counts().idxmin()))

        print("\nThe most earliest birth year: ")
        print(int(df['Birth Year'].min()))
	
    print("\nThis took %s seconds." % (time.time() - time_beginning))
    print("-"*40)
   
#edit 
def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        df = pd.read_csv(CITY_DATA[city])

        tul=0
        while True:
            ViewFirst5 = input("\nWould you like to view first 5 line? Enter yes or no.\n")
            if ViewFirst5.lower() == 'yes':
                print(df[tul:tul+5])
                tul+=5
            elif ViewFirst5.lower() == 'no':
                break

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break
#edit 
print ("_Congrat!_")
if __name__ == "__main__":
	main()