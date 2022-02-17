"""
*********Python可视化工具Plotly的应用教程
环境:Jupyter Notebook
plotly内置了数据集，方便大家不受数据分析思路的背景下，练手用
"""
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import numpy as np

df = px.data.gapminder()
df_2007 = df[df['year'] == 2007]

# 旭日图
def Risingsun():
    px.sunburst(df_2007,path=['continent', 'country'],#指定路径：从洲到国家
                values='pop', #数据大小,人口数
                color='lifeExp',#颜色
                hover_data=['iso_alpha'])#显示数据
