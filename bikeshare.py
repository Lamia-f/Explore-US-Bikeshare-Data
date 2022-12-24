import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv','newyorkcity': 'new_york_city.csv','newyork': 'new_york_city.csv' }

def HelloUser():
    return print("Hello user")

def PrintA(A):
    return print(A)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) filter_choice - type of filter applied to pandas data frame
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            #Ask the user to enter his choice
            city = input('Which city would you like to explore the data of? Chicago, New York or Washington?\n').lower()
            #run the exception if the user enter nonString value
        except:
            print('Invalid input. Please enter valid city name\n')
        else:
            #Check if the choice is in the CITY_DATA
            if not city in CITY_DATA:
                 print('No avialable data for entered city. Please try another city.\n')
            else:
                #End the loop if the choice met the requierments
                break
    #Choosing filtering option
    while True:
        try:
             #Ask the user to enter his choice
            filter_choice = input('would you like to filter the date by month, day, both or none? Type "none" for no time filter\n').lower()
             #run the exception if the user enter nonString value
        except:
            print('Invalid input. Please enter valid choice\n')
        else:
             #Check if the choice is correct
            if not filter_choice in ['month','day','both','none']:
                print('Invalid input. Please enter valid choice\n')
            else:
                #End the loop if the choice met the requierments
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    month = 'all'
    months = ['January','February','March','April','May','June']
    day = 'all'
    days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
    #If the user choose both or any day this code will run
    if filter_choice == 'both' or filter_choice == 'day' :
        while True:
            try:
                day = input('Please enter desired day name: ({})\n'.format(",".join(days))).title()
                #run the exception if the user enter nonString value
            except:
                print('Invalid input. Please enter valid day name\n')
            else:
                #Check if the choice is correct
                if not day in days:
                    print('Please enter valid day name.\n')
                else:
                    break
    #If the user choose both or any month this code will run
    if filter_choice == 'both' or filter_choice == 'month' :
        while True:
            try:
                month = input('Please enter desired month name: ({})\n'.format(",".join(months))).title()
                #run the exception if the user enter nonString value
            except:
                print('Invalid input. Please enter valid month name\n')
            else:
                #Check if the choice is correct
                if not month in months:
                    print('Please enter valid month name.\n')
                else:
                    break

    print('-'*40)
    return city, month, day, filter_choice


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
    #read the csv file
    df = pd.read_csv(CITY_DATA[city])
    #Convert the start date time to date type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #month column
    df['month'] = df['Start Time'].dt.month_name()
    #day column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, filter_choice):
    """Displays statistics on the most frequent times of travel."""

    print('\nThe Most Popular Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    month_mo = df['month'].mode()[0]
    month_number = df['month'].value_counts().iloc[0]
    print('The Most popular travelling month of travel is {}, Count:{} ,Filtered by:{}'.format(month_mo, month_number, filter_choice))

    # TO DO: display the most common day of week
    day_mo = df['day_of_week'].mode()[0]
    day_number = df['day_of_week'].value_counts().iloc[0]
    print('The Most popular day of week of travel is {}, Count:{} ,Filtered by:{}'.format(day_mo, day_number, filter_choice))

    # TO DO: display the most common start hour
    hour_mo = df['hour'].mode()[0]
    hour_number = df['hour'].value_counts().iloc[0]
    print('The Most popular start hour of travel is {}, Count:{} ,Filtered by:{}'.format(hour_mo, hour_number, filter_choice))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df, filter_choice):
    """Displays statistics on the most popular stations and trip."""

    print('\nThe Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['trip'] = df['Start Station'] + " , " + df['End Station']

    # TO DO: display most commonly used start station
    start_station_mo = df['Start Station'].mode()[0]
    start_station_number = df['Start Station'].value_counts().iloc[0]
    print('The Most popular start station of travel is {}, Count:{} ,Filtered by:{}'.format(start_station_mo, start_station_number, filter_choice))

    # TO DO: display most commonly used end station
    end_station_mo = df['End Station'].mode()[0]
    end_station_number = df['End Station'].value_counts().iloc[0]
    print('The Most popular end station of travel is {}, Count:{} ,Filtered by:{}'.format(end_station_mo, end_station_number, filter_choice))

    # TO DO: display most frequent combination of start station and end station trip
    trip_mo = df['trip'].mode()[0]
    trip_number = df['trip'].value_counts().iloc[0]
    print('The Most popular trip is {}, Count:{} ,Filtered by:{}'.format(trip_mo, trip_number, filter_choice))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, filter_choice):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip Duration...\n')
    start_time = time.time()
    total_trip_duration = df['Trip Duration'].sum()
    average_trip_duration = df['Trip Duration'].mean()

    # TO DO: display total travel time
    print('The total trips duration is {}s, Filtered by:{}'.format(total_trip_duration, filter_choice))

    # TO DO: display mean travel time
    print('The average trips duration is {}s, Filtered by:{}'.format(average_trip_duration, filter_choice))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, filter_choice):
    """Displays statistics on bikeshare users."""

    print('\nUser Information \n')
    start_time = time.time()
    dataframe_columns = list(df.columns)

    # TO DO: Display counts of user types
    print('Each user type count:\n{}\nFiltered by:{}'.format(df['User Type'].value_counts().to_string(), filter_choice))

    # TO DO: Display counts of gender
    if 'Gender' in dataframe_columns:
        print('Each gender count:\n{}\nFiltered by:{}'.format(df['Gender'].value_counts().to_string(), filter_choice))
    else:
        print('No gender data to dispaly')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in dataframe_columns:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        birth_year_mode = df['Birth Year'].mode()[0]
        print('The earliest year of birth: {}\nThe most recent year of birth: {}\nMost common year of birth: {}\nFiltered by:{}'.format(earliest_birth_year, recent_birth_year, birth_year_mode, filter_choice))
    else:
        print('No birth year data to dispaly')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_Dataframe(df):
    """Displays invidual data from Data Frame."""
    i = 0
    while True:
        try:
            display_data = input('\nWould you like to view invidual trip data? Enter yes or no.\n').lower().replace(" ","")
        except:
            print('that invalid choice. Please choose yes or no.\n')
        else:
            if not display_data in ['yes','no']:
                print('that invalid choice. Please choose yes or no.\n')
            else:
                break
    while display_data == 'yes':
        if i+5 <= len(df):
            print(df.iloc[i:i+5])
            i += 5
            while True:
                try:
                    display_data = input('\nWould you like to continue viewing invidual trip data? Enter yes or no.\n').lower().replace(" ","")
                except:
                    print('that invalid choice. Please choose yes or no.\n')
                else:
                    if not display_data in ['yes','no']:
                       print('that invalid choice. Please choose yes or no.\n')
                    else:
                        break
        else:
          print(df.iloc[i:len(df)])
          print('No more data to view')
          break






def main():
    while True:
        city, month, day, filter_choice = get_filters()
        df = load_data(city, month, day)

        time_stats(df, filter_choice)
        station_stats(df, filter_choice)
        trip_duration_stats(df, filter_choice)
        user_stats(df, filter_choice)
        display_Dataframe(df)

        while True:
            try:
                restart = input('\nWould you like to restart? Enter yes or no.\n').lower().replace(" ","")
            except:
                print('that invalid choice. Please choose yes or no.\n')
            else:
                if not restart in ['yes','no']:
                    print('that invalid choice. Please choose yes or no.\n')
                else:
                    break

        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
