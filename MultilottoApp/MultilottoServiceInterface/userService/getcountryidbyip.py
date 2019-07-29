from MultilottoServiceInterface.BaseService import BaseService


class GetCountryIdByIp(BaseService):

    def request_getcountryidbyip_service(self):
        result = self.request_service('getcountryidbyip')
        return result


if __name__ == '__main__':
    getidbyip = GetCountryIdByIp()
    #getidbyip.request_getcountryidbyip_service()
    print(getidbyip.request_getcountryidbyip_service())
