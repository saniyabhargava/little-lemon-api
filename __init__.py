# allow Django's MySQL backend to work with PyMySQL
import pymysql
pymysql.install_as_MySQLdb()
