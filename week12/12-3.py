# week12-3.py 質數篩子法
table = [True] * 240000
ans = 0 #有幾個質數
for i in range(2, 240000): #找出所有可能的質數 質數並不會被整除 表格留著繼承權
    if table[i]==True: #找到,他是質數,沒被消滅
    ans +=1 #多一個答案
    for k in range(i*i, 240000, i): table[k] = False #找出後繼續del其他非質數
print('找到', ans, '個質數')
