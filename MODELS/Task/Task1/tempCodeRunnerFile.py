# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

file_path = 'student_performance.csv'
# Load the dataset
file_path = 'student_performance.csv'  # Update with your actual file path
data = pd.read_csv(file_path)

# Drop non-predictive columns like 'StudentID' and 'Name'
data = data.drop(columns=['StudentID', 'Name'])

# Encode categorical variables
label_encoder = LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['ParentalSupport'] = label_encoder.fit_transform(data['ParentalSupport'])
data['Gender'] = label_encoder.fit_transform(data['Gender'])  # Encode gender (Male/Female)
data['ParentalSupport'] = label_encoder.fit_transform(data['ParentalSupport'])  # Encode parental support levels

# Separate features and target variable
X = data.drop(columns=['FinalGrade'])
y = data['FinalGrade']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a linear regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = linear_model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R² Score: {r2}")


# Visualization
plt.figure(figsize=(14, 6))

# Scatter Plot of Predicted vs Actual Grades
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.7, color="teal")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Line of perfect prediction
plt.xlabel("Actual Grades")
plt.ylabel("Predicted Grades")
plt.title("Actual vs Predicted Grades")

# Residual Plot: Residuals vs Predicted Grades
plt.subplot(1, 2, 2)
residuals = y_test - y_pred
plt.scatter(y_pred, residuals, alpha=0.7, color="purple")
plt.axhline(y=0, color="red", linestyle="--")
plt.xlabel("Predicted Grades")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted Grades")

plt.tight_layout()
plt.show()

