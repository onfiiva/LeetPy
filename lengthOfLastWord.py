def lengthOfLastWord(s: str) -> int:
    sList = s.split()
    return len(sList[-1])
            