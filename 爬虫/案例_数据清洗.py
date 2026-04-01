"""
正则表达式，由特定语法规则组成的文本模式，用来描述、匹配字符串中符合规则的字符序列。
通过语法对复杂文本进行搜索、匹配、提取和替换工资高
"""


import os
import requests 
import csv
from lxml import html

Movie_List_File="爬虫/csv_data/ovie_list.csv"
Base_url='http://www.themoviedb.org'
Top_url='http://www.themoviedb.org/movie/top-rated'
Top_url_2='http://www.themoviedb.org/discover/movie/items'

def get_movie_info(url):
    movie_response = requests.get(url, timeout=60)
    movie_document = html.fromstring(movie_response.text)
    name = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    year=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
    date=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="release"]/text()')
    tags=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="genres"]/a/text()')
    runtime=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="runtime"]/text()')
    score=movie_document.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    language=movie_document.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    directors=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
    authors=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
    descriptions=movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')


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
    dir_name=os.path.dirname(Movie_List_File)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open(Movie_List_File, 'w', encoding='utf-8-sig', newline='') as csvfile:
       writer= csv.DictWriter(csvfile, fieldnames=['电影名', '年份', '上映日期', '类型', '时长', '评分', '语言', '导演', '作者', '介绍'])
       writer.writeheader()
       writer.writerows(all_movies)

def main():
    all_movies=[]

    for page_num in range(1, 6):
        if page_num==1:
            response=requests.get(Top_url,timeout=60)
        else:
            response=requests.post(Top_url_2,
                                   f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2026-10-01&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                   timeout=60)
        document=html.fromstring(response.text)
        movie_list=document.xpath(f'//*[@id="page_{page_num}"]/div[@class="card style_1"]')

        for movie in movie_list:
            movie_urls=movie.xpath('./div/div/a/@href')
            if movie_urls:
                movie_info_url=Base_url+movie_urls[0]
                movie_info=get_movie_info(movie_info_url)
                all_movies.append(movie_info)
            
    print('保存数据中...')
    save_csv(all_movies)    


if __name__ == '__main__':
    main()
