import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class J1203423
{
    public static List<int[]> split(int[] sequence, int numberOfChunks) {
        int partitionSize = sequence.length / numberOfChunks;
        int rest = sequence.length % numberOfChunks;
        boolean includeRest = rest > 0 && rest <= partitionSize / 2;
        List<int[]> result = new ArrayList<>();
        int bound = sequence.length - (includeRest ? partitionSize : 0);

        for(int i = 0; i < bound; i += partitionSize) {
            int next_i = i + partitionSize;
            boolean isLastChunk = next_i >= bound;
            int[] chunk = Arrays.copyOfRange(sequence, i,
                  (isLastChunk && includeRest) // Включаем остаток в последний чанк?
                      ? sequence.length
                      : Math.min(sequence.length, next_i));

            result.add(chunk);
        }
        return result;
    }
    public static void main(String[] args) {
        int[] source = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14};
        List<int[]> chunks = split(source, 3);

        for(int i = 0; i < chunks.size(); i++) {
            System.out.println(Arrays.toString(chunks.get(i)));
        }
    }
}

/*

int partitionSize = files.length / numberOfChunks;
int rest = files.length % numberOfChunks;
boolean includeRest = rest < partitionSize / 2;
int bound = sequence.length - (includeRest ? partitionSize : 0);
for(int i = 0; i < bound; i += partitionSize){
    boolean isLastChunk = (i + partitionSize) >= bound;
    File[] chunk = Arrays.copyOfRange(files, i,
          (isLastChunk && includeRest) // Включаем остаток в последний чанк?
              ? files.length
              : Math.min(files.length, i + partitionSize));
    // ...
}

*/
