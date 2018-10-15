song_lrc_analyze

---

爬取中国古诗文，进行分析，看看古诗文中到底写了什么东西

此项目只要分为两大块:

---

data_download: 此目录为一个以Scrapy框架结构的爬虫,主要从网站上自动爬取古诗文的内容

使用scrapy从古诗词网站上抓取了大概5000首古诗词和文章

---
data_analyze: 此目录为使用NLTK和jieba分词库进行数据的筛选和清洗,以及分词和标注,还有数据展示

使用jieba分词，还有python进行数据分析
