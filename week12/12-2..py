/// week12-2.py �C�Xn�H�U���������
n = int(input('�п�J�@�Ӽ�'))
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True ///�S���ѴN�O���\�F
for i in range(2,n+1):
    if isPrime(i): print(i,end=' ')
