from collections import defaultdict
from django.conf import settings

def view_counter_middleware(get_response):
    print("***** In initializare")
    view_counter = defaultdict(lambda: 0)
    def middleware(request):
        view_counter[request.path] += 1
        request.view_counter = view_counter
        print("**** Inainte de view")
        #import time; time.sleep(5)
        response = get_response(request)
        print("**** Dupa view")
        return response
    return middleware
