"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
def canConstruct(ransomNote, magazine):
    es = True
    for i in ransomNote:
        if ransomNote.count(i) > magazine.count(i):
            es = False
    print(es)
    return es

canConstruct("aa","aab")