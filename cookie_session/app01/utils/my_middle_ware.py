from django.utils.deprecation import MiddlewareMixin

class MD1(MiddlewareMixin):

    def process_request(self,request):

        print('MD1请求来了')

    def process_response(self,request,response):

        print('MD1响应来了')
        #必须返回response,否则无返回报错
        return response
