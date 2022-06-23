# https://leetcode.cn/problems/substring-with-concatenation-of-all-words/
# 滑动窗口 + 哈希
from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def findSubstring(s: str, words: List[str]) -> List[int]:
        ans = []
        N = len(s)
        w_len = len(words[0])
        cki_len = len(words) * w_len
        hm = Counter(words)
        l = 0
        r = cki_len - 1
        # 切割方案，可以从0开始切（步长为一个单词长度），也可以从1开始...以此类推，共有 w_len 种方案，原因如下
        # 从 w_len 开始切就与从0开始切得到的结果大部分一样，相差的只是两个单词（一前一后）
        # 从 w_len + 1 开始切就与从1开始切得到的结果大部分一样，相差的只是两个单词（一前一后）
        # ...之后同理
        for offset in range(w_len):
            # 确定滑动窗口范围
            left = l + offset
            right = r + offset
            cki_s = string2list(s, left, right, w_len)  # 将待检测的s[i:j]以w_len为步长切割成一个list
            cki_s_mp = Counter(cki_s)  # 后期需要维护的那个表
            while right < N:
                if cki_s_mp == hm:  # 哈希表相同即为答案
                    ans.append(left)
                # 以一个单词的长度为跨度来滑动窗口
                left += w_len
                right += w_len
                del_w = s[left - w_len: left]  # 往后滑动后减少的单词
                if right < N:
                    ins_w = s[right - w_len + 1: right + 1]  # 往后滑动后增加的单词
                else:
                    ins_w = s[right - w_len + 1:]  # right越界，直接取到最后
                # 对那两个变动的单词做一些操作（从哈希表中增、删）
                cki_s_mp[del_w] -= 1
                if cki_s_mp[del_w] == 0:
                    del cki_s_mp[del_w]  # 为0即不存在，删除之，不删除会影响后续哈希表的比较
                if ins_w in cki_s_mp:
                    cki_s_mp[ins_w] += 1
                else:
                    cki_s_mp[ins_w] = 1

        return ans

# 切割器，如"abcdef"会被切割为["abc", "def"]，切割长度为words中的单词长度
def string2list(s, start, end, step):
    res = []
    for i in range(start, end + 2, step):
        res.append(s[i: i + step])
        if i + step == end + 1:
            return res
