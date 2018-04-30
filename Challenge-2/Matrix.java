public class Matrix {
    // Number of rows and columns of a matrix (game grid)
    static int rows, cols;
    // Ratio of mines to blanks
    static double ratio;

    // Initialize a matrix (game grid)
    public static boolean[][] initMatrix () {
        boolean[][] mines = new boolean[rows+2][cols+2];
        // Access each element in matrix laying mines
        for (int i=1; i<=rows; i++)
            for (int j=1; j<=cols; j++)
                mines[i][j] = (Math.random() < ratio);
        return mines;
    }

    // Print a matrix
    public static void printMatrix (boolean[][] mines) {
        for (int i=1; i<=rows; i++) {
            for (int j=1; j<=cols; j++) {
                if (mines[i][j])
                    System.out.print("* ");
                else
                    System.out.print(". ");
            }
            System.out.println();
        }
    }

    // Print a solution matrix
    public static void printSolution (boolean[][] mines) {
        // Initialize a solution matrix
        int[][] sol = new int[rows+2][cols+2];
        // For each element in matrix, search for adjacent mines
        for (int i=1; i<=rows; i++)
            for (int j=1; j<=cols; j++)
                for (int k=i-1; k<=i+1; k++)
                    for (int l=j-1; l<=j+1; l++)
                        if (mines[k][l])
                            sol[i][j]++;

        // Print a matrix
        for (int i=1; i<=rows; i++) {
            for (int j=1; j<=cols; j++) {
                if (mines[i][j])
                    System.out.print("* ");
                else
                    System.out.print(sol[i][j] + " ");
            }
            System.out.println();
        }
    }
}
