"""Flatten a nested list recursively."""


def flatten_list(values):
    out_list = []
    for item in values:
        if isinstance(item, list):
            out_list.extend(flatten_list(item))
        else:
            out_list.append(item)
    return out_list


input_list = [1, [2, 3, [4, 5]]]
output_list = flatten_list(input_list)
print(output_list)
