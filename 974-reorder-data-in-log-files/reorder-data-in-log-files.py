class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def get_key(log):
            identifier, content=log.split(" ", 1)
            if content[0].isdigit():
                return (1, )
            return (0, content, identifier)
        return sorted(logs, key=get_key)