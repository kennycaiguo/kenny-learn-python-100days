### 计算最大公约数最常用的是**欧几里得算法（又称辗转相除法）**，其核心计算公式为： [[1](https://www.volcengine.com/article/130032), [2](https://baike.baidu.com/item/欧几里得算法/1647675), [3](https://cloud.tencent.com/developer/article/1467099), [4](https://zhuanlan.zhihu.com/p/691806667)]

\(\gcd (a,b)=\gcd (b,a\mod b)\)

*其中 \(\gcd \) 代表最大公约数，\(\mod \) 代表求余数。当 \(a \bmod b = 0\) 时，此时的 \(b\) 即为最大公约数。* [[1](https://www.volcengine.com/article/130032), [2](https://zhuanlan.zhihu.com/p/691806667), [3](https://cloud.tencent.com/developer/article/1467099)]

核心计算方法

1. 辗转相除法（欧几里得算法）

用较大数除以较小数，再用除数除以出现的余数，反复相除，直到余数为 \(0\) 为止。最后的除数就是最大公约数。 [[1](https://cloud.tencent.com/developer/article/1467099)]

- **示例**：求 \(24\) 和 \(36\) 的最大公约数
  1. \(36 \div 24 = 1 \dots \text{余数 } 12\)
  2. \(24 \div 12 = 2 \dots \text{余数 } 0\)
  3. 余数为 \(0\) 时，最后的除数是 \(12\)。因此，\(\gcd(36, 24) = 12\)。 [[1](https://developer.aliyun.com/article/1285037)]
- 关系公式法（与最小公倍数的关系）

若已知两个数 \(a\) 和 \(b\)，它们的最大公约数 \(\gcd(a, b)\) 与最小公倍数 \(\text{lcm}(a, b)\) 满足以下公式： [[1](https://www.cnblogs.com/perseveredonotgiveup/p/19045736)]

\(\gcd (a,b)\times \text{lcm}(a,b)=a\times b\)

- 因此求最大公约数的公式也可以转换为：
  \(\gcd (a,b)=\frac{a\times b}{\text{lcm}(a,b)}\)
- 质因数分解法

将每个数分别分解质因数，然后找出两数所有共有的质因数，将它们连乘起来。 [[1](https://zh.wikipedia.org/zh-cn/最大公因數)]

- #### **示例**：求 \(24\) 和 \(36\)

  - \(24 = 2 \times 2 \times 2 \times 3\)
  - \(36 = 2 \times 2 \times 3 \times 3\)
  - 共同的质因数是：\(2 \times 2 \times 3 = 12\)。

常用工具

如需快速验证，可直接使用内置支持的工具： [[1](https://support.microsoft.com/zh-cn/office/gcd-函数-d5107a51-69e3-461f-8e4c-ddfc21b5073a)]

- **Excel / Google Sheets**：使用 `=GCD(数值1, 数值2)`