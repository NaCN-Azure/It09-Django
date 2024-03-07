## 一、项目说明
### 1. git建议
- 咱就不搞什么分支开发了，我git merge那边学的也不好，每次自己push的时候记得先pull一下最新的，然后push的时候给群里通个气
## 二、如何运行
进入根目录DjangoWork,然后在命令行运行
```doctest
python manage.py runserver
```

## 三、目录结构说明
### 1.application
这一部分是主要的开发区域，绝大部分python后端代码应该在这里完成
- 子目录migrations：这一部分是和数据库迁移有关的，目前为止用不到
- 子目录models：这一部分定义了和**数据库连通**的模型，是和数据库连接用的
- 子目录forms：这一部分定义了和**前端连通**的表单
- 子目录services：这一部分是对接models的**主要业务区**，其他的逻辑实现代码应该在这一层实现
- 子目录views：这一部分对接了**前端的request请求**，向前端调用以及url的调用
- admin.py：貌似是管理员用户管理，好像用不到
- apps.py：貌似也用不到
- tests.py：测试用到，估计项目也用不到
### 2.DjangoWork(次级目录) 
- asgi.py/wsgi.py: 这俩好像也用不上
- settings.py：整个项目的配置文件，一般来说不需要改太多，正常开发中也不需要太多改动他
- urls.py：配置前端网页的访问urls，可以类比为**前后端的接口**
### 3.static
- css：**存放前端的css文件**
- image：**存放用于装饰网页的图片/图标文件**
- js：**存放javaScript文件**
### 4.template
存放前端的静态html文件
### 5.根目录下的其他文件
- 1.txt：服务器mysql的密码，具体怎么访问去setting里看，或者下个navicat或者别的什么数据库管理的东西自己看，具体教程问GPT
- manage.py：用于启动Django服务的文件，不需要动
- nacnit.sql：咱们服务的SQL转储文件，这是备份

## 四、近期留言：
- user和application的视图完毕，调用因为缺少前端，post方法我没法正常测试，数据库连通应该是没问题的
- login和register稍微定义了一点点的逻辑，这个写login和register的人可以看看，尤其是register的，当然界面本质上只写了逻辑
- **_(:з」∠)_那个回头哈**，咱都把css和js尽量写status里（我承认我在register里也犯懒了），自己命个名比如index.css或者index.js啥的，然后拿来引用调用，现在看着是没多大事哈，要是全塞html里后面连通后就成灾难了，不然后面**血压会有点高**
