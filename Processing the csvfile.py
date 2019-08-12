import pandas as p
csvfile = pd.read_csv('E:\\technicalconfferenceproject\\Employee.csv')
data = csvfile[['Age','Salary']]
dob = input('Enter the age column')
sal = input('Enter the Salary column')
print("--sorting with age----")

if dob in data:
    data.sort_values(['Age'], axis=0,ascending=True, inplace=True)
    print(csvfile)
print("==== sorting with salary =====")

if sal in data:
    data.sort_values(['Salary'], axis=0,ascending=True, inplace=True)
    print(csvfile)

