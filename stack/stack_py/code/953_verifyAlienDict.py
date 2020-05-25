class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if alpha[word1[k]] > alpha[word2[k]]:
                        return False
                    break
            # else will execuate directly after for loop, and it can be breaked if the break the loop
            else:
                if len(word1) > len(word2):
                    return False
        return True