import time
from pyecharts import Pie, Bar, Gauge, EffectScatter, WordCloud, Map
import numpy as np
import pandas as pd
from functools import reduce
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
cities = list(company_data_info.company_address.unique())
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
work_list_sum = []
assessment_sum_list = []
mine_income_list = []
mine_rate_list = []
mine_turn_list = []
mine_depolit_list = []
#各个城市对应的商铺
for city in cities:
    #根据公司名查找公司中包含city的公司名字
    company_name = list(company_data_info[company_data_info['company_address'].str.contains(city)]['company_name'])
    work_list_sum.append(len(company_name))
    #客户对公司的印象
    assessment1 = list(company_data_info[company_data_info['company_address'].str.contains(city)]['ability_number1'])
    assessment2 = list(company_data_info[company_data_info['company_address'].str.contains(city)]['ability_number2'])
    assessment3 = list(company_data_info[company_data_info['company_address'].str.contains(city)]['ability_number3'])
    assessment_ = (assessment1+assessment2+assessment3)
    if len(assessment_) > 0 :
        assessment_all = ((reduce(lambda x,y:x+y,assessment_))/(len(assessment_)*3))
    else:
        assessment_all = 0
    assessment_sum_list.append(assessment_all)
    #公司的近三月收入
    company_incom_list = list(company_data_info[company_data_info['company_address'].str.contains(city)]['company_income'])
    mine_incom = (reduce(lambda x,y:x+y,company_incom_list))/len(company_incom_list)
    mine_income_list.append(mine_incom)
    #公司的好评率
    good_rate_list = list(company_data_info[company_data_info['company_address'].str.contains(city)]['good_rate'])
    mine_rate = (reduce(lambda x, y: x + y, good_rate_list)) / len(good_rate_list)
    mine_rate_list.append(mine_rate)
    #雇客的回头率
    head_turn_list = list(company_data_info[company_data_info['company_address'].str.contains(city)]['head_turn'])
    mine_turn = (reduce(lambda x, y: x + y, head_turn_list)) / len(head_turn_list)
    mine_turn_list.append(mine_turn)
bar = Bar("不同城市的"+'\n'+"各种平均值")
bar.add("城市公司个数",cities,work_list_sum,is_label_emphasis=True,is_datazoom_show=True)
bar.add("平均印象",cities,assessment_sum_list,is_label_emphasis=True,is_datazoom_show=True)
bar.add("平均收入",cities,mine_income_list,is_label_emphasis=True,is_datazoom_show=True)
bar.add("平均好评率",cities,mine_rate_list,is_label_emphasis=True,is_datazoom_show=True)
bar.add("平均雇客回头率",cities,mine_turn_list,is_label_emphasis=True,is_datazoom_show=True)
bar.render("good_mine_zhu.html")
