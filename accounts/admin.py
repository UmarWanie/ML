from django.contrib import admin
from .models import *





class PredAdmin(admin.ModelAdmin):
	list_display = ('patient', 'Gender', 'Polyuria', 'Polydipsia',  'Sudden_weight_loss','Partial_paresis', 'Polyphagia', 'Irritability',
	 'Alopecia', 'Visual_blurring','Weakness', 'Prediction')

class PredAdmin2(admin.ModelAdmin):
	list_display = ('username', 'Gender', 'Polyuria', 'Polydipsia',  'Sudden_weight_loss','Partial_paresis', 'Polyphagia', 'Irritability',
	 'Alopecia', 'Visual_blurring','Weakness', 'Prediction')

admin.site.register(Profile)
admin.site.register(Prediction, PredAdmin)
admin.site.register(Prediction2, PredAdmin2)
