import os
import subprocess
import time

files = []
def DirAll(pathName):
    if os.path.exists(pathName):
        fileList = os.listdir(pathName);
        for f in fileList:
            if f == "$RECYCLE.BIN" or f == "System Volume Information":
                continue;
            f = os.path.join(pathName, f);
            if os.path.isdir(f):
                DirAll(f);
            else:
                dirName = os.path.dirname(f);
                baseName = os.path.basename(f);
                if dirName.endswith(os.sep):
                    files.append(dirName + baseName);
                else:
                    files.append(dirName + os.sep + baseName);

def main():
    status = False
    count = 0
    str_error = ''
    password_fist = []
    password = []
    pathname = 'D:\\pytest\\zip1'
    DirAll(pathname);
    print(files)
    #读取字典
    pswf = open('D:\\pytest\\zidian.txt',encoding= 'utf-8')
    for line in pswf.readlines():
        password_fist.append(line.strip('\n'))

    for i in password_fist:
        if not i in password:
            password.append(i)

    for i in range(len(files)):
        filename = files[i]#文件路径
        list_rsplit = filename.rsplit('.', 1) # 从右侧开始以.号切片1次
        filedir = list_rsplit[0]#解压路径.replace('\\','/')
        print("正在解压："+filename)
        for i in range(len(password)):
            thispassword = password[i]

            command = '7z x ' +'"'+ filename +'"' + ' -p'+ thispassword +' -o'+'"'+ filedir +'"' + ' -y'
            '''if os.system(command) == 0:
                print("密码为：" + thispassword)'''
            child = subprocess.call(command)
            # os.popen(command)#这个也可以用,但是不好监控解压状态
            if child == 0:
                count +=1
                print('文件：'+filename +" 密码为：" + thispassword)
                status = True
                break


        if status == False:
            str_error += filename+'\n'
            print('文件：'+filename +'解压错误')
        time.sleep(3)
    print('文件总数：'+str(len(files))
          +'\n已解压：'+str(count)
          +'\n错误文件：\n'+str_error)

if __name__ == "__main__":
    main()