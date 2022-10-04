#   _*_coding=utf-8_*_
import xlwt
import xlrd


class WriteExcel:
    def __init__(self, sheet_name=None):
        """初始化写表格对象

        :param sheet_name: 写表格的sheet名，默认为1
        """
        if sheet_name:
            self.sheetname = sheet_name
        else:
            self.sheetname = "1"
        self.workbook = xlwt.Workbook()
        self.worksheet = self.workbook.add_sheet(sheetname=self.sheetname)

    def write_values(self, row, col, values):
        """向目标sheet的某个行列写入值

        :param row: 目标行
        :param col: 目标列
        :param values: 想要写入的值
        """
        self.worksheet.write(row, col, values)

    def save_file(self, filename=None):
        """保存表格

        :param filename: 保存的文件名
        """
        if filename:
            self.filename = filename
        else:
            self.filename = "test.xls"
        self.workbook.save(self.filename)


class OpenExcel:

    def __init__(self, file_name=None, sheet_id=None):
        """初始化读取Excel表格

        :param file_name: 需要读取的表格名
        :param sheet_id: 需要读取的表格sheet
        """
        if file_name:

            self.file_name = file_name

            self.sheet_id = sheet_id

        else:

            self.file_name = 'static/database.xlsx'

            self.sheet_id = 0

        self.data = self.get_data()

    def get_data(self):
        """读取表格数据

        :return: 返回读取的表格数据
        """
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """读取表格总行数

        :return: 返回表格总行数
        """
        tables = self.data
        return tables.nrows

    def get_cols(self):
        """读取表格总行数

        :return: 返回表格总列数
        """
        tables = self.data
        return tables.ncols


    def get_value(self, row, col):
        """读取表格中具体的行、列对应的值

        :param row: 目标行
        :param col: 目标列
        :return: 返回目标行、列的值
        """
        return self.data.cell_value(row, col)


if __name__ == '__main__':
    openexcel = OpenExcel(file_name="static/database.xlsx",sheet_id=0)
    print (openexcel.get_lines())
    write_excel = WriteExcel()
    for j in range(0,openexcel.get_cols()):
        for i in range(0,openexcel.get_lines()):
            write_excel.write_values(i,j,openexcel.get_value(i,j))
    write_excel.write_values(100,100,"我是谁")




    write_excel.save_file()

