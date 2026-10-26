class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i]^=1
        return image