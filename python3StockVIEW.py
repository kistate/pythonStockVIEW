import urllib.request
import urllib.parse,re
import time
import os,random
import threading
def __request(url):
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    response = opener.open(url).read()
    response_decode = response.decode("utf-8").replace('\n','')
    myItems=re.findall('<div.*?class="stock-bets">(.*?)</div>',response_decode,re.S)
    return myItems[0].replace('\n','').strip() + '</div>'
    
def ifExist(url):
    _requestVal = __request(url)
    if _requestVal.find('price ') == -1:
        return False
    else:
        return _requestVal

def distMes(re_str):
    arr = {}
    spanCompile = re.compile(r'<.?span>') #替换掉价span
    re_str = re_str.replace('&nbsp;','')
    d = {'title':'<a.*?class="bets-name".*?>(.*?)</a>', 'time':'<span.*?class="state f-up">(.*?)</span>', 'price':'<strong.*?class="_close">(.*?)</strong>', 'fluctuate':'</strong>(.*?)</div>'}
    for keys in d:
        pattern = re.compile(d.get(keys))
        re_str0=pattern.findall(re_str)
        str = re_str0[0]
        if keys=='fluctuate':
            str = ' '.join(str.split())
        else:
            str = str.replace(' ','').replace('&nbsp;','')
        str=spanCompile.sub('',str)
        arr[keys] = str
    return arr
    
#req = urllib.request.Request(url, headers)
#myResponse = urllib.request.urlopen(req)
#html = response.read(myResponse)
#while True:
#print(__request())
#    time.sleep(5)

def viewVal(url):
    re_Request = ifExist(url)
    if re_Request == False:
         print("Request fault.")
         exit()
    distArr = distMes(re_Request)
    gPtitle = distArr.get('title')
    gPprice = distArr.get('price')
    gPfluctuate = distArr.get('fluctuate')
    gPtime = distArr.get('time')
    print("%10s | %-6s | %-10s | %-30s"%(gPtitle,gPprice,gPfluctuate,gPtime))
    #viewVal(distMes(__request(url)),url)


urlcode = ['sz002798','sz002550','sz000868','sz000620','sz000762']
url = 'http://gupiao.baidu.com/stock/'

def main():
    while True:
        print("%-16s | %-6s | %-10s | %-30s"%("Name(CODE)","Present price","Fluctuate(price|fluctuate)","UPDATA TIME"))
        for i in urlcode:
            urltmep = url + i + ".html"
            viewVal(urltmep)
            urltmep = ''
            time.sleep(1)
        time.sleep(random.randint(1,5))
        os.system("cls")
        
if __name__ == "__main__":
    main()




#<h1>
#<a class="bets-name"href="/stock/sz002550.html">
#千红制药(<span>002550</span>)
#</a>
#<spanclass="statef-up">午间休市2016-06-29&nbsp;11:29:58
#</span>
#</h1>
#<divclass="prices-down">
#<strongclass="_close">8.37</strong>
#<span>-0.04</span>
#<span>-0.48%</span>
