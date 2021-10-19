class Solution {
    private class UnionFind{
        private int[] parent;
        private double[] weight;
        public UnionFind(int n){
            this.parent = new int[n];
            this.weight = new double[n];
            for(int i=0;i<n;i++){
                parent[i] = i;
                weight[i] = 1.0d; // 边的权重全部初始化为1(自己指向自己，x/x=1)
            }
        }
        public int find(int x){
            if(x!=parent[x]){
                // 查询以及路径压缩
                int origin = parent[x];
                // 递归查找，一定会查找到最顶上的节点，所以就将该路径下的所有节点拼接到最顶上那个节点下方
                parent[x] = find(parent[x]);
                weight[x]*=weight[origin];
            }
            return parent[x];
        }
        public void union(int p,int q,double value){
            int rootP = find(p);
            int rootQ = find(q);
            if(rootP==rootQ) return;
            parent[rootP] = rootQ;
            weight[rootP] = weight[q]*value/weight[p];
        }
        public double isConnected(int p,int q){
            int rootP = find(p);
            int rootQ = find(q);
            if(rootP==rootQ){
                return weight[p]/weight[q];
            }else{
                return -1.0d;
            }
        }
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int size = equations.size();
        UnionFind uf = new UnionFind(2*size);
        Map<String,Integer> hashMap = new HashMap<>(2*size);
        int id = 0; // 记录有效符号个数
        // step1. 建立有向图
        for(int i=0;i<size;i++){
            List<String> equation = equations.get(i);
            String var1 = equation.get(0);
            String var2 = equation.get(1);
            if(!hashMap.containsKey(var1)){
                hashMap.put(var1,id);
                id++;
            }
            if(!hashMap.containsKey(var2)){
                hashMap.put(var2,id);
                id++;
            }
            uf.union(hashMap.get(var1),hashMap.get(var2),values[i]);
        }
        // step2. 求解
        int queriesSize = queries.size();
        double[] res = new double[queriesSize];
        for (int i = 0; i < queriesSize; i++) {
            String var1 = queries.get(i).get(0);
            String var2 = queries.get(i).get(1);

            Integer id1 = hashMap.get(var1);
            Integer id2 = hashMap.get(var2);

            if (id1 == null || id2 == null) {
                res[i] = -1.0d;
            } else {
                res[i] = uf.isConnected(id1, id2);
            }
        }
        return res;
    }
}