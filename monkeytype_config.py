from monkeytype.config import DefaultConfig

class MyConfig(DefaultConfig):
    def sample_rate(self):
        return 1000

CONFIG = MyConfig()
