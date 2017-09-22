#-*- coding: utf-8 -*-

'''
     - - - - - -- - - - - - - - - - - - - - - - - - - - - - -
    Name - - CNN - Convolution Neural Network For Photo Recognizing
    Goal - - Recognize Handing Writting Word Photo
    Detail：Total 5 layers neural network
            * Convolution layer
            * Pooling layer
            * Input layer layer of BP
            * Hiden layer of BP
            * Output layer of BP
    Author: Stephen Lee
    Program: PYTHON
    Date: 2017.9.20
    - - - - - -- - - - - - - - - - - - - - - - - - - - - - -
          '''
import numpy as np
import matplotlib.pyplot as plt


class CNN():
    conv1 = []
    w_conv1 = []
    thre_conv1 = []
    step_conv1 = 0
    size_pooling1 = 0
    num_bp1 = 0
    num_bp2 = 0
    num_bp3 = 0
    thre_bp1 = []
    thre_bp2 = []
    wkj = np.mat([])
    vji = np.mat([])
    rate_weight = 0
    rate_thre = 0


    def __init__(self,conv1_get,size_p1,bp_num1,bp_num2,bp_num3,rate_w=0.2,rate_t=0.2):
        '''
        :param conv1_get: [a,c,d]，size, number, step of convolution kernel
        :param size_p1: pooling size
        :param bp_num1: units number of flatten layer
        :param bp_num2: units number of hidden layer
        :param bp_num3: units number of output layer
        :param rate_w: rate of weight learning
        :param rate_t: rate of threshold learning
        '''
        self.num_bp1 = bp_num1
        self.num_bp2 = bp_num2
        self.num_bp3 = bp_num3
        self.conv1 = conv1_get[:2]
        self.step_conv1 = conv1_get[2]
        self.size_pooling1 = size_p1
        self.rate_weight = rate_w
        self.rate_thre = rate_t
        self.w_conv1 = [np.mat(-1*np.random.rand(self.conv1[0],self.conv1[0])+0.5) for i in range(self.conv1[1])]
        self.wkj = np.mat(-1 * np.random.rand(self.num_bp3, self.num_bp2) + 0.5)
        self.vji = np.mat(-1*np.random.rand(self.num_bp2, self.num_bp1)+0.5)
        self.thre_conv1 = -2*np.random.rand(self.conv1[1])+1
        self.thre_bp2 = -2*np.random.rand(self.num_bp2)+1
        self.thre_bp3 = -2*np.random.rand(self.num_bp3)+1


    def save_model(self,save_path):
        #将模型保存
        import pickle
        model_dic = {'num_bp1':self.num_bp1,
                    'num_bp2':self.num_bp2,
                    'num_bp3':self.num_bp3,
                    'conv1':self.conv1,
                    'step_conv1':self.step_conv1,
                    'size_pooling1':self.size_pooling1,
                    'rate_weight':self.rate_weight,
                    'rate_thre':self.rate_thre,
                    'w_conv1':self.w_conv1,
                    'wkj':self.wkj,
                    'vji':self.vji,
                    'thre_conv1':self.thre_conv1,
                    'thre_bp2':self.thre_bp2,
                     'thre_bp3':self.thre_bp3}
        with open(save_path, 'wb') as f:
            pickle.dump(model_dic, f)

        print('模型已经保存： %s'% save_path)


    def paste_model(self,save_path):
        #实例方法，
        #虽然这么写一点也不简洁。。。。
        #卸载这个里面的话，只是用于修改已经存在的模型，要根据读取的数据返回实例的模型，再写一个吧
        import pickle
        with open(save_path, 'rb') as f:
            model_dic = pickle.load(f)
        self.num_bp1 = model_dic.get('num_bp1')
        self.num_bp2 = model_dic.get('num_bp2')
        self.num_bp3 = model_dic.get('num_bp3')
        self.conv1 = model_dic.get('conv1')
        self.step_conv1 = model_dic.get('step_conv1')
        self.size_pooling1 = model_dic.get('size_pooling1')
        self.rate_weight = model_dic.get('rate_weight')
        self.rate_thre = model_dic.get('rate_thre')
        self.w_conv1 = model_dic.get('w_conv1')
        self.wkj = model_dic.get('wkj')
        self.vji = model_dic.get('vji')
        self.thre_conv1 = model_dic.get('thre_conv1')
        self.thre_bp2 = model_dic.get('thre_bp2')
        self.thre_bp3 = model_dic.get('thre_bp3')
        print('已经成功读取模型')

    @classmethod
    def ReadModel(cls,model_path):
        #类方法，读取保存的模型，返回一个实例。
        import pickle
        with open(model_path, 'rb') as f:
            model_dic = pickle.load(f)

        conv_get= model_dic.get('conv1')
        conv_get.append(model_dic.get('step_conv1'))
        size_p1 = model_dic.get('size_pooling1')
        bp1 = model_dic.get('num_bp1')
        bp2 = model_dic.get('num_bp2')
        bp3 = model_dic.get('num_bp3')
        r_w = model_dic.get('rate_weight')
        r_t = model_dic.get('rate_thre')
        #创建实例
        conv_ins = CNN(conv_get,size_p1,bp1,bp2,bp3,r_w,r_t)
        #修改实例的参数
        conv_ins.w_conv1 = model_dic.get('w_conv1')
        conv_ins.wkj = model_dic.get('wkj')
        conv_ins.vji = model_dic.get('vji')
        conv_ins.thre_conv1 = model_dic.get('thre_conv1')
        conv_ins.thre_bp2 = model_dic.get('thre_bp2')
        conv_ins.thre_bp3 = model_dic.get('thre_bp3')
        return conv_ins


    def sig(self,x):
        return 1 / (1 + np.exp(-1*x))
    def do_round(self,x):
        return round(x, 3)
    #卷积
    def Convolute(self,data,convs,w_convs,thre_convs,conv_step):
        size_conv = convs[0]
        num_conv =convs[1]
        size_data = np.shape(data)[0]
        #得到原图像滑动的小图，data_focus
        data_focus = []
        for i_focus in range(0, size_data - size_conv + 1, conv_step):
            for j_focus in range(0, size_data - size_conv + 1, conv_step):
                focus = data[i_focus:i_focus + size_conv, j_focus:j_focus + size_conv]
                data_focus.append(focus)
        #计算所有卷积核得到的特征图，每个特征图以矩阵形式，存储为一个列表data_featuremap
        data_featuremap = []
        Size_FeatureMap = int((size_data - size_conv) / conv_step + 1)
        for i_map in range(num_conv):
            featuremap = []
            for i_focus in range(len(data_focus)):
                net_focus = np.sum(np.multiply(data_focus[i_focus], w_convs[i_map])) - thre_convs[i_map]
                featuremap.append(self.sig(net_focus))
            featuremap = np.asmatrix(featuremap).reshape(Size_FeatureMap, Size_FeatureMap)
            data_featuremap.append(featuremap)

        #将data_focus中的focus展开为一维
        focus1_list = []
        for each_focus in data_focus:
            focus1_list.extend(self.Expand_Mat(each_focus))
        focus_list = np.asarray(focus1_list)
        return focus_list,data_featuremap

    # 池化
    def Pooling(self,featuremaps,size_pooling):
        size_map = len(featuremaps[0])
        size_pooled = int(size_map/size_pooling)
        featuremap_pooled = []
        for i_map in range(len(featuremaps)):
            map = featuremaps[i_map]
            map_pooled = []
            for i_focus in range(0,size_map,size_pooling):
                for j_focus in range(0, size_map, size_pooling):
                    focus = map[i_focus:i_focus + size_pooling, j_focus:j_focus + size_pooling]
                    #平均池化
                    map_pooled.append(np.average(focus))
                    #最大池化
                    #map_pooled.append(np.max(focus))
            map_pooled = np.asmatrix(map_pooled).reshape(size_pooled,size_pooled)
            featuremap_pooled.append(map_pooled)
        return featuremap_pooled

    def Expand(self,datas):
        #将三元的数据展开为1为的list
        data_expanded = []
        for i in range(len(datas)):
            shapes = np.shape(datas[i])
            data_listed = datas[i].reshape(1,shapes[0]*shapes[1])
            data_listed = data_listed.getA().tolist()[0]
            data_expanded.extend(data_listed)
        #连接所有数据
        data_expanded = np.asarray(data_expanded)
        return data_expanded

    def Expand_Mat(self,data_mat):
        #用来展开矩阵为一维的list
        data_mat = np.asarray(data_mat)
        shapes = np.shape(data_mat)
        data_expanded = data_mat.reshape(1,shapes[0]*shapes[1])
        return data_expanded

    def Getpd_From_Pool(self,out_map,pd_pool,num_map,size_map,size_pooling):
        '''
        误差反传，从pooled到前一个map, 例如将池化层6*6的误差矩阵扩大为12*12的误差矩阵
        pd_pool: 是采样层的误差，list形式。。。。要改要改
        out_map: 前面特征图的输出，数量*size*size的列表形式
        return: pd_all:前面层所有的特征图的pd， num*size_map*size_map的列表形式
        '''
        pd_all = []
        i_pool = 0
        for i_map in range(num_map):
            pd_conv1 = np.ones((size_map, size_map))
            for i in range(0, size_map, size_pooling):
                for j in range(0, size_map, size_pooling):
                    pd_conv1[i:i + size_pooling, j:j + size_pooling] = pd_pool[i_pool]
                    i_pool = i_pool + 1
            pd_conv2 = np.multiply(pd_conv1,np.multiply(out_map[i_map],(1-out_map[i_map])))
            pd_all.append(pd_conv2)
        return pd_all

    def trian(self,patterns,datas_train, datas_teach, n_repeat, error_accuracy,draw_e = bool):
        print('----------------------Start Training-------------------------')
        print(' - - Shape: Train_Data  ',np.shape(datas_train))
        print(' - - Shape: Teach_Data  ',np.shape(datas_teach))
        rp = 0
        all_mse = []
        mse  = 10000
        while rp < n_repeat and mse >= error_accuracy:
            alle = 0
            print('-------------进行第%d次学习--------------'%rp)
            for p in range(len(datas_train)):
                #print('------------学习第%d个图像--------------'%p)
                data_train = np.asmatrix(datas_train[p])
                data_teach = np.asarray(datas_teach[p])
                data_focus1,data_conved1 = self.Convolute(data_train,self.conv1,self.w_conv1,
                                           self.thre_conv1,conv_step=self.step_conv1)
                data_pooled1 = self.Pooling(data_conved1,self.size_pooling1)
                shape_featuremap1 = np.shape(data_conved1)
                '''
                print('  -----original shape   ', np.shape(data_train))
                print('  ---- after convolution  ',np.shape(data_conv1))
                print('  -----after pooling  ',np.shape(data_pooled1))
               '''
                data_bp_input = self.Expand(data_pooled1)
                # 计算第一层输入输出
                bp_out1 = data_bp_input
                # 计算第二层输入输出
                bp_net_j = np.dot(bp_out1,self.vji.T) - self.thre_bp2
                bp_out2 = self.sig(bp_net_j)
                # 计算第三层输入输出
                bp_net_k = np.dot(bp_out2 ,self.wkj.T) - self.thre_bp3
                bp_out3 = self.sig(bp_net_k)

                # 计算一般化误差
                pd_k_all = np.multiply((data_teach - bp_out3), np.multiply(bp_out3, (1 - bp_out3)))
                pd_j_all = np.multiply(np.dot(pd_k_all,self.wkj), np.multiply(bp_out2, (1 - bp_out2)))
                pd_i_all = np.dot(pd_j_all,self.vji)

                pd_conv1_pooled = pd_i_all / (self.size_pooling1*self.size_pooling1)
                pd_conv1_pooled = pd_conv1_pooled.T.getA().tolist()
                pd_conv1_all = self.Getpd_From_Pool(data_conved1,pd_conv1_pooled,shape_featuremap1[0],
                                                    shape_featuremap1[1],self.size_pooling1)

                #卷积层1的权重和阈值修正，每个卷积核的权重需要修正 12*12(map) 次
                #修正量为featuremap中点的偏导值 乘以 前一层图像focus， 整个权重模板一起更新
                for k_conv in range(self.conv1[1]):
                    pd_conv_list = self.Expand_Mat(pd_conv1_all[k_conv])
                    delta_w = self.rate_weight * np.dot(pd_conv_list,data_focus1)

                    self.w_conv1[k_conv] = self.w_conv1[k_conv] + delta_w.reshape((self.conv1[0],self.conv1[0]))

                    self.thre_conv1[k_conv] = self.thre_conv1[k_conv] - np.sum(pd_conv1_all[k_conv]) * self.rate_thre
                # 更新kj层的权重

                self.wkj = self.wkj + pd_k_all.T * bp_out2 * self.rate_weight
                # 更新ji层的权重
                self.vji = self.vji + pd_j_all.T * bp_out1 * self.rate_weight
                # 更新阈值
                self.thre_bp3 = self.thre_bp3 - pd_k_all * self.rate_thre
                self.thre_bp2 = self.thre_bp2 - pd_j_all * self.rate_thre
                # 计算总误差
                errors = np.sum(abs((data_teach - bp_out3)))
                alle = alle + errors
                #print('   ----Teach      ',data_teach)
                #print('   ----BP_output  ',bp_out3)
            rp = rp + 1
            mse = alle/patterns
            all_mse.append(mse)
        def draw_error():
            yplot = [error_accuracy for i in range(int(n_repeat * 1.2))]
            plt.plot(all_mse, '+-')
            plt.plot(yplot, 'r--')
            plt.xlabel('Learning Times')
            plt.ylabel('All_mse')
            plt.grid(True, alpha=0.5)
            plt.show()
        print('------------------Training Complished---------------------')
        print(' - - Training epoch: ', rp, '     - - Mse: %.6f' % mse)
        if draw_e:
            draw_error()
        return mse

    def produce(self,datas_test):
        #对验证和测试数据集进行输出
        produce_out = []
        print('-------------------Start Testing-------------------------')
        print(' - - Shape: Test_Data  ',np.shape(datas_test))
        for p in range(len(datas_test)):
            print('--------测试第%d个图像----------' % p)
            data_test = np.asmatrix(datas_test[p])
            data_focus1, data_conved1 = self.Convolute(data_test, self.conv1, self.w_conv1,
                                                     self.thre_conv1, conv_step=self.step_conv1)
            data_pooled1 = self.Pooling(data_conved1, self.size_pooling1)
            data_bp_input = self.Expand(data_pooled1)
            # 计算第一层输入输出
            bp_out1 = data_bp_input
            # 计算第二层输入输出
            bp_net_j = bp_out1 * self.vji.T - self.thre_bp2
            bp_out2 = self.sig(bp_net_j)
            # 计算第三层输入输出
            bp_net_k = bp_out2 * self.wkj.T - self.thre_bp3
            bp_out3 = self.sig(bp_net_k)
            produce_out.extend(bp_out3.getA().tolist())
        res = [list(map(self.do_round,each)) for each in produce_out]
        return np.asarray(res)

    def convolution(self,data):
        #返回卷积和池化后的数据,用于查看图像
        data_test = np.asmatrix(data)
        data_focus1, data_conved1 = self.Convolute(data_test, self.conv1, self.w_conv1,
                                                     self.thre_conv1, conv_step=self.step_conv1)
        data_pooled1 = self.Pooling(data_conved1, self.size_pooling1)

        return data_conved1,data_pooled1


