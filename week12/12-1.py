#week12-1.py
n = int(input('��J1�Ӽ�:'))
def isPrime(n):
  for i in range(2,n): #�u��1�Mn�������
    if n%i==0:
      return False
  return True #�S���ѴN�O���\

if isPrime(n): print('n�O���')
else: print('n���O���')
