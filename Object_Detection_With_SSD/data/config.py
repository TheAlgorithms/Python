# config.py
import os.path

# gets home dir cross platform
home = os.path.expanduser("~")
ddir = os.path.join(home,"data/VOCdevkit/")

# note: if you used our download scripts, this should be right
VOCroot = ddir # path to VOCdevkit root dir

# default batch size
BATCHES = 32
# data reshuffled at every epoch
SHUFFLE = True
# number of subprocesses to use for data loading
WORKERS = 4


#SSD300 CONFIGS
# newer version: use additional conv11_2 layer as last layer before multibox layers
v2 = {
    'feature_maps' : [38, 19, 10, 5, 3, 1],

    'min_dim' : 300,

    'steps' : [8, 16, 32, 64, 100, 300],

    'min_sizes' : [30, 60, 111, 162, 213, 264],

    'max_sizes' : [60, 111, 162, 213, 264, 315],

    # 'aspect_ratios' : [[2, 1/2], [2, 1/2, 3, 1/3], [2, 1/2, 3, 1/3],
    #                    [2, 1/2, 3, 1/3], [2, 1/2], [2, 1/2]],
    'aspect_ratios' : [[2], [2, 3], [2, 3], [2, 3], [2], [2]],

    'variance' : [0.1, 0.2],

    'clip' : True,

    'name' : 'v2',
}

# use average pooling layer as last layer before multibox layers
v1 = {
    'feature_maps' : [38, 19, 10, 5, 3, 1],

    'min_dim' : 300,

    'steps' : [8, 16, 32, 64, 100, 300],

    'min_sizes' : [30, 60, 114, 168, 222, 276],

    'max_sizes' : [-1, 114, 168, 222, 276, 330],

    # 'aspect_ratios' : [[2], [2, 3], [2, 3], [2, 3], [2, 3], [2, 3]],
    'aspect_ratios' : [[1,1,2,1/2],[1,1,2,1/2,3,1/3],[1,1,2,1/2,3,1/3],
                        [1,1,2,1/2,3,1/3],[1,1,2,1/2,3,1/3],[1,1,2,1/2,3,1/3]],

    'variance' : [0.1, 0.2],

    'clip' : True,

    'name' : 'v1',
}
