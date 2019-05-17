
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
    traverse_dict = _dict
    for i, key in enumerate(keys[:-1]):
        traverse_dict = traverse_dict.get(key)
        if i == len(keys) - 2:
            traverse_dict[keys[-1]] = value
            break            
    return _dict

def _deep_replace(_dict, keys, value):  
    """
    replace the value of the last key in `keys` with `value`
    """
    return _deep_put(
        _dict,
        keys,
        value
    )

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

    # replace the k3.1 dictionary
    replace_dictionary = _deep_replace(put_dictionary, ["k1.1", "k2.1", "k3.1"], "replaced")
    print(_deep_get(replace_dictionary, ["k1.1", "k2.1", "k3.1"]))
    print(replace_dictionary)
