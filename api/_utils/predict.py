import os
import pickle
import numpy as np
_model = None
def get_model():
    if not _model:
        with open(f"{os.path.dirname(__file__)}/model.pickle", 'rb') as fp:
            _model = pickle.load(fp)
    return _model

def predict(arr):
    model = get_model()
    return list(model.predict(np.array(arr)))