class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d = [(0,1),(1,0),(0,-1),(-1,0)]


        visited = set()
        i=0
        j=0
        cur=0
        ret=[matrix[i][j]]
        visited.add((0,0))
        while len(visited)<len(matrix)*len(matrix[0]):
            di,dj = d[cur]
            new_i= i+di
            new_j=j+dj
            if (new_i,new_j) in visited or new_i>=len(matrix) or new_i<0 or new_j>=len(matrix[0]) or new_j<0:
                cur = cur+1
                cur=cur%4

                di,dj = d[cur]
                new_i= i+di
                new_j=j+dj
            ret.append(matrix[new_i][new_j])
            visited.add((new_i,new_j))
            i=new_i
            j=new_j
        return ret
