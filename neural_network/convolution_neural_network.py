import pickle
import numpy as np
from matplotlib import pyplot as plt

class CNN:
    def __init__(
        self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w=0.2, rate_t=0.2
    ):
        """
        Initialize the Convolution Neural Network.

        Args:
            conv1_get: [a, c, d], size, number, step of convolution kernel
            size_p1: pooling size
            bp_num1: units number of flatten layer
            bp_num2: units number of hidden layer
            bp_num3: units number of output layer
            rate_w: rate of weight learning
            rate_t: rate of threshold learning
        """
        self.num_bp1 = bp_num1
        self.num_bp2 = bp_num2
        self.num_bp3 = bp_num3
        self.conv1 = conv1_get[:2]
        self.step_conv1 = conv1_get[2]
        self.size_pooling1 = size_p1
        self.rate_weight = rate_w
        self.rate_thre = rate_t
        self.w_conv1 = [
            np.mat(-1 * np.random.rand(self.conv1[0], self.conv1[0]) + 0.5)
            for i in range(self.conv1[1])
        ]
        self.wkj = np.mat(-1 * np.random.rand(self.num_bp3, self.num_bp2) + 0.5)
        self.vji = np.mat(-1 * np.random.rand(self.num_bp2, self.num_bp1) + 0.5)
        self.thre_conv1 = -2 * np.random.rand(self.conv1[1]) + 1
        self.thre_bp2 = -2 * np.random.rand(self.num_bp2) + 1
        self.thre_bp3 = -2 * np.random.rand(self.num_bp3) + 1

    def save_model(self, save_path):
        """
        Save the model to a file using pickle.

        Args:
            save_path: The file path to save the model.

        Returns:
            None
        """
        model_dic = {
            "num_bp1": self.num_bp1,
            "num_bp2": self.num_bp2,
            "num_bp3": self.num_bp3,
            "conv1": self.conv1,
            "step_conv1": self.step_conv1,
            "size_pooling1": self.size_pooling1,
            "rate_weight": self.rate_weight,
            "rate_thre": self.rate_thre,
            "w_conv1": self.w_conv1,
            "wkj": self.wkj,
            "vji": self.vji,
            "thre_conv1": self.thre_conv1,
            "thre_bp2": self.thre_bp2,
            "thre_bp3": self.thre_bp3,
        }
        with open(save_path, "wb") as f:
            pickle.dump(model_dic, f)

        print(f"Model saved: {save_path}")

    @classmethod
    def read_model(cls, model_path):
        """
        Read a saved model from a file.

        Args:
            model_path: The file path of the saved model.

        Returns:
            A CNN instance loaded with the model parameters.
        """
        with open(model_path, "rb") as f:
            model_dic = pickle.load(f)

        conv_get = model_dic.get("conv1")
        conv_get.append(model_dic.get("step_conv1"))
        size_p1 = model_dic.get("size_pooling1")
        bp1 = model_dic.get("num_bp1")
        bp2 = model_dic.get("num_bp2")
        bp3 = model_dic.get("num_bp3")
        r_w = model_dic.get("rate_weight")
        r_t = model_dic.get("rate_thre")
        conv_ins = CNN(conv_get, size_p1, bp1, bp2, bp3, r_w, r_t)
        conv_ins.w_conv1 = model_dic.get("w_conv1")
        conv_ins.wkj = model_dic.get("wkj")
        conv_ins.vji = model_dic.get("vji")
        conv_ins.thre_conv1 = model_dic.get("thre_conv1")
        conv_ins.thre_bp2 = model_dic.get("thre_bp2")
        conv_ins.thre_bp3 = model_dic.get("thre_bp3")
        return conv_ins

    def sig(self, x):
        return 1 / (1 + np.exp(-1 * x))

    def do_round(self, x):
        return round(x, 3)

    def convolute(self, data, convs, w_convs, thre_convs, conv_step):
        """
        Perform the convolution process on input data.

        Args:
            data: The input data.
            convs: [size, number] size and number of convolution kernels.
            w_convs: List of convolution kernels' weights.
            thre_convs: List of convolution kernels' thresholds.
            conv_step: Step size for convolution.

        Returns:
            focus_list: List of convoluted data.
            data_featuremap: List of feature maps.
        """
        size_conv = convs[0]
        num_conv = convs[1]
        size_data = np.shape(data)[0]
        data_focus = []

        for i_focus in range(0, size_data - size_conv + 1, conv_step):
            for j_focus in range(0, size_data - size_conv + 1, conv_step):
                focus = data[
                    i_focus : i_focus + size_conv, j_focus : j_focus + size_conv
                ]
                data_focus.append(focus)

        data_featuremap = []
        size_feature_map = int((size_data - size_conv) / conv_step + 1)

        for i_map in range(num_conv):
            featuremap = []
            for i_focus in range(len(data_focus):
                net_focus = (
                    np.sum(np.multiply(data_focus[i_focus], w_convs[i_map]))
                    - thre_convs[i_map]
                )
                featuremap.append(self.sig(net_focus))

            featuremap = np.asmatrix(featuremap).reshape(
                size_feature_map, size_feature_map
            )
            data_featuremap.append(featuremap)

        focus1_list = []

        for each_focus in data_focus:
            focus1_list.extend(self.Expand_Mat(each_focus))

        focus_list = np.asarray(focus1_list)
        return focus_list, data_featuremap

    def pooling(self, featuremaps, size_pooling, pooling_type="average_pool"):
        """
        Perform pooling on feature maps.

        Args:
            featuremaps: List of feature maps.
            size_pooling: Size of the pooling window.
            pooling_type: Type of pooling, 'average_pool' or 'max_pooling' (default: 'average_pool').

        Returns:
            featuremap_pooled: List of pooled feature maps.
        """
        size_map = len(featuremaps[0])
        size_pooled = int(size_map / size_pooling)
        featuremap_pooled = []

        for i_map in range(len(featuremaps):
            feature_map = featuremaps[i_map
