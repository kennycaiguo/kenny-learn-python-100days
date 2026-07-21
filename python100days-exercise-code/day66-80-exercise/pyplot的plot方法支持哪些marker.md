`pyplot.plot()` 支持丰富的标记（Marker）类型，主要分为以下几类： [[1](https://matplotlib.org/3.5.0/gallery/lines_bars_and_markers/marker_reference.html)]

**常见基础标记**

- `'o'`：圆圈 (Circle)
- `'s'`：正方形 (Square)
- `'p'`：五边形 (Pentagon)
- `'8'`：八边形 (Octagon)
- `'h'`：六角形1 (Hexagon1)
- `'H'`：六角形2 (Hexagon2)
- `'*'`：星形 (Star)
- `'D'`：菱形 (Diamond)
- `'d'`：瘦菱形 (Thin Diamond) [[1](https://matplotlib.org/3.1.0/api/markers_api.html)]

**多边形标记**

- `'^'`：上三角 (Triangle up)
- `'v'`：下三角 (Triangle down)
- `'<'`：左三角 (Triangle left)
- `'>'`：右三角 (Triangle right) [[1](https://matplotlib.org/3.1.0/api/markers_api.html)]

**直线与十字标记**

- `'+'`：加号 (Plus)
- `'x'`：乘号 (X)
- `'P'`：实心加号 (Filled Plus)
- `'X'`：实心乘号 (Filled X)
- `'|'`：垂直线 (Vline)
- `'_'`：水平线 (Hline) [[1](https://matplotlib.org/3.1.0/api/markers_api.html)]

**微小标记**

- `'.'`：点标记 (Point)
- `','`：像素标记 (Pixel) [[1](https://matplotlib.org/3.1.0/api/markers_api.html)]

此外，还支持无标记（`'None'`、`' '` 或 `''`）、TeX数学公式（如 `"$f$"`）、各类**刻度/插入符标记**（如 `4` 到 `11` 代表四方向的 Caret 符号），甚至自定义顶点坐标数组