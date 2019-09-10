from time import time
import json
import hashlib
from flask import Flask, jsonify, request


# 定义一个工具类，里面有实现区块链结构的方法和属性
class BlockChain(object):  # 默认是继承object，也可以不写
    def __init__(self):
        self.blockChain = []  # 用来存储区块的信息（就是区块链）
        self.current_transactions = []  # 一个区块中有多笔交易数据，存储到此列表
        self.new_block()  # 创建第一个区块（创始区块）

    # 创建区块(索引、时间戳、交易列表、Nonce、上一个区块的Hash)
    def new_block(self):
        # 每一个区块，采用字典表示（字典与json的区别）
        '''
        python字典本质上是一种数据结构，json仅仅是格式
        1.字典有很多内置函数
        2.字典的格式：{key: value}
        3.json的格式比字典丰富，{key: value}, {key: {key: value}}, {key: [key: value]}等
        4.获取数据的方式不同：dic[key] = value,  json.key = value
        '''
        block = {
            'index': len(self.blockChain),
            'timestamp': time(),
            'transaction': self.current_transactions,
            'nonce': -1,
            'pre_hash': None if len(self.blockChain) == 0 else self.get_block_hash(self.blockChain[-1])
        }
        # 挖矿的过程就是通过已知的变量 + Nonce去匹配系统符合条件的hash值的过程
        hash = None
        while not self.valid_proof(hash, 4):
            block['nonce'] = block['nonce'] + 1
            hash = self.get_block_hash(block)
        # 把区块添加到区块链中
        self.blockChain.append(block)
        # 把之前的交易信息清空
        self.current_transactions = []
        return block

    # 根据区块 + 摘要算法得到hash过程
    def get_block_hash(self, block):
        # 把区块的数据转化为json格式（并且按照顺序），摘要算法在加密时需要设置编码
        block_str = json.dumps(block, sort_keys=True).encode('utf8')
        # 对当前json格式进行加密（顺序是不能改变）
        return hashlib.sha256(block_str).hexdigest()

    # 获取前端交易信息（flask）  区块与交易记录的关系：one to many
    def new_transaction(self, sender, receive, amount):
        # 向交易列表，追加一条交易信息
        self.current_transactions.append({
            'sender': sender,
            'receive': receive,
            'amount': amount
        })

    # 此方法用来判断当前生成的hash是否满足系统指定的难度
    def valid_proof(self, hash, difficulty):
        return False if hash == None else hash[:difficulty] == '0000'


app = Flask(__name__)  # python特殊成员  __name__    app就代表flask实例

if __name__ == '__main__':
    block = BlockChain()  # 创建一个对象

    # 此函数用来显示交易页面信息
    @app.route('/trans', methods=['get'])
    def trans_form():
        return '''<form action='/trans' method='post'>
                      from:  <input name='sender'><br />
                      to:    <input name='receive'><br />
                      amount:<input name='amount'><br />
                      <button type='submit'>trans</button>
                  </form>'''

    @app.route('/trans', methods=['post'])
    def add_transaction():
        # 获取前端的交易数据
        sender = request.form['sender']
        receive = request.form['receive']
        amount = request.form['amount']
        # 把数据添加到交易列表中
        block.new_transaction(sender, receive, amount)
        return 'success'

    # 定义路由
    @app.route('/mine', methods=['GET', 'POST'])  # 完成地址与函数的映射操作
    def mine():
        return jsonify(block.new_block())  # 返回当前生成的区块（挖矿过程），并且转化josn格式返回

    @app.route('/chain', methods=['GET', 'POST'])  # 完成地址与函数的映射操作
    def full_chain():
        json = {'length': len(block.blockChain), 'chain': block.blockChain}
        return jsonify(json)


    app.run()
