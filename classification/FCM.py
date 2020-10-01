from tools import *

# https://en.wikipedia.org/wiki/Fuzzy_clustering


class FuzzyCMeans:
    def __init__(self, n_clusters, initial_centers, data, max_iter=250, m=2, error=1e-5):
        assert m > 1
        #assert initial_centers.shape[0] == n_clusters
        self.U = None
        self.centers = initial_centers
        self.max_iter = max_iter
        self.m = m
        self.error = error
        self.data = data

    def membership(self, data, centers):
        U_temp = cdist(data, centers, 'euclidean')
        U_temp = numpy.power(U_temp, 2/(self.m - 1))
        denominator_ = U_temp.reshape(
            (data.shape[0], 1, -1)).repeat(U_temp.shape[-1], axis=1)
        denominator_ = U_temp[:, :, numpy.newaxis] / denominator_
        return 1 / denominator_.sum(2)

    def Centers(self, data, U):
        um = U ** self.m
        return (data.T @ um / numpy.sum(um, axis=0)).T

    def newImage(self, U, centers, im):
        best = numpy.argmax(self.U, axis=-1)
        # print(best)
        # numpy.round()
        image = im.astype(int)
        for i in range(256):
            image = numpy.where(image == float(i), centers[best[i]][0], image)
        return image

    def compute(self):
        self.U = self.membership(self.data, self.centers)

        past_U = numpy.copy(self.U)
        begin_time = datetime.datetime.now()
        for i in range(self.max_iter):

            self.centers = self.Centers(self.data, self.U)
            self.U = self.membership(self.data, self.centers)

            if norm(self.U - past_U) < self.error:
                break
            past_U = numpy.copy(self.U)
        x = datetime.datetime.now() - begin_time
        return self.centers, self.U, x

# that's how you run it, data being your data, and the other parameters being the basic FCM parameters such as numbe rof cluseters, degree of fuzziness and so on
# f = FuzzyCMeans(n_clusters=C, initial_centers=Initial_centers,
#                 data=data m=2, max_iter=1000, error=1e-5)
# centers, U, time = f.compute()
