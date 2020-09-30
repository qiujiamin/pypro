def gen_se_personal_number(birthday, thirdnum):
    nums = str(birthday) + str(thirdnum)
    sum = int(nums[1]) + int(nums[3]) + int(nums[5]) + int(nums[7])
    double = [int(nums[0]) * 2, int(nums[2]) * 2, int(nums[4]) * 2, int(nums[6]) * 2, int(nums[8]) * 2]
    for v in double:
        v = str(v)
        if len(v) == 2:
            sum += int(v[0]) + int(v[1])
            continue
        sum += int(v)
    sum = str(sum)
    check_num = str(10 - int(sum[-1]))
    return nums + check_num[-1]


print (gen_se_personal_number('940705', '237'))

# https://www.fakenamegenerator.com/gen-male-sw-sw.php