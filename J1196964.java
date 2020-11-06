class J1196964 {

    public static void swapChars(char[] s, int i, int j) {
        char t = s[i]; s[i] = s[j]; s[j] = t;
    }
    public static String reverseWord(String word) {
        char[] letters = word.toCharArray();
        for (int i = 0, j = letters.length - 1; i < j; ) {
            if (!Character.isAlphabetic(letters[i]))
                i++;
            else if (!Character.isAlphabetic(letters[j]))
                j--;
            else {
                swapChars(letters, i, j);
                i++;
                j--;
            }
        }
        return String.valueOf(letters);
    }

    interface SkipChar { public boolean is(char ch); }
    static String reverses(String str)
    {
        // SkipChar skipChar = (char ch) -> {return ch == ' ';};
        SkipChar skipChar = (char ch) -> {
            return !Character.isAlphabetic(ch) && ch != '\0';
        };

        char[] inputArray = str.toCharArray();
        char[] result = new char[inputArray.length];

        for (int i = 0; i < inputArray.length; i++) {
            if (skipChar.is(inputArray[i])) {
                result[i] = inputArray[i];
            }
        }

        int j = result.length - 1;
        for (int i = 0; i < inputArray.length; i++) {
            if (skipChar.is(inputArray[i])) continue;
            while (skipChar.is(result[j])) j--;

            result[j] = inputArray[i];
            j--;
        }

        return String.valueOf(result);
    }

    public static void main(String[] args) {
        String input = "«My Worlds,  Hello»";
        System.out.println(reverseWord(input));
        System.out.println(reverses(input));

        System.out.println(new StringBuilder().append(input).reverse().toString());
    }
}
