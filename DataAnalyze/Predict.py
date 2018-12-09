import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

company_data = pd.read_csv('company.csv')
type_data_all = pd.read_csv('datas.csv')
type_data = type_data_all[['work_type','work_price','company_area']]
def yuce(x,y):
    #找出所有的城市
    citys = type_data.company_area.unique()
    #找出所有的业务类型
    work_type = type_data.work_type.unique()
    def city_int(item):
        index = np.argwhere(citys == item)[0, 0]
        return index
    def type_int(item):
        index = np.argwhere(work_type == item)[0, 0]
        return index
    type_data['company_area'] = type_data['company_area'].map(city_int)
    type_data['work_type'] = type_data['work_type'].map(type_int)
    city_index = city_int(city)
    typex_index = type_int(work_types)
    #取出训练数据
    X_train = type_data[['work_type','company_area']]
    Y_train = type_data[['work_price']]
    KNN =KNeighborsClassifier(10)
    KNN.fit(X_train,Y_train.astype('int'))
    X_test = [[city_index,typex_index]]
    y_ = KNN.predict(X_test)[0]
    print('本市的此业务价格大概为：',y_,'元')
work_types = input("请输入业务类型:")
city = input("请输入城市:")
yuce(city,work_types)



