from rest_framework import generics
from .models import Product
from rest_framework.response import Response
from rest_framework.views import APIView


# class GetProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     # queryset.value
#     # pass
GENERIC_API_FAILURE = {
    "success": False,
    "data": {
        "msg": "We are unable to process your request at this moment. Please try after sometime.",
    }
}
DATA_NOT_FOUND = {
    "success": False,
    "data": {
        "msg": "Data Not Found",
    }
}
DATA_NOT_PROVIDED = {
    "success": False,
    "data": {
        "msg": "Please Provide ID",
    }
}
DATA_CREATED = {
    "success": True,
    "data": {
        "msg": "Data Created Successfully..",
    }
}
DATA_DELETED = {
    "success": True,
    "data": {
        "msg": "Data Deleted Successfully..",
    }
}

class GetProductList(APIView):

    def get(self, request):
        try:
            id = request.data.get("id", "")
            kwargs = {}
            if id:
                kwargs['id'] = id
            data_obj = Product.objects.filter(**kwargs).values()
            if not data_obj:
                return Response(DATA_NOT_FOUND, 200)
            data = {
                "success": True,
                "data": data_obj
            }
            return Response(data, 200)
        except Exception as ex:
            return Response(GENERIC_API_FAILURE, 412)


class AddProduct(APIView):

    def post(self, request):
        try:
            # id = request.data.get("id", "")
            name = request.data.get("name", "")
            description = request.data.get("description", "")
            image_url = request.data.get("image_url", "")
            video_url = request.data.get("video_url", "")
            data_obj = Product.objects.create(
                name=name,
                description=description,
                image_url=image_url,
                video_url=video_url,
            )
            return Response(DATA_CREATED, 200)
        except Exception as ex:
            print(ex)
            return Response(GENERIC_API_FAILURE, 412)


class DeleteProduct(APIView):

    def post(self, request):
        try:
            id = request.data.get("id", "")
            if not id:
                return Response(DATA_NOT_PROVIDED, 200)
            Product.objects.filter(id=id).delete()
            return Response(DATA_DELETED, 200)
        except Exception as ex:
            return Response(GENERIC_API_FAILURE, 412)