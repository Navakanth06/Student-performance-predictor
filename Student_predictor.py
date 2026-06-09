import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import numpy as np

df = pd.read_csv("student_data.csv")

df.fillna(df.mean(numeric_only=True), inplace=True)

X = df[["hours_studied", "attendance", "prev_marks"]]
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)


results = pd.DataFrame({
    "Actual_Marks": y_test,
    "Predicted_Marks": predictions
})

results.to_csv("predictions.csv", index=False)

print("Predictions saved successfully!")