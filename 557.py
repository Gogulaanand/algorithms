https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        s = s.split(' ')
        for word in s:
            word = list(word)
            for i in range(len(word)//2):
                word[i], word[-i-1] = word[-i-1], word[i]
            ans.append(''.join(word))
        return ' '.join(ans)


class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        return ' '.join(s.split()[::-1])[::-1]                