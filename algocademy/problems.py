# Magical Number - O(log n)
# Input: N = 39
# Output: 3
# Explanation: magicNumber(39) = magicNumber(3 + 9) = magicNumber(12) = magicNumber(1 + 2) = 3

def magic_number(n):
    while n > 9:
        n = inner_sum(n)
    return n


def inner_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


print(magic_number(928435))


def count_binary_strings(n, k):
    dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k + 1):
            dp[i + 1][0] += dp[i][j]
            if j < k:
                dp[i + 1][j + 1] += dp[i][j]
            print(dp)
    result = 0
    for j in range(k + 1):
        result += dp[n][j]
    return result


print(count_binary_strings(4, 2))


class Solution:

    def concatAllPairs(self, first, second):
        result = []
        for firstPart in first:
            for secondPart in second:
                result.append(firstPart + secondPart)
        return result

    def __init__(self):
        self.index = 0

    def parsePaths(self, input):
        currentLevel = []
        strings = [""]
        while self.index < len(input):
            if input[self.index] == '{':
                self.index += 1
                nextLevel = self.parsePaths(input)
                strings = self.concatAllPairs(strings, nextLevel)
            elif input[self.index] == '}':
                break
            elif input[self.index] == ',':
                currentLevel += strings
                strings = [""]
            else:
                for i in range(len(strings)):
                    strings[i] += input[self.index]
            self.index += 1
        currentLevel += strings
        return currentLevel

    def decompress(self, input):
        return self.parsePaths(input)

s1 = Solution()
input = "README.md,resources/js/app.js,resources/js/boot.js,resources/js/comp/a.js,resources/js/comp/b.js"
print(s1.decompress(input))

