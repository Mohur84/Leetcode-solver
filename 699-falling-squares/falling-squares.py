class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        coords=sorted({
            x
            for left, side in positions
            for x in(left, left+side-1)
        })
        index={x: i for i, x in enumerate(coords)}
        size=len(coords)
        tree=[0]*(4*size)
        lazy=[0]*(4*size)
        def query(node, start, end, left, right):
            if left<=start and end<=right:
                return tree[node]
            if lazy[node]:
                for child in (node*2, node*2+1):
                    tree[child]=lazy[node]
                    lazy[child]=lazy[node]
                lazy[node]=0
            mid=(start+end)//2
            result=0
            if left<=mid:
                result=max(
                    result,
                    query(node*2, start, mid, left, right)
                )
            if right>mid:
                result=max(
                    result,
                    query(node*2+1, mid+1, end, left, right)
                )
            return result
        def update(node, start, end, left, right, value):
            if left<=start and end<=right:
                tree[node]=value
                lazy[node]=value
                return
            if lazy[node]:
                for child in (node*2, node*2+1):
                    tree[child]=lazy[node]
                    lazy[child]=lazy[node]
                lazy[node]=0
            mid=(start+end)//2
            if left<=mid:
                update(node*2, start, mid, left, right, value)
            if right>mid:
                update(node*2+1, mid+1, end, left, right, value)
            tree[node]=max(tree[node*2], tree[node*2+1])
        answer=[]
        max_height=0
        for left, side in positions:
            right=left+side-1
            l=index[left]
            r=index[right]
            base_height=query(1, 0, size-1, l, r)
            new_height=base_height+side
            update(1, 0, size-1, l, r, new_height)
            max_height=max(max_height, new_height)
            answer.append(max_height)
        return answer