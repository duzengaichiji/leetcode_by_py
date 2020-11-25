class UF{
    int count;
    private int[] parent;

    public UF(int num){
        count = num;
        parent = new int[num];
        for(int i=0;i<num;i++) parent[i] = i;
    }

    public void setParent(int i,int val){
        parent[i] = val;
    }

    public void setCount(int num){
        count = num;
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
        count--;
        return false;
    }
}

class Solution {
    public int minSwapsCouples(int[] row) {
        int n = row.length;
        UF uf = new UF(n);
        for(int i=0;i<n;i+=2) uf.setParent(i+1,i);
        uf.setCount(n/2);

        for(int i=0;i<n;i+=2){
            if((row[i]%2==0&&row[i+1]==row[i]+1)||(row[i+1]%2==0&&row[i]==row[i+1]+1)){}
            else uf.union(row[i],row[i+1]);
        }
        return n/2-uf.count;
    }
}