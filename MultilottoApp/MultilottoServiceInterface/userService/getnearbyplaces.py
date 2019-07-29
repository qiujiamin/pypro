from MultilottoServiceInterface.BaseService import BaseService


class GetNearByPlaces(BaseService):

    def getnearbyplaces_service(self, reslut_type_is_str=False):
        result = self.request_service(reslut_type_is_str)
        return result


if __name__ == '__main__':
    getcountry = GetNearByPlaces("getnearbyplaces")
    print(type(getcountry.getnearbyplaces_service()))
    print(getcountry.getnearbyplaces_service())
