import pandas
import pyodbc

server = "DESKTOP-NAA91LO"
database = "Restored_Bayer_v3"
username = ""
password = ""
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' f'SERVER={server};' f'DATABASE={database};' 'Trusted_Connection=yes;')
query = "select * from [Employees] where Last_Name like 'Luk%'"
df = pandas.read_sql(query, conn)
output_file = "results_database.xlsx"
df.to_excel(output_file, index = False)
print(df)
conn.close()