#week12-1.py
n = int(input('輸入1個數:'))
def isPrime(n):
  for i in range(2,n): #只能1和n本身整數
    if n%i==0:
      return False
  return True #沒失敗就是成功

if isPrime(n): print('n是質數')
else: print('n不是質數')
