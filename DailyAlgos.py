def multiply(array, x):
    for i in range(len(array)):
        array[i] *= x
    return array

# function 2
# Given an array and y return a count of all values greater than y


def count(array, y):
    count = 0
    for i in range(len(array)):
        if array[i] > y:
            count += 1
    return count
# function 3
# Given an array of strings, return the same array with each string being replaced by it's length. ex. ["Hello", "World"] => [5, 5]


def replace_string(array):
    for i in range(len(array)):
        array[i] = len(array[i])
    return array


print(replace_string(["Hello", "World"]))
# function 4
# Given an array of positive and negative numbers, return that same array with all values turned positive


def positive(array):
    for i in range(len(array)):
        if (array[i] < 0):
            array[i] *= -1
    return array


print(positive([-3, -5, -8, 1, 3]))
# function 5
# Given an array of strings, return that same array with each string replaced by it's first letter ex. ["Hello", "World", "pie"] => ["H", "W", "p"]


def first_letter(array):
    for i in range(len(array)):
        array[i] = array[i][0]
    return array


print(first_letter(["Hello", "World", "pie"]))
# function 6
# Given an array of strings, return the average length of the strings in the array ["Hello", "P"] => 3


def avg_length(array):
    sum = 0
    for i in range(len(array)):
        sum += len(array[i])
    avg = sum / len(array)
    return int(avg)


print(avg_length(["Hello", "P"]))
# function 7
# Given an array, reverse it in place and return the array


def reverse_array(arr):
    for i in range(int(len(arr)/2)):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    return arr


print(reverse_array([3, 5, 8, 10, 12, 14]))
# function 8
# Write a function that takes degrees and isCels - a boolean True or False. If True, return the degrees in Fahrenheit, if false, assume the degrees are already Fahrenheit, and return celsius instead. F = C * 9/5 + 32


def fahreheit_or_celsius(degrees, isCels):
    if isCels == True:
        return degrees * 9/5 + 32
    else:
        return ((degrees-32) * 5) / 9
# function 9
# Given a string, return a new string without the first and last letters


def cut_string(string):
    length = len(string)
    new_string = string[1]
    for i in range(2, length - 1):
        new_string += string[i]
    return new_string
# "Hello" => "ell"


print(cut_string("Hello"))

# function 10
# Given an array of strings, return a new array with only even-length strings remaining, in their original order


def even_string(array):
    new_array = []
    for i in range(len(array)):
        if (len(array[i]) % 2 == 0):
            new_array.append(array[i])
    return new_array


print(even_string(["Hello", "World", "Tumbler", "SpaceX", "spice", "tulips"]))

# String: Is Palindrome

# Create a function that returns a boolean whether the string is a strict palindrome.
#   - palindrome = string that is same forwards and backwards

# Given: "a x a" or "racecar" => return true
# Given: "Dud" or "oho!" => return false .
# Do not ignore spaces, punctuation and capitalization


def palindrome(string):
    new_string = ""
    for i in range(len(string) - 1, -1, -1):
        new_string += string[i]
    if new_string == string:
        return True
    else:
        return False


print(palindrome('racecar'))
print(palindrome('Dud'))
print(palindrome('oho!'))
# Longest Palindrome

# For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring.

# Given: "what up, daddy-o?" , return "dad"
# Given: "uh... not much" , return "u"

# Include spaces as well
# Given: "Yikes! my favorite racecar erupted!" , return "e racecar e" .

# Strings longer or shorter than complete words are OK.

# All the substrings of "abc" are:
# a, ab, abc, b, bc, c

# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# For example, there are # socks with colors . There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is # .
# Function Description
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
# sockMerchant has the following parameter(s):
#   n: the number of socks in the pile
#   ar: the colors of each sock


def sockMerchant(arr):
    arr.sort()
    pair_count = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i+1]:
            i += 1
            pair_count += 1
        i += 1
    return pair_count


print(sockMerchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sockMerchant([20, 30, 40, 20, 30, 40, 50, 50, 60, 60, 90]))

# Input Format
# Theline contains space-separated integers describing the colors of the socks in the pile.
# Output Format
# Return the total number of matching pairs of socks that John can sell.
# Sample Input
# 10 20 20 10 10 30 50 10 20
# Sample Output
# 3

# Given an array of numbers, create a new string where it looks like page numbers


def book_index(arr):
    output = ""
    count = 0
    for i in range(len(arr)):
        if i == (len(arr) - 1) and count == 0:
            output += str(arr[len(arr) - 1])
        elif i == (len(arr) - 1) and count > 0:
            output += str(arr[i - count]) + "-" + str(arr[i])
        elif arr[i] + 1 == arr[i + 1]:
            count += 1
        else:
            if count > 0:
                output += str(arr[i - count]) + "-" + str(arr[i]) + ", "
                count = 0
            else:
                output += str(arr[i]) + ", "
    return output


def book_index_two(arr):
    output = str(arr[0])
    if arr[0] == arr[1] - 1:
        check = 0
    else:
        check = 1
    for i in range(1, len(arr)):
        if check == 1:
            output += f", {arr[i]}"
            if i != (len(arr) - 1) and arr[i] == arr[i+1] - 1:
                check = 0
            else:
                check = 1
        elif check == 0:
            if i != (len(arr) - 1) and arr[i] == arr[i + 1] - 1:
                check = 0
            else:
                check = 1
                output += f"-{arr[i]}"
    return output


print(book_index([1, 2, 3, 5, 7, 15, 16, 17]))
print(book_index([1, 2, 3, 5, 7, 15, 17]))
print(book_index([1, 3, 5, 7, 15, 17, 19, 20]))
print(book_index_two([1, 2, 3, 5, 7, 15, 16, 17]))
print(book_index_two([1, 2, 3, 5, 7, 15, 17]))
print(book_index_two([1, 3, 5, 7, 15, 17, 19, 20]))

#Given an dictionary, swap the key and the value in it
def swap(obj):
    new_obj = {}
    for key in obj:
        new_obj[str(obj[key])] = key
    return new_obj
obj ={'name': 'Michelle', 'color': 'black'}
print(swap(obj))

def invert_hash(obj):
    for key, value in obj.items():
        key = str(value)
        obj[value] = key
        del obj[key]
    return obj
print(invert_hash(obj))

#Given 2 arrays, create a new dictionary with the keys from array1 and values from array2
def zip_arrays_infomap(arr1, arr2):
    dict = {}
    for i in range(len(arr1)):
        key = str(arr1[i])
        dict[key] = arr2[i]
    return dict
print(zip_arrays_infomap(["ABC", 3, "yo"], [42, "whatsup", True]))