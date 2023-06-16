# 定义函数来执行加法运算
def add(num1, num2):
    return num1 + num2

# 定义函数来执行减法运算
def subtract(num1, num2):
    return num1 - num2

# 定义函数来执行乘法运算
def multiply(num1, num2):
    return num1 * num2

# 定义函数来执行除法运算
def divide(num1, num2):
    # 需要处理除数为零的情况
    if num2 == 0:
        return "除数不能为零"
    else:
        return num1 / num2

# 主程序
print("欢迎使用简易计算器！")
while True:
    print("请选择要执行的操作：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 退出")
    
    choice = input("请输入选项（1-5）：")
    
    if choice == '5':
        print("感谢使用计算器，再见！")
        break
    
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    
    if choice == '1':
        result = add(num1, num2)
        print("结果：", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("结果：", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("结果：", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("结果：", result)
    else:
        print("无效的选项，请重新选择！")