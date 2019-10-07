s = 'native_webview.py'


def get_hzm(s):
    l = s.split('.')
    print(l)
    return l[-1]


print(get_hzm(s))
