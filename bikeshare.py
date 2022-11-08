import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months_dic = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6", 'no':'no'}
days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
            'sunday','no']

def get_filters():
    """
    Asking user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True: #handling invalid inputs with an infite loop
        city = input('Choose The City Name To Start, [ chicago , new york city , washington ] : ').lower()#Getting City Name
        if city in CITY_DATA:
            break
        else:
            print("\nlook like you entered an invalid city!\n")

    while True:
        print('\n[january, february, march, april, may, june]\n') #Showing The Avilable Months For Filtering
        month = input('Choose The Month You Want To Filter With. \' Type \"no\" If You Dont Want a Month Filter and Make Sure To Write The Month Full Name\' : ').lower() #Getting The Month Name
        if month in months_dic: #Cheaking The Avilability
            break
        else:
            print("\nlook like you entered an invalid month!\n")

    while True:
        print( '\n[monday, tuesday, wednesday, thursday, friday, saturday, sunday]\n') #Showing days input style to user 
        day = input('\nChoose The Day You Want To Filter With. \' Type \"no\" If You Dont Want a Day Filter and Make Sure To Write The Day Full Name If You Want a Day Filter\' : ').lower()#Getting The day Name
        if day in days_list: #Cheaking The Validation
            break
        else:
            print("\nlook like you entered an invalid day!\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loading data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city]) #Loading the city data into df
    df['Start Time'] = pd.to_datetime(df['Start Time']) #converting from str into date
    df['month_col'] = df['Start Time'].dt.month #creating months colmun
    df['day_col'] = df['Start Time'].dt.day_name() #creating days colmun
    df['hour_col'] = df['Start Time'].dt.hour #creating hours colmun
    if month != 'no': #filtering by month if exist
        df = df[df.month_col == int(months_dic[month])] #filter by month number
    
    if day != 'no' : #filtering by day if exist
        df = df[df.day_col == day.title()] #filtering by Day name

    return df


def time_stats(df):
    """Displaying statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    comm_month = df['month_col'].mode()[0] #Getting The Most Commont Month From The DataFrame 
    comm_month_name = list(months_dic.keys())[list(months_dic.values()).index(str(comm_month))] #Getting Month Name From The Dic
    print('Most Common Month IS : {}'.format(comm_month_name.title())) #Displaying

    comm_day = df['day_col'].mode()[0] #Getting The Most Common Day From  The DataFrame
    print('Most Common Day Is : {}'.format(comm_day)) #Displaying

    comm_st_hour = df['hour_col'].mode()[0] #Getting The Most Common Hour From  The DataFrame
    print('The Most Common Start Hour Is : {}'.format(comm_st_hour)) #Displaying
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    comm_st_station = df['Start Station'].mode()[0] #Getting the most commonly used start station
    print('Most Commnly Used Start Station Is : {}'.format(comm_st_station)) #displaying

    comm_end_station = df['End Station'].mode()[0] #Getting the most commonly used end station
    print('Most Commnly Used End Station Is : {}'.format(comm_end_station))  #displaying

    df['start end']= df['Start Station'] + ' --> ' + df['End Station'] #Creating new colmun with start and end stations
    comm_trip = df['start end'].mode()[0] #Getting the most commonly used start --> end stations
    print('Most Common trip is : {}'.format(comm_trip)) #displaying

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum()/60 #Counting Total Time In Minutes
    print('Total Travel Time = {} Min'.format(total_time))

    ave_time = df['Trip Duration'].mean()/60 #Coounting Average Time In Minutes
    print('Total Travel Time = {} Min'.format(ave_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    val_counts = df['User Type'].value_counts() # Counting User Type
    print('Users counts :\n{}\n'.format(val_counts))
    
    if city == 'chicago' or city == 'new york city': #Cheaking City Name To avoide errors in Calcs With Wascington City
    
        gender_count = df['Gender'].value_counts() #Counting Gender Values
        print('Gender Counts :\n{}'.format(gender_count))
    
        old = df['Birth Year'].min() #Getting The oldest Year Of Birth 
        new = df['Birth Year'].max() #Getting The Leatest Year Of Birth
        comm_birth = df['Birth Year'].mode()[0] #Getting Most Common Year of Birth
        print('Oldest birth Year Is      :{}'.format(int(old)))
        print('Most recent birth Year Is :{}'.format(int(new)))
        print('Most common birth Year Is :{}'.format(int(comm_birth)))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_city_data (df):
    respo = input('Do You Want To See The First Five Rows Of Data! [ yes / no ]').lower() #Getting User Desire
    
    if respo != 'yes': #return if response not equal to yes
        return
    
    print(df.head()) #print first five rows if response is 'yes'
    counter = 5
    
    while True :
        '''
        Getting User Desire for showing the next five rows
        '''
        next_respo = input('Do You Want To Print The Next Five Rows! [ yes / no ]').lower() 
        
        if next_respo != 'yes': #return if response not equal to yes
            return
        else: #print next five rows if response is 'yes'
            print(df.iloc[counter:counter+5])
            counter +=5
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_city_data (df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
