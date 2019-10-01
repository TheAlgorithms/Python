import pyodbc
import pandas


# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# server = 'tcp:myserver.database.windows.net' for a server over the internet
server = 'localhost\SQLEXPRESS'
database = 'master'
username = ''
password = ''
# Provide the file name. The complete path is required. Leave the r behind the ' as it is need to successfully upload.
filename = r'/Users/matthenley/Desktop/Houston Northwest UPDATED.xlsx'


# User will get an error if unable to connect to the database.
try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server +
                          ';DATABASE=' + database + ';UID=' + username + ';Trusted_Connection=yes;PWD=' + password)
except:
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    except Exception as e:
        print(e)
        exit(0)


def send_excel(data_frames):
    for num, (sheet, data_frame) in enumerate(data_frames.items()):
        # print(sheet, data_frame)
        # print(data_frame.columns)
        if not len(data_frame.columns):
            continue
        drop_columns = [x for x in data_frame.columns if 'Unnamed' not in x]
        for col in drop_columns:
            data_frame.drop([col], axis=1)

        # Table Names
        table_name = excel.sheet_names[num].split('.')

        if len(table_name) > 1:
            table_name = table_name[1].rstrip().lstrip()
        else:
            table_name = table_name[0].rstrip().lstrip()
        print('Processing Sheet:', num, '   Sheet Name:',
              excel.sheet_names[sheet], '   Table Name:', table_name)

        # Columns processing
        columns_str = ', ' .join(
            ['"%s" text' % x for x in data_frame.columns if 'Unnamed' not in x])
        delete_statement = """DROP TABLE IF EXISTS "{0}"; """.format(
            table_name)
        columns = [x for x in data_frame.columns if "Unnamed" not in x]
        columns_q = ','.join(['?' for x in columns])

        insert_statement = """CREATE TABLE "{0}" (
            {1}
        ) """.format(table_name, columns_str)

        cursor = cnxn.cursor()
        cursor.execute(delete_statement)
        cursor.execute(insert_statement)

        for index, row in data_frame.iterrows():
            cursor.execute("""INSERT INTO "{0}" VALUES ({1})""".format(table_name, columns_q),
                           [str(row[x]) if str(row[x]) !=
                            'nan' else None for x in columns]
                           )
        cursor.close()
        cnxn.commit()


file_type = None
if filename.endswith('.xls') or filename.endswith('.xlsx'):
    dataframes = {}
    excel = pandas.ExcelFile(filename)
    for sheet in range(len(excel.sheet_names)):
        dataframes[sheet] = pandas.read_excel(excel, sheet)
    file_type = 'excel'
    send_excel(dataframes)
else:
    print('Provide a valid Excel file')
    exit()
