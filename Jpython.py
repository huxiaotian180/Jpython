# -*-coding:utf-8-*-
import jpype
from jpype import *

# 获得默认jvm路径，即jvm.dll文件路径
jvmPath = jpype.getDefaultJVMPath()
print(jvmPath)
# java扩展包路径
ext_classpath = r'F:\Jpython\target\Jpython-1.0-SNAPSHOT.jar'
jvmArg = '-Djava.class.path=%s' % ext_classpath
print(jvmArg)
if not jpype.isJVMStarted():
    # 启动Java虚拟机
    jpype.startJVM(jvmPath, '-ea', jvmArg)

jpype.java.lang.System.out.println('Hello world!')

# 获取相应的Java类
javaClass = JClass("com.Javatest")
jd = javaClass()
jprint = java.lang.System.out.println
jprint(jd.run("waw"))
a = jd.testParam("test")
print("%s"% a)
shutdownJVM()
