import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings('ignore')


def find_best_random_state(data: pd.DataFrame, target_column: str, iterations: int = 200) -> int:
    """
    Find the best random state for the Random Forest Classifier that maximizes accuracy.

    Args:
        data (pd.DataFrame): The dataset containing features and target variable.
        target_column (str): The name of the target column in the dataset.
        iterations (int): Number of random states to test. Default is 200.

    Returns:
        int: The random state that provides the best accuracy.
    """
    # Split dataset into predictors and target
    predictors = data.drop(target_column, axis=1)
    target = data[target_column]

    # Split dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.20, random_state=0)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    max_accuracy_rf = 0
    best_random_state = 0

    # Loop through specified random states
    for random_state in range(iterations):
        rf = RandomForestClassifier(random_state=random_state)
        rf.fit(X_train_scaled, y_train)
        y_pred_rf = rf.predict(X_test_scaled)
        
        current_accuracy = round(accuracy_score(y_test, y_pred_rf) * 100, 2)
        if current_accuracy > max_accuracy_rf:
            max_accuracy_rf = current_accuracy
            best_random_state = random_state

    print(f"The best random state is: {best_random_state} with an accuracy score of: {max_accuracy_rf} %")
    return best_random_state


if __name__ == "__main__":
    # Load dataset
    dataset = pd.read_csv("heart.csv")
    
    # Find the best random state
    best_state = find_best_random_state(dataset, target_column="target")
