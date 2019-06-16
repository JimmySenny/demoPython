
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook();
sheet = workbook.active;

data = [
        [1001, '张三', '男', '13800001111' ],
        [1002, '李四', '男', '13800001112' ],
        [1003, '王麻子', '女', '13800001113' ]
        ];
sheet.append(['序号', '姓名', '性别', '电话号码' ] );

for row in data:
    sheet.append(row);

tab = Table( displayName='Table1', ref = 'A1:D4' );

tab.tableStyleInfo = TableStyleInfo(
        name = 'TableStyleMedium9', showFirstColumn = False,
        showLastColumn = False, showRowStripes = True, showColumnStripes = True);
sheet.add_table(tab);
workbook.save('./res/openyxl_tst.xlsx');

