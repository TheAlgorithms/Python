# Implementation of Naive Bayes Classifier
# https://www.github.com/JehanPatel

# What is Naive Bayes Classifier?
# The Naïve Bayes classifier is a supervised machine learning algorithm,
# which is used for classification tasks, like text classification.
# Unlike discriminative classifiers, like logistic regression, it does not
# learn which features are most important to differentiate between classes.

# Implementation

dataset = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Rainy", "Cool", "High", "Weak", "Yes"],
]

# converting string labels to integer


def preprocess_dataset(dataset):
    classes = set(example[-1] for example in dataset)
    class_mapping = {class_: i for i, class_ in enumerate(classes)}
    preprocessed_dataset = []
    for example in dataset:
        preprocessed_example = example[:-1] + [class_mapping[example[-1]]]
        preprocessed_dataset.append(preprocessed_example)
    return preprocessed_dataset, class_mapping


preprocessed_dataset, class_mapping = preprocess_dataset(dataset)

# calculating probabilities


def calculate_probabilities(dataset):
    attribute_counts = {}
    class_counts = {}
    for example in dataset:
        class_ = example[-1]
        if class_ not in class_counts:
            class_counts[class_] = 0
        class_counts[class_] += 1
        for i in range(len(example[:-1])):
            attribute = example[i]
            if attribute not in attribute_counts:
                attribute_counts[attribute] = {}
            if class_ not in attribute_counts[attribute]:
                attribute_counts[attribute][class_] = 0
            attribute_counts[attribute][class_] += 1
    probabilities = {}
    for attribute in attribute_counts:
        probabilities[attribute] = {}
        for class_ in class_counts:
            probabilities[attribute][class_] = (
                attribute_counts[attribute][class_] / class_
            )
