class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {
            "1": "qwertyuiop",
            "2": "asdfghjkl",
            "3": "zxcvbnm"
        }
        ans = []
        for i in range(len(words)):
            curr_row = set()
            for j in range(len(words[i])):
                curr_char = words[i][j].lower()
                if curr_char in rows["1"]:
                    curr_row.add("1")
                elif curr_char in rows["2"]:
                    curr_row.add("2")
                else:
                    curr_row.add("3")
            if len(curr_row) == 1:
                ans.append(words[i])
        return ans
        