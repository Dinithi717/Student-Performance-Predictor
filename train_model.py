import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("student-mat.csv", sep=";")

# Select features
X = df[["studytime", "absences"]]

# Convert absences to attendance
X["attendance"] = 100 - X["absences"]

# Target
y = df["G3"]

# Use only studytime and attendance
X = X[["studytime", "attendance"]]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("Model Trained Successfully!")