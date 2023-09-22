import json

def decorator(func):
    def wrapper(path:str):
        name, suffix = path.split('.')
        if suffix == "json":
            return func(path)
        else:
            return "not json file"

    return wrapper

@decorator
def readJson(path:str):
    f = open(path)
    data = json.load(f)
    return data
    
print(readJson('data.csv'))