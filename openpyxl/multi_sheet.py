from openpyxl import Workbook

wb = Workbook()

# 멀티 시트 생성
sheets = ['하나증권', '교보증권', 'LS증권', '한국투자증권', 'KB증권']
for sheet_name in sheets:
    wb.create_sheet(title=sheet_name)

# 파일 저장
excel_file_path = "multisheet.xlsx" # Excel 파일 이름
wb.save(excel_file_path)