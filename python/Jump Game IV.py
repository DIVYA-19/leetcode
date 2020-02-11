class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = {}
        if len(arr) == 1:
            return 0
        if len(list(set(arr))) == 1:
            return(1)

        for i,item in enumerate(arr):
            if item in d:
                d[item].append(i)
            else:
                d[item] = [i]

        steps = [0] + [float('INF')]*(len(arr)-1)

        q = [0]

        while(q):
            x = q[0]
            del q[0]

            if x == len(arr)-1:
                return(steps[x])
            try:
                v = d[arr[x]]
            except:
                pass
            for i in range(len(v)):
                child = v[i]

                if steps[child] > steps[x] + 1:
                    steps[child] = steps[x] + 1
                    q.append(child)

            if x-1>=0 and steps[x-1] >= steps[x]+1:
                steps[x-1] = steps[x]+1
                q.append(x-1)
            if x+1<len(arr) and steps[x+1] >= steps[x]+1:
                steps[x+1] = steps[x] + 1
                q.append(x+1)
                
            try:
                del d[arr[x]]
            except:
                pass
            
        return(steps[len(arr)-1])
