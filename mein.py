import json
import tkinter as tk
import webbrowser
import requests

def webbrowser_open():
    print("oopen_browser START")
    url='https://www.google.co.jp/maps/'
    webbrowser.open_new(url)
    webbrowser.open(url)
    webbrowser.open(url,1)

def station(ido,keido):
    print(ido, keido)
    print("station START")
    api='http://express.heartrails.com/api/json?method=getStations&x={x},&y={y}'
    url=api.format(y=ido, x=keido)
    ret=requests.get(url)
    ret_json=json.loads(ret.text)
    print(ret_json)
    Line=ret_json["response"]["station"][0]["line"]
    station=ret_json["response"]["station"][0]["name"]
    distance=ret_json["response"]["station"][0]["distance"]
    
    msg_info(Line,station,distance)
    
def msg_info(Line,station,distance):
    print("msg_info START")
    station_info_line_name_dis["text"]=Line+"の"+station+"駅です。"+"距離は"+distance+"です。"
    
webbrowser_open()
root=tk.Tk()
root.title("最寄駅検索")
root.geometry("500x300")

idokeido=tk.Label(text="緯度と経度を入力してください")
ido=tk.Entry(text="緯度")
keido=tk.Entry(text="経度")

gm=tk.Label(text="Google Mapを起動します")
bt_gm=tk.Button(text="Google Mapを起動します")
bt_sc =tk.Button(text="検索",command=lambda:station(ido.get(), keido.get()))

station_info=tk.Label(text="最寄り駅は・・・")
station_info_line_name_dis=tk.Label(text="○○○線。○○○駅。距離は○○○m")

gm.pack()
bt_gm.pack()
idokeido.pack()
ido.pack()
keido.pack()
bt_sc.pack()
station_info.pack()
station_info_line_name_dis.pack()

root.mainloop()