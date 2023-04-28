from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from .save import save_model_pickle
from .dataset import X, y
import os

best_model = None
max_s = 0
for i in range(20):
     model = RandomForestRegressor(random_state=i, max_depth=11) 
     model.fit(X, y)
     s =  model.score(X, y)
     if s > max_s:
             max_s = s
             best_model = model
             print(max_s, i)
 
save_model_pickle(best_model, f"{os.path.dirname(__file__)}/model.pickle")
