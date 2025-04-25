from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    biggest_count = 1
    result = ''
    if len(strs) == 1:
        return strs[0]
    for i in range(len(strs[0]), -1, -1):
        substring = strs[0][:i]
        print('sub: ', substring, i, len(strs[0]))
        count = sum(1 for s in strs if substring in s)
        print('co: ', count)
        if (count > biggest_count):
            print('re: ', substring, biggest_count, len(substring))
            result = substring
            biggest_count = count
    return result

def longestCommonPrefix1(strs: List[str]) -> str:
    if not strs:
        return ''
    
    prefix = strs[0]

    for items in strs[1:]:
        while not items.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ''
    
    return prefix

strs = ["ab", "a"]

print('result: ', longestCommonPrefix(strs))