import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']
df = pd.read_fwf('data/auto-mpg-data.txt', header=None)
df.columns = columns

print(df)

df.describe()

print(df.dtypes)

df.horsepower = pd.to_numeric(df.horsepower, errors="coerce")

print(df.dtypes)

df = df.dropna()

X = df.iloc[:,1:8].copy()

y = df.mpg.copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

lreg_pre = LinearRegression()

lreg_pre.fit(X_train, y_train)
