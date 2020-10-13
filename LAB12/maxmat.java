import java.util.*;

class maxmat {

    private static int sum, ans;

    private static void solve(int[][] mat, boolean[] visited, int n, int m, int curr) {
        if (curr == n) {
            ans = Math.max(ans, sum);
            return;
        }

        for (int i = 0; i < m; i++) {
            if (visited[i] == false) {
                visited[i] = true;
                sum += mat[curr][i];
                solve(mat, visited, n, m, curr + 1);
                sum -= mat[curr][i];
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(); // n-rows m-cols

        int[][] mat = new int[n][m];
        sum = 0;
        ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                mat[i][j] = sc.nextInt();
            }
        }

        boolean[] visited = new boolean[m];
        solve(mat, visited, n, m, 0);
        System.out.println(ans);
    }
}
