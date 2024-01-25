"""
@author: Manish Kumar Chintha
"""

"""
list of libraries imported for the program to work.
"""
import math
import numpy as np
import csv
from collections import defaultdict
import operator
import random

"""
Class for DecisionTree classifier and all of it's related model.
I have called this class in RandomForest Class to build multiple tree models
and saved the objects and models in RandomForest class to use for classification

Building a Decision Tree and testing it on  training data.
I've separated the Decision Tree classifier and related function,
so that I can even test it independently.
"""


class DecisionTree(object):
    """
    class attributes; classIndex define the target class index in the data. In
    our case target class index is always the last index of the data. training
    sampels is the training data provided to Decision Tree Class every time

    We're getting random bootstrap sample data with replacement every time
    for each decision tree model built:
    """

    classIndex = 0
    trainingSamples = []

    """
    init function to initialize the classIndex and trainingSamples
    """

    def __init__(self, classIndex, trainingSamples):
        self.classIndex = classIndex
        self.trainingSamples = trainingSamples

    """
    This function is used to determine the entropy of the complete dataset
    provided. Which helps in finding Information Gain
    """

    def classEntropy(self, data):
        targetClassValuesCount = {}  # variable for saving different class labels count
        classEntropy = 0  # variable to save dataset entropy

        """Logic to find the class's different labels count of the dataset provided"""
        for row in data:
            if row[self.classIndex] in targetClassValuesCount:
                targetClassValuesCount[row[self.classIndex]] += 1
            else:
                targetClassValuesCount[row[self.classIndex]] = 1

        """Logic to calculate Entropy for dataset"""
        for eachKey in targetClassValuesCount:
            classEntropy -= (targetClassValuesCount[eachKey] / len(data)) * math.log(
                targetClassValuesCount[eachKey] / len(data), 2
            )
        return classEntropy  # Returning calculated entropy

    """
    Function to calculate the information for a particular attribute, this
    function use class entropy function also. The input for this function is
    index of the particular attribute for which we want to find the information
    gain.
    """

    def getInfoGainForSingleAttribute(self, data, attributeIndex):
        targetAttributeValuesCount = (
            {}
        )  # variable for saving different attribute labels count
        attributeEntropy = 0  # variable to save attribute entropy
        classEntropy = self.classEntropy(data)  # dataset entropy

        """Logic to find the attribute's different labels count of the dataset provided"""
        for row in data:
            if row[attributeIndex] in targetAttributeValuesCount:
                if (
                    row[self.classIndex]
                    in targetAttributeValuesCount[row[attributeIndex]]
                ):
                    targetAttributeValuesCount[row[attributeIndex]][
                        row[self.classIndex]
                    ] += 1
                else:
                    targetAttributeValuesCount[row[attributeIndex]][
                        row[self.classIndex]
                    ] = 1
            else:
                targetAttributeValuesCount[row[attributeIndex]] = {}
                targetAttributeValuesCount[row[attributeIndex]][
                    row[self.classIndex]
                ] = 1

        """
        Logic to calculate the entropy for the attribute based on the formula
        of Information Gain
        """
        entropies = {}
        entropiesTotal = {}
        for eachKey in targetAttributeValuesCount:
            keytotal = 0
            entropies[eachKey] = 0
            for value in targetAttributeValuesCount[eachKey]:
                keytotal += targetAttributeValuesCount[eachKey][value]
            for value in targetAttributeValuesCount[eachKey]:
                entropies[eachKey] -= (
                    targetAttributeValuesCount[eachKey][value] / keytotal
                ) * math.log(targetAttributeValuesCount[eachKey][value] / keytotal, 2)
            entropiesTotal[eachKey] = keytotal
        for eachEntropy in entropies:
            attributeEntropy += (entropiesTotal[eachEntropy] / len(data)) * entropies[
                eachEntropy
            ]

        """ Returning InfoGain of the attribute"""
        return classEntropy - attributeEntropy

    """
    Function to get the index of the attribute with highest information gain.
    Input for this function is the data and the attributes range.
    """

    def getHighestInfoGainForAttributesRange(self, data, attributesRange):
        allAttributesInfoGain = (
            {}
        )  # variable to save infoGain for each attribute provided

        """Getting infoGain for each attribute by calling function getInfoGainForSingleAttribute()"""
        for i in attributesRange:
            allAttributesInfoGain[i] = self.getInfoGainForSingleAttribute(data, i)

        """Finding the attribute with highest InfoGain and returning it's index"""
        allAttributesInfoGain = sorted(
            allAttributesInfoGain.items(), key=operator.itemgetter(1)
        )
        return allAttributesInfoGain[len(allAttributesInfoGain) - 1][0]

    """
    Function to build decision tree classifier based on the training data provided.
    In this function we're always getting the random bootstrap sample data with replacement.
    """

    def buildDecisionTreeModel(self, data, attributesRange=None):
        """
        This condition is true only first time when data set is provided, so
        for the first time we consider all attributes index except target class
        index.
        """
        if attributesRange is None:
            attributesRange = [
                i for i in range(0, len(data[0])) if i != self.classIndex
            ]

        """
        Below is the logic to calculate the majority class label from the dataset
        provided. The reason to find the Majority class label is comes in picture,
        when we have inadequate data (eg. no attributes indexes or all instances
        belong to same class). In such cases we return the majority class label as
        classifier predicted value.
        """
        targetClassLabels = {}
        for instance in data:
            if instance[self.classIndex] in targetClassLabels:
                targetClassLabels[instance[self.classIndex]] += 1
            else:
                targetClassLabels[instance[self.classIndex]] = 1

        targetClassLabels = sorted(
            targetClassLabels.items(), key=operator.itemgetter(1)
        )
        majorityClassLabel = targetClassLabels[len(targetClassLabels) - 1][0]

        """If there is no attribute (as explained above) I'm returning majority class label"""
        if len(attributesRange) == 0:
            return majorityClassLabel

        """If all instances belong to same target class, returning the majority class label"""
        if len(targetClassLabels) == 1:
            return majorityClassLabel

        """
        Below is the logic of getting the attribute with Highest InfoGain and
        building the nodes of the decision tree based on the attribute with highest
        information gain.
        """
        attributeWithHighestInfoGain = self.getHighestInfoGainForAttributesRange(
            data, attributesRange
        )
        decisionTree = {attributeWithHighestInfoGain: {}}

        """
        Excluding the index of the attribute with highest information gain, so
        that we can pass the remaining attributes indexes in the recursive call
        to build the next levels of the decision tree, until tree completes.
        """
        remainingAttributesRange = [
            i for i in attributesRange if i != attributeWithHighestInfoGain
        ]

        """
        Below is the logic to support random feature selection in Decision Tree
        i.e. at every level of the tree, I'm selecting a random subset of features
        and passing only those selected features, so that the next level tree should
        be based on only those features.

        This feature is used to reduce the training time of building the model.


        """
        if len(remainingAttributesRange) != 0:
            random.shuffle(remainingAttributesRange)
            remainingAttributesRange = remainingAttributesRange[
                : round(len(remainingAttributesRange) * 3 / 4)
            ]

        """
        I'm partitioning data based on the values of attribute with highest
        information gain. This data then passed to each recursive call of
        building the tree levels.
        """
        partitionOfDataForTreesNextLevelTraining = defaultdict(list)
        for eachInstance in data:
            partitionOfDataForTreesNextLevelTraining[
                eachInstance[attributeWithHighestInfoGain]
            ].append(eachInstance)

        """
        Logic to build the next levels to the tree by calling the function
        recursively again and again until all nodes are pure in the model built
        """
        for eachDataSet in partitionOfDataForTreesNextLevelTraining:
            generateSubTree = self.buildDecisionTreeModel(
                partitionOfDataForTreesNextLevelTraining[eachDataSet],
                remainingAttributesRange,
            )
            decisionTree[attributeWithHighestInfoGain][eachDataSet] = generateSubTree

        """returning the decision tree model built"""
        return decisionTree

    """
    Function to classify the instance based on the model provided. The function
    start traversing the trained model from top node based on the attribute index
    value at each node and traverse until it gets pure node. The value of the
    pure node is then returned.
    """

    def classifyInstance(self, model, instance, defaultTargetClass=None):
        if not model:  # if the model is empty then returning the majority class label
            return defaultTargetClass
        if not isinstance(model, dict):  # if the node is a leaf, return its class label
            return model
        attributeIndex = list(model.keys())[0]  # using list(dict.keys())
        attributeValues = list(model.values())[0]
        instance_attribute_value = instance[attributeIndex]
        if (
            instance_attribute_value not in attributeValues
        ):  # this value was not in training data
            return defaultTargetClass
        """
        Recursively traversing the DT model, to predict the instance target class"""
        return self.classifyInstance(
            attributeValues[instance_attribute_value], instance, defaultTargetClass
        )


"""
Class of Random Forest Classifier used to built the complete random forest
classifier with Bagging and random feature selection.

"""


class RandomForest(object):
    """
    no.OfTrees are the number of DT models to be built. treeModels is to save each
    model built using DecisionTree class. DecisionTreeObjects holds the objects
    of the DecisionTree class. classIndex is the index of target class passed.
    """

    nuOfTrees = 0
    treeModels = {}
    trainingSamples = []
    DecisionTreeObjects = {}
    classIndex = 0

    """Function to initialize the nuOfTrees, trainingSamples and target class"""

    def __init__(self, nuOfTrees, trainingSamples, classIndex):
        self.nuOfTrees = nuOfTrees
        self.trainingSamples = trainingSamples
        self.classIndex = classIndex

    """
    This function takes the random bootstrap data from the training samples
    provided with replacement.

    """

    def getRandomBootstrapSamplesWithReplacement(self, sampleSize):
        trainingSampleRange = [x for x in range(len(self.trainingSamples))]
        """randomising the data every time, when I take sample dataset for tree"""
        random.shuffle(trainingSampleRange)
        randomBootstrapSample = []
        for i in trainingSampleRange[:sampleSize]:
            randomBootstrapSample.append(self.trainingSamples[i])
        randomBootstrapSample = np.array(randomBootstrapSample)

        """Returning the bootstrap sample data with replacement"""
        return randomBootstrapSample

    """
    This function facilitate to find the predicted class label based on majority
    voting. It takes account the predicted class label of each and every model's
    precited class and then find the final result based on majority voting.

    """

    def getSimpleMajorityVoting(self, instance, defaultLabel):
        predictedClasses = {}  # variable to save predicted value of each model
        """Logic to count the predicted class labels count"""
        for i in range(self.nuOfTrees):
            predictedClass = self.DecisionTreeObjects[i].classifyInstance(
                self.treeModels[i], instance, defaultLabel
            )
            if predictedClass in predictedClasses:
                predictedClasses[predictedClass] += 1
            else:
                predictedClasses[predictedClass] = 1

        """Logic to find the maximum predicted label, returing it"""
        predictedClasses = sorted(predictedClasses.items(), key=operator.itemgetter(1))
        return predictedClasses[len(predictedClasses) - 1][0]

    """
    Function to build the random forest classifer model. It takes number of
    decision trees to build and pass random sample data for each decision tree
    model to to built.

    This function calls functions from DecisionTree class for decision tree
    model and saves the trained model as well as the objects of the Decision
    Tree class
    """

    def buildRandomForest(self):
        """Getting random bootstrap data for each decision tree learning"""
        bootstrapDataSampleSize = round(len(self.trainingSamples) * 3 / 4)

        """Building the ensembeles. calling the functions to train DT"""
        for i in range(self.nuOfTrees):
            trainingDataForThisTree = self.getRandomBootstrapSamplesWithReplacement(
                bootstrapDataSampleSize
            )
            self.DecisionTreeObjects[i] = DecisionTree(
                self.classIndex, trainingDataForThisTree
            )
            self.treeModels[i] = self.DecisionTreeObjects[i].buildDecisionTreeModel(
                trainingDataForThisTree
            )

    """
    Function to classify the test data, finding the accuracy and building the
    confusion model based on the predicted value of the test data instances.
    """

    def classifyTestData(self, testInstances):
        """Variables to find accuracy"""
        total = 0
        correct = 0

        """Logic to find the majority calss value"""
        majorityValuesCount = {}
        for instance in testInstances:
            if instance[self.classIndex] in majorityValuesCount:
                majorityValuesCount[instance[self.classIndex]] += 1
            else:
                majorityValuesCount[instance[self.classIndex]] = 1
        majorityValuesCount = sorted(
            majorityValuesCount.items(), key=operator.itemgetter(1)
        )
        majorityClassValue = majorityValuesCount[len(majorityValuesCount) - 1][0]

        """Logic to initialize the confusion matrix"""
        confusionMatrix = {}
        for instance in testInstances:
            if instance[self.classIndex] not in confusionMatrix:
                confusionMatrix[instance[self.classIndex]] = {}

        """
        Logic to predict the label of the instance provided, couting the total
        and correctly classified instances and saving the data for creating
        confusion matrix below
        """
        for instance in testInstances:
            total += 1
            actual_label = instance[self.classIndex]
            predicted_label = self.getSimpleMajorityVoting(instance, majorityClassValue)
            if predicted_label not in confusionMatrix[actual_label]:
                confusionMatrix[actual_label][predicted_label] = 1
            else:
                confusionMatrix[actual_label][predicted_label] += 1
            if predicted_label == actual_label:
                correct += 1

        """
        The logic below tries to print the confusion matrix based on the
        predicted label and total data of the test instances.


        """
        confusionHeader = "\t"
        for key in confusionMatrix:
            confusionHeader = confusionHeader + key + "\t"
        confusionHeader = confusionHeader + "<-- Predicted as"
        print(confusionHeader)
        for key1 in confusionMatrix:
            confustionLine = key1 + "\t"
            for key2 in confusionMatrix:
                if key2 in confusionMatrix[key1]:
                    confustionLine = (
                        confustionLine + str(confusionMatrix[key1][key2]) + "\t"
                    )
                else:
                    confustionLine = confustionLine + "0\t"
            print(confustionLine)
        print("\n")
        print("Accuracy :: ", round((correct * 100) / total, 2), "%")


"""
The main reason to make this class is just to encapsulate all the program
in one, so that the complete program look as a RandomForest classifier.
"""


class RandomForestClassifier(object):
    """
    variable to save the training data, test data and classIndex of the data
    from the filename provided.
    """

    trainingData = []
    testData = []
    classIndex = 0
    filename = ""
    nuOfTrees = 0

    """Initialize the filename and number of trees to be used in ensemble"""

    def __init__(self, filename, nuOfTrees):
        self.nuOfTrees = nuOfTrees
        self.filename = filename

    """
    This fnction separates the file data into training data; test data; header
    and saves it into the variables declared above to use in the program
    """

    def createTrainingAndTestSamplesFromData(self):
        rows = csv.reader(open(self.filename))
        self.classIndex = len(next(rows)) - 1
        data = []
        for row in rows:
            data.append(row)
        random.shuffle(data)
        data = np.array(data)
        cutOff = round(len(data) * 3 / 4)
        self.trainingData = data[:cutOff]
        self.testData = data[cutOff:]

    """
    This function create RandomForest class object and calls the function to
    classify the test data provided
    """

    def performClassification(self):
        randomForestClassifier = RandomForest(
            numberOfTrees, self.trainingData, self.classIndex
        )
        randomForestClassifier.buildRandomForest()
        randomForestClassifier.classifyTestData(self.testData)


"""Number of trees defined to built a random forest classifier"""
numberOfTrees = 10

print("+++++++++++++++++Classification Results for Tennis Data+++++++++++++++")
randomForestClassifier = RandomForestClassifier("tennis.csv", numberOfTrees)
randomForestClassifier.createTrainingAndTestSamplesFromData()
randomForestClassifier.performClassification()
print(
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    end="\n\n\n",
)
print("+++++++++++++++++Classification Results for Banks Data+++++++++++++++")
randomForestClassifier = RandomForestClassifier("banks.csv", numberOfTrees)
randomForestClassifier.createTrainingAndTestSamplesFromData()
randomForestClassifier.performClassification()
print(
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    end="\n\n\n",
)
print("++++++++++++++++Classification Results for Politics Data++++++++++++++")
randomForestClassifier = RandomForestClassifier("politics.csv", numberOfTrees)
randomForestClassifier.createTrainingAndTestSamplesFromData()
randomForestClassifier.performClassification()
print(
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    end="\n\n\n",
)
