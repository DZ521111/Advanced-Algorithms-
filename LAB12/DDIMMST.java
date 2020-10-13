import java.io.*;
import java.util.*;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

class DDIMAXSPANNINGTREE 
{
    private static class points_of_dim
    {
        final private int[] x;
        private int w = 0;

        public points_of_dim(int[] x)
        {
            this.x = x;
        }

        public int w()
        {
            return (this.w);
        }

        public void set(int w)
        {
            this.w = w;
        }
    }

    private static int distance(points_of_dim p1, points_of_dim p2)
    {
        final int D = p1.x.length;
        int w = 0;
        for (int i = 0; i < D; i++)
        {
            w += Math.abs(p1.x[i] - p2.x[i]);
        }
        return (w);
    }

    public static void main(String[] args) throws Exception
    {
        final Field q = PriorityQueue.class.getDeclaredField("q");
        q.setAccessible(true);
        final Method sU = PriorityQueue.class.getDeclaredMethod("sU", int.class, Object.class);
        sU.setAccessible(true);
        final Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        final int N = sc.nextInt();
        final int D = sc.nextInt();
        final points_of_dim[] p = new points_of_dim[N];
        for (int n = 0; n < N; n++)
        {
            final int[] x = new int[D];
            for (int d = 0; d < D; d++)
            {
                x[d] = sc.nextInt();
            }
            p[n] = new points_of_dim(x);
        }
        int weight = 0;
        final PriorityQueue<points_of_dim> pq = new PriorityQueue<>(N, Comparator.comparingInt(points_of_dim::w).reversed());
        pq.addAll(Arrays.asList(p));
        final Object[] array = (Object[]) q.get(pq);
        while (!pq.isEmpty()) {
            final points_of_dim s = pq.remove();
            points_of_dim t = null;
            for (int n = 0; n < N && (t = (points_of_dim) array[n]) != null; n++)
            {
                final int w = distance(s, t);
                if (w > t.w)
                {
                    t.set(w);
                    sU.invoke(pq, n, t);
                }
            }
            weight += s.w;
        }
        System.out.println(weight);
        sc.close();
    }
}