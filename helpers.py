
def escape_dquotes(input):
    if '#' in input or '"' in input or ';' in input or '\\' in input:
        return "'" + str(input) + "'"

def find_key(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find_key(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, str):
                    if key in d:
                        yield d
                else:
                    for result in find_key(key, d):
                        yield result

def get_key(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield k
        elif isinstance(v, dict):
            for result in get_key(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, str):
                    if key in d:
                        yield d
                else:
                    for result in get_key(key, d):
                        yield result

def replace_key(key, value, replacement, dictionary):
    for k, v in dictionary.items():
        if k == key:
            if v == value:
                dictionary[k] = replacement
            # yield dictionary
        elif isinstance(v, dict):
            # for result in
            replace_key(key, value, replacement, v)
                # yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, str):
                    if key in d:
                        pass
                else:
                    # for result in
                    replace_key(key, value, replacement, d)
                        # yield result

def replace_property(field, original_value, replacement_value, prop_list, separator):
    new_prop_list = []
    for line in prop_list:

        if str(line).split(separator)[0].strip() == field and str(line).split(separator)[1].strip() == original_value:
            # print(str(line).split(separator)[1])
            line = '{}{}{}{}'.format(str(line).split(separator)[0].strip(), separator, replacement_value, '\n')

        new_prop_list.append(line)
    return new_prop_list
