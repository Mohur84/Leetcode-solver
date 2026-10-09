class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4(ip):
            parts = ip.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part or len(part) > 3:
                    return False
                if any(c < '0' or c > '9' for c in part):
                    return False
                if len(part) > 1 and part[0] == '0':
                    return False
                if int(part) > 255:
                    return False
            return True
        def is_ipv6(ip):
            parts = ip.split(":")
            if len(parts) != 8:
                return False
            allowed = "0123456789abcdefABCDEF"
            for part in parts:
                if not 1 <= len(part) <= 4:
                    return False
                if any(c not in allowed for c in part):
                    return False
            return True
        if "." in queryIP and ":" not in queryIP:
            return "IPv4" if is_ipv4(queryIP) else "Neither"
        if ":" in queryIP and "." not in queryIP:
            return "IPv6" if is_ipv6(queryIP) else "Neither"
        return "Neither"