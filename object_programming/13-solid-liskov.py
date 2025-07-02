"""
if S is a subtype of T,
then objects of type S without altering any of the desirable properties of the program.
"""

# example of correct


class ConnectionDB:
    def connect(self):
        print("Connection success")


class SqlRepository(ConnectionDB):
    def select(self):
        print("select * from database")


class NoSqlRepository(ConnectionDB):
    def select(self):
        print("select * from NOSQL")


class DBHandler:  # this broke liskov rule, dois not have select statement to replacement class.
    def alter_table(self):
        print("alter table TABLE")
