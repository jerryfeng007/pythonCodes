product = [['iphone', 6888], ['mac', 14800], ['xiaomi', 2499], ['coffee', 31], ['book', 60], ['nike', 699]]
cart = []
while True:
    print(product)
    s = input('您想买什么？q/退出')
    if s.lower() == 'q':
        if not cart:
            print('您的购物车为空！')
        else:
            print(f'您的购物车中商品为：{cart}')
        break
    if s not in [product[0][0], product[1][0], product[2][0], product[3][0], product[4][0], product[5][0]]:
        print('只能选择列表中的商品哦！')
        continue
    cart.append(s)
    print(f'你想买的产品为{s}，已经加入购物车喽！')
    print(f'目前购物车的商品有：{cart}')
