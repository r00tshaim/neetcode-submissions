class Solution:
    def scoreOfString(self, s: str) -> int:
        score_list = list()
        score = 0
        for ch in s:
            score_list.append(ord(ch))

        score = 0

        for i in range(len(score_list) - 1):
            diff = abs(score_list[i + 1] - score_list[i])
            score += diff

        return score

            