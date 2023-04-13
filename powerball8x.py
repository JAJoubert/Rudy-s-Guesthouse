# Importing the required libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from numbers_2 import numbers

# Creating a Pandas DataFrame with the historical data
data = pd.DataFrame(numbers, columns=['num1', 'num2', 'num3', 'num4', 'num5'])

# Initializing a set to keep track of previously predicted numbers
prev_nums = set()

# Initializing a list to keep track of the last set of predicted numbers
last_nums = []

# Training and predicting on each column individually
for i in range(5):
    # Splitting the DataFrame into input features (X) and target variable (y)
    X = data[['num1', 'num2', 'num3', 'num4']]
    y = data[f'num{i+1}']

    # Removing the last row from the DataFrame
    X = X[:-1]
    y = y[:-1]

    # Training the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Predicting the next possible number for this column
    next_num = int(model.predict(X.tail(1))[0])

    # Checking if the predicted number has already been predicted
    while next_num in prev_nums or next_num in last_nums or next_num > 50:
        next_num = int(model.predict(X.tail(1))[0])

    # Adding the predicted number to the set of previously predicted numbers
    prev_nums.add(next_num)

    # Adding the predicted number to the list of last predicted numbers
    last_nums.append(next_num)
    if len(last_nums) > 4:
        last_nums.pop(0)

    # Printing the next possible numbers for this column
    print(f"Possible numbers for column {i+1}:")
    for j in range(5):
        possible_num = next_num+j
        if possible_num not in last_nums and possible_num <= 50:
            print(possible_num)
