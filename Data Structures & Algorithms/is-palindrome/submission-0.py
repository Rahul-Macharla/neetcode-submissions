class Solution:
  def isPalindrome(self, word: str):
    lowercase = word.lower()
    collection = ""
    for letters in lowercase:
      if letters.isalnum():
        collection = collection + letters
    reversed_collection = collection[::-1]
    if reversed_collection == collection:
      return True
    else:
      return False    