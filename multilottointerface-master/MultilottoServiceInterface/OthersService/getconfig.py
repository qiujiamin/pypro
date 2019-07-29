from MultilottoServiceInterface.BaseService import BaseService


class  Getconfig(BaseService):

    def getconfig_service(self, result_type_is_str=False):
        result = self.request_service(result_type_is_str)
        return result


if __name__ == '__main__':
    getconfigIOS = Getconfig("get_config_ios")
    print(getconfigIOS.getconfig_service())
