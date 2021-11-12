# from union_find import UnionFind
import sys

class UnionFind:
    
    def __init__(self, elements=None):
        self.n_elts = 0  # current num of elements
        self.n_comps = 0  # the number of disjoint sets or components
        self._next = 0  # next available id
        self._elts = []  # the elements
        self._indx = {}  #  dict mapping elt -> index in _elts
        self._par = []  # parent: for the internal tree structure
        self._siz = []  # size of the component - correct only for roots

        if elements is None:
            elements = []
        for elt in elements:
            self.add(elt)


    def __repr__(self):
        return  (
            '<UnionFind:\n\telts={},\n\tsiz={},\n\tpar={},\nn_elts={},n_comps={}>'
            .format(
                self._elts,
                self._siz,
                self._par,
                self.n_elts,
                self.n_comps,
            ))

    def __len__(self):
        return self.n_elts

    def __contains__(self, x):
        return x in self._indx

    def __getitem__(self, index):
        if index < 0 or index >= self._next:
            raise IndexError('index {} is out of bound'.format(index))
        return self._elts[index]

    def __setitem__(self, index, x):
        if index < 0 or index >= self._next:
            raise IndexError('index {} is out of bound'.format(index))
        self._elts[index] = x

    def add(self, x):
        if x in self:
            return
        self._elts.append(x)
        self._indx[x] = self._next
        self._par.append(self._next)
        self._siz.append(1)
        self._next += 1
        self.n_elts += 1
        self.n_comps += 1

    def find(self, x):
        
        if x not in self._indx:
            raise ValueError('{} is not an element'.format(x))

        p = self._indx[x]
        while p != self._par[p]:
            # path compression
            q = self._par[p]
            self._par[p] = self._par[q]
            p = q
        return p

    def union(self, x, y):
        for elt in [x, y]:
            if elt not in self:
                self.add(elt)

        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self._siz[xroot] < self._siz[yroot]:
            self._par[xroot] = yroot
            self._siz[yroot] += self._siz[xroot]
        else:
            self._par[yroot] = xroot
            self._siz[xroot] += self._siz[yroot]
        self.n_comps -= 1

   

def fusoes(N, lista):
    # print(lista)
    uf = UnionFind(list(range(1,N+1)))
    # L = []
    for c,c1,c2 in lista:
        if(c =='C'):
            x = uf.find(c1);
            y = uf.find(c2);  
            if(x==y):
                # L.append('S')
                print('S')
            else:
                # L.append('N')
                print('N')
        else:
            uf.union(c1,c2)
    # print(L)

if __name__ == '__main__':
    # print("Digite o N e M")
    n, m = map(int, sys.stdin.readline().split())
    lista = []
    for _ in range(m):
        c , c1 , c2 = input().split()
        lista.append((c, int(c1), int(c2)))
    fusoes(n, lista)