from sklearn.neural_network import MLPClassifier
# if mlp_config cannot be loaded, make sure to append "PROJECT_ROOT/model" in your `PYTHONPATH` variable
from mlp_config import sizes
from mlp_config import random_seed as seed

model = MLPClassifier()
param_dist = {
    "hidden_layer_sizes": sizes,
    "activation": ["logistic", "tanh", "relu"],
    "solver": ["lbfgs"],
    "alpha": [0, 2e-5, 5e-5, 1e-4, 2e-4, 5e-4, 1e-3, 2e-3],
    "random_state": [seed],
    "max_iter": [100, 200, 500],
}
