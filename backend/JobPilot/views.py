from django.shortcuts import render
from .models import CreateJob, ApplyJob
from .serializers import CreateJobSerializer,ApplyJobSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail
ordering_fields = ['salary', 'created_at']
ordering = ['-created_at']


class CreateJobView(viewsets.ModelViewSet):
    queryset = CreateJob.objects.all()
    serializer_class = CreateJobSerializer
    permission_classes = [AllowAny]
    search_fields = ['job_title', 'description', 'location', 'category', 'company_name']
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_fields = ['salary']

    def get_queryset(self):
        queryset = CreateJob.objects.all()
        min_salary = self.request.query_params.get('min_salary')
        max_salary = self.request.query_params.get('max_salary')
        
        if min_salary:
         queryset = queryset.filter(salary__gte=min_salary)

        if max_salary:
         queryset = queryset.filter(salary__lte=max_salary)
         
        return queryset

class ApplyJobView(viewsets.ModelViewSet):
    queryset = ApplyJob.objects.all()
    serializer_class = ApplyJobSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
    
    def perform_create(self, serializer):
        application = serializer.save()
        send_mail(
        subject="Application received",
        message="Thanks for applying.",
        from_email="baabahanif@gmail.com",
        recipient_list=[application.email],
        fail_silently=True,
        )
    
    # def validate_salary(self, value):
    #     if value <= 0:
    #         raise serializers.ValidationError("Salary must be greater than zero.")
    #     return value

