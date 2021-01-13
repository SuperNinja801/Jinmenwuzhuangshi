import requests
import json
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    post_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    position=input('enter a position:')
    data={
        'cname':'' ,
        'pid':'' ,
        'keyword': position ,
        'pageIndex': '1',
        'pageSize': '10'
    }
    response=requests.post(url=post_url,data=data,headers=headers)
    response_text=response.text
    fp = open('./肯德基地点查询.json','w',encoding='utf-8')
    fp.write(response_text)
    print('over!')