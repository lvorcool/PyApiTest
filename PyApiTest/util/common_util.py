# coding=utf-8
class CommonUtil:
    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否在另一个字符串中
        :param str_one: 查找的字符串
        :param str_two: 被查找的字符串
        :return:
        判断是否包含,得确定数据类型要一致, 不一致时就转数据类型,
        以下例子是str_two可能是list或dict,所以要转str才能判断
        '''
        flag = None
        if str_one in str(str_two):
            flag = True
        else:
            flag = False
        return flag