# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 9:42
# @Author  : man.jiang
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import pymysql
import re
import time
from swagger_data import http_swagger

class DB_COM:
    def __init__(self):
        try:#连接数据库
            self.conn = pymysql.connect(host = '192.168.105.68', port = 23306,
                                   user = 'uat_test', passwd = 'Z6oXEIsg50qS',db = "ztest")
            self.cursor = self.conn.cursor()# 创建游标
        except pymysql.Error as e:#查看连接是否正常
            print("数据库连接信息报错")
            raise e
    #创建数据库
    def Create_database(self,database):
        sql = "show databases"
        self.cursor.execute(sql)#执行SQL
        databases = [self.cursor.fetchall()]#获取SQL结果
        databases_list = re.findall('(\'.*?\')', str(databases))
        databases_list = [re.sub("'", '', each) for each in databases_list]#提取数据
        if database in databases_list:
            print("{}数据库已存在".format(database))
        else:
            # 创建数据库
            sql = "CREATE DATABASE IF NOT EXISTS " + database
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                print("{}数据库创建成功".format(database))
            except Exception as e:#创建是否正常
                self.conn.rollback()
                print("数据库创建失败")
                raise e
        self.cursor.close()  # 关闭游标
        self.conn.close()  # 关闭连接
    #创建表单
    def Create_Table(self,table = "Test_Key" ):
        #查看库中是否存在表单
        sql = "show tables;"
        self.cursor.execute(sql)#执行SQL
        tables = [self.cursor.fetchall()]#获取SQL结果
        table_list = re.findall('(\'.*?\')', str(tables))
        table_list = [re.sub("'", '', each) for each in table_list]#提取数据
        if table not in table_list:
            print("{}表单不存在".format(table))
            sql_Create = '''CREATE TABLE {} (
                        `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
                        `operationId` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '操作ID',
                        `codea` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '系统',
                        `http_url` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '请求地址',
                        `http_mthod` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '请求方式',
                        `parame_data` varchar(5000) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '请求值',
                        `summary` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '说明',
                        `tags` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '标签',
                        `tags_des` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '标签说明',
                        `responses` varchar(5000) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '响应值',
                        `create_time` datetime(6) DEFAULT NULL COMMENT '创建时间',
                        `modify_time` datetime(6) DEFAULT NULL COMMENT '更新时间',
                        PRIMARY KEY (`id`,`operationId`)
                        ) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;'''.format(table)
            try:
                self.cursor.execute(sql_Create)#执行语句
                self.conn.commit()#提交
                print("表单创建成功")
            except Exception as e:
                self.conn.rollback()#回滚
                print("创建失败")
                raise e
        else:
            print("表单已存在")
        self.cursor.close()  # 关闭游标
        self.conn.close()  # 关闭连接
    #更新表单
    def Modify_Table(self,url,codea,table = "Test_Key"):
        sql_select = '''SELECT operationId FROM %s'''%(table)
        self.cursor.execute(sql_select)#执行SQL
        databases = [self.cursor.fetchall()]#获取SQL结果
        databases_list = re.findall('(\'.*?\')', str(databases))
        databases_list = [re.sub("'", '', each) for each in databases_list]#提取数据
        swagger_data = http_swagger.get_swagger(url).swagger_data()#拉取JSON数据
        localtime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        for db_data  in swagger_data:
            SQL = "insert into %s (codea,operationId,http_url,http_mthod,parame_data,summary,tags,tags_des,responses,create_time) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" \
                  % (table,codea, db_data["operationId"], db_data["http_url"], db_data["http_mthod"],
                     db_data["parame_data"], db_data["summary"], db_data["tags"], db_data["tags_des"],
                     db_data["responses"], localtime)
            if db_data["operationId"] not in databases_list :#取出需updat的数据
                try:
                    self.cursor.execute(SQL)  # 执行SQL
                    self.conn.commit()#提交，保存新建或者修改的数据
                    print("{}新增成功".format(db_data["operationId"]))
                except Exception as e:
                    self.conn.rollback()  # 回滚
                    print("{}创建失败".format(db_data["operationId"]))
                    raise e
            else:
                pass
        self.cursor.close()# 关闭游标
        self.conn.close()# 关闭连接


    def Select_Table(self,codea,operationId,table = "Test_Key"):
        SQL = "SELECT * from {} WHERE codea = '{}' and operationId ='{}'".format(table,codea,operationId)
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(SQL)  # 执行SQL
            databases = [cursor.fetchall()][0][0]  # 获取SQL结果字典格式(不提交，只接收查询的结果)
            return databases
        except Exception as e:
            self.conn.rollback()#回滚
            raise e
        finally:
            self.cursor.close()  # 关闭游标
            self.conn.close()  # 关闭连接

if __name__ == '__main__':
    url = "user/v2/api-docs?group=user"
    # test = DB().Select_Table("/user","creatAccountUsingPOST")
    # print(test)
    # print(test["id"])
    # test = DB().Create_Table()
    test2 = DB_COM().Modify_Table("/auth-internet/v2/api-docs?group=authority","auth-internet")





