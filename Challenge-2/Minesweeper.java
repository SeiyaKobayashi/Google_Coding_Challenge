public class Minesweeper {
    public static void main (String[] args) {
        // Take inputs from user
        if (args[0] != null && args[1] != null && args[2] != null) {
            Matrix.rows = Integer.parseInt(args[0]);
            Matrix.cols = Integer.parseInt(args[1]);
            Matrix.ratio = Double.parseDouble(args[2]);
        } else {
            System.out.println("You have to pass three arguments: [rows columns ratio]\n\te.g. 5 5 0.3");
        }

        boolean[][] mines = Matrix.initMatrix();
        System.out.println("\nGenerating a new game grid...\n");
        Matrix.printMatrix(mines);
        System.out.println();
        System.out.println("Here's the solution!\n");
        Matrix.printSolution(mines);
        System.out.println();
    }
}
