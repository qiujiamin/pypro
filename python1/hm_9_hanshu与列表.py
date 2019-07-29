def print_line(char,time):

    print(char*time)

def print_lines(char,rows,times):
    """打印多行分割线

    :param char:分隔线使用得分隔字符
    :param rows:分割线行数
    :param times:分割线重复次数
    """
    row = 0
    while row<rows:
        print_line(char,times)
        row+=1

name ="黑马程序员"