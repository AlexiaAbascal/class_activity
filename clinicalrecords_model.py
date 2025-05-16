from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
df = df.sample(frac=1).reset_index(drop=True)
df = df.rename(columns={"DEATH_EVENT":"target"})

# print(df["time"].describe())

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

print("\nRandom Forest Results:")
print("Accuracy:", accuracy_score(y_test, rf_preds))
print(classification_report(y_test, rf_preds))

import pickle

with open("classifier.pkl", "wb") as model_file:
    pickle.dump(rf_model, model_file)
    