# dify_plugins
Self deveoped Dify plugin
# 字符串类型转换
Dify的插件输出都是字符串，转给条件组件的时候，有时想根据数字范围比较，要加个代码插件来转换下，有时代码运行时不行，还被逼着用大模型的参数提取器去做，太难受了。
于是自己写了个，输入字符串，会转成int，float，eval计算表达式，根据需要，下一个节点按需选择输出变量即可
![image](https://github.com/user-attachments/assets/7f3f8c77-798f-4a0a-89f8-0773781bf962)
![image](https://github.com/user-attachments/assets/4e10d2ab-7bdd-4e6b-beba-7598c62c4d4d)

