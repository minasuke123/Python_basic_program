import matplotlib.pyplot as plt
import numpy as np

#sin関数
t=np.arange(0,10,0.1) # x軸の範囲を0~10, 0.1刻みでリスト型で設定
y=np.sin(t) # 軸を変数とした関数を設定
y1=np.cos(t)

#グラフの作成
plt.plot(t,y)
plt.plot(t,y1,linestyle="dashed")
plt.axhline(0.5, ls="-.", color="magenta") # 水平線を引く
plt.axvline(5, ls="dotted", color="red") # 垂直線を引く

#軸ラベル
plt.ylabel('sin [mm]',fontsize=14)
plt.style.use('ggplot')
#タイトル
#plt.title('test')

plt.show() # グラフを表示する
