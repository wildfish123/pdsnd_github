import time
import pandas as pd
import numpy as np

AVAILABLE_CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nSelect a city to filter by New York City, Chicago or Washington\n").capitalize()
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("Invalid input. Try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\n Select a month to filter by January, February, March, April, May, June or 'All'\n").capitalize()
        
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
        print("Invalid input. Try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nSelect a day to filter by Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'All'.\n").capitalize()
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
        print("Invalid input. Try again.")
        continue
      else:
        break

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
    # load data file 
    df = pd.read_csv(AVAILABLE_CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df

def get_time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('The most common month is :', popular_month)


    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('The most common day is :', popular_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour is :', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station are:', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('Most Commonly used end station are:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('Most Commonly used combination of start station and end station trip:', Start_Station, " and ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time is:', Total_Travel_Time)


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\n Gender types are:\n', gender_types)
    except KeyError:
      print("\n Gender types:\n Erorr no data available.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\n Earliest year is:', Earliest_Year)
    except KeyError:
      print("\n Earliest year:\n Erorr no data available.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\n Most recent year is:', Most_Recent_Year)
    except KeyError:
      print("\n Most recent year:\n Erorr no data available.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\n Most common year is:', Most_Common_Year)
    except KeyError:
      print("\n Most Common Year:\n Erorr no data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data (df):
    print('Press enter to see row data, press no to skip')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        get_time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()