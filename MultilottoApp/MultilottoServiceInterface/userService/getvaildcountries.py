from MultilottoServiceInterface.BaseService import BaseService


class GetVaildCountries(BaseService):

    def request_getvaildcountries_service(self):
        result = self.request_service('getvalidcountries', 'post')
        return result


if __name__ == '__main__':

    vaildcountrt = GetVaildCountries()
    vaildcountrt.request_getvaildcountries_service()
    print(vaildcountrt.request_getvaildcountries_service())