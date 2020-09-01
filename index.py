"""
文件名：index2.0.py
功能：遍历当前目录下的文件名（统一格式），写到xlsx文件中
升级：增加了命令行参数，增加了-d模式遍历一级子目录，-D模式深度遍历子目录
"""
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, colors
import os
import sys


def raw_data_in_line(path):
    # 遍历文件名到列表中
    file_names = []
    for file in os.listdir(path):
        if file == '目录附件.xlsx':
            os.remove(path + "\\目录附件.xlsx")
        elif file == 'index.exe':
            pass
        else:
            file_names.append(os.path.splitext(file)[0])

    # 排序
    file_names.sort()

    # 组合每一行，输出为列表
    rows = []
    for count, name in enumerate(file_names, start=1):
        rows.append([count, name, " "])

    return rows


def to_xlsx(rows, path):
    # 创建xlsx文件
    wb = openpyxl.Workbook()
    sheet = wb.active
    # 表格名称
    sheet.title = '目录'

    # 首行为表头
    sheet['A1'] = '序号'
    sheet['B1'] = '项目内容'
    sheet['C1'] = '备注'
    # 写入每一行，并计算行数
    for count, row in enumerate(rows):
        sheet.append(row)
    line_num = count + 2

    # 设置格式
    side_set = Side(style='medium', color=colors.BLACK)
    for row in sheet['A1:C{}'.format(line_num)]:
        for cell in row:
            cell.font = Font(name='仿宋_GB2312', size=16)
            cell.alignment = Alignment(horizontal='center', vertical='center')
            cell.border = Border(left=side_set, right=side_set, top=side_set, bottom=side_set)
    # 设置列宽行高
    sheet.column_dimensions['A'].width = 7
    sheet.column_dimensions['B'].width = 100
    sheet.column_dimensions['C'].width = 7
    for i in range(line_num):
        sheet.row_dimensions[i + 1].height = 30

    # 保存
    wb.save(path + "\\目录附件.xlsx")
    print ('{} 生成目录附件！'.format(path))


if __name__ == '__main__':
    root_list = []
    if len(sys.argv) <= 1:
        exit()
    elif sys.argv[1] == "-d":
        dirss = []
        for home, dirs, files in os.walk(sys.argv[2], topdown=True):
            dirss.append(dirs)
        for dir_name in dirss[0]:
            new_dir = os.path.join(sys.argv[2], dir_name)
            root_list.append(new_dir)
    elif sys.argv[1] == "-D":
        for home, dirs, files in os.walk(sys.argv[2], topdown=True):
            if dirs:
                for dir_name in dirs:
                    new_dir = os.path.join(home, dir_name)
                    root_list.append(new_dir)
    else:
        for i in range(len(sys.argv)):
            if i == 0:
                continue
            root_list.append(sys.argv[i])

    for root in root_list:
        rows = raw_data_in_line(root)
        to_xlsx(rows, root)
