public class HelloWorld {
     private final static String VOWELS = "aeiouyAEIOUY";
     public static String interviewRecursionTest(String line) {
         if (line.length() == 1) {
             return "" + line.charAt(0);
         }

         int pivot = line.length() / 2;
         String left = line.substring(0, pivot);
         String right = line.substring(pivot);
         boolean needSep = VOWELS.indexOf(left.charAt(pivot-1)) != -1 
                        || VOWELS.indexOf(right.charAt(0)) != -1;

         return interviewRecursionTest(left) 
              + (needSep ? "*" : "") 
              + interviewRecursionTest(right);
     }
     public static void main(String []args){
        System.out.println(interviewRecursionTest("oab, friend"));
     }
}
