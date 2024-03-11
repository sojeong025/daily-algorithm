from collections import defaultdict
import sys
input = sys.stdin.readline

_dict = defaultdict(int)
n = 0
while True:
    try:
      tree = input().rstrip()
      if not tree:
          break
      _dict[tree] += 1
      n += 1
    except EOFError:
        break

tree_lst = list(_dict.keys())
tree_lst.sort()
for tree in tree_lst:
    print('%s %.4f' %(tree, _dict[tree]/n*100))
