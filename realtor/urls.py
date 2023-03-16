from django.urls import path
from .views import AgentListView, AgentDetailView, TopSellerListView

urlpatterns = [
    path('', AgentListView.as_view(), name='agents'),
    path('top/', TopSellerListView.as_view(), name='top-seller'),
    path('<pk>/', AgentDetailView.as_view(), name='agent-detail'),
] 
