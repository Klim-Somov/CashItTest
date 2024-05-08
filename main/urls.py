from django.urls import path
from .views import *

urlpatterns = [
    path('', NewIndexView.as_view(), name='index'),
    path('test/', TestView.as_view(), name='test'),
    path('business/', BusinessView.as_view(), name='business'),
    path('business/any-business', AnyBusinessView.as_view(), name='any-business'),
    path('business/taxi', TaxiView.as_view(), name='taxi'),
    path('business/delivery', DeliveryView.as_view(), name='delivery'),
    path('business/freelance', FreelanceView.as_view(), name='freelance'),
    path('business/recycling', RecyclingView.as_view(), name='recycling'),
    path('business/autodealers', DealersView.as_view(), name='autodealers'),
    path('business/realtors', RealtorsView.as_view(), name='realtors'),
    path('business/others', OthersView.as_view(), name='others'),
    path('self/', SelfView.as_view(), name='self'),
    path('service/', ServiceView.as_view(), name='service'),
    path('policy/', PolicyView.as_view(), name='policy'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article'),
    path('features/payment', PaymentView.as_view(), name='payment'),
    path('features/acquiring', AcquiringView.as_view(), name='acquiring'),
    path('features/salary', SalaryView.as_view(), name='salary'),
    path('features/donate', DonateView.as_view(), name='donate'),
    path('features/tips', TipsView.as_view(), name='tips'),
]
