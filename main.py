# Calling module module_reference.a from main module
# There is no need to use sys module, because main module was placed at root package level
# from module_reference.a import A

# class D:
#     def function_c(self):
#         print("This is function_d from class D")

# A().function_a()


from databases.ddl_mysql import DatabaseDefinitionSQL
from databases.dml_mysql import DatabaseManipulationSQL

# 1. Create table python_table_1 if not exists
# DatabaseDefinitionSQL().create_table()

# 2. Insert data into table python_table_1
# DatabaseManipulationSQL().insert_data()

# 3. Select data
DatabaseManipulationSQL().select_data()