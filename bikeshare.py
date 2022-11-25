#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
    city = input("Please enter the city you would like to explore: ").lower()
    while city not in ["new york city", "chicago", "washington"]:
        city = input("Please choose from new york city, chicago, washington OR none in lower case: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter the month you would like to explore: ").lower()
    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        month = input("Please choose a month from january to june or choose all in lower case: ").lower()
    
  
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the day you would like to explore: ")
    while day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
         day = input("Please choose a weekday from monday to sunday or choose all in lower case: ")
       
    print('-'*40)
    return city, month, day


# In[9]:


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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week
    
    if month !='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] ==month]
    
    if day !='all':
        days = ['monday', 'tuesday', 'wednesday','thrusday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]

    return df


# In[12]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('The most common month is: {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day of the week is: {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour is: {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[14]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('The most common used start station is: {}'.format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('The most common used station is: {}'.format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    popular_start_and_end_station = df.groupby(['Start Station','End Station']).value_counts().idxmax()
    print('The most frequent combination of start station and end station is: {}'.format(popular_start_and_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[16]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The count of user types is: {}'.format(user_type))


    # TO DO: Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print('The count of gender is: {}'.format(gender_type))
    except:
        print('This column is not available in this city')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('The most earliest year is: {}'.format(earliest_year))
        print('The most recent year is:  {}'.format(most_recent_year))
        print('The most common year of birth is: {}'.format(most_common_year))
    except:
         print('This column is not available in this city')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[17]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(travel_time))


    # TO DO: display mean travel time
    mean_travel_time  = df['Trip Duration'].mean()
    print(' The average of travel time is: {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



# In[24]:


def raw_data(df):
    """Displays if the user want to see 5 rows of raw bikeshare data at the time. The code was fixed 
    with the review suggestion"""
    
    while True:
         question = input("Would you like to see the raw data?, answer yes or no in lower case").lower()
         if question != 'yes':
            break
        print(tabulate(df_default.iloc[np.arrange(0+i,5+i)], headers = "keys"))
        i+=5
    
       


# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
