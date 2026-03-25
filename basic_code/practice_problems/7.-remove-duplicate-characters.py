"""Remove repeated characters while preserving first appearance order."""


def remove_duplicate(text):
    unique_text = ""
    for char in text:
        if char not in unique_text:
            unique_text += char
    return unique_text


in_a = "1231"
out_a = remove_duplicate(in_a)
print(out_a)
