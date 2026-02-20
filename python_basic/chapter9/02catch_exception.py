'''异常处理示例'''
# 1.捕获用except 具体异常
# 2.获取具体信息用as
# 3.无论如何都执行用finally


while 'q' != input('是否继续？（如果需要退出请输入q）'):
    try:
        # print(x)
        a = int(input('请输入第一个数'))
        b = int(input('请输入第一个数'))
        res = a / b
        print(f'{a}除以{b}的结果为{res}')
    # else:
    #     print('')
    except ZeroDivisionError as e:
        print(f'除数为0，无法处理，具体信息为{e}')
    except ValueError as e:
        print(f'输入的内容无法转为数字，请重新输入，具体信息为{e}')
    except Exception as e:
        import traceback
        traceback.print_exc()
    else:
        # 需要注意else不能写到finally下面，也不能写到except上面，必须在except和finally之间
        print('else--这一轮没有异常，真棒！没有异常才能走到这里哦')
    finally:
        print('finally--不管异常与否都会执行到这里哦')

# 统一捕获不同的异常，格式为(e1, e2, e3 ... )
while 'q' != input('是否继续？（如果需要退出请输入q）'):
    try:
        # print(x)
        a = int(input('请输入第一个数'))
        b = int(input('请输入第一个数'))
        res = a / b
        print(f'{a}除以{b}的结果为{res}')
    except (ZeroDivisionError, ValueError, Exception) as e:
        traceback.print_exc()
