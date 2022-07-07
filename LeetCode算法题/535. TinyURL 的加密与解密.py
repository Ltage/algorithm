# https://leetcode.cn/problems/encode-and-decode-tinyurl/
# 哈希 + 映射
class Codec:
    def __init__(self):
        self.hm = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        s = str(hash(longUrl))
        while s in self.hm and self.hm[s] != longUrl:  # 哈希冲突重新哈希
            s = str(hash(longUrl))
        self.hm[s] = longUrl
        return "http://tinyurl.com/" + s

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s = shortUrl.split("http://tinyurl.com/")[1]
        return self.hm[s]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))