#-*- coding:utf-8 -*-
'''
Author: Stephen Lee
Date: 2017.9.21

BP neural network with three layers
'''

import numpy as np
import matplotlib.pyplot as plt

class Bpnw():

    def __init__(self,n_layer1,n_layer2,n_layer3,rate_w=0.3,rate_t=0.3):
        '''
        :param n_layer1: number of input layer
        :param n_layer2: number of hiden layer
        :param n_layer3: number of output layer
        :param rate_w: rate of weight learning
        :param rate_t: rate of threshold learning
        '''
        self.num1 = n_layer1
        self.num2 = n_layer2
        self.num3 = n_layer3
        self.rate_weight = rate_w
        self.rate_thre = rate_t
        self.thre2 = -2*np.random.rand(self.num2)+1
        self.thre3 = -2*np.random.rand(self.num3)+1
        self.vji = np.mat(-2*np.random.rand(self.num2, self.num1)+1)
        self.wkj = np.mat(-2*np.random.rand(self.num3, self.num2)+1)

    def sig(self,x):
        return 1 / (1 + np.exp(-1*x))

    def sig_plain(self,x):
        return 1 / (1 + np.exp(-1*x))

    def do_round(self,x):
        return round(x, 3)

    def trian(self,patterns,data_train, data_teach, n_repeat, error_accuracy,draw_e = bool):
        '''
        :param patterns: the number of patterns
        :param data_train: training data x; numpy.ndarray
        :param data_teach: training data y; numpy.ndarray
        :param n_repeat: echoes
        :param error_accuracy: error accuracy
        :return: None
        '''
        data_train = np.asarray(data_train)
        data_teach = np.asarray(data_teach)
        print('-------------------Start Training-------------------------')
        print(' - - Shape: Train_Data  ',np.shape(data_train))
        print(' - - Shape: Teach_Data  ',np.shape(data_teach))
        rp = 0
        all_mse = []
        mse  = 10000
        while rp < n_repeat and mse >= error_accuracy:
            alle = 0
            final_out = []
            for g in range(np.shape(data_train)[0]):
                net_i = data_train[g]
                out1 = net_i

                net_j = out1 * self.vji.T  - self.thre2
                out2=self.sig(net_j)

                net_k = out2 * self.wkj.T  - self.thre3
                out3 = self.sig(net_k)

                # learning process
                pd_k_all = np.multiply(np.multiply(out3,(1 - out3)),(data_teach[g]-out3))
                pd_j_all = np.multiply(pd_k_all * self.wkj,np.multiply(out2,1-out2))
                #upgrade weight
                self.wkj = self.wkj + pd_k_all.T * out2 *self.rate_weight
                self.vji = self.vji + pd_j_all.T * out1 * self.rate_weight
                #upgrade threshold
                self.thre3 = self.thre3 - pd_k_all * self.rate_thre
                self.thre2 = self.thre2 - pd_j_all * self.rate_thre
                #calculate sum of error
                errors = np.sum(abs((data_teach[g] - out3)))

                alle = alle + errors
                final_out.extend(out3.getA().tolist())
            final_out3 = [list(map(self.do_round,each)) for each in final_out]

            rp = rp + 1
            mse = alle/patterns
            all_mse.append(mse)
        def draw_error():
            yplot = [error_accuracy for i in range(int(n_repeat * 1.2))]
            plt.plot(all_mse, '+-')
            plt.plot(yplot, 'r--')
            plt.xlabel('Learning Times')
            plt.ylabel('All_mse')
            plt.grid(True,alpha = 0.7)
            plt.show()
        print('------------------Training Complished---------------------')
        print(' - - Training epoch: ', rp, '     - - Mse: %.6f'%mse)
        print(' - - Last Output: ', final_out3)
        if draw_e:
            draw_error()

    def predict(self,data_test):
        '''
        :param data_test: data test, numpy.ndarray
        :return: predict output data
        '''
        data_test = np.asarray(data_test)
        produce_out = []
        print('-------------------Start Testing-------------------------')
        print(' - - Shape: Test_Data  ',np.shape(data_test))
        print(np.shape(data_test))
        for g in range(np.shape(data_test)[0]):

            net_i = data_test[g]
            out1 = net_i

            net_j = out1 * self.vji.T - self.thre2
            out2 = self.sig(net_j)

            net_k = out2 * self.wkj.T - self.thre3
            out3 = self.sig(net_k)
            produce_out.extend(out3.getA().tolist())
        res = [list(map(self.do_round,each)) for each in produce_out]
        return np.asarray(res)


def main():
    #I will fish the mian function later
    pass

if __name__ == '__main__':
    main()
