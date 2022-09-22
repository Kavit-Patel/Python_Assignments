# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:45:06 2022

@author: Kpatel
"""
# BELOW IS THE PYTHON.PY FILE

# def city_search(filename,city):
#     with open(filename,'r') as f:
#         # print(f.read())
#         l = (f.read()).split(' ')
#         for e in l:
#             if e == city:
#                 print(city,'is present in file')
#                 break
#         else:
#             print(city,'is not present')


# city_search('cities.txt','Ahmedabad')



import keyword

# print(keyword.kwlist)

with open('python.py','r') as f:
    l = (f.read()).split(' ')
    kw = keyword.kwlist
    for e in kw:
        for ee in l:
            if e == ee:
                print(e)