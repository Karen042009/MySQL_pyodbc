import pyodbc


conn = pyodbc.connect(
    "DRIVER={MySQL ODBC 9.3 Unicode Driver};"
    "SERVER=localhost;"
    "PORT=3306;"
    "DATABASE=test_python;"
    "USER=root;"
    "PASSWORD=KarenAni474;"
    "charset=utf8mb4;"
)


def show_tables():
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    cursor.close()


def run():
    while True:
        text = input("Select, Truncate, Insert, Delete, Drop, Create: ")

        if text == "Insert":
            show_tables()
            table_name = input("Enter table name: ")
            cursor = conn.cursor()
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()
            column_names = []
            for column in columns:
                column_names.append(column[0])
            if "id" in column_names:
                column_names.remove("id")
            values = []
            for column in column_names:
                value = input(f"Enter {column}: ")
                values.append(value)
            placeholders = ", ".join(["?"] * len(values))
            cursor.execute(
                f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders})",
                tuple(values),
            )
            conn.commit()
            cursor.close()

        elif text == "Delete":
            show_tables()
            name = input("Table name: ")
            id = int(input("Enter id: "))
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {name} WHERE id = {id}")
            conn.commit()
            cursor.close()

        elif text == "Create":
            table_name = input("Table name: ")
            cursor = conn.cursor()
            command = f"CREATE TABLE `{table_name}` ("
            num_columns = int(input("Columns: "))
            for _ in range(num_columns):
                column_name = input("Column name: ")
                data_type = input(f"Datatype (INT, VARCHAR) for '{column_name}': ")
                command += f"`{column_name}` {data_type}, "
            command = command.rstrip(", ") + ");"
            cursor.execute(command)
            conn.commit()
            cursor.close()

        elif text == "Select":
            show_tables()
            cursor = conn.cursor()
            table_name = input("Enter table name: ")
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            str_ = ""
            for row in rows:
                for i in row:
                    str_ += str(i) + " "
                str_ += "\n"
            print(str_)

        elif text == "Truncate":
            show_tables()
            cursor = conn.cursor()
            name = input("Table name: ")
            cursor.execute(f"TRUNCATE TABLE {name};")
            conn.commit()
            cursor.close()

        elif text == "Drop":
            table_name = input("Table name: ")
            cursor = conn.cursor()
            command = f"DROP TABLE IF EXISTS {table_name};"
            cursor.execute(command)
            conn.commit()
            cursor.close()

        elif text == "Select":
            show_tables()
            cursor = conn.cursor()
            table_name = input("Enter table name: ")
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            str_ = ""
            for row in rows:
                for i in row:
                    str_ += str(i) + " "
                str_ += "\n"
            print(str_)


run()
conn.close()
