import java.util.*;
import java.awt.Point;

public class Algorithm_patrol {
    // 2点間の距離を計算
    static double distancePoint(Point p, Point q) {
        // return Math.sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y));
        return p.distance(q);
    }

    // 経路の距離
    static double distanceRoute(int n, List<Point> route) {
        double sum = 0;
        for (int i = 0; i < n - 1; i++) {
            sum += distancePoint(route.get(i), route.get(i + 1));
        }
        return sum;
    }

    // 経路の表示
    static void info(int n, List<Point> route) {
        for (int i = 0; i < n; i++) {
            System.out.println(route.get(i).x + " " + route.get(i).y);
        }
        System.out.println("distance: " + distanceRoute(n, route));
    }

    // pointsを並び替えた経路
    static List<Point> tsp(int n, List<Point> points) {
        List<Point> resultRoute = new ArrayList<>(); // 結果を保存
        List<Point> openPoints = new ArrayList<>(points); // 未訪問の点の一覧
        resultRoute.add(openPoints.remove(0)); // 最初に加えてある(0,0)の点を候補から取り除いて現在地点aに代入する
        while (!openPoints.isEmpty()) {
            // a:今いる点, b:移動候補の点
            Point a = resultRoute.get(resultRoute.size() - 1);
            Point b = null;
            // 全ての未訪問の点について、aとの距離を調べ、最も距離の近い点をbとする
            for (Point p : openPoints) {
                if (b == null || distancePoint(a, p) < distancePoint(a, b)) {
                    b = p;
                }
            }
            resultRoute.add(b);
            openPoints.remove(b);
        }
        return resultRoute;
    }

    public static void main(String[] args) {
        // 入力処理
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Point> points = new ArrayList<>();
        points.add(new Point(0, 0)); // 最初の点として(0,0)を追加
        for (int i = 0; i < n; i++) {
            Point p = new Point(scanner.nextInt(), scanner.nextInt());
            points.add(p);
        }

        // 座標を並べ替えた経路を作る
        // List<Point> resultRoute = tsp(n + 1, points); // 貪欲法
        List<Point> resultRoute = points; // ダイレクト

        // 経路を表示する
        info(n + 1, resultRoute);
        // - 続くn個の点を1行ずつ表示

        // Point a = new Point(0, 0);
        // Point b = new Point(3, 4);
        // System.out.println("a: " + a.x + " " + a.y);
        // System.out.println("b: " + b.x + " " + b.y);
        // System.out.println(distancePoint(a, b));
        // List<Point> route = new ArrayList<Point>();
        // route.add(a);
        // route.add(b);
        // route.add(new Point(8, 1));
        // info(route.size(), route);
    }
}
