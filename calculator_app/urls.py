from django.urls import path
from . import views




urlpatterns = [

	path('', views.index, name = 'index'),  
	path('interest_calculator/results/', views.results_interest, name = 'results_interest'), 
	path('interest_calculator/', views.interest_calc, name = 'interest_calculator'), 
	path('loan_calculator/', views.loan_calculator, name = 'loan_calculator')
		
]

