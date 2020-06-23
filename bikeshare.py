########### bikeshare################

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

# Get user input for city (chicago, new york city, washington)

    input_city = input("Do you want to look at data from Chicago, New York City, or Washington? Enter the city name: ").lower()
    while input_city != 'chicago' and input_city != 'new york city' and input_city != 'washington':
        print('Please enter a valid city name. There is only data of Chicago, NYC, and Washington.')
        input_city = input("Do you want to look at data from Chicago, New York City, or Washington? Enter the city name: ").lower()
        continue

    if input_city == 'chicago'or input_city == 'new york city' or input_city == 'washington':
        city = input_city
        print("\nGreat! Let's look at {} then!".format(city))


    # Get user input for month (all, january, february, ... , june)

    input_month = input("What month do you want to look at? If you don't want to specify, type 'all'. Please enter the month: ").lower()
    while input_month not in ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',     'december', 'all'):
        print('Sorry, this seems to be an unvalid entry. Please enter a valid month.')
        input_month = input("What month do you want to look at? If you don't want to specify, type 'all'. Please enter the month: ").lower()
        continue

    if input_month in ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all'):
        month = input_month
        print("\nGreat! Let's look at {} then!".format(month))

    # Get user input for day of week (all, monday, tuesday, ... sunday)

    input_day = input("Do you want to filter by day of the week? If not, type 'all'. If yes, please enter the name of the weekday: ").lower()
    while input_day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print('Sorry, this seems to be an unvalid entry. Please enter a valid name of a weekday.')
        input_day = input("Do you want to filter by day of the week? If not, type 'all'. If yes, please enter the name of the weekday: ").lower()
        continue

    if input_day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        day = input_day
        print("\nGreat! Let's look at {} then!".format(day))

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # displays name of the month

    df['month'] = df['Start Time'].dt.month
    popular_month_number = df['month'].mode()[0]
    months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    popular_month = months_list[popular_month_number-1]
    print('Most Popular Start Month:', popular_month)

    # TO DO: display the most common day of week

    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print('Most Popular Start Day: ', popular_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + ' to ' + df['End Station']
    popular_start_end = df['Start End'].mode()[0]
    print('Most Popular Trip:', popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    total_time_min = total_time/60
    print('Total Travel Time: ', "{:.2f}".format(total_time), ' seconds which equals ', "{:.2f}".format(total_time_min), ' minutes')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    mean_time_min =  mean_time/60
    print('Mean Travel Time: ', "{:.2f}".format(mean_time), ' seconds which equals ', "{:.2f}".format(mean_time_min), ' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_count = df['User Type'].value_counts()
    print('Counts of User Types: ', type_count)

    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('\nCounts of Genders: ', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = int(df['Birth Year'].min())
    recent_year = int(df['Birth Year'].max())
    common_year = int(df['Birth Year'].mode()[0])
    print('\nEarliest Birth Year: ', earliest_year)
    print('Most Recent Birth Year: ', recent_year)
    print('Most Common Birth Year: ', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_dc(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_count = df['User Type'].value_counts()
    print('Counts of User Types: ', type_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == 'washington':
            user_stats_dc(df)
        else:
            user_stats(df)

        show_raw_data = input('\nWould you like to see the raw data basis? Enter yes to show 5 rows or enter no: ')
        x=0
        while show_raw_data.lower() == 'yes':
            print(df.iloc[x:(x+5)])
            x+=5
            show_raw_data = input('\nWould you like to see 5 more rows? Enter yes or no: ')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
