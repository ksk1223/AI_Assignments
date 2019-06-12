# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:28:57 2019

@author: Intel
"""

import pandas as pd
empl=[{'year':1990,'name':"alice",'dept':"HR",'age':25,'salary':25000},
     {'year':1990,'name':"bob",'dept':"RD",'age':30,'salary':480000},
     {'year':1990,'name':"charlie",'dept':"admin",'age':40,'salary':55000},
     {'year':1991,'name':"alice",'dept':"HR",'age':26,'salary':52000},
     {'year':1991,'name':"bob",'dept':"RD",'age':26,'salary':50000},
     {'year':1991,'name':"charlie",'dept':"admin",'age':46,'salary':60000},
     {'year':1992,'name':"alice",'dept':"HR",'age':27,'salary':60000},
     {'year':1992,'name':"bob",'dept':"RD",'age':32,'salary':60000},
     {'year':1992,'name':"charlie",'dept':"admin",'age':28,'salary':60000}]

data=pd.DataFrame(empl)
data
data.groupby(['year'])['salary'].sum()
data.groupby(['name'])['salary'].sum()
data.groupby(['dept','year'])['salary'].sum()
