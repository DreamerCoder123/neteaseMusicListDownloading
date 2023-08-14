# 一定要在main.exe所在文件夹下新建music文件夹，不然无法启动
# 使用步骤

一定要联网


1. 下载release中的最新版本的main.exe文件

2. 在main.exe文件夹内新建一个music文件夹

3. 输入歌曲id等待下载（一定要联网）
## FAQ
- 如何获取歌单的id？

    - iphone/android
        
        1.点开你想分享的歌单，点击转发后复制链接
        
        2.在浏览器中打开

        3.在连接url里含有“id=”后面的数字截取

    - windows
        
        1.在浏览器中打开歌单主页面
        
        2.将list_id后字段截取

## 我想自己搭建服务器！
- 你需要python基础 并有一定的捣鼓能力 这在多文件下载时速度会有很大提升！


1. 配置好网易云api服务，文档[在此](https://binaryify.github.io/NeteaseCloudMusicApi/)

1. 将源代码下载下来

2. 更改main.py中external后面的字符串（需要一定基础）

3. 运行并输入list_id
### 目前问题

1.在ios上可能无法在pythonIDE中正确运行

2.在ios上概率失败

3.可能会获取到重复歌曲（重复歌曲的下载会重复，但不会生成两个文件）

4.在歌单较大时可能会少歌


### 鸣谢
- autumnfish
- 陈
- 我自己
- binaryify
#### 尾声
    我爱大家
#####  最后的期许
```c
int getIQ(){
    return 0;
}
```
