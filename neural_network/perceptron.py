"""
Perceptron
w = w + N * (d(k) - y) * x(k)

Using perceptron network for oil analysis, with Measuring of 3 parameters
that represent chemical characteristics we can classify the oil, in p1 or p2
p1 = -1
p2 = 1

Reference: https://en.wikipedia.org/wiki/Perceptron
"""

import random


class Perceptron:
    def __init__(
        self,
        sample: list[list[float]],
        target: list[int],
        learning_rate: float = 0.01,
        epoch_number: int = 1000,
        bias: float = -1,
        seed: int | None = 0,
    ) -> None:
        """
        Initializes a Perceptron network for oil analysis
        :param sample: sample dataset of 3 parameters with shape [30,3]
        :param target: variable for classification with two possible states -1 or 1
        :param learning_rate: learning rate used in optimizing.
        :param epoch_number: number of epochs to train network on.
        :param bias: bias value for the network.
        :param seed: seed for the (internal) random number generator so that
            training is reproducible; pass ``None`` for non-deterministic weights.

        >>> p = Perceptron([], (0, 1, 2))
        Traceback (most recent call last):
            ...
        ValueError: Sample data can not be empty
        >>> p = Perceptron(([0], 1, 2), [])
        Traceback (most recent call last):
            ...
        ValueError: Target data can not be empty
        >>> p = Perceptron(([0], 1, 2), (0, 1))
        Traceback (most recent call last):
            ...
        ValueError: Sample data and Target data do not have matching lengths
        """
        self.sample = sample
        if len(self.sample) == 0:
            raise ValueError("Sample data can not be empty")
        self.target = target
        if len(self.target) == 0:
            raise ValueError("Target data can not be empty")
        if len(self.sample) != len(self.target):
            raise ValueError("Sample data and Target data do not have matching lengths")
        self.learning_rate = learning_rate
        self.epoch_number = epoch_number
        self.bias = bias
        self.number_sample = len(sample)
        self.col_sample = len(sample[0])  # number of columns in dataset
        self.weight: list = []
        # A dedicated RNG instance keeps training reproducible without touching
        # the global ``random`` state (which other code/tests may rely on).
        self._rng = random.Random(seed)

    def training(self) -> int:
        """
        Trains the perceptron until it stops misclassifying the training data
        or the maximum number of epochs (``epoch_number``) is reached, whichever
        comes first. The epoch cap guarantees termination even if the data is
        not linearly separable.

        :return: the number of epochs the network was trained for.

        >>> data = [[2.0149, 0.6192, 10.9263]]
        >>> targets = [-1]
        >>> perceptron = Perceptron(data, targets)
        >>> perceptron.training()
        5
        """
        for sample in self.sample:
            sample.insert(0, self.bias)

        for _ in range(self.col_sample):
            self.weight.append(self._rng.random())

        self.weight.insert(0, self.bias)

        epoch_count = 0

        while epoch_count < self.epoch_number:
            has_misclassified = False
            for i in range(self.number_sample):
                u = 0
                for j in range(self.col_sample + 1):
                    u = u + self.weight[j] * self.sample[i][j]
                y = self.sign(u)
                if y != self.target[i]:
                    for j in range(self.col_sample + 1):
                        self.weight[j] = (
                            self.weight[j]
                            + self.learning_rate
                            * (self.target[i] - y)
                            * self.sample[i][j]
                        )
                    has_misclassified = True
            epoch_count = epoch_count + 1
            # stop early once every sample is classified correctly
            if not has_misclassified:
                break

        return epoch_count

    def sort(self, sample: list[float]) -> int:
        """
        Classifies a single observation as P1 (-1) or P2 (1). The network must
        be trained first.

        :param sample: example row to classify as P1 or P2
        :return: -1 if the sample is classified as P1, otherwise 1

        >>> data = [[2.0149, 0.6192, 10.9263]]
        >>> targets = [-1]
        >>> perceptron = Perceptron(data, targets)
        >>> perceptron.training()
        5
        >>> perceptron.sort([2.0149, 0.6192, 10.9263])
        -1
        """
        if len(self.sample) == 0:
            raise ValueError("Sample data can not be empty")
        sample.insert(0, self.bias)
        u = 0
        for i in range(self.col_sample + 1):
            u = u + self.weight[i] * sample[i]

        return self.sign(u)

    def sign(self, u: float) -> int:
        """
        threshold function for classification
        :param u: input number
        :return: 1 if the input is greater than or equal to 0, otherwise -1
        >>> data = [[0], [-0.5], [0.5]]
        >>> targets = [1, -1, 1]
        >>> perceptron = Perceptron(data, targets)
        >>> perceptron.sign(0)
        1
        >>> perceptron.sign(-0.5)
        -1
        >>> perceptron.sign(0.5)
        1
        """
        return 1 if u >= 0 else -1


samples = [
    [-0.6508, 0.1097, 4.0009],
    [-1.4492, 0.8896, 4.4005],
    [2.0850, 0.6876, 12.0710],
    [0.2626, 1.1476, 7.7985],
    [0.6418, 1.0234, 7.0427],
    [0.2569, 0.6730, 8.3265],
    [1.1155, 0.6043, 7.4446],
    [0.0914, 0.3399, 7.0677],
    [0.0121, 0.5256, 4.6316],
    [-0.0429, 0.4660, 5.4323],
    [0.4340, 0.6870, 8.2287],
    [0.2735, 1.0287, 7.1934],
    [0.4839, 0.4851, 7.4850],
    [0.4089, -0.1267, 5.5019],
    [1.4391, 0.1614, 8.5843],
    [-0.9115, -0.1973, 2.1962],
    [0.3654, 1.0475, 7.4858],
    [0.2144, 0.7515, 7.1699],
    [0.2013, 1.0014, 6.5489],
    [0.6483, 0.2183, 5.8991],
    [-0.1147, 0.2242, 7.2435],
    [-0.7970, 0.8795, 3.8762],
    [-1.0625, 0.6366, 2.4707],
    [0.5307, 0.1285, 5.6883],
    [-1.2200, 0.7777, 1.7252],
    [0.3957, 0.1076, 5.6623],
    [-0.1013, 0.5989, 7.1812],
    [2.4482, 0.9455, 11.2095],
    [2.0149, 0.6192, 10.9263],
    [0.2012, 0.2611, 5.4631],
]

target = [
    -1,
    -1,
    -1,
    1,
    1,
    -1,
    1,
    -1,
    1,
    1,
    -1,
    1,
    -1,
    -1,
    -1,
    -1,
    1,
    1,
    1,
    1,
    -1,
    1,
    1,
    1,
    1,
    -1,
    -1,
    1,
    -1,
    1,
]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    network = Perceptron(
        sample=samples, target=target, learning_rate=0.01, epoch_number=1000, bias=-1
    )
    epochs = network.training()
    print(f"Finished training perceptron in {epochs} epoch(s)")
    print("Enter values to predict or q to exit")
    while True:
        sample: list = []
        for i in range(len(samples[0])):
            user_input = input("value: ").strip()
            if user_input == "q":
                break
            observation = float(user_input)
            sample.insert(i, observation)
        classification = network.sort(sample)
        label = "P1" if classification == -1 else "P2"
        print(f"Sample: {sample} classification: {label}")
