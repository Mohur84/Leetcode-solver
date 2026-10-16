class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_map=defaultdict(list)
        for path in paths:
            parts=path.split()
            dictionary=parts[0]
            for file_info in parts[1:]:
                name, content=file_info.split('(', 1)
                content=content[:-1]
                full_path=dictionary+"/"+name
                content_map[content].append(full_path)
        return[
            files
            for files in content_map.values()
            if len(files)>1
        ]