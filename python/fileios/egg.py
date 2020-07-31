#! /usr/bin/env/python
# -*- coding:utf-8 -*-
def egg_trick():
    """
    拿鸡蛋的智力题:穷举，排除法
    :return:
    """
    print('run in egg tricks')
    x = range(5000)
    out_file_name = 'egg_trick.txt'
    out_file = open(out_file_name, mode='w', encoding='utf-8')
    for egg_total  in x:
        if (egg_total % 4) != 1:
            continue
        if (egg_total % 5) != 4:
            continue
        if (egg_total % 6) != 3:
            continue
        if (egg_total % 7) != 5:
            continue
        if (egg_total % 8) != 1:
            continue
        if (egg_total % 9) != 0:
            continue
        print(egg_total)

        out_file.writelines(str(egg_total)+'\n')
    out_file.close()
if __name__ == '__main__':
    egg_trick()