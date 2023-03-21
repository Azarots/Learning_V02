"Given a string and a non-negative int n, return a larger string that is n copies of the original string"


def string_times(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result

print(string_times("Help", 2))


"Given a string and a non-negative int n, we'll say that the front of the string " \
"is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;"

def front_times(str, n):
    front = str[:3]
    result = ""
    for i in range(n):
        result += front
    return  result

print(front_times("Hel", 3))

def string_bits(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result

print(string_bits("Hekko"))


def string_splosion(str):
    result = ""
    for i in range(len(str)):
        partial_str = str[:i+1]
        result += partial_str
    return result

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

print(array_count9(1,2,3,4,9,9))