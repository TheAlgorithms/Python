"""
Naive bayes from scratch on a custom dataset

Naive Bayes Algorithm is a probability based classification technique
for classifying labelled data. It makes use of Bayes Theorem in order to predict
the class of the given data. It is called Naive because it makes an assumption that
the features of the dependent variable are mutually independent of each other.
Although it is named naive, it is a very efficient model, often used as a baseline
for text classification and recommender systems.

You can find the detailed notes on this algorithm contributed by me on this notebook: -
    https://git.io/JTkvO
"""
import numpy as np
import pandas as pd


class naive_bayes:
    def __init__(self, X, y):
        """
        This method initializes all the required data fields of the NaiveBayes class

        Input -
            X: A pandas dataframe consisting of all the dependent variables
            y: A pandas dataframe consisting of labels
        """
        # Initializing the Dependent and Independent Variables
        self.X = X
        self.y = y

        # Initializing the column name y. (came in handy for me.
        # If you do not require it, then you can delete it)
        self.y_label = y.columns[0]

        # Initializing the variables to store class priors. Initiallt set to None.
        # They will be the assigned the correct values by executing calculate_prior
        # p_pos is probability of positive class
        # p_neg is probability of negative class
        self.p_pos = None
        self.p_neg = None

        # A dictionary to store all likelihood probabilities
        self.likelihoods = {}

        # Executing calculate_prior and calculate_likelihood to calculate prior and
        # likelihood probabilities
        self.calculate_prior()
        self.calculate_likelihood()

    def calculate_prior(self):
        """
        Method for calculating the prior probabilities

        Input - None

        Expected output: Expected to assign p_pos and p_neg their correct log
                         probability values. No need to return anything
        """
        # Concatenating X and y for easy access to features and labels
        df = pd.concat([self.X, self.y], axis=1)

        # Get the total number of positive points
        total_positive = df[self.y_label][df[self.y_label] == "Yes"].count()

        # Get the total number of negative points
        total_negative = df[self.y_label][df[self.y_label] == "No"].count()

        # Get the total number of points
        total = df["Play"].count()

        # Calculate log probability of positive class
        self.p_pos = np.log(total_positive / total)
        # Calculate log probability of negative class
        self.p_neg = np.log(total_negative / total)

    def calculate_likelihood(self):
        """
        Method for calculating the all the likelihood probabilities

        Input - None

        Expected output: Expected to create a dictionary of likelihood probabilities
                         and assign it to likelihoods.
        """
        # Concatenating X and y for easy access to features and labels
        df = pd.concat([self.X, self.y], axis=1)

        # Get the count of all positive and negative points
        total_positive = self.y[self.y[self.y_label] == "Yes"][self.y_label].count()
        total_negative = self.y[self.y[self.y_label] == "No"][self.y_label].count()

        # Traversing through each column of the dataframe
        for feature_name in self.X.columns:
            # Storing likelihood for each value this column
            self.likelihoods[feature_name] = {}

            # Traversing through each unique value in the column
            for feature in df.loc[:, feature_name].unique():
                # Calculate P(feature_name|'yes')
                feature_given_yes = df[
                    (df[feature_name] == feature) & (df[self.y_label] == "Yes")
                ][feature_name].count()

                # Get the log probability
                feature_given_yes = (
                    0
                    if feature_given_yes == 0
                    else np.log(feature_given_yes / total_positive)
                )

                # Calculate P(feature_name|'yes')
                feature_given_no = df[
                    (df[feature_name] == feature) & (df[self.y_label] == "No")
                ][feature_name].count()

                # Get the log probability
                feature_given_no = (
                    0
                    if feature_given_no == 0
                    else np.log(feature_given_no / total_negative)
                )

                # Store the likelihood the the dict
                self.likelihoods[feature_name][f"{feature}|yes"] = feature_given_yes
                self.likelihoods[feature_name][f"{feature}|no"] = feature_given_no

    def predict(self, test_data):
        """
        A method to predict the label for the input

        Input -
            test_data: A dataframe of dependent variables

        Expected output: Expected to return a dataframe of predictions. The column name
                         of dataframe should match column name of y
        """
        feature_names = test_data.columns
        # List to store the predictions
        prediction = []

        # Traversing through the dataframe
        for row in test_data.itertuples():
            # A list to store P(y=yes|X) and P(y=no|X)
            p_yes_given_X = []
            p_no_given_X = []

            # Traversing through each row of datadrame to get the value of each column
            for i in range(len(row) - 1):

                # Slicingthe 1st element as it is not needed (index)
                row = row[1:]

                # getting the likelihood probabilities from likelihood dict and
                # storing them in the list
                p_yes_given_X.append(
                    self.likelihoods[feature_names[i]][f"{row[0]}|yes"]
                )
                p_no_given_X.append(self.likelihoods[feature_names[i]][f"{row[0]}|no"])

            # Adding probability of positive and negative class to the list
            p_yes_given_X.append(self.p_pos)
            p_no_given_X.append(self.p_neg)

            # Since we are using log probabilities, we can ad them instead of
            # multiplying since log(a*b) = log(a) + log(b)
            p_yes_given_X = np.sum(p_yes_given_X)
            p_no_given_X = np.sum(p_no_given_X)

            # If p_yes_given_X > p_no_given_X, then we assign positive class
            # i.e True else False
            # Add the prediction to the prediction list
            prediction.append(p_yes_given_X > p_no_given_X)

        # Creating the prediction dataframe
        prediction = pd.DataFrame({self.y_label: prediction})

        # Converting True to yes and False to No
        prediction[self.y_label] = prediction[self.y_label].map(
            {True: "Yes", False: "No"}
        )

        # return the prediction
        return prediction


def main():
    df = pd.DataFrame(
        {
            "Outlook": [
                "Sunny",
                "Sunny",
                "Overcast",
                "Rain",
                "Rain",
                "Rain",
                "Overcast",
                "Sunny",
                "Sunny",
                "Rain",
                "Sunny",
                "Overcast",
                "Overcast",
                "Rain",
            ],
            "Temperature": [
                "Hot",
                "Hot",
                "Hot",
                "Mild",
                "Cool",
                "Cool",
                "Cool",
                "Mild",
                "Cool",
                "Mild",
                "Mild",
                "Mild",
                "Hot",
                "Mild",
            ],
            "Humidity": [
                "High",
                "High",
                "High",
                "High",
                "Normal",
                "Normal",
                "Normal",
                "High",
                "Normal",
                "Normal",
                "Normal",
                "High",
                "Normal",
                "High",
            ],
            "Wind": [
                "Weak",
                "Strong",
                "Weak",
                "Weak",
                "Weak",
                "Strong",
                "Strong",
                "Weak",
                "Weak",
                "Weak",
                "Strong",
                "Strong",
                "Weak",
                "Strong",
            ],
            "Play": [
                "No",
                "No",
                "Yes",
                "Yes",
                "Yes",
                "No",
                "Yes",
                "No",
                "Yes",
                "Yes",
                "Yes",
                "Yes",
                "Yes",
                "No",
            ],
        }
    )

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1:]

    model = naive_bayes(X, y)

    print(model.predict(X))


main()
