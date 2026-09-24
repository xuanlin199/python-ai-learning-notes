# 温度转换器，摄氏 ⇄ 华氏，循环运行直到用户输入 q
while True:
    choice = input('请选择转换方向：1: 摄氏→华氏  2: 华氏→摄氏  q: 退出')

    if choice=='q':                      # 空1：和哪个字符串比较才算"要退出"？
        print('感谢使用')               # 空2：告别语
        break                      # 空3：用什么跳出无限循环？

    elif choice== '1':                   # 空4：方向 1 怎么判断？（比较字符串！）
        c = float(input('请输入摄氏度：'))
        f = 9/5*c+32                  # 空5：查上面的公式表，别装反
        print(f'对应的华氏度为：{f}')

    elif choice =='2':
        f = float(input('请输入华氏度：'))
        c = 5/9*(f-32)                  # 空6
        print(f'对应的摄氏度为：{c}')

    else:
        print('无效选项，请重新输入')





