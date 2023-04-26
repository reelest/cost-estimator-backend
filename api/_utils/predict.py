import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

_model = None
def get_model():
    global _model
    if not _model:
        with open(f"{os.path.dirname(__file__)}/model.pickle", 'rb') as fp:
            _model = pickle.load(fp)
    return _model

def predict(arr):
    model:RandomForestRegressor = get_model()
    return model.predict(np.array(arr).reshape(1, 20)).reshape(-1).tolist()