def operation(num1, num2, oper):
    if(oper == "+"):
        return num1 + num2;
    if(oper == "-"):
        return num1 - num2;
    if(oper == "*"):
        return num1 * num2;
    if(oper == "/"):
        return num1 / num2;


def is_palindrome(word):
    arr = list(word)
    res = True;
    for i in range(0, len(word) // 2):
        res = res and arr[i] == arr[len(word) - 1 - i];
    return res;
    

def primes_of(nums: list):
    nums.sort();
    res = [];
    primes = [];
    current = 0;
    for i in range(2, nums[len(nums) - 1]):
        is_prime = True;
        for j in primes:
            is_prime = is_prime and i % j != 0;
        if(is_prime and nums[current] == i):
            res.append(i);
            current += 1
    return res;


def suma_consecutiva(nums):
    max = None;
    for i in range(0, len(nums) - 1):
        if(max == None or max < nums[i] + nums[i+1]):
            max = nums[i] + nums[i + 1];
    return max;


def is_equal(palabra1, palabra2):
    for char in palabra2:
        if(not char in palabra1):
            return False;
    return True;


def contains(dict, word):
    for key in dict:
        if word in dict[key]:
            return True;
    return False;


def palabras_iguales(lst):
    words_dict = {};
    for word in lst:
        if(len(words_dict) == 0):
            words_dict[word] = [word];
        else:
            is_different = True;
            for key in words_dict:
                if(is_equal(key, word)):
                    words_dict[key].append(word);
                    is_different = False;
            if is_different:
                words_dict[word] = [word];

    res = []
    for key in words_dict:
        if(len(words_dict[key]) > 1):
            res.append(words_dict[key]);
    return res;





