#1
def filter_list(lst):
    return [item for item in lst if type(item) == int]

# Test examples
print(filter_list([1, 2, "a", "b"]))          # ➞ [1, 2]
print(filter_list([1, "a", "b", 0, 15]))      # ➞ [1, 0, 15]
print(filter_list([1, 2, "aasf", "1", "123", 123]))  # ➞ [1, 2, 123]

#2
def reverse(text):
    reversed_text = text[::-1]          # Step 1: Reverse the string
    changed_case = reversed_text.swapcase()  # Step 2: Swap the case
    return changed_case

# Test examples
print(reverse("Hello World"))  # ➞ "DLROw OLLEh"
print(reverse("ReVeRsE"))      # ➞ "eSrEvEr"
print(reverse("Radar"))        # ➞ "RADAr"

#3
lst = [1, 2, 3, 4, 5, 6]

first, *middle, last = lst

print("First:", first)
print("Middle:", middle)
print("Last:", last)

#4
def move_to_end(lst, val):
    result = [x for x in lst if x != val]        # Keep all values except 'val'
    result += [val] * lst.count(val)             # Add 'val' to the end as many times as it appears
    return result

# Test examples
print(move_to_end([1, 3, 2, 4, 4, 1], 1))        # ➞ [3, 2, 4, 4, 1, 1]
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))     # ➞ [7, 8, 1, 2, 3, 4, 9]
print(move_to_end(["a", "a", "a", "b"], "a"))    # ➞ ["b", "a", "a", "a"]



