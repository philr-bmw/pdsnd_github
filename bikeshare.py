import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    cities = ['chicago', 'new york city', 'washington']
    # Errorhandler will detect cities chosen but not in scope. User is requested to reenter valid value.
    while True:
        city = input("Please enter the city (chicago, new york city, washington) you're interested in ").lower() #.lower() as safety mechanism 
        if city in cities:
            break
        else:
            print("This city is not included in our database scope, please reenter (chicago, new york city, washington)")  

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']  
    # Errorhandler will detect months chosen but not in scope. User is requested to reenter valid value.
    while True:
        month = input("Please enter the month (january to june or 'all') ").lower()
        if month in months:
            break
        else:
            print("This month is not included in our database scope, please reenter")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']         
    # Errorhandler will detect values entered but not valid. User is requested to reenter valid value.
    while True:
        day = input("Please enter a day (monday, tuesday, wednesday, thursday, friday, saturday, sunday or 'all') ").lower()
        if day in days:
            break
        else:
            print ("This is no valid entry, please reenter day of the week or 'all'")

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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()  #Function "dt.weekday_name" had to be used in Anaconda ...
    # extract the hours for additional investigation
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: ',most_common_month) #cal.month_name[most_common_month])

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trips ...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_start_station = df['Start Station'].mode()[0]
    print("The most common start station is: ", mc_start_station)

    # TO DO: display most commonly used end station
    mc_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ", mc_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequent combination of start and end is: {}'.format((df['Trip'].mode()[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is:", total_travel_time, " seconds or " , total_travel_time / 3600, " hours")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is :", mean_travel_time, " seconds" , mean_travel_time / 60, " minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("User types distribution: \n", user_counts)

    # TO DO: Display counts of gender
    # Errorhandler: Check first whether gender info is available
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Gender distribution: \n", gender_counts)
    else:
        print("There is no Gender Data available for the scope chosen.")

    # TO DO: Display earliest, most recent, and most common year of birth
    # Errorhandler: Check first whether info on birth year is available    
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        
        # earliest
        earliest_byear = birth_year.min()
        print("The earliest birth year is:", earliest_byear)
        
        # most recent
        most_recent_byear = birth_year.max()
        print("The most recent birth year is:", most_recent_byear)
        
        # most common
        mc_byear = birth_year.mode()[0]
        print("The most common birth year is:", mc_byear)
        
    else:
        print("There is no information on birth years available for the scope chosen.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def vis_raw_data(df):
    """Displays 5 lines of raw data on user request. Iterates through data till sufficient for user"""
    
    visualize_raw_data = input('\nWould you be interested in the raw data? Please enter yes or no: ').lower()
    if visualize_raw_data == 'yes':
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            additional_rows = input('Would you like to investigate a further set of lines? Please enter yes or no: ').lower()
            if additional_rows != 'yes':
                break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        vis_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
