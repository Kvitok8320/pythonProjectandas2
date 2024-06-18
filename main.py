import pandas as pd

data = pd.read_csv("Student_performance_data _.csv")

df = pd.DataFrame(data)
print(df.head(3))
print(df.info())
print(df.describe())
print(f"средний возраст {df['Age'].mean()}")

data2 = pd.read_csv("dz.csv")
df2=pd.DataFrame(data2)
mean_salary = df2.groupby("City")["Salary"].mean()
print(f'Средняя зарплата по городам {mean_salary}')


data3 = pd.read_csv("Sheet1.csv")
df3=pd.DataFrame(data3)
print(df3.head())
print(df3.info())
print(df3.describe())
#mean_estimate = df3.mean()
print(df3.select_dtypes(include='number').mean())

Q1_math = df3['Math'].quantile(0.25)

Q3_math = df3['Math'].quantile(0.75)

print(f"Квартиль 0.25 = {Q1_math} квартиль 0.75 = {Q3_math}")

