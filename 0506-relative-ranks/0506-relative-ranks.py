class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_dict = {score[i]: i for i in range(len(score))}
        score.sort(reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(score))]
        result = [0] * len(score)
        for i, s in enumerate(score):
            index = score_dict[s]
            result[index] = ranks[i]
        return result