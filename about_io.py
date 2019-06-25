import pymysql
import json
import openpyxl

def save_xls():
    wb=openpyxl.Workbook()
    ws=wb.active
    # ws1=wb.create_sheet('Mysheet')
    result=read_json('result.json')
    for x,name in enumerate(result.keys()):
        ws.cell(column=2*x+1,row=1,value=name)
        for y,value in enumerate(result[name]):
            ws.cell(column=2*x+1,row=y+2,value=value)
    wb.save('result.xlsx')



def save_json(name,data):
    with open(name,'w') as f:
        json.dump(data,f)

def read_json(name):
    with open(name,'r') as f:
        result=json.load(f)
    return result
