import pandas as pd
import numpy as np

df = pd.read_csv('G:/3D_P/Data/3D/CT/b_plt/0.05.csv')

#--------------------- basic ---------------------#

##  get information of the data:
# print(df.shape)
# print(df.info())

##  to see the specific data :
# print(df.head(400))  # first 400 data
# print(df.tail(40))  # last 400 data


#--------------------- DataFrame ---------------------#


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df2 = pd.DataFrame(people)
# print(df2)

# print(df2['email'])
# print(df2.email)
# print(type(df2['email']))     # see the datatype

# print(df2[['last', 'email']])     # get specific data

# print(df2.columns)    # get all the key of the dataframe


##  location: [row, column]
##  iloc
# print(df2.iloc[0])      # get the data of first row
# print(df2.iloc[[0,1]])      # first, second row
# print(df2.iloc[[0,1], 2])      # third column of 1. & 2. row 

    ## loc
# print(df2.loc[0])      # get the data of first row
# print(df2.loc[[0,1]])      # first, second row (get a DataFrame back)
# print(df2.loc[[0,1], ['email', 'last']])      # (iloc can not do it) use the keyword

#--------------------- Index ---------------------#

## 
# print(df2.set_index('email'))  # no change
# df2.set_index('email', inplace=True)  # changed


##  change ID (set the first column):
# df = df = pd.read_csv('G:/3D_P/Data/3D/CT/b_plt/0.05.csv', index_col='time')

##  sort
# df.sort_index()
# df.sort_index(ascending=False)  # in reverse order

#--------------------- Filtering ---------------------#

##   set a filter,
##   then use 'loc' to get the dataframe that we want.

##  df2
filter_1 = (df2['last'] == 'Doe') & (df2['first'] == 'John')    # and
filter_2 = (df2['last'] == 'Schafer') | (df2['first'] == 'John')

# print(df2.loc[filter_2, 'email']) # can also select specific value
# print(df2.loc[~filter_2, 'email']) # give the opposite of those result

##  df3
##  set 'Res' and 'Col' as the first column
df3 = pd.read_csv('G:/3D_P/data_analysis/pandas/survey_results_public.csv', index_col='Respondent')
schema_df3 = pd.read_csv('G:/3D_P/data_analysis/pandas/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


##   use high salary as a filter:
high_salary = (df3['ConvertedComp'] > 70000)   # the data which's salary is bigger than 70000
##   show up the data about 'Country', 'LanguageWorkedWith', 'ConvertedComp' in high_salary
# print(df3.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])


##   pick up the data of the "countries" that we interested in: 
countries = ['China', 'United States', 'India', 'Germany', 'United Kingdom']
filter_3 = df3['Country'].isin(countries)
# print(df3.loc[filter_3, 'Country'])


##  pick up the data contain "Python"
filter_4 = df3['LanguageWorkedWith'].str.contains('Python', na=False)
# print(df3.loc[filter_4, 'LanguageWorkedWith'])

#--------------------- Modify Data within DataFrames ---------------------#

##  df2

df2.columns = ['first_name', 'last_name', 'email']  # change all the keys
df2.columns = [x.lower() for x in df2.columns]  # turn all label to capital 
df2.columns = df2.columns.str.replace('_', ' ') # replace specific word to another 
df2.rename(columns={'first name':'first', 'last name':'last'}, inplace=True)    # change specific key 

df2.loc[2] = ['Fannie', 'Li', 'feifanlili0623@gmail.com'] # change specific row's data
df2.loc[2, ['last','email']] = ['Smith', 'JohnSmith@email.com']
df2.loc[2] = ['John', 'Doe', 'JohnDoe@email.com']

filter_5 = (df2['email']=='JohnDoe@email.com')
df2.loc[filter_5, 'last'] = 'Smith' # "df2[filter_5]['last'] = 'Smith'" cannot change 

df2['email'] = df2['email'].str.lower() # must use '=' !!

##  apply(function):
# print(df2['email'].apply(len))    # see the infor about data

def update_email(email):
    return email.upper()

df2['email'] = df2['email'].apply(update_email) # use selfset function
df2['email'] = df2['email'].apply(lambda x: x.lower())  # use 'lambda' function

# print(df2.apply(len))     # tell us how many value in each keyword, same principle as len(df['email'])
# print(df2.apply(lambda x: x.min()))    # "x" here is a series
# print(df2.applymap(len))    # get data map
# print(df2.applymap(str.lower))

#--------------------- Add/Remove rows & columns ---------------------#

# df2

# df2['full_name'] = df2['first'] + ' ' + df2['last'] # Add

# df2.drop(columns=['first', 'last'], inplace=True)   # Remove

# ##  split fullname to 'first' and 'last'
# df2[['first', 'last']] = df2['full_name'].str.split(' ', expand=True)

filter_6 = (df2['last'] == 'Doe')
# df2.drop(index=df2[filter_6].index, inplace=True)

#--------------------- Sorting ---------------------#

## df2
# df2 = df2.sort_values(by='last')
# df2 = df2.sort_values(by='last', ascending=False)
# df2 = df2.sort_values(by=['last', 'first'], ascending=[False, True])

# df2.sort_index(inplace=True)    # return

# df2_last = df2['last'].sort_values()    # get sorted 'last'


# ## df3
# ##  sort country in ascending order, and salary in descending order
# df3.sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False] ,inplace=True) 
# # print(df3[['Country', 'ConvertedComp']].head(45))   # here needs 2 brackets!!

# ##  to see the smallest/largest value:
# df3_10_largest = df3['ConvertedComp'].nlargest(10)  # just salary
# df3_10_larges = df3.nlargest(10, 'ConvertedComp')   # all infor

# print(df3_10_largest)
# print(df3_10_larges)

#--------------------- Grouping & Aggregating ---------------------#

## df3

##  median: a value in the middle of a series of values
##  mean: average
salary_median = df3['ConvertedComp'].median()  # get median value (return: value)
all_median = df3.median()   # return: data
describe = df3.describe()   # get a broad overview

salary_amount = df3['ConvertedComp'].count()    # how many people answered this question

hobby_counter = df3['Hobbyist'].value_counts()  # how many people answer yes & no
media_counter = df3['SocialMedia'].value_counts(normalize=True) # to see the popularity in percentage


##  Grouping :Split -> Apply Function -> Combine Results

##  we want to see the data of different *country*
country_grp = df3.groupby(['Country'])
data_US = country_grp.get_group('United States')   # data of US
    ## It's similar to filter method
    ## filt = df['Country'] == 'United States'
    ## df3.loc[filt]
filt = df3['Country'] == 'United States'
socialMed_US = df3.loc[filt]['SocialMedia'].value_counts()

socialMed_all = country_grp['SocialMedia'].value_counts()    # count SocialMedia of each country_group
socialMed_China = country_grp['SocialMedia'].value_counts(normalize=True).loc['China']

salary_median_all = country_grp['ConvertedComp'].median()
salary_median_ger = country_grp['ConvertedComp'].median().loc['Germany']

salary_median_mean_all = country_grp['ConvertedComp'].agg(['median', 'mean'])
salary_median_mean_Canada = country_grp['ConvertedComp'].agg(['median', 'mean']).loc['Canada']


filt = df3['Country'] == 'India'
amount_India_py = df3.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()

amount_China_py = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()).loc['China']
amount_py = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())

##  what % of each country use python?
country_respondents = df3['Country'].value_counts()
country_use_py = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())

python_df = pd.concat([country_respondents, country_use_py], axis='columns', sort=False)
python_df.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True)


print(python_df)

#pfmfrac/080/res/E
