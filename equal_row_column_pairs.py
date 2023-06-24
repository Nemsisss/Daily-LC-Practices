class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #APPROACH #1 (faster, using tuples as keys in a hashmap)
        diction={}
        for i in grid:
            curr= tuple(i)
            if curr in diction:
                diction[curr]+=1
            else:
                diction[curr]=1
        
        sizeOfEach= len(grid[0])
        byCols=[[ 0 for i in range(len(grid))] for i in range(sizeOfEach)]
        for i in range(sizeOfEach):
            for j in range(sizeOfEach):
                byCols[i][j]=grid[j][i]
        
        count=0
        for i in byCols:
            if tuple(i) in diction:
                count+= diction[tuple(i)]
        return count
        
        #APPROACH #2
        # sizeOfEach= len(grid[0])
        # byCols=[[ 0 for i in range(len(grid))] for i in range(sizeOfEach)]
        # for i in range(sizeOfEach):
        #     for j in range(sizeOfEach):
        #         byCols[i][j]=grid[j][i]

        # count=0
        # for i in byCols:
        #     num=grid.count(i)
        #     count+=num
        # return count
