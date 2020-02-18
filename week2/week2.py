from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV, KFold
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
def train_grid_search(X, y):
    grid_searcher = GridSearchCV(KNeighborsRegressor(),
                             param_grid={'n_neighbors': range(1, 21),
                                         'weights': ['uniform', 'distance'],
                                         'p': [1, 2, 3]},
                             cv=KFold(n_splits=5, random_state=10))
    grid_searcher.fit(X, y)
    return grid_searcher.cv_results_['mean_test_score']
    # TODO

mean_test_scores = []

for i in range(1000):
  X, y = make_moons(n_samples=1000, noise=0.5)
  mean_test_score = train_grid_search(X, y)
  mean_test_scores.append(mean_test_score)
  #print(f'i={i}, score={mean_test_score}')

plt.plot(np.arange(1, 21), np.mean(mean_test_scores, axis=0))