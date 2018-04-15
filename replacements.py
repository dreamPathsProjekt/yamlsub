import yaml, pprint
from helpers import find_key, get_key, replace_key, replace_property, escape_dquotes

def replace_yaml(field, original_value, replacement_value, filename):
    with open(filename) as file:
        data = yaml.load(file)

    replace_key(field, original_value, replacement_value, data)

    with open(filename, mode='w') as file:
        yaml.dump(data, file)

def replace_application_properties(field, original_value, replacement_value, filename):
    with open(filename) as file:
        data = [ line for line in file.readlines() ]
        new_data = replace_property(field, original_value, replacement_value, data, '=')

    with open(filename, mode='w') as file:
        file.writelines(new_data)

def replace_ini(field, original_value, replacement_value, filename):

    with open(filename) as file:
        data = [ line for line in file.readlines() ]
        new_data = replace_property(field, original_value, replacement_value, data, ' = ')

    with open(filename, mode='w') as file:
        file.writelines(new_data)







