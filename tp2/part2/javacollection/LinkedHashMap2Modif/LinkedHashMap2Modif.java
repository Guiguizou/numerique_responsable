import java.util.*;  

public class LinkedHashMap2Modif {
    public static void main(String args[]) {
        LinkedHashMap<Integer, String> map = new LinkedHashMap<Integer, String>();

        insertElements(map, 10000000);
        accessElements(map);
        removeElements(map, 5000000);
        accessElements(map);
    }

    public static void insertElements(LinkedHashMap<Integer, String> map, int count) {
        for (int i = 0; i < count; i++) {
            map.put(i, "Number is " + i);
        }
    }

    public static void accessElements(LinkedHashMap<Integer, String> map) {
        for (Map.Entry<Integer, String> m : map.entrySet()) {
            m.getKey();  
            m.getValue(); 
        }
    }

    public static void removeElements(LinkedHashMap<Integer, String> map, int count) {
        for (int i = 0; i < count; i++) {
            map.remove(i);
        }
    }
}
