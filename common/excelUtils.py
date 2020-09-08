import xlrd
from common.pathUtils import PathUtils
from common.logUtils import Logger

# 日志实例
log = Logger(logger='readExcel').getlog()


class ReadExcelUtils:
    file_name = PathUtils().testcasedata_path + '\\testCase.xlsx'

    # 初始化一个excel对象wb和sheet对象ws
    def __init__(self, sheet_name):
        try:
            self.wb = xlrd.open_workbook(self.file_name)
            self.ws = self.wb.sheet_by_name(sheet_name)
            log.info('打开文件:' + self.file_name + '成功！')
        except FileNotFoundError as e:
            log.error('未找到文件:' + self.file_name + '！')

    # 处理表单中的合并单元格信息
    def _getMergedCellValue(self, row_index, col_index):
        mergerd_info = self.ws.merged_cells
        value = self.ws.cell_value(row_index, col_index)
        # 判断当前单元格是否属于合并单元格，是则返回合并单元格的值，否则返回正常读取到的单元格的值
        for(rlow, rhigh, clow, chigh) in mergerd_info:
            if rlow <= row_index < rhigh:
                if clow <= col_index < chigh:
                    value = self.ws.cell_value(rlow, clow)
                    break
                else:
                    value = self.ws.cell_value(row_index, col_index)
            else:
                value = self.ws.cell_value(row_index, col_index)
        return value

    # 读取excel数据
    def get_data(self):
        data_list = []
        for row in range(1, self.ws.nrows):
            data_rows = {}
            for col in range(0, self.ws.ncols):
                the_key = str(self.ws.cell_value(0, col))
                data_rows[the_key] = self._getMergedCellValue(row, col)
            data_list.append(data_rows)
        return data_list


if __name__ == '__main__':
    ws = ReadExcelUtils('Operation')
    print(ws.get_data())
