
def _deep_get(_dict, keys, default=None):
    for key in keys:
        if isinstance(_dict, dict):
            _dict = _dict.get(key, default)
        else:
            return default
    return _dict

def _deep_put(_dict, keys, value):
    """
    add a key with `value` at the path given in `keys`
    """
    # first verify the key does not exists at the given path
    if _deep_get(_dict, keys) is not None:
        raise KeyError

    traverse_dict = _dict
    for i, key in enumerate(keys[:-1]):
        traverse_dict = traverse_dict.get(key)
        if i == len(keys) - 2:
            traverse_dict[keys[-1]] = value
            break            
    return _dict

# def _deep_put(_dict, keys, value):
#     """
#     replace the value of the last key in `keys` with `value`
#     """
#     import copy

#     # first verify the key exists
#     if _deep_get(_dict, keys) is None:
#         raise KeyError

#     temp_dict = copy.deepcopy(_dict)

#     # look for the last key-value pair in input
#     # and reset its value
#     for i, key in enumerate(keys[0:-1]):
#         temp_dict[key] = _dict.get(key)

#         # -1 for starting at 0
#         # -1 for iterating over all keys except the last
#         if i == len(keys) - 1 - 1:
#             print("key is: ", key)
#             print({keys[-1]: value})
#             temp_dict[key] = {keys[-1]: value}

#     return temp_dict

if __name__=="__main__":
    base_dictionary = {
        "k1.1": {
            "k2.1": {
                "k3.1": "v3.1",
                # this is what I want to put
                # "k3.2": {
                #     "v3.2"
                # }
            },
            "k2.2": "v2.2"
        },
        "k1.2": "v1.2"
    }

    # show the k3 dictionary
    print(_deep_get(base_dictionary, ["k1.1", "k2.1"]))

    # add the k3.2 dictionary
    put_dictionary =_deep_put(base_dictionary, ["k1.1", "k2.1", "k3.2"], "v3.2")
    print(_deep_get(put_dictionary, ["k1.1", "k2.1"]))
    print(put_dictionary)
