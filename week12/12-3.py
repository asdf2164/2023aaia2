# week12-3.py ��ƿz�l�k
table = [True] * 240000
ans = 0 #���X�ӽ��
for i in range(2, 240000): #��X�Ҧ��i�઺��� ��ƨä��|�Q�㰣 ���d���~���v
    if table[i]==True: #���,�L�O���,�S�Q����
    ans +=1 #�h�@�ӵ���
    for k in range(i*i, 240000, i): table[k] = False #��X���~��del��L�D���
print('���', ans, '�ӽ��')
