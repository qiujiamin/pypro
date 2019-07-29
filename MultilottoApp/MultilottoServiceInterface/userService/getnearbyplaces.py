from MultilottoServiceInterface.BaseService import BaseService


class GetNearByPlaces(BaseService):

    def request_getnearbyplaces_service(self):
        result = self.request_service('getnearbyplaces')
        return result


if __name__ == '__main__':
    getcountry = GetNearByPlaces()
    print(type(getcountry.request_getnearbyplaces_service()))
    print(getcountry.request_getnearbyplaces_service())
