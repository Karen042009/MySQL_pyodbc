# MySQL_pyodbc
## Create databas and install pyodbc
```
Open cmd
pip install pyodbc
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql" -u your_name -p
Enter password: your_password
CREATE DATABAS name;
exit
```
## We exchange data with you.
```
conn = pyodbc.connect(
    "DRIVER={...};"
    "SERVER=...;"
    "PORT=...;"
    "DATABASE=...;"
    "USER=...;"
    "PASSWORD=...;"
    "charset=utf8mb4;"
)
```
## Run python file
