import requests
from bs4 import BeautifulSoup
class HaokanAuthor():
    def __init__(self,authorId):
        self.authorId=authorId
        self.name=""
        self.videoList=[]

    def getAuthorName(self):
        if self.name == "":
            self.name=self.getAuthorNameFromWeb()
        return self.name

    def getAuthorNameFromWeb(self):
        resp=requests.get("https://haokan.hao123.com/author/"+self.authorId)
        #中文页面有时候需要指定页面编码，否则会乱码
        resp.encoding='UTF-8'
        authorPageHtml=resp.text
        authorPageDom=BeautifulSoup(authorPageHtml,features="html5lib")
        #获取视频作者名字
        authorNameTag=authorPageDom.find("h1",class_="uinfo-head-name")
        authorName=authorNameTag.string
        return authorName

    def getVideoList(self):
        #测试桩
        # videoName1="傲日其愣《鸿雁》悠远旷达，沁人心扉｜吉林省市民文化节.flv"
        # videoName2="傲日其愣《祝酒歌》清唱，萦绕耳畔的魅力之音.flv"
        # videoSrc1="https://vd2.bdstatic.com/mda-mbtf67qj8vzriqgv/v1-cae/1080p/mda-mbtf67qj8vzriqgv.mp4?v_from_s=hkapp-haokan-hna&auth_key=1614659995-0-0-bdbebe96b8659a0aa196e3713be192aa&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest="
        # videoSrc2="https://vd2.bdstatic.com/mda-mbtc7waqpae1us00/v1-cae/1080p/mda-mbtc7waqpae1us00.mp4?v_from_s=gz_videoui_4135&auth_key=1614660110-0-0-865be9bc4b185fb319d704dec291a9f7&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest="
        # return [{"videoName":videoName1,"videoSrc":videoSrc1},{"videoName":videoName2,"videoSrc":videoSrc2}]
        if len(self.videoList)>0:
            return self.videoList
        self.dealHaokanResponse("https://haokan.hao123.com/author/"+self.authorId+"?_format=json&rn=16&ctime=0&_api=1")
        return self.videoList
            
    def dealResponse(self,response):
        ctime=response['ctime'] 
        results=response['results']
        # downloader=DownloadHelp()
        if len(results)>0:
            for video in results:
                videoContent=video['content']
                videoName=videoContent['title']
                videoSrc=videoContent['video_src']
                self.videoList.append({"videoName":videoName+'.flv',"videoSrc":videoSrc})
                # downloader.download(videoSrc,videoName+'.flv')
                # common.any_download(url=videoSrc,output_dir="d:\\download",merge=True,info_only=False,stream_id="flv")
        return "https://haokan.hao123.com/author/1660856148856519?_format=json&rn=16&ctime="+ctime+"&_api=1"

    def dealHaokanResponse(self,url):
        resp=requests.get(url)
        respJson=resp.json()
        response=respJson['data']['response']
        if int(response['response_count'])>0:
            nextRequestUrl=self.dealResponse(response)
            self.dealHaokanResponse(nextRequestUrl)