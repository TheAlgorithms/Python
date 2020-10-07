import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def breast_cancer(training_size, test_size, n, plot_data):
    """returns breast cancer dataset

    Wikipedia reference: https://en.m.wikipedia.org/wiki/Breast_cancer
    The function return four values: return sample_train, training_input, test_input, class_labels

    >>> breast_cancer(10, 4, 7, False)
    (array([[-0.80381589, -0.17496736,  0.02153529, ..., -0.1397565 ,
            -0.4738706 , -0.21959184],
           [-0.19172231, -0.48047638, -0.5502895 , ..., -0.02604959,
            -0.2322415 , -0.19774116],
           [-0.8333448 , -0.25876499, -0.26384514, ..., -0.32234254,
            -0.17787827,  0.01960881],
           ...,
           [-0.88227162, -0.50950835, -0.48471936, ...,  0.06051423,
             0.05369423, -0.01157853],
           [-0.36471423, -0.4851768 , -0.58003495, ..., -0.00202821,
            -0.1576751 , -0.25529689],
           [-0.81134279, -0.25945047, -0.54472716, ..., -0.06312866,
            -0.14663466,  0.03603051]]), {'A': array([[-0.19172231, -0.48047638, -0.5502895 ,  0.62866253, -0.02604959,
            -0.2322415 , -0.19774116],
           [-0.08931675, -0.69047276, -0.34473474,  0.2430907 ,  0.06598203,
            -0.43104084, -0.15886876],
           [-0.50124222, -0.38404633, -0.66125808,  0.09100724,  0.10701545,
            -0.13283072, -0.0307179 ],
           [-0.04524656, -0.06299861, -0.5886886 ,  0.33959658, -0.09071451,
            -0.43135931,  0.02902253],
           [-0.36503477, -0.4966686 , -0.20393198,  0.56148734,  0.18131077,
            -0.21103257, -0.14178392],
           [-0.44318575, -0.59164354, -0.29118452,  0.04301003, -0.18131692,
             0.20621245, -0.09727456],
           [-0.4146524 , -0.22790637, -0.69929679,  0.32207269,  0.10755013,
            -0.33974676, -0.11637961],
           [ 0.18070867, -0.79119457, -0.29254301,  0.04961691, -0.14589901,
            -0.41185356, -0.01666176],
           [-0.05916688, -0.00087508, -0.31287342,  0.35885527,  0.1041368 ,
            -0.34113249,  0.08670244],
           [ 0.17702071, -0.80782303, -0.06138567, -0.18814197,  0.04569151,
            -0.10576475,  0.15044493]]), 'B': array([[-0.80381589, -0.17496736,  0.02153529, -0.07187231, -0.1397565 ,
            -0.4738706 , -0.21959184],
           [-0.8333448 , -0.25876499, -0.26384514,  0.1756967 , -0.32234254,
            -0.17787827,  0.01960881],
           [-0.70730804, -0.29054463, -0.44993423,  0.03257197, -0.10219939,
            -0.25074147, -0.08352498],
           [-0.79008762, -0.3313085 , -0.28353916,  0.19137684, -0.42320134,
            -0.036884  , -0.24138241],
           [-0.67599686, -0.50282222, -0.41082298,  0.05409269,  0.08031647,
            -0.19597253, -0.10733675],
           [-0.67547425, -0.15140441, -0.52477832,  0.02062338, -0.10116737,
            -0.13453581, -0.07837964],
           [-0.79041979, -0.352277  , -0.39978347,  0.24391654, -0.31451085,
             0.11470016, -0.1341472 ],
           [-0.78150554, -0.41353571, -0.48452891, -0.05467579,  0.03033078,
            -0.32269787, -0.06426137],
           [-0.76212084, -0.40881569, -0.48040504,  0.1081265 ,  0.02596033,
            -0.20427163,  0.09202506],
           [-0.74304803, -0.36890094, -0.41951978,  0.2119361 , -0.17708908,
            -0.08143223, -0.20604129]])}, {'A': array([[-0.10389794,  0.17924751, -0.67583766,  0.55657289,  0.11036026,
            -0.13329861,  0.10039272],
           [-0.53086407, -0.4573074 , -0.17817215,  0.40169334, -0.08631139,
            -0.27384232, -0.31916126],
           [-0.21040012, -0.42492679, -0.16556034, -0.00830156, -0.28627151,
             0.05469112, -0.08206313],
           [-0.02115007, -0.46893251, -0.14647214,  0.31570857,  0.03058135,
            -0.5329338 ,  0.28794908]]), 'B': array([[-0.82652554, -0.4336021 , -0.28307103,  0.32561542, -0.15712862,
            -0.23854447, -0.08516069],
           [-0.73291597, -0.5064755 , -0.35806246,  0.53985827, -0.15899323,
            -0.2870263 , -0.15924347],
           [-0.90409716, -0.00762145, -0.43410622, -0.03133913, -0.50751343,
            -0.42602392,  0.28785164],
           [-0.7863327 , -0.3957758 , -0.37520181,  0.27611366, -0.14239159,
            -0.18478963,  0.01562388]])}, ['A', 'B'])
    """
    class_labels = [r"A", r"B"]
    data, target = datasets.load_breast_cancer(return_X_y=True)
    sample_train, sample_test, label_train, label_test = train_test_split(
        data, target, test_size=0.3, random_state=12
    )

    # Now we standardize for gaussian around 0 with unit variance
    std_scale = StandardScaler().fit(sample_train)
    sample_train = std_scale.transform(sample_train)
    sample_test = std_scale.transform(sample_test)

    # Now reduce number of features to number of qubits
    pca = PCA(n_components=n).fit(sample_train)
    sample_train = pca.transform(sample_train)
    sample_test = pca.transform(sample_test)

    # Scale to the range (-1,+1)
    samples = np.append(sample_train, sample_test, axis=0)
    minmax_scale = MinMaxScaler((-1, 1)).fit(samples)
    sample_train = minmax_scale.transform(sample_train)
    sample_test = minmax_scale.transform(sample_test)

    # Pick training size number of samples from each distro
    training_input = {
        key: (sample_train[label_train == k, :])[:training_size]
        for k, key in enumerate(class_labels)
    }
    test_input = {
        key: (sample_test[label_test == k, :])[:test_size]
        for k, key in enumerate(class_labels)
    }

    return sample_train, training_input, test_input, class_labels

    # plot_data can be set to true to plot graph of array output

    if plot_data:
        try:
            import matplotlib.pyplot as plt
        except ImportError as e:
            print(e)
        for k in range(0, 2):
            plt.scatter(
                sample_train[label_train == k, 0][:training_size],
                sample_train[label_train == k, 1][:training_size],
            )

        plt.title("PCA dim. reduced Breast cancer dataset")
        plt.show()
