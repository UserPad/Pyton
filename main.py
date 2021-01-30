import pickle
import json
data = [
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0]
]
from timeit import timeit
def json_t():
    with open('json', 'w') as file:
        json.dump(data, file, indent=4)
def pickle_t():
    with open('pickle', 'wb') as file:
        pickle.dump(data, file)
print(timeit(json_t, number=10)/10)
print(timeit(pickle_t, number=10)/10)