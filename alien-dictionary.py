#User function Template for python3

class Solution:
    def topoSort(self,adj,N):
        indegree = [0 for i in range(0,N)]
        queue = []
        topo = []
        for i in range(0,N):
            for v in adj[i]:
                indegree[v] += 1
        for i in range(0,N):
            if indegree[i] == 0:
                queue.append(i)
        while(len(queue)!=0):
            node = queue.pop(0)
            topo.append(chr(node+97))
            for v in adj[node]:
                indegree[v] -=1
                if indegree[v] == 0:
                    queue.append(v)
        return topo
    def findOrder(self,alien_dict, N, K):
        adj = [[] for i in range(0,K)]
        for i in range(0,N-1):
            s1 = alien_dict[i]
            s2 = alien_dict[i+1]
            l = min(len(s1),len(s2))
            for i in range(0,l):
                if s1[i]!=s2[i]:
                    adj[ord(s1[i])-97].append(ord(s2[i]) - 97)
                    break
        return self.topoSort(adj,K)
    # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
