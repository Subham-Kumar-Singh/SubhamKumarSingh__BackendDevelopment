from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    # path('<str:trade_id>/',views.Home,name="Home"),
    # path("trade_detail/all/", views.Viewall, name="trade_detail"),

    # path('tradedetail/<str:trade_id>/',
    #      views.TradeDetailView.as_view(), name="trade-detail"),
    path('trade/', views.TradeAll.as_view(), name="tarde-all"),

    # Searching
    path('tradesearch/', views.SearchTrade.as_view(), name="search"),

    # Filtering
    path('tradefilter/', views.TradeList.as_view(), name="filter"),
    
    # Ordering
    path('tradeordering/',views.TradeOrder.as_view(),name="order"),
]
