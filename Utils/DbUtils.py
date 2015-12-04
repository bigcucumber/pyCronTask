__author__ = 'Administrator'

import  MySQLdb

class DbUtils:

    connector = None

    @staticmethod
    def getConnection():
        if not DbUtils.connector:
            DbUtils.connector = MySQLdb.connect(host="localhost", user="root", passwd="luowen", port=3306, db="mms_new")
        return DbUtils.connector

    @staticmethod
    def fetchOne(sql, bindValue = None, assoc = True):
        connector = DbUtils.getConnection()
        if assoc:
            cursorObj = connector.cursor(MySQLdb.cursors.DictCursor)
        else:
            cursorObj = connector.cursor()

        if bindValue:
            sql = sql.format(bindValue)
        cursorObj.execute(sql)

        return cursorObj.fetchone()

    @staticmethod
    def fetchMany(sql, bindValue = None, size = None, assoc = True):
        connector = DbUtils.getConnection()

        if assoc:
            cursorObj = connector.cursor(MySQLdb.cursors.DictCursor)
        else:
            cursorObj = connector.cursor()

        if bindValue:
            sql.format(bindValue)

        cursorObj.execute(sql)

        if size:
            return cursorObj.fetchmany(size)
        return cursorObj.fetchmany()

    @staticmethod
    def fetchAll(sql, bindValue = None, assoc = True):
        connector = DbUtils.getConnection()
        if assoc:
            cursorObj = connector.cursor(MySQLdb.cursors.DictCursor)
        else:
            cursorObj = connector.cursor()

        if bindValue:
            sql = sql.format(bindValue)
        cursorObj.execute(sql)

        return cursorObj.fetchall()

    @staticmethod
    def closeConnection():
        connector = DbUtils.getConnection()
        return connector.close()

    @staticmethod
    def insert(sql):
        connector = DbUtils.getConnection()
        cursorObj = connector.cursor()
        cursorObj.execute(sql)

        sql = "select last_insert_id()"
        return DbUtils.fetchOne(sql, None, False)



"""
sql = "select * from pc_users limit {0}"

resultSet = DbUtils.fetchOne(sql, 2, False)
print(resultSet)
"""

"""
sql = "select * from pc_users"

resultSet = DbUtils.fetchMany(sql, None)
print(len(resultSet))
"""

sql = "select * from pc_userxxs"
resultSet = DbUtils.fetchAll(sql)
print(len(resultSet))

