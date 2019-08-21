# https://time.geekbang.org/column/article/98998

# 一个搜索引擎由搜索器、索引器、检索器和用户接口四个部分组成
# 搜索器，通俗来讲就是我们常提到的爬虫（scrawler），它能在互联网上大量爬取各类网站的内容，送给索引器。
# 索引器拿到网页和内容后，会对内容进行处理，形成索引（index），存储于内部的数据库等待检索。
# 最后的用户接口很好理解，是指网页和 App 前端界面，例如百度和谷歌的搜索页面。
# 用户通过用户接口，向搜索引擎发出询问（query），询问解析后送达检索器；
# 检索器高效检索后，再将结果返回给用户。

# 假设搜索样本存在于本地磁盘上。

# SearchEngineBase是可以被继承的基类。继承的类分别代表不同的算法引擎。
# 每一个引擎都应该实现process_corpus() 和 search() 两个函数，对应索引器和检索器。
# main() 函数提供搜索器和用户接口


class SearchEngineBase(object):
    def __init__(self):
        pass

    # 读取文件内容
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    # 对文件内容进行处理，处理后的内容（也就是索引）存下来
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    # 处理询问，再通过索引检索，然后返回
    def search(self, query):
        raise Exception('search not implemented.')


# 实现一个最基本的搜索引擎
class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}  # 初始化了自己的私有变量，也就是这个用来存储文件名到文件内容的字典

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text  # 将文件内容插入到字典中

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input('输入要搜索的内容：')
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


search_engine = SimpleEngine()
main(search_engine)
