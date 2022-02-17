"""
********
功能:Python爬虫练习
环境:pycharm2021,wind10
"""
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm #显示进度，使代码可视化进度加快
# 模拟浏览器访问
def pachun():
    Headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
    # 题目数据
    subjects = []
    # 表头
    csvHeaders = ['题号', '难度', '标题', '通过率', '通过数/总提交数']
    #定义爬取函数，并删选信息
    for pages in tqdm(range(1,11+1)):
        r = requests.get(f'http://www.51mxd.cn/problemset.php-page={pages}.htm', Headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text,'html5lib')
        td = soup.find_all('td') #所有含TD的项提取出来
        subject = []
        for t in td:
            if t.string is not None :
                subject.append(t.string)
                if len(subject)==5:
                    subjects.append(subject)
                    subject = []

    #写入文件
    with open("D:/NYOJ_Subjects.csv",'w',newline='') as file:
        filewrite = csv.writer(file)
        filewrite.writerow(csvHeaders) #写入表头
        filewrite.writerows(subjects)  #写入数据
        print('\n题目信息爬取完成！！！')

if __name__ == '__main__':
    pachun()