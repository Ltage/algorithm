# https://leetcode.cn/problems/get-watched-videos-by-your-friends/
# 找到level层的好友，统计他们看过的视频，然后排序
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        f = {id, }
        l = 0
        q = [id, ]
        temp = []
        v = defaultdict(int)
        while l < level:
            cur = q.pop(0)
            for i in friends[cur]:
                if i not in f:
                    temp.append(i)
                    f.add(i)
            if not q:
                q, temp = temp, q
                l += 1
        for i in q:
            for j in watchedVideos[i]:
                v[j] += 1
        return [i[0] for i in sorted(v.items(), key=lambda k: (k[1], k[0]))]
