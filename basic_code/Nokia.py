# import re
# def extract_error_messages(log_file_path, output_file_path):
#     error_pattern = r'\[ERROR\].*'  # Regex to match lines with "[ERROR]"
#     extracted_errors = []
#     try:
#         # Open and read the log file
#         with open(log_file_path, 'r') as log_file:
#             for line in log_file:
#                 if re.search(error_pattern, line):
#                     extracted_errors.append(line.strip())

#         # Save the extracted errors to a separate file
#         with open(output_file_path, 'w') as output_file:
#             output_file.write("\n".join(extracted_errors))
#         print(f"Extracted {len(extracted_errors)} error messages. Saved to {output_file_path}")
#     except FileNotFoundError:
#         print(f"Error: The file '{log_file_path}' was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# # Example usage
# log_file_path = "logs.txt"  # Path to your log file
# output_file_path = "error_logs.txt"  # Path for the extracted error messages
# extract_error_messages(log_file_path, output_file_path)



# def extract_data_from_file(file_path, keyword=None):
#     extracted_data = []
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 if not keyword or keyword in line:
#                     extracted_data.append(line.strip())
#         return extracted_data
#     except FileNotFoundError:
#         print(f"Error: File not found at {file_path}")
#         return []
# # Example Usage
# file_path = 'data.txt'  # Replace with your file path
# keyword = 'ERROR'       # Optional: Filter lines containing this keyword
# data = extract_data_from_file(file_path, keyword)
# print("Extracted Data:", data)



import requests
# Function to perform GET request
def fetch_json_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during GET request: {e}")
        return None

# Function to perform POST request
def post_json_to_url(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")
        return None
# Example Usage
url = "https://jsonplaceholder.typicode.com/posts"  # Example API endpoint
# GET example
print(fetch_json_from_url(url))
# POST example
post_data = {"title": "foo", "body": "bar", "userId": 1}
print(post_json_to_url(url, post_data))


def extract_data(list1, list2, key1, key2, match_key):
    result = []
    for item1 in list1:
        for item2 in list2:
            if item1[match_key] == item2[match_key]:  # Match condition
                result.append({key1: item1[key1], key2: item2[key2]})
    return result
# Example Usage
list1 = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
list2 = [
    {"id": 1, "age": 25},
    {"id": 2, "age": 30}
]
# Extract "name" from list1 and "age" from list2 where "id" matches
key1 = "name"
key2 = "age"
match_key = "id"
print(extract_data(list1, list2, key1, key2, match_key))


def find_minimum_xor(arr):
    # Step 1: Sort the array
    arr.sort()    
    # Step 2: Initialize the minimum XOR value
    min_xor = float('inf')    
    # Step 3: Compute XOR for adjacent pairs
    for i in range(len(arr) - 1):
        xor_value = arr[i] ^ arr[i + 1]
        min_xor = min(min_xor, xor_value)    
    return min_xor
# Example Usage
arr = [9, 5, 3, 10]
print(f"Minimum XOR value: {find_minimum_xor(arr)}")


def divide(dividend, divisor):
    # Handle edge cases
    if divisor == 0:
        raise ValueError("Division by zero is undefined")
    if dividend == 0:
        return 0    
    # Determine the sign of the result
    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)    
    # Perform the division using bit manipulation
    quotient = 0
    while dividend >= divisor:
        temp_divisor, multiple = divisor, 1
        # Find the largest shift where temp_divisor fits into dividend
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        # Subtract the largest shifted divisor
        dividend -= temp_divisor
        quotient += multiple    
    # Apply the sign to the result
    return -quotient if negative else quotient
# Example Usage
print(divide(10, 3))  # Output: 3
print(divide(43, -8))  # Output: -5
print(divide(-15, -3))  # Output: 5


def is_valid_bracket_string(s):
    stack = []
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}  
    for char in s:
        if char in bracket_map.values():  # Opening brackets
            stack.append(char)
        elif char in bracket_map.keys():  # Closing brackets
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            return False  # Invalid character   
    # If stack is empty, all brackets are matched
    return len(stack) == 0
# Example Usage
test_string = "{{([(())})}}"
print(is_valid_bracket_string(test_string))  # Output: False

# A cycle occurs when a node in the list points back to a previous node, forming a loop.
# "To solve this problem, I used Floyd's Cycle Detection Algorithm, also known as the Tortoise and Hare algorithm. The idea is to use two pointers: a slow pointer that moves one step at a time and a fast pointer that moves two steps at a time."
# "If there is a cycle, the fast pointer will eventually 'lap' the slow pointer and they will meet inside the cycle. If there is no cycle, the fast pointer will reach the end of the list (i.e., None)."
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    # Initialize two pointers
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next          # Move slow pointer one step
        fast = fast.next.next     # Move fast pointer two steps
        
        if slow == fast:          # Cycle detected
            return True
    
    return False  # No cycle found

# Example Usage
# Creating a linked list with a cycle:
# 1 -> 2 -> 3 -> 4 -> 5 -> back to 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Cycle here

print(has_cycle(node1))  # Output: True
