from pyecharts import options as opts
#from pyecharts.charts import Map
from pyecharts.charts import Map
import pandas as pd

FileNameStr = 'dataset.csv'
# 读取csv，以第二行作为表头
df = pd.read_csv(FileNameStr, encoding='utf-8', header=1)
# 新建列表，并将已删除'万'字的数据存入
num_2000 = []
for row in df['2000年']:
    num_2000.append(row)


map2 = Map()
map2.set_global_opts(
    title_opts=opts.TitleOpts(title="Eco-efficiency of natural gas consumption "),
    visualmap_opts=opts.VisualMapOpts(
        # 由于数据分布较为集中，线性无法形象反映，故设置为分段显示
        is_piecewise=True,
        # 自定义分段区间、描述和颜色
        pieces=[{"min": 0, "max": 0.2, "label": "≤0.2", "color": "#e0e9bb"},
                {"min": 0.2, "max": 0.4, "label": "0.2-0.4", "color": "#eee8aa"},
                {"min": 0.4, "max": 0.6, "label": "0.4-0.6", "color": "#c3d47c"},
                {"min": 0.6, "max": 0.8, "label": "0.6-0.8", "color": "#7ab8cc"},
                {"min": 0.8,  "label":" ＞0.8", "color": "#008b8b"},
                #  不指定 max，表示 max 为无穷大
                ]
    )
)
map2.add(
"in 2000",
    [list(z) for z in zip(list(df['省/市']), list(df['2000年']))],
    "china",
    is_map_symbol_show=False  # 不显示省会的小红点
)
map2.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
map2.render("map2.html")

