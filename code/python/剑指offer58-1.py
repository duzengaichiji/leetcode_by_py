class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split(' ')
        temp = [t.strip() if t.strip()!='' else "" for t in temp]
        temp_ = []
        for t in temp:
            if t!="":
                temp_.append(t)
        return " ".join(temp_[::-1])