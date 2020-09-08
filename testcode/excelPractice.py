import xlrd
from common.pathUtils import PathUtils

wb = xlrd.open_workbook(PathUtils().testcasedata_path + '\\testCase.xlsx')
ws = wb.sheet_by_name('Operation')

merger_info = ws.merged_cells
print(merger_info)
