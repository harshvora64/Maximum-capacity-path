class maxheap():                # to store edges in the form of a maxheap
    def __init__(self,lst):
        self._heap=lst          # initially stores all the edges originating from s
        self._len=len(self._heap)
        j=self._len-1
        while(j>=0):                    # fast build heap algorithm using heap_down from the bottom of the heap to the top
                                        # complexity O(n) - runs only once 
            self.downheap(j)
            j-=1

    def insert(self,e):             # add an element to the heap (O(log(m))) time complexity, as it uses upheap
        self._heap.append(e)
        self.upheap(self._len)          # bring to correct position
        self._len=len(self._heap)

    def upheap(self,location):          # upheap, O(log(m)) time complexity
        self._len=len(self._heap)
        j=(location-1)//2
        l=self._len
        while j>=0:
            hloc=self._heap[location][0]
            hj=self._heap[j][0]
            if hloc<hj:
                break
            else:
                self._heap[location],self._heap[j]=self._heap[j],self._heap[location]
                location = j                                                            # update location of object and parent
                j=(location-1)//2



    def downheap(self,location):                # downheap - O(log(m)) complexity
        self._len=len(self._heap)
        j=location*2+1
        l=self._len
        while j<l:
            hloc=self._heap[location][0]
            hj=self._heap[j][0]
            if j+1<l:
                hj1=self._heap[j+1][0]
            else:
                hj1=0
        
            if hloc>max(hj,hj1):
                break
            else:
                k=j if hj>hj1 else j+1
                self._heap[location],self._heap[k]=self._heap[k],self._heap[location]
                location=k
                j=location*2+1



    def extractmax(self):                   # finds the top element and removes it 
        if self._len!=0:
            self._heap[0],self._heap[-1]=self._heap[-1],self._heap[0]
        res=self._heap.pop()
        self.downheap(0)
        self._len=len(self._heap)
        return res


def findMaxCapacity(n,links,s,t):
    v=[]
    for i in range(n):
        v.append([[],n])                # stores the list of edges originating from the current vertex
                                        # the second element stores prev - the element previous to it in the best possible path from s to that vertex
        m=links[0][2]                   # m stores the maximum capacity of the graph.. initialised to the capacity of first edge...
    for i in links:
        v[i[0]][0].append((i[2],i[0],i[1]))     # stores edge of the current vertex in the format of capacity,current vertex, next vertex ... (tuple)
        v[i[1]][0].append((i[2],i[1],i[0]))
        m=max(m,i[2])
    v[s][1]=s

    cap=m                                       # to store the capacity
    h=maxheap(v[s][0])                          # initialise maxheap with initial value of the edges originating from s
    while(h._len!=0):

        d=h.extractmax()                        # extract max

        cap=min(cap,d[0])                       # update capacity as min of currently extracted edge and prev capacity

        
        if(v[d[2]][1]==n):                      # if prev is not n, then 2nd vertex is already visited, so ignore it, or set the prev of the vertex as the beginning vertex of this edge
            v[d[2]][1]=d[1]
        else:
            continue
        if d[2]==t:
            break
        else:
            for i in v[d[2]][0]:                # see the neighbours of the second vertex
                if v[i[2]][1]==n:               # if neighbour not visited,
                    h.insert(i)                 # insert it into the heap


    z=t                                         # this is to get the path, travelling backwards along prev starting from t
    lst=[t]                                     # initialise it to t
    while z!=s:

        z=v[z][1]                               
        lst.append(z)
    return (cap,list(reversed(lst)))            # reverse, as stored backwards

    # each vertex is visited atmost once, so atmost m edges are added to the heap, and each insertion takes max O(log(m)) time.. So O(mlog(m)) complexity
