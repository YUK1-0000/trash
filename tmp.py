import numpy as np
import matplotlib.pyplot as plt

def plot_function(func, x_min, x_max, num_points=1000):
    # x座標の値を生成
    x_values = np.linspace(x_min, x_max, num=num_points)

    # y座標の値を計算
    y_values = func(x_values)

    # グラフを描画
    plt.plot(x_values, y_values)

    # グラフのタイトルを設定
    plt.title("Graph of {}".format(func.__name__))

    # x軸のラベルを設定
    plt.xlabel("x")

    # y軸のラベルを設定
    plt.ylabel("y")

    # グラフを表示
    plt.show()

# 例： f(x) = x^2 を描画する場合
def f(x):
    return x ** 2

plot_function(f, -10, 10)
