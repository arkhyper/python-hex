import os
input_path = r'C:\Users\xx\Desktop\333\Download\2'  #自动读取该目录下所有文件二进制格式
out_path=r"C:\\Users\\xx\\Desktop\\333\\Download\\3\\" #自动输出到该目录 转义
#out_path = os.listdir(out_path)
#本代码由于切去二进制文件开头部分，可以自由设定。
#环境：python3.9 20210901 win10 用go语言也可以代码也不多可以直接生成可执行文件，不过目前电脑没装环境
#GitHub：https://github.com/Tecbin/python-hex/
#bilibili：https://space.bilibili.com/506230167/article
#多些注释，好好学习，避免忘记。
#开源协议 ：GNU General Public License v3.0 


def Decode(f,fn):
    data_read = open(f, "rb") #只读
    out=out_path+fn+".m4a"  #其它文件同理
    data_write = open(out, "wb")
    a = 0
    for data in data_read:
        #类型不一样
        for dataByte in data:
            # 到这里也是每个字节的十进制操作了
            
            a= a + 1  #建议在内部循环里面写操作,python不吃++
            if a < 4097: #按需修改，使用查看hex，每行16位，假如左边为ff（256）X16=4096
                continue 
            else:
                data_write.write(bytes([dataByte]))
                #类型
    data_read.close()
    data_write.close()
 
def getFile(f):
    fsinfo = os.listdir(f)
    for fd in fsinfo:
        file_path = os.path.join(f, fd)
        if not os.path.isdir(file_path):
            print('文件路径: {}' .format(file_path)) #输出文件的路径
            print(fd)  #输出文件名
            Decode(file_path,fd)
        else:
            continue

getFile(input_path)
