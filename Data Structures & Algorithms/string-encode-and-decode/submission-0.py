from typing import List
class Solution:
  def encode(self, message: List[str]):
    output = ""
    for i in message:
      output = output + str(len(i)) + "#" + i
    return output

  def decode(self, message: str):
    decodedoutput = []
    i = 0
    while i < len(message):
      nums = ""
      while True:
        if message[i] == "#":
          break
        nums = nums + message[i]
        i = i + 1
      i = i + 1
      length = int(nums)
      slicing = message[i: i + length]
      decodedoutput.append(slicing)
      i = i + length
    return decodedoutput     