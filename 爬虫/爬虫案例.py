# 明确robots.txt的抓取规则
# 查看页面结构，拆取步骤，按步骤开发
# 获取高分电影的榜单数据，获取每部电影的详情
# 1、访问高分电影的榜单数据页面
# 2、遍历电影列表，获取每部电影的详情页面链接
# 3、将每部电影的详情页面链接，发送给详情页面解析函数
# 4、详情页面解析函数，获取每部电影的详情数据
# 5、将每部电影的详情数据，保存到csv文件中
# 要参照原本网页的结构进行解析

import os

import requests 
import csv
from lxml import html

Movie_List_File="爬虫/csv_data/ovie_list.csv"
Base_url='http://www.themoviedb.org'
Top_url='http://www.themoviedb.org/movie/top-rated'#高分电影榜单的首页
Top_url_2='http://www.themoviedb.org/discover/movie/items'#高分电影榜单第二页（首页之后的）
# 之后的路径都是一致，尽在page处表示了参数的不同，表明所存有的数据信息不同

# 获取电影详情页面数据
def get_movie_info(url):
    # 发送请求，获取数据
    movie_response = requests.get(url, timeout=60)
    movie_document = html.fromstring(movie_response.text)
    # 名字
    name = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    # 年份
    year=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
    # 上映日期
    date=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="release"]/text()')
    # 类型
    tags=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="genres"]/a/text()')
    # 时长
    runtime=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="runtime"]/text()')
    # 评分
    score=movie_document.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    # 语言
    language=movie_document.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    # 导演
    directors=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
    # 作者
    authors=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
    # 介绍
    descriptions=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')
# 由于有的时候某些数据写的不规范，可能存在获取信息错误或缺漏，那么就要进行兼容性改造等。如上映日期、类型、时长、评分等数据可能因为span顺序的不同而导致获取信息失败，那么就可以找共同点，可能就是class一致的特征来修改进行信息的的完整获取


    # 返回数据成一个字典形式
    movie_data={
        '电影名':name[0].strip() if name else '',
        '年份':year[0].strip() if year else '',
        '上映日期':date[0].strip() if date else '',
        '类型':','.join(tags) if tags else '',
        '时长':runtime[0].strip() if runtime else '',
        '评分':score[0].strip() if score else '',
        '语言':language[0].strip() if language else '',
        '导演':directors[0].strip() if directors else '',
        '作者':authors[0].strip() if authors else '',
        '介绍':descriptions[0].strip() if descriptions else ''    
    }   
    return movie_data


def save_csv(all_movies):
    # 查询目录文件是否存在，不存在则创建
    dir_name=os.path.dirname(Movie_List_File)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open(Movie_List_File, 'w', encoding='utf-8-sig', newline='') as csvfile:
       writer= csv.DictWriter(csvfile, fieldnames=['电影名', '年份', '上映日期', '类型', '时长', '评分', '语言', '导演', '作者', '介绍'])
       writer.writeheader()#写入表头
       writer.writerows(all_movies)#写入数据

def main():
    all_movies=[]#保存所有的电影数据

    for page_num in range(1, 6):#第一页到第五页（100个电影的信息）
        # 1、发送请求，获取榜单数据
        if page_num==1:
            response=requests.get(Top_url,timeout=60)
        else:
            response=requests.post(Top_url_2,
                                   f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2026-10-01&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                   timeout=60)
        # 2、解析数据，获取列表
        document=html.fromstring(response.text)
        movie_list=document.xpath(f'//*[@id="page_{page_num}"]/div[@class="card style_1"]')
        # 3、遍历列表，获取详情

        for movie in movie_list:
        # 获取详情页链接
            movie_urls=movie.xpath('./div/div/a/@href')
            if movie_urls:
                # 组合成电影详情的url
                movie_info_url=Base_url+movie_urls[0]
                # 发送请求，获取数据
                movie_info=get_movie_info(movie_info_url)
                all_movies.append(movie_info)
            
    # 4、保存数据，保存为csv
    print('保存数据中...')
    save_csv(all_movies)    


if __name__ == '__main__':
    main()
