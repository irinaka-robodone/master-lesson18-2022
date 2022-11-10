import json
import tkinter as tk
import webbrowser
import requests

def webbrowser_open():
    print("webbrowser_open START")
    url = "https://www.google.co.jp/maps/"
    webbrowser.open_new(url)
    webbrowser.open(url,1)

def station(keido,ido):
    print("station START")
    api="http://express.heartrails.com/api/json?method=getStations&x={x},&y={y}"
    url=api.format(x=keido,y=ido)
    ret=requests.get(url)
    ret_json=json.loads(ret.text)
    Line=ret_json["response"]["station"][0]["Line"]
    station=ret_json["response"]["station"][0]["distance"]
    distance=ret_json["response"]["station"][0]["distance"]

    msg_info(Line,station,distance)

def msg_info(Line,statioon,distance):
    print("msg_info START")
    station_info_line_name_dis["text"]=Line+"の"+station+"駅です。"+"距離は"+distance+"です。"

root = tk.Tk()
root.title("最寄駅検索")
root.geometry("500x300")

gm=tk.Label(text="Google Mapを起動します")
bt_gm=tk.Button(text="Google Map",command=webbrowser_open)

idokeido=tk.Label(text="緯度と経度を入力してください")
ido=tk.Entry(text="緯度")
keido=tk.Entry(text="経度")

bt_sc=tk.Button
(text="検索",command = lambda:station(keido.get(),ido.get()))

station_info=tk.Label(text="最寄りの駅は・・・")
station_info_line_name_dis=tk.Label(text="○○○線。○○○駅。距離は○○○ｍ")

gm.pack()
bt_gm.pack()
idokeido.pack()
ido.pack()
keido.pack()
bt_sc.pack()
station_info.pack()
station_info_line_name_dis.pack()

root.mainloop()
