class UF{
    private int count;
    private int[] parent;

    public int getCount(){
        return count;
    }

    public UF(int num){
        count = num;
        parent = new int[num];
        for(int i=0;i<num;i++) parent[i] = i;
    }

    public int find(int x){
        while(x!=parent[x]){
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public boolean union(int p,int q){
        int rootP = find(p);
        int rootQ = find(q);
        if(rootP==rootQ) return true;
        parent[rootQ] = rootP;
        count-=1;
        return false;
    }
}

class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        UF uf = new UF(edges.length);
        for(int[] edge:edges){
            if(uf.union(edge[0]-1,edge[1]-1)) return edge;
        }
        return null;
    }
}