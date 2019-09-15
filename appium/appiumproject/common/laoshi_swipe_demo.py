'''
滑动代码封装
swipe（int start x,int start y,int end x,int end y,duration)
解释：
int start x－开始滑动的x坐标，
int start y －开始滑动的y坐标。
int end x －结束点x坐标，
int end y －结束点y坐标。
duration 滑动时间（默认5毫秒）；
由于swipe方法需要指定的是坐标，但是由于每个手机的分辨率不同，
如果我们指定了一个固定的坐标，在其他手机上也不一定能适用，
所以最好的办法就是通过获取手机屏幕的坐标来滑动，
'''


class SwipeDemo:
    # 获得机器屏幕大小x,y
    def getSize(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return x, y
    
    # 屏幕向上滑动
    def swipeUp(self, driver, t):
        l = self.getSize(driver)  # 调用这个类的getSize()方法
        x1 = int(l[0] * 0.5)      # x坐标
        y1 = int(l[1] * 0.75)     # 起始y坐标
        y2 = int(l[1] * 0.25)     # 终点y坐标
        driver.swipe(x1, y1, x1, y2, t)
    
    # 屏幕向下滑动
    def swipeDown(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)    # x坐标
        y1 = int(l[1] * 0.25)   # 起始y坐标
        y2 = int(l[1] * 0.75)   # 终点y坐标
        driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipeLeft(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0]*0.75)
        y1 = int(l[1]*0.8)
        x2 = int(l[0]*0.05)
        driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipeRight(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0]*0.05)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.75)
        driver.swipe(x1, y1, x2, y1, t)
