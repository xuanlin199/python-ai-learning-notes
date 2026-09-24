# 用 input() 问姓名和出生年份，打印问候语和年龄（f-string
name = input('请输入姓名:')
age = int(input('请输入出生年份:'))
age = 2026-age
print(f'您好，亲爱的{name},您当前的年龄是{age}')


# 温度转换器，摄氏 ⇄ 华氏
A = float(input('请输入摄氏度；'))
H = (9/5 * A)+32
print(f'对应的华氏度是：{H} °F')

def ZH(C):
    H =(9/5 * C)+32
    print(f'{C}所对应的华氏度为：{H}')
    pass