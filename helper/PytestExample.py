import yaml
import re

function_pattern = re.compile(r'^\$\{(\w+):(.+)}')

def yaml_load(fp) :
    with open(fp, encoding='utf-8') as y:
        data = open(fp)
    data = yaml.load(data)
 
    ana_yaml(data)

def ana_yaml(data):
    if isinstance(data, (list, tuple)):
        for i, _ele in enumerate(data):
            data[i] = ana_yaml(data) 
    elif isinstance(data, dict):
        for k, v in data.items():
            data[k] = ana_yaml(v)
    elif isinstance(data, (str, bytes)):
        func = function_pattern.