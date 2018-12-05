import time
from pyecharts import Pie, Bar, Gauge, EffectScatter, WordCloud, Map
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from pandas import DataFrame
from sklearn.externals import joblib
company_data = pd.read_csv('company.csv')
comment_data = pd.read_csv('comments.csv')
#取出能用到的数据
company_data_info = company_data[['company_name','company_address','company_level','company_type','serviced_employer',
                                  'head_turn','good_rate','company_income','item_title','link_name','company_id',
                                  'ability_number1','ability_number2','ability_number3']]
#城市种类
cities = company_data_info.company_address.unique()
#公司等级
level = company_data_info.company_level.unique()
#业务类型
work_type = company_data_info.item_title.unique()
#服务雇主数量
server_num = company_data_info.serviced_employer.unique()
#雇主回头率
head_turn = company_data_info.head_turn.unique()
#好评率
good_tare = company_data_info.good_rate.unique()
work_list = []
for city in cities:
    company_name = list(company_data_info[company_data_info['company_name'].str.contains(city)]['company_name'])
    work_list.append(company_name)

print(cities[10])
print(work_list[10])
# map = Map("Map 结合 city 示例图",width=1200,height=600)
# map.add("",cities,work_list,maptype='china',is_visualmap=True,visual_text_color='#000')
# map.render('map.html')