class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        result=[]
        row=col=0
        for ch in target:
            new_row=(ord(ch)-ord('a'))//5
            new_col=(ord(ch)-ord('a'))%5
            while row>new_row:
                result.append('U')
                row-=1
            while col>new_col:
                result.append('L')
                col-=1
            while row<new_row:
                result.append('D')
                row+=1
            while col<new_col:
                result.append('R')
                col+=1
            result.append('!')
        return ''.join(result)