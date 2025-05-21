import yaml

class Config:
    def __init__(self):
        with open("E:\py code\RunningMan\iOSRealRun-cli-18-main\config.yaml", 'r') as f:
            config = yaml.safe_load(f)
        for i in config:
            setattr(self, i, config[i])


config = Config()
