# https://leetcode.cn/problems/validate-ip-address/
class Solution:
    @staticmethod
    def validIPAddress(queryIP: str) -> str:
        import re
        pattern_ipv4 = r"((0|([1-9][0-9]{0,2}))\.){3,3}(0|([1-9][0-9]{0,2}))"
        pattern_ipv6 = r"((0|(([0-9]|[a-f]|[A-F]){1,4})):){7,7}(0|(([0-9]|[a-f]|[A-F]){1,4}))"

        match_ipv4 = re.fullmatch(pattern_ipv4, queryIP)
        match_ipv6 = re.fullmatch(pattern_ipv6, queryIP)

        if match_ipv4:
            list_ipv4 = queryIP.split(".")
            for i in list_ipv4:
                if int(i) > 255:
                    return "Neither"
            return "IPv4"

        if match_ipv6:
            return "IPv6"

        return "Neither"


print(Solution.validIPAddress("192.0.0.1"))