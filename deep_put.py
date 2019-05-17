
def _deep_get(_dict, keys, default=None):
    for key in keys:
        if isinstance(_dict, dict):
            _dict = _dict.get(key, default)
        else:
            return default
    return _dict

def _deep_put(_dict, keys, value):


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
        "a0": {
            "a": "b"
        },
        "a1": {
            "b0": "b",
            "b1": {
                "c0": "c",
                # this is what I want to put
                # "c1": {
                #     "d0": "d"
                # }
            }
        },
        "a2": {
            "b2": {
                "c2": {
                    "d2": "d"
                }
            }
        }
    }

    get_d = _deep_get(base_dictionary, ["a1", "b1", "c1"])
    print(get_d)
    put_d = _deep_put(base_dictionary, ["a1", "b1", "c1"], {"e0": "e"})
    print(put_d)
    print(_deep_get(put_d, ["a1", "b1", "c1"]))
