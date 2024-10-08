"""
Implementation of SimCLR. 
Self-Supervised Learning (SSL) with SimCLR. SimCLR is a framework for learning visual representations without labels by maximizing the agreement between different augmented views of the same image.
"""
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.applications import ResNet50
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


def data_handling(data: dict) -> tuple:
    """
    Handles the data by splitting features and targets.
    
    >>> data_handling({'data': np.array([[0.1, 0.2], [0.3, 0.4]]), 'target': np.array([0, 1])})
    (array([[0.1, 0.2], [0.3, 0.4]]), array([0, 1]))
    """
    return (data["data"], data["target"])


def simclr_model(input_shape=(32, 32, 3), projection_dim=64) -> Model:
    """
    Builds a SimCLR model based on ResNet50.
    
    >>> simclr_model().summary()  # doctest: +ELLIPSIS
    Model: "model"
    _________________________________________________________________
    ...
    """
    base_model = ResNet50(include_top=False, input_shape=input_shape, pooling="avg")
    base_model.trainable = True
    
    inputs = layers.Input(shape=input_shape)
    x = base_model(inputs, training=True)
    x = layers.Dense(projection_dim, activation="relu")(x)
    outputs = layers.Dense(projection_dim)(x)
    return Model(inputs, outputs)


def contrastive_loss(projection_1, projection_2, temperature=0.1):
    """
    Contrastive loss function for self-supervised learning.
    
    >>> contrastive_loss(np.array([0.1]), np.array([0.2]))
    0.0
    """
    projections = tf.concat([projection_1, projection_2], axis=0)
    similarity_matrix = tf.matmul(projections, projections, transpose_b=True)
    labels = tf.range(tf.shape(projections)[0])
    loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels, similarity_matrix)
    return tf.reduce_mean(loss)


def main() -> None:
    """
    >>> main()
    """
    # Load a small dataset (using CIFAR-10 as an example)
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Use label encoder to convert labels into numerical form
    le = LabelEncoder()
    y_train = le.fit_transform(y_train.flatten())
    y_test = le.transform(y_test.flatten())
    
    # Split data into train and validation sets
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2)

    # Build the SimCLR model
    model = simclr_model()
    optimizer = Adam()
    loss_fn = SparseCategoricalCrossentropy(from_logits=True)

    # Training the SimCLR model
    for epoch in range(10):
        with tf.GradientTape() as tape:
            projections_1 = model(x_train)
            projections_2 = model(x_train)  # Normally, this would use augmented views
            loss = contrastive_loss(projections_1, projections_2)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        print(f"Epoch {epoch+1}: Contrastive Loss = {loss.numpy()}")

    # Create a new model with a classification head for evaluation
    classifier = layers.Dense(10, activation="softmax")(model.output)
    classifier_model = Model(model.input, classifier)
    classifier_model.compile(optimizer=Adam(), loss=loss_fn, metrics=["accuracy"])
    classifier_model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=5)

    # Display the confusion matrix of the classifier
    ConfusionMatrixDisplay.from_estimator(
        classifier_model,
        x_test,
        y_test,
        display_labels=le.classes_,
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - CIFAR-10")
    plt.show()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()
