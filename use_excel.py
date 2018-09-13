#read data from excel
import xlrd
data=xlrd.open_workbook('F:\开发中心年会节目.xlsx')
table=data.sheets()[0]
print(table.col_values(1))  #读取第二列
print(table.row_values(0))  #读取表头
#write data to excel
import xlwt
wb=xlwt.Workbook(encoding='ascii')
ws=wb.add_sheet('00')
ws.write(0,0,label='name')
ws.write(0,1,label='age')
ws.write(1,0,label='lilei')
ws.write(1,1,label='50')
wb.save('ws.xls')
