# from rest_framework.decorators import api_view
# from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView , RetrieveUpdateDestroyAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets









# Crud Operation by just two classes in concrete view

# class StudentRUD(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentLC(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer







# # Concrete view classes (All available Options)

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentLC(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRU(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRD(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRUD(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer













# # Generic API view and Model Mixin (In two classes)

# # List and Create (pk not needed)
# class StudentLC(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# # Retrieve, update and destroy in one class (all need pk)
# class StudentRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# # Get all data
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# # Update data
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# # Delete data
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)















# # Generic API view and Model Mixin (all operations One by One)

# # Get all data
# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# # Create data in Database
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# # Get one data
# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# # Update data
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# # Delete data
# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)















# # Testing by browseable api

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def student_api(request,pk=None):

#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)


#     if request.method == 'POST':
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     if request.method == 'PUT':
#         id=pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data updated'})
#         return Response(serializer.errors)


#     if request.method == 'PATCH':
#         id=pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data updated'})
#         return Response(serializer.errors)


#     if request.method == 'DELETE':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})        















# if we use a 3rd party application for testing thaan we use this function

# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)

#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)


#     if request.method == 'POST':
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'})
#         return Response(serializer.errors)


#     if request.method == 'PUT':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data updated'})
#         return Response(serializer.errors)


#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})        
