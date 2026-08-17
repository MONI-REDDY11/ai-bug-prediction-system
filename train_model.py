import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("dataset/bug_dataset.csv")

X = data.drop("bug", axis=1)
y = data["bug"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)

print("AI Bug Prediction Model Started")
print("Model Accuracy:", round(accuracy * 100, 2), "%")
print("Prediction completed successfully")