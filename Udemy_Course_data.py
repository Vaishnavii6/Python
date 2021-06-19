import pandas as pd

data=pd.read_csv('7. Udemy Courses.csv')
# print(data)
# print(data.head())

# WHAT ARE ALL DIFFERENT SUBJECTS FOR WHICH UDEMY IS OFFERING COURSES?
# print(data.subject.unique())

# WHAT SUBJECTS HAS THE MAXIMUM NO OF COURSES
# print(data.subject.value_counts())

# SHOW ALL THE CIURSES WHICH ARE FREE OF COST
# print(data.is_paid == False)
# print(data[data.is_paid==False])               #IN DataFrame

# SHOW THE COURSES WHICH ARE PAID
# print(data.is_paid==True)
# print(data[data.is_paid == True])                 #IN DataFrame

# WHICH ARE TOP SELLING COURSES?
# myvar=(data.sort_values('num_subscribers',ascending=False))
# print(myvar.to_string())
# print(myvar)

# WHICH ARE LEAST SELLING COURSES?
# print(data.sort_values('num_subscribers',ascending=True))

# SHOW ALL COURSES OF GRAPHICS DESIGN WHERE THE PRICE IS BELOW 100?
# store=data[(data.price<'100') & (data.subject=='Graphic Design')]
# print(store)
# print(data[data.price<'100'])

# LIST OUT ALL THE COURSES THAT ARE RELATED WITH PYTHON
# print(data[data.course_title.str.contains('Python')])

# WHAT ARE COURSES THAT PUBLISHED IN YEAR 2015?
# data['published_timestamp']=pd.to_datetime(data.published_timestamp)
# # print(data.dtypes)
# data['Year']=data['published_timestamp'].dt.year
# # print(data)
# print(data[data.Year == 2015])

# WHAT ARE THE MAX. NO OF SUBSCRIBERS FOR EACH LEVEL OF COURSES?
# print(data.groupby('level')['num_subscribers'].max())
myvar=(data.groupby('level').max())
print(myvar.to_string())