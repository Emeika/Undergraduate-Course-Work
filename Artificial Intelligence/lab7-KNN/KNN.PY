import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def KNN_Classifier(X_train, y_train, X_test, k=10):
    predictions = []
    for x_test in X_test:
        distances = []
        for x_train in X_train:
            distance = np.sqrt(np.sum((x_test - x_train)**2))
            distances.append(distance)
        nearest_indices = np.argsort(distances)[:k]
        nearest_labels = [y_train[i] for i in nearest_indices]
        predicted_label = max(set(nearest_labels), key=nearest_labels.count)
        predictions.append(predicted_label)
    return predictions


# Read the file using Pandas
df = pd.read_csv('diabetes.csv')

# Separate features (X) and target variable (y) using column names
X = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']].values  # Features
y = df['Outcome'].values  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the KNN classifier
knn_predictions = KNN_Classifier(X_train, y_train, X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, knn_predictions)
# accuracy = np.mean(knn_predictions == y_test)
print("Accuracy:", accuracy)
