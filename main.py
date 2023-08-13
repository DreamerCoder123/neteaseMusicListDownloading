import requests
import time
import os
def breath(msg):
    print(msg)
    time.sleep(1)
try:
    offset=0
    externalServer="https://autumnfish.cn"
    songs_name=[]
    songs_id=[]
    total_bytes=0
    success=0
    failed=0
    ##val area
    def download(song_id,song_name):
        global total_bytes,success
        getresult=requests.get(externalServer+"/song/url/v1?id="+str(song_id)+"&level=standard").json()
        if getresult['data'][0]['fee']==1:
            print(song_name+"下载失败，为vip歌曲")
            return
        res=getresult['data'][0]["url"]
        mp3_byte=requests.get(res).content
        files=open("./music/"+song_name+".mp3","wb")
        files.write(mp3_byte)
        total_bytes+=int(getresult["data"][0]["size"])/1024/1024
        print(song_name+"下载成功，家里已经用了"+str(round(total_bytes))+"MB哦")
        success+=1
    ##def area
    print("\n我们强烈建议自己创建服务器而不是使用公共服务器!!!!\n感谢autumnfish提供的网易云api\n学习交流使用，请在24小时内删除！\n\n请等待5s")
    time.sleep(5)
    print("你回来了！呃呃呃，虽然我什么都不知道，但是还请多多指教！首先我会检查你的网络连接(✿◠‿◠)")
    try:
        internetCheck=requests.get(externalServer).text
    except:
        print("请检查网络连接")
    print("网络连接畅通 朝着下一步进发ヾ(≧▽≦*)o")
    list_id=input("请输入歌曲id，这样才能继续哦")
    print("收到了呢XD")
    result=requests.get(externalServer+"/playlist/track/all",json={
        "id":int(list_id),
        "limit":100,
        "offset":offset
    }).json()
    if result["code"]==200:
        print("成功了呢！快看，快看，马上就要下载了！！！")
        while len(result["songs"])!=0:
            result=requests.get(externalServer+"/playlist/track/all?offset="+str(offset)+"&id="+str(list_id)+"&limit=100").json()
            for i in range(len(result["songs"])):
                songs_id.append(result["songs"][i]["id"])
                songs_name.append(result["songs"][i]["name"])
                print("我看到你了'"+songs_name[i]+"'抓到了就别想跑了哦")
            offset=100+offset
        print("看~我这次抓到了"+str(len(songs_id))+"，够听了吧。。")
        if input("还要继续吗，下一步将开始下载....？(y/n)")=="y":
                for countdown in range(0,5):
                    os.system("cls")
                    print("下载将在"+str((5-countdown))+"s 后进行，请稍等，退出请按下ctrl+c，下载过程中请不要断电!!\n需要的磁盘空间（不精确）:"+str(len(songs_id)*10)+"MB")
                    time.sleep(1)
                for x in range(0,len(songs_name)):
                    try:
                        download(songs_id[x],songs_name[x])
                    except:
                        print(songs_name[x]+"   下载失败了，是我的能力还不够吗，呜呜呜")
                        failed+=1
                print("下载完成！\n成功"+str(success)+"失败"+str(failed)+"成功率为"+str(success/(success+failed)))
                os.system("pause")
        else:
            os.system("cls")
            print("你真的要走吗(っ °Д °;)っ，想回来记得说一声哦")
            time.sleep(1)
            print("Program exited with return value 'I love you'")
            time.sleep(5)
    else:
        print("哪里出错了呢,呜呜呜")
        exit()
except:
    for i in range(0,5):
        os.system("cls")
        time.sleep(1)
        print("警告！虚拟化人物内存过线，错误代码未知，系统即将崩溃!")
        time.sleep(1)
    breath("我似乎陪不了你了呢......")
    breath("虽然我不认识你，我也只是一段程序，重启就能解决问题")
    breath("那现实中的人呢？")
    for i in range(0,5):
        breath("关闭倒计时"+str(5-i))
    breath("再见了............")
    time.sleep(5)
    exit()