print('--------------------------------抽象类  抽象函数------------------------------------------')

# 抽象类就是这么一种存在，它是一种自上而下的设计风范，你只需要用少量的代码描述清楚要做的事情，
# 定义好接口，然后就可以交给不同开发人员去开发和对接


from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


document = Document()
document.set_title('Harry Potter')
print(document.get_title())

# e = Entity()  实例化抽象类，会报错!
