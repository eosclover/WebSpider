# # import csv
# #
# # with open('data.csv','w') as csvfile:
# #     #默认逗号分隔符
# #     writer=csv.writer(csvfile)
# #
# #     #修改列与列之间的分隔符
# #     # writer=csv.writer(csvfile,delimiter='')
# #
# #     #每次写一行
# #     writer.writerow(['id','name','age'])
# #     writer.writerow(['1001','Mike','23'])
# #     writer.writerow(['1002','Alice','12'])
# #     writer.writerow(['1003','clover','18'])
# #     #每次写多行
# #
# #     writer.writerows([['1001','Mike','23'],['1002','Alice','12'],['1003','clover','18']]
# #
#
# # import csv
# # with open('data.csv','w') as csvfile:
# #     # 头信息
# #     fieldnames=['id','name','age']
# #     #字典写入对象  dictionary
# #     writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
# #     writer.writeheader()
# #     #一行一行的写  字典类型
# #     writer.writerow({'id':'1001','name':'MIke','age':'20'})
# #     writer.writerow({'id':'1002','name':'Alice', 'age': '12'})
# #     writer.writerow({'id':'1003','name':'Clover', 'age': '18'})
#
#
#
# # 写入文件的内容包含中文时，要考虑编码的问题
# import csv
# with open ('data.csv','a',encoding='utf-8') as csvfile:
#     filednames=['id','name','age']
#     writer=csv.DictWriter(csvfile,fieldnames=filednames)
#     writer.writerow({'id':'1004','name':'豆豆王','age':'23'})
#
#
#

#
# #读取CSV文件的内容
# import csv
# with open('data.csv','r',encoding='utf-8') as csvfile:
#     reader=csv.reader(csvfile)
#     for row in reader:
#         print(row)


#利用pandas读取csv文件
import pandas as pd
df=pd.read_csv('data.csv')
print(df)





