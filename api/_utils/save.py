import pickle
from skompiler import skompile
import sympy


def save_model_pickle(model, path):
    with open(path, "wb") as fp:
        pickle.dump(model, fp)

def save_model_dart(model, path):
    with open(path, "w") as fp:
        expr = skompile(model.predict)
        sympy_expr = expr.to('sympy/js')
        fp.write(sympy_expr)