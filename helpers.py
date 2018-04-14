
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

def replace_property(field, original_value, replacement_value, prop_list):
    new_prop_list = []
    for line in prop_list:

        if str(line).split('=')[0].strip() == field and str(line).split('=')[1].strip() == original_value:
            # print(str(line).split('=')[1])
            line = str(line).split('=')[0].strip() + '=' + replacement_value + '\n'

        new_prop_list.append(line)
    return new_prop_list
