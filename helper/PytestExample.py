import yaml
import re

def yaml_load(fp) :
    with open(fp, encoding='utf-8') as y:
        data = open(fp)
    data = yaml.load(data)

    function_pattern = re.compile(r'^\${(?<func>\w+):(?<parms>.+)}$')
    ana_yaml(data)

def ana_yaml(data):
    if isinstance(data, (list, tuple)):
        for i, _ele in enumerate(data):
            data[i] = ana_yaml(data) 