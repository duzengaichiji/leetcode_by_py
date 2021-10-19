class Solution {
    public void postOrder(int root,int parent,int[] nodeNum,int[] distSum,List<List<Integer>> graph){
        List<Integer> neighbors = graph.get(root);
        for(Integer neighbor:neighbors){
            if(neighbor==parent) continue;
            postOrder(neighbor,root,nodeNum,distSum,graph);
            nodeNum[root]+=nodeNum[neighbor];
            distSum[root]+=nodeNum[neighbor]+distSum[neighbor];
        }
    }

    public void preOrder(int root,int parent,int[] nodeNum,int[] distSum,List<List<Integer>> graph){
        List<Integer> neighbors = graph.get(root);
        for(Integer neighbor:neighbors){
            if(neighbor==parent) continue;
            distSum[neighbor] = distSum[root]-nodeNum[neighbor]+(graph.size()-nodeNum[neighbor]);
            preOrder(neighbor,root,nodeNum,distSum,graph);
        }
    }

    public int[] sumOfDistancesInTree(int N, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0;i<N;i++){
            graph.add(new ArrayList<Integer>());
        }
        for(int i=0;i<edges.length;i++){
            graph.get(edges[i][0]).add(edges[i][1]);
            graph.get(edges[i][1]).add(edges[i][0]);
        }

        int[] nodeNum = new int[N];
        int[] distSum = new int[N];
        for(int i=0;i<N;i++) nodeNum[i] = 1;

        postOrder(0,-1,nodeNum,distSum,graph);
        preOrder(0,-1,nodeNum,distSum,graph);

        return distSum;
    }
}