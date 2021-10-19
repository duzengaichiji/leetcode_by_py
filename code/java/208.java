public class TrieNode{
    public int path; //当前节点链接到的其他节点的个数
    public int end;  //表示以当前节点为结尾的单词的个数
    public HashMap<Character,TrieNode> next;  //链接的节点列表
    public TrieNode(){
        path = 0;
        end = 0;
        next = new HashMap<>();
    }
}

class Trie {
    private TrieNode root;
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        if(word==null||word.equals("")) return;
        TrieNode node = root;
        for(int i=0;i<word.length();i++){
            char ch = word.charAt(i);
            if(!node.next.containsKey(ch)){
                node.next.put(ch,new TrieNode());
            }
            node = node.next.get(ch);
            node.path++; //这个节点上的分支数量+1
        }
        node.end++; //这个节点上的单词数量+1
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        if(word == null || word.equals("")) return false;
        TrieNode node = root;
        for(int i=0;i<word.length();i++){
            char ch = word.charAt(i);
            if(!node.next.containsKey(ch)) return false;
            node = node.next.get(ch);
        }
        // 没有以这个节点结尾的单词
        if(node.end==0) return false;
        return true;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String word) {
        if(word == null || word.equals("")) return false;
        TrieNode node = root;
        for(int i=0;i<word.length();i++){
            char ch = word.charAt(i);
            if(!node.next.containsKey(ch)) return false;
            node = node.next.get(ch);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */