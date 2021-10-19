class Solution {
    public int[] constructArr(int[] a) {
        if(a.length==0) return new int[]{};
        int[] pre = new int[a.length-1];
        int[] order = new int[a.length-1];
        pre[0] = a[0];
        for(int i=1;i<a.length-1;i++) pre[i] = pre[i-1]*a[i];
        order[a.length-2] = a[a.length-1];
        for(int i=a.length-3;i>=0;i--) order[i] = order[i+1]*a[i+1];
        int[] res = new int[a.length];

        // for(int i=0;i<pre.length;i++) System.out.println(pre[i]);
        // System.out.println();
        // for(int i=0;i<pre.length;i++) System.out.println(order[i]);

        for(int i=0;i<a.length;i++){
            if(i==0) res[i] = order[0];
            else if(i==a.length-1) res[i] = pre[a.length-2];
            else res[i] = pre[i-1]*order[i];
        }
        return res;
    }
}