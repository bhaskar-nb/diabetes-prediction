import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE

df = pd.read_csv("diabetes.csv")

print("Dataset loaded successfully\n")
print(df.head())

cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']

for col in cols:
    df[col] = df[col].replace(0, np.nan)
    df[col] = df[col].fillna(df[col].median())

print("\nData cleaned successfully\n")
print("\nMissing values:\n", df.isnull().sum())

x = df.drop("Outcome",axis=1)
y = df["Outcome"]

print("\nFeatures and traget separated")
print("x shape:", x.shape)
print("x shape:", y.shape)

sm = SMOTE(random_state=42)
x, y = sm.fit_resample(x, y)

print("\nAfter SMOTE:\n", pd.Series(y).value_counts())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("\nData split completed")

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

print("\nScalling completed")

model = RandomForestClassifier(n_estimators=500, max_depth=10, min_samples_split=5, min_samples_leaf=2, max_features='sqrt', random_state = 42)
model.fit(x_train, y_train)
print("\nModel training completed")

y_pred = model.predict(x_test)

print("\n--- Random Forest ---")
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nconfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(x_train, y_train)
lr_pred = lr_model.predict(x_test)

print("\n--- Logistic Regression ---")
print("Accuracy:", accuracy_score(y_test, lr_pred))

importance = model.feature_importances_

feature_importance = pd.DataFrame({'Feature': x.columns, 'Importance': importance}).sort_values(by = 'Importance', ascending=False)
print("\nFeature Importance:\n", feature_importance)

pickle.dump(model, open("model.pkl","wb"))
pickle.dump(scaler, open("scaler.pkl","wb"))

print("\nModel saved successfully")

def predict_diabetes(input_data):
    input_df = pd.DataFrame([input_data], columns = x.columns)
    input_scaled = scaler.transform(input_df)
    result = model.predict(input_scaled)

    return "Diabetic" if result[0] == 1 else "Not Diabetic"

sample = [2, 120, 70, 20, 79, 25.0, 0.5, 30]

print("\nSample Input:", sample)
print("Prediction:", predict_diabetes(sample))