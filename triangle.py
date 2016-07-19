#キーボードから数字を入力して
#その高さの三角形を*で出力してください
"""
例）５と入力すると
*
**
***
****
*****
と出力する
"""
x = int(input('高さを入力してください'))

for vertical in range(x + 1):
      for horizontal in range(vertical):
          if horizontal == 0 or horizontal == vertical - 1\
                  or vertical == x:
              print('*', end=' ')
          else:
              print('+', end=' ')
      print()
