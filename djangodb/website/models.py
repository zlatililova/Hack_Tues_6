from django.db import models


class Park(models.Model):
	#name = models.CharField(max_length = 100)
	neigh = models.CharField(max_length = 100)
	str = models.CharField(max_length = 100)
	num = models.IntegerField()
	phone = models.IntegerField()
	#img = models.ImageField() #dg doc
	
	#def __str__(self):
	#	return 'кв. '+ self.neigh + " " + self.str 
	 
