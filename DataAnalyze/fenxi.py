import time

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from pandas import DataFrame
from sklearn.externals import joblib
company_data = pd.read_csv('company.csv')
comment_data = pd.read_csv('comments.csv')
company_data_info = company_data[['company_name','company_address','company_level','company_type','serviced_employer',
                                  'head_turn','good_rate','company_income','item_title','link_name','company_id',
                                  'ability_number1','ability_number2','ability_number3']]
#城市种类
city = company_data_info.company_address.unique()
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
for type in work_type:
    company = company_data_info[company_data_info['item_title'].str.contains(type)]
    shuzu = np.array([type,len(company)])
    work_list.append(shuzu)
print(work_list)