#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ziyi'

from selenium import webdriver
import pandas as pd
import time
from pypinyin import lazy_pinyin
import os

def get_movie(url):
    df = pd.DataFrame({})
    contents = {}
    driver.get(url)
    try:
        movie_url = driver.find_element_by_xpath('//*[@id="moreRegion"]/li/h3/a').get_attribute('href')
        driver.find_element_by_xpath ('//*[@id="moreRegion"]/li/h3/a').click ()
        print(movie_url)
        driver.get(movie_url)
        time.sleep(5)
    except:
        pass
    try:
        contents['movie_name'] = driver.find_element_by_xpath('//*[@id="db_head"]/div[2]/div/div[1]/h1').text.encode('gbk','ignore').decode('gbk')
        print(contents)
        try:
            contents['movie_english_name'] = driver.find_element_by_xpath('//*[@id="db_head"]/div[2]/div/div[1]/p[2]').text.encode('gbk','ignore').decode('gbk')
        except:
            print(contents['movie_name'],'没有英文名称')
        try:
            contents['movie_time'] = driver.find_element_by_xpath('//*[@id="db_head"]/div[2]/div/div[2]/span').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影时间')
        try:
            movie_classes = driver.find_elements_by_xpath('//*[@id="db_head"]/div[2]/div/div[2]//a[@property="v:genre"]')
            classes = []
            for classify in movie_classes:
                classes.append(classify.text.encode('gbk','ignore').decode('gbk'))
            contents['movie_classify'] = ','.join(one for one in classes)
        except:
            print('没有电影类型')
        try:
            contents['movie_show_time'] = driver.find_element_by_xpath('//*[@id="db_head"]/div[2]/div/div[2]/a[last()]').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的上映时间')
        try:
            contents['movie_introduce_videos'] = driver.find_element_by_xpath('//*[@id="movieNavigationRegion"]/dd[1]/a').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的介绍视频')
        try:
            contents['movie_introduce_pictures'] = driver.find_element_by_xpath('//*[@id="movieNavigationRegion"]/dd[2]/a').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的介绍图片')
        try:
            contents['movie_introduce_actors'] = driver.find_element_by_xpath('//*[@id="movieNavigationRegion"]/dd[3]/a').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的介绍演员')
        try:
            contents['movie_introduce_comments'] = driver.find_element_by_xpath('//*[@id="movieNavigationRegion"]/dd[4]/a').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的介绍评论')
            contents['movie_introduce_comments'] = None
        try:
            contents['movie_introduce_news'] = driver.find_element_by_xpath('//*[@id="movieNavigationRegion"]/dd[5]/a').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的简介')
        try:
            contents['movie_scores'] = driver.find_element_by_xpath('//*[@id="ratingRegion"]/div[1]/b').text.encode('gbk','ignore').decode('gbk')
            contents['movie_scores_total'] = driver.find_element_by_xpath('//*[@id="ratingRegion"]/div[1]/p').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的得分')
        try:
            contents['movie_income'] = driver.find_element_by_xpath('//*[@id="ratingRegion"]/div[2]/span').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的票房')
        try:
            contents['movie_cinema'] = driver.find_element_by_xpath ('//*[@id="descripRegion"]/div/div/div[1]/b[1]').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的得分')
        try:
            contents['movie_play_times'] = driver.find_element_by_xpath('//*[@id="descripRegion"]/div/div/div[1]/b[2]').text.encode('gbk','ignore').decode('gbk')
        except:
            print('没有电影的播放次数')
        try:
            contents['movie_director'] = driver.find_element_by_xpath('//*[@id="movie_warp"]/div[2]/div[3]/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/a').text.encode('gbk','ignore').decode('gbk')
        except:
            print ('没有电影的导演')
        try:
            contents['movie_scenarist'] = driver.find_element_by_xpath('//*[@id="movie_warp"]/div[2]/div[3]/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]').text.encode('gbk','ignore').decode('gbk')
        except:
            print ('没有电影的场景')
        try:
            contents['movie_country'] = driver.find_element_by_xpath('//*[@id="movie_warp"]/div[2]/div[3]/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[3]/a').text.encode('gbk','ignore').decode('gbk')
        except:
            print ('没有电影的城市')
        try:
            contents['movie_company'] = driver.find_element_by_xpath('//*[@id="movie_warp"]/div[2]/div[3]/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[4]/a').text.encode('gbk','ignore').decode('gbk')
        except:
            print ('没有电影的公司')
        try:
            driver.find_element_by_xpath('//*[@id="movie_warp"]/div[2]/div[3]/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dt/p[2]/a').click()
            time.sleep(3)
            contents['movie_introduction'] = driver.find_element_by_xpath('//*[@id="paragraphRegion"]/div/div[2]/div[2]/p[2]').text.encode('gbk','ignore').decode('gbk')
        except:
            print ('没有电影的介绍')
    except Exception as e:
        print(e)
    # '//*[@id="paragraphRegion"]/div/div[3]/div[2]/p[1]'
    # '//*[@id="paragraphRegion"]/div/div[4]/div[2]/p[1]'
    # '//*[@id="paragraphRegion"]/div/div[2]/div[2]/p[2]'
    try:
        comments_url = driver.find_element_by_xpath ('//*[@id="movieNavigationRegion"]/dd[5]/a').get_attribute('href')
        print(comments_url)
    except:
        comments_url = None

    try:
        if contents['movie_introduce_comments'] == '999+ 条影评':
            driver.find_element_by_xpath ('//*[@id="movieNavigationRegion"]/dd[5]/a').click ()
            print('bingo')
            time.sleep (2)
            driver.get(comments_url)
            time.sleep(3)
            contents['movie_long_comments'] = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[1]/a').text.encode('gbk','ignore').decode('gbk').split('(')[-1].split(')')[0]
            contents['movie_short_comments'] = driver.find_element_by_xpath ('//html/body/div[5]/div/div[1]/ul/li[2]/a').text.encode('gbk','ignore').decode('gbk').split('(')[-1].split(')')[0]
            contents['movie_introduce_comments'] = int(contents['movie_short_comments'])+int(contents['movie_long_comments'])
    except:
        pass
    print(contents)
    df = df.append(contents, ignore_index=True)
    return df,comments_url

def long_comments_pages(comments_url):
    next_page = None
    driver.get(comments_url)
    time.sleep (3)
    driver.execute_script ('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep (2)
    driver.execute_script ('window.scrollTo(document.body.scrollHeight,200)')
    time.sleep (2)
    driver.execute_script ('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep (2)
    pages = driver.find_elements_by_xpath('//*[@id="PageNavigator"]/a')
    all_pages = len(pages)-2
    return all_pages

def get_long_comments(comments_url,pages):
    df = pd.DataFrame({})
    long_comments = {}
    comments_content_url = []
    writer_url = []
    have_score = None
    top = None
    driver.get(comments_url)
    time.sleep (3)
    driver.execute_script ('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep (2)
    driver.execute_script ('window.scrollTo(document.body.scrollHeight,200)')
    time.sleep (2)
    movie_long_comments = driver.find_element_by_xpath ('/html/body/div[5]/div/div[1]/ul/li[1]/a').text.encode('gbk','ignore').decode('gbk').split ('(')[-1].split (')')[0]
    print(movie_long_comments)
    # long_comments_one = driver.find_element_by_xpath ('//*[@id="reviewRegion"]/dl[1]/dd[1]/div[1]/h3/a')
    # print(long_comments_one)
    for page in range(pages):
        next_page = None
        try:
            next_page = driver.find_element_by_xpath('//*[@id="key_nextpage"]')
        except:
            print('已经翻到最后一页了')
        finally:
            next_page = next_page
        if next_page or page:
            long_comments_list = driver.find_elements_by_xpath('//*[@id="reviewRegion"]/dl[@class="clearfix"]')
            for i,one_comments in enumerate(long_comments_list):
                print(i+1, one_comments)
                long_comments['header_name'] = one_comments.find_element_by_xpath('//*[@id="reviewRegion"]/dl[{}]/dd[1]/div[1]/h3/a'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                long_comments['comment_href'] = one_comments.find_element_by_xpath('//*[@id="reviewRegion"]/dl[{}]/dd[1]/div[1]/h3/a'.format(i+1)).get_attribute('href')
                long_comments['praise'] = one_comments.find_element_by_xpath('//*[@id="reviewRegion"]/dl[{}]/dd[1]/div[2]/a[1]'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                long_comments['share'] = one_comments.find_element_by_xpath('//*[@id="reviewRegion"]/dl[{}]/dd[1]/div[2]/a[2]'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                long_comments['reply'] = one_comments.find_element_by_xpath('//*[@id="reviewRegion"]/dl[{}]/dd[1]/div[2]/a[3]'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                long_comments['writer'] = one_comments.find_element_by_xpath('//*[@id="reviewRegion"]/dl[{}]/dd[2]/div/p[1]/a'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                long_comments['writer_url'] = one_comments.find_element_by_xpath ('//*[@id="reviewRegion"]/dl[{}]/dd[2]/div/p[1]/a'.format(i+1)).get_attribute('href')
                long_comments['pubtime'] = one_comments.find_element_by_xpath('//*[@id="reviewRegion"]/dl[{}]/dd[2]/div/p[2]/a'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                try:
                    have_score = one_comments.find_element_by_xpath('//*[@id="reviewRegion"]/dl[{}]/dd[2]/div/p[3]/span'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                except:
                    print('该用户未进行评分')
                finally:
                    long_comments['score'] = have_score

                try:
                    top = one_comments.find_element_by_xpath('//*[@id="reviewRegion"]/dl[{}]/dt'.format(i+1)).text.encode('gbk','ignore').decode('gbk').replace('\n','')
                except:
                    print('该影评非top')
                finally:
                    long_comments['top'] = top
                long_comments['savetime'] = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime (time.time ()))
                # print (long_comments)
                comments_content_url.append(long_comments['comment_href'])
                writer_url.append(long_comments['writer_url'])
                # long_comments['comment_content'] = get_comments_content(long_comments['comment_href'])
                # long_comments['people_location'],long_comments['people_constellatory'],long_comments['people_gender'] = get_people_infor(long_comments['writer_url'])
                df = df.append(long_comments, ignore_index=True)
                print (long_comments)
            if next_page:
                next_page.click ()
                time.sleep(3)
    return df,comments_content_url,writer_url

# def get_comments_content(comment_content_url):
#     comments_content = {}
#     for one_content_url in comment_content_url:
#         driver.get(one_content_url)
#         time.sleep(3)
#         content = '\n'.join(p.text.encode('gbk','ignore').decode('gbk') for p in driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[3]//p'))
#         comments_content[one_content_url] = content
#         print('评论的内容获取成功')
#     print(comments_content)
#     return comments_content

# def get_people_infor(people_url):
#     writer_infro = {}
#     for one_url in people_url:
#         driver.get(one_url)
#         time.sleep(3)
#         driver.set_page_load_timeout (15)
#         writer_infro['people_location'] = driver.find_element_by_xpath('//*[@id="left_col"]/div[1]/div/div/div[1]/div/div[2]/p[1]/span').text.encode('gbk','ignore').decode('gbk')
#         writer_infro['people_constellatory'] = driver.find_element_by_xpath('//*[@id="left_col"]/div[1]/div/div/div[1]/div/div[2]/p[2]').text.encode('gbk','ignore').decode('gbk').split('')[-1]
#         writer_infro['people_gender'] = driver.find_element_by_xpath ('//*[@id="left_col"]/div[1]/div/div/div[1]/div/div[2]/p[2]').text.encode('gbk','ignore').decode('gbk').split ('')[1]
#         print('评论者信息获取成功')
#     return writer_infro

def short_comments_pages(comments_url):
    driver.get(comments_url)
    time.sleep (1)
    short_comments_href = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[2]/a').get_attribute('href')
    driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[2]/a').click()
    driver.get(short_comments_href)
    driver.execute_script ('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep (1)
    driver.execute_script ('window.scrollTo(document.body.scrollHeight,200)')
    time.sleep (1)
    driver.execute_script ('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep (1)
    pages = driver.find_elements_by_xpath('//*[@id="PageNavigator"]/a')
    all_pages = len(pages)-2
    return all_pages

def get_short_comments(comments_url,pages):
    df = pd.DataFrame({})
    short_comments = {}
    have_score = None

    driver.get(comments_url)
    time.sleep(1)
    movie_short_comments = driver.find_element_by_xpath ('//html/body/div[5]/div/div[1]/ul/li[2]/a').text.encode('gbk','ignore').decode('gbk').split ('(')[-1].split (')')[0]
    short_comments_href = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[2]/a').get_attribute('href')
    driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[2]/a').click()
    driver.get(short_comments_href)
    time.sleep(1)
    a = driver.find_element_by_xpath('//*[@id="tweetRegion"]/dd[1]/div/h3').text.encode('gbk','ignore').decode('gbk')
    print(a)
    for page in range(pages):
        next_page = None
        try:
            next_page = driver.find_element_by_xpath('//*[@id="key_nextpage"]')
        except:
            print('已经翻到最后一页了')
        finally:
            next_page = next_page
        if next_page or page:
            short_comments_list = driver.find_elements_by_xpath('//*[@id="tweetRegion"]/dd/div/h3')
            for i, one_comment in enumerate(short_comments_list):
                short_comments['short_comment'] = one_comment.find_element_by_xpath('//*[@id="tweetRegion"]/dd[{}]/div/h3'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                short_comments['short_praise'] = one_comment.find_element_by_xpath ('//*[@id="tweetRegion"]/dd[{}]/div/div[2]/div/div[2]/a[1]'.format (i + 1)).text.encode('gbk','ignore').decode('gbk')
                short_comments['short_share'] = one_comment.find_element_by_xpath ('//*[@id="tweetRegion"]/dd[{}]/div/div[2]/div/div[2]/a[2]'.format (i + 1)).text.encode('gbk','ignore').decode('gbk')
                short_comments['short_reply'] = one_comment.find_element_by_xpath ('//*[@id="tweetRegion"]/dd[{}]/div/div[2]/div/div[2]/a[3]'.format (i + 1)).text.encode('gbk','ignore').decode('gbk')
                short_comments['short_writer'] = one_comment.find_element_by_xpath('//*[@id="tweetRegion"]/dd[{}]/div/div[1]/div[1]/p[1]/a'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                short_comments['short_writer'] = one_comment.find_element_by_xpath ('//*[@id="tweetRegion"]/dd[{}]/div/div[1]/div[1]/p[1]/a'.format (i + 1)).text.encode('gbk','ignore').decode('gbk')
                short_comments['short_writer_url'] = one_comment.find_element_by_xpath ('//*[@id="tweetRegion"]/dd[{}]/div/div[1]/div[1]/p[1]/a'.format (i + 1)).get_attribute('href')
                short_comments['short_pubtime'] = one_comment.find_element_by_xpath ('//*[@id="tweetRegion"]/dd[{}]/div/div[1]/div[2]/a'.format (i + 1)).get_attribute ('entertime')
                try:
                    have_score = one_comment.find_element_by_xpath('//*[@id="tweetRegion"]/dd[{}]/div/div[1]/div[1]/p[2]/span'.format(i+1)).text.encode('gbk','ignore').decode('gbk')
                except:
                    print ('该用户未进行评分')
                finally:
                    short_comments['short_score'] = have_score
                short_comments['savetime'] = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime (time.time ()))
                df = df.append (short_comments, ignore_index=True)
                print (short_comments)
            if next_page:
                next_page.click ()
                time.sleep(3)
    return df

def create_foleder(foldernames):
    current_position="data/movie/"
    foldername=str(current_position)+str(foldernames)+"/"
    isCreated=os.path.exists(foldername)
    if not isCreated:
        os.makedirs(foldername)
        print(str(foldername)+'is created')
        return foldername
    else:
        print("the folder has been created before")
        return foldername

def read_movies():
    df = pd.read_csv ('data/movie/movie_list.csv', encoding='gbk')
    movie_names = df['movie_name'].values.tolist()
    # print(movie_names)
    return movie_names

def save_info(contents,foldername, name):
    df = pd.DataFrame()
    df = df.append(contents.copy())
    df.to_csv(foldername+'{}.csv'.format(name), encoding='gbk',index=None)

if __name__ == '__main__':
    movie_names = read_movies()
    for movie_name in movie_names:
        url = 'http://search.mtime.com/search/?q={}'.format (movie_name)
        # driver = webdriver.PhantomJS (executable_path=r'D:\anaconda python\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        driver = webdriver.Chrome (executable_path=r'D:\ksdler\chromedriver_win32_new\chromedriver')
        # 获取某部影片的基本信息
        contents, comments_url = get_movie (url)
        now = time.strftime ('%Y-%m-%d', time.localtime (time.time ())).split (' ')[0]
        movie_name = movie_name.replace('|','')
        movie_name = movie_name.replace(':','')
        movie_name = movie_name.replace('：','')
        movie_name = movie_name.replace('.','')
        movie_name = movie_name.replace(' ','')
        movie_name_pinyin = lazy_pinyin (movie_name)
        # foldername = '_'.join (i for i in movie_name_pinyin)
        foldernames = '_'.join (i for i in movie_name_pinyin)

        try:
            save_path = create_foleder (foldernames)
        except:
            save_path = None
        if save_path :
            save_info (contents, save_path, foldernames + now)
            print (now, save_path, '存储成功')

        # comments_url = 'http://movie.mtime.com/219107/comment.html'
        # if comments_url:
        #     # 获取长影评并且完成存储
        #     pages = long_comments_pages(comments_url)
        #     long_comments, comment_content_url, writer_url = get_long_comments(comments_url, pages)
        #     save_info(long_comments, save_path,foldernames+'_long_comments')
        #     # 获取长影评的内容
        #     # get_comments_content(comment_content_url)
        #     # 获取用户的个人信息
        #     # get_people_infor(writer_url)
        #     # 获取短影评并且完成存储
        #     short_pages = short_comments_pages(comments_url)
        #     short_comments = get_short_comments(comments_url,short_pages)
        #     save_info (short_comments, save_path, foldernames+'short_comments')
        driver.close()
    # movie_name = '头号玩家'
    # url = 'http://search.mtime.com/search/?q={}'.format (movie_name)
    # driver = webdriver.Chrome (executable_path=r'D:\ksdler\chromedriver_win32_new\chromedriver')
    # # 获取某部影片的基本信息
    # contents, comments_url = get_movie(url)
    # now = time.strftime('%Y-%m-%d', time.localtime(time.time())).split(' ')[0]
    # save_info(contents,movie_name+now)
    # comments_url = 'http://movie.mtime.com/219107/comment.html'
    # 获取长影评并且完成存储
    # pages = long_comments_pages(comments_url)
    # long_comments, comment_content_url, writer_url = get_long_comments(comments_url, pages)
    # save_info(long_comments, movie_name+'_long_comments')
    # 获取长影评的内容
    # get_comments_content(comment_content_url)
    # 获取用户的个人信息
    # get_people_infor(writer_url)
    # 获取短影评并且完成存储
    # short_pages = short_comments_pages(comments_url)
    # short_comments = get_short_comments(comments_url,short_pages)
    # save_info (short_comments, 'short_comments')
