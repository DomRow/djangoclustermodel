from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
	help = 'Clusters numerical input'


	def definedata():
		data=[(2,3),(1,2),(3,4)]
		return data

	data=definedata()


	def kmeans(data):
		data2=data*2
		
		#return data2

