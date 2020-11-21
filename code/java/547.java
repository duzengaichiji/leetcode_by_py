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

    public void union(int p,int q){
        int rootP = find(p);
        int rootQ = find(q);
        if(rootP==rootQ) return;
        parent[rootQ] = rootP;
        count--;
    }
}

class Solution {
    public int findCircleNum(int[][] M) {
        int num = M.length;
        UF uf = new UF(num);
        for(int i=0;i<num;i++){
            for(int j=0;j<num;j++){
                if(M[i][j]==1) uf.union(i,j);
            }
        }
        return uf.getCount();
    }
}