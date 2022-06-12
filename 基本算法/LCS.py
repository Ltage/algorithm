# 最长公共子序列
def LCS(x: str, y: str):
    ans = []
    dp = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    i = 1
    while i <= len(x):
        j = 1
        while j <= len(y):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            j += 1
        i += 1
    return print_LCS(dp, len(x), len(y), x, ans)


def print_LCS(dp, i, j, x, ans):
    if i == 0 or j == 0:
        return
    if dp[i][j] == max(dp[i][j - 1], dp[i - 1][j]):
        if max(dp[i][j - 1], dp[i - 1][j]) == dp[i][j - 1]:
            print_LCS(dp, i, j - 1, x, ans)
        else:
            print_LCS(dp, i - 1, j, x, ans)
    else:
        print_LCS(dp, i - 1, j - 1, x, ans)
        ans.append(x[i - 1])
    return ans


str1 = "ABCBABAISLFHIUAHBFKJAGFKASGHRSUGFKJ"
str2 = "BDCAAIUASHDFKSHFKJSLHGFIUASLTSADFS"
print(LCS(str1, str2))
