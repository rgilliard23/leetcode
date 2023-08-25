class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:



        @cache
        def recurse(sWord):
            if len(sWord) == 0:
                return True
            for word in wordDict:
                if sWord.startswith(word):
                    if recurse(sWord[len(word):]):
                        return True
            return False
        return recurse(s)
