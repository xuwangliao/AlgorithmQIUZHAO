class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # init
        wordList = set(wordList)

        # BFs
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        queue.append((next_word, length + 1))
                        wordList.remove(next_word)
        return 0