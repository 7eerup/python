from openpyxl import Workbook

wb = Workbook()

default_sheet = wb['Sheet']
default_sheet.title = '시트1'

ws = wb.create_sheet('시트2')

print('모든 시트:', wb.sheetnames)

# 파일 저장
excel_file_path = "test.xlsx"
wb.save(excel_file_path)