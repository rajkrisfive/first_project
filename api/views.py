from rest_framework import generics

from .serializers import BranchSerializer, BranchListSerializer
from bank.models import Branch
from .pagination import BranchListPagination


class BranchDetailAPIView(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'


class BranchListAPIView(generics.ListAPIView):
    serializer_class = BranchListSerializer
    pagination_class = BranchListPagination

    def get_queryset(self, **kwargs):
        queryset = Branch.objects.all()
        city = self.kwargs.get('city')
        bank = self.kwargs.get('bank')
        queryset = queryset.filter(bank__name=bank, city=city)
        return queryset

