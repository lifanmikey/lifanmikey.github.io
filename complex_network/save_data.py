# coding:utf-8
'''''
Created on 2016年1月22日
@author: cf
'''
import xlwt
import xlrd
workbook=xlwt.Workbook(encoding='utf-8')
booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
DATA=(('学号','姓名','年龄','性别','成绩'),
      ('1001','A','11','男','12'),
      ('1002','B','12','女','22'),
      ('1003','C','13','女','32'),
      ('1004','D','14','男','52'),
      )
for i,row in enumerate(DATA):
    for j,col in enumerate(row):
        booksheet.write(i,j,col)
workbook.save('grade.xls')
# workbook1 =xlrd.open_workbook('grade.xls')
# sheet2 = workbook1.sheet_by_name('Sheet 1')
# while True:
#     i = 0
#     if (sheet2.cell_value(i,0) != None):
#         i += 1
#     else:
#         booksheet.write(i, 0, 'sdf')
#         break
# workbook.save('grade.xls')
# def save_data(AUC):
#     workbook = xlwt.Workbook(encoding='utf-8')
#     booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
#     for i in range():
#         if (booksheet.cell(i,0).value != None):
#             i += 1
#         else:
#             booksheet.write(i, 0, AUC)
#     workbook.save('AUC_result.xls')