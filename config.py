import yaml

class Config:
    # Annotate expected top-level keys from config.yaml so static checkers
    # (like Pylance) know these attributes exist.
    v: float
    routeConfig: str

    def __init__(self):
        with open("config.yaml", 'r') as f:
            config = yaml.safe_load(f)
        for i in config:
            setattr(self, i, config[i])
            
config = Config()
