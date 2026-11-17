class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        result=[]
        for path in folder:
            if not result or not path.startswith(result[-1]+"/"):
                result.append(path)
        return result