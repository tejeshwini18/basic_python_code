"""Compress repeated characters using char+count format."""


def compress_string(input_str):
    if not input_str:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            compressed.append(f"{input_str[i - 1]}{count}")
            count = 1

    compressed.append(f"{input_str[-1]}{count}")
    return "".join(compressed)


result_str = compress_string("AAAABBBBCCCAAADDDDEEF")
print(result_str)
