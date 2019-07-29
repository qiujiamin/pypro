#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from MultilottoServiceInterface.BaseService import BaseService


class  IsNeedUpdateTranslations(BaseService):

    def isneedupdatetranslations_IOS(self, result_type_is_str=False):
        result = self.request_service(result_type_is_str)
        return result


if __name__ == '__main__':
    is_ud_tr = IsNeedUpdateTranslations("isneedupdatetranslations_ios")
    print(is_ud_tr.getconfig_service())
