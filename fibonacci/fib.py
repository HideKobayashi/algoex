class Fib:
    def __init__(self) -> None:
        # フィボナッチ数の結果をメモするためのグローバル変数
        self.fib_list_global = [0] * 101

    def fib1(self, n: int) -> int:
        """n番目のFibonacci数を再帰関数で計算する"""
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib1(n - 1) + self.fib1(n - 2)

    def fib2(self, n: int) -> int:
        """n番目のFibonacci数を再帰関数で計算する

        メモ化して一度計算した値はメモして再利用する方式
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            # メモに結果がない場合のみ再帰で計算
            if self.fib_list_global[n] == 0:
                self.fib_list_global[n] = self.fib2(n - 1) + self.fib2(n - 2)

            # print("fib_list_global:", self.fib_list_global)
            return self.fib_list_global[n]

    def fib3(self, n: int) -> int:
        """n番目のFibonacci数をボトムアップで計算する"""
        fib_list = [0] * (n + 1)
        fib_list[1] = 1

        # 2番目からn番目の値を順番に求めていく
        for i in range(2, n + 1):
            fib_list[i] = fib_list[i - 1] + fib_list[i - 2]

        # print("fib_list:", fib_list)
        return fib_list[n]

    def fibx(self, n: int) -> int:
        """n番目のFibonacci数をボトムアップで計算する別の方法"""
        a, b = 0, 1
        fib_list = [a, b]
        for k in range(2, n + 1):
            a, b = b, a + b
            fib_list.append(b)
            # print(f"{k} {b}")
        # print(fib_list)
        return b
