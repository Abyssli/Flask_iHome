#coding:utf-8
from ihome import create_app,db
from flask_script import Manager
# 迁移的执行者,迁移的解析人员
from flask_migrate import Migrate,MigrateCommand

# 创建flask的应用对象
app = create_app("develop")

manger = Manager(app)
Migrate(app,db)
manger.add_command("db",MigrateCommand)



if __name__ == "__main__":
    manger.run()