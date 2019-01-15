# coding: utf-8

from huffman_util import *
import random

class HNode(object):
    def __init__(self, letter="", freq=0, left=None, right=None):
        self.letter = letter
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        return "<HNode '%s' %d>"%(self.letter, self.freq)

    def traverse(self, code=""):
        if self.letter:
            print self.letter, code
        else:
            self.left.traverse(code+"0")
            self.right.traverse(code+"1")
        return


def build_tree():
    """构造哈夫曼树"""

    nodes = [HNode(o[0], o[1]) for o in letters]
    nodes.sort(key=lambda x: x.freq)
    content = ""

    while len(nodes) > 1:
        if random.randint(0, 1):
            l, r = nodes[0], nodes[1]
        else:
            r, l = nodes[0], nodes[1]

        nodes = nodes[2:]
        node = HNode(freq=l.freq+r.freq, left=l, right=r)

        i = 0
        while (i < len(nodes)) and (nodes[i].freq < node.freq):
            i += 1
        nodes.insert(i, node)

    root = nodes[0]
    return root


def generate(root, code):
    """根据哈夫曼树生成文章"""
    content = ""
    p = root
    for c in code:
        if c == "0":
            p = p.left
        else:
            p = p.right

        if p.letter:
            content += p.letter
            p = root
    return content
    

def main():
    while True:
        root = build_tree()
        content = generate(root, code)
        if ("  " not in content) and ("the answer is" in content):
            print content
            root.traverse()
            break


if __name__ == '__main__':
    main()
