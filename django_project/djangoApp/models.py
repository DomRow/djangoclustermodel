from __future__ import unicode_literals
from math import sqrt
import random,json
from django.db import models



class Movies(models.Model):
	id=models.IntegerField(primary_key=True)
	imid=models.CharField(max_length=50)
	title=models.CharField(max_length=50)
	type=models.CharField(max_length=50)
	year=models.IntegerField()
	series_id=models.CharField(max_length=30)
	series_name=models.CharField(max_length=300)
	series_episode=models.IntegerField()
	series_season=models.IntegerField()
	rating=models.DecimalField(max_digits=11,decimal_places=10)
	rating_count=models.IntegerField()
	release_date=models.CharField(max_length=30)
	plot=models.CharField(max_length=1000)

class Director(models.Model):
	id=models.IntegerField(primary_key=True)
	fullname=models.CharField(max_length=200)
	movie_id=models.IntegerField()

class Genres(models.Model):
	id=models.IntegerField(primary_key=True)
	genre=models.CharField(max_length=30)
	movie_id=models.IntegerField()

class Actors(models.Model):		
	id=models.IntegerField(primary_key=True)
	fullname=models.CharField(max_length=200)
	movie_id=models.IntegerField()



def euclidean(p,q):
    #Differences - (x2-x1) (y2-y1)
    diffv1=q[0]-p[0]
    diffv2=q[1]-p[1]
    #Squares - differences square
    sqdiff1=diffv1**2
    sqdiff2=diffv2**2
    #Sum of sq diffs
    sum=sqdiff1+sqdiff2
    #Square root of sum
    sqsum=sqrt(sum)
    return sqsum


def norm(d):
    #Normalize values
        minX=min(d)
        maxX=max(d)
        newvals=[]
        for i,val in enumerate(d):
            #Xi-min(x)
            top=float(val-minX)
            bottom=float(maxX-minX)
            normalized=float(top/bottom)
            newvals.append(normalized)
        return newvals

def kmeans(rows,distance=euclidean,k=4):
    
    
    #ranges finds the min and max to use as initial partition
    ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows]))

    for i in range(len(rows[0]))] 

    #create k randomly placed centroids within len of 'data'
    clusters=[[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0]
    
    for i in range(len(rows[0]))] for j in range(k)]
        
    lastmatches=None
    for t in range(5):
       #print 'Iteration %d' % t

        bestmatches=[[] for i in range(k)]

        #find which centroid is the closts to each row
        for j in range(len(rows)):
            
            row=rows[j]
            
            bestmatch=0
            for i in range(k):
                ##apply pearson to clusters[0],row
                d=distance(clusters[i],row)
                ##if pearson(randomInitCent) LESSTHAN pearson(cluster[0],row)
                ##iterate bestmatch :. 
                if d<distance(clusters[bestmatch],row):
                    bestmatch=i
                
            bestmatches[bestmatch].append(j)

            
        if bestmatches==lastmatches: break
        lastmatches=bestmatches
        
        #move centroids to the avg of memebers
        for i in range(k):
            avgs=[0.0]*len(rows[0])
            if len(bestmatches[i])>0:
                #print(len(bestmatches[i]))
                for rowid in bestmatches[i]:
                    for m in range(len(rows[rowid])):
                        avgs[m]+=rows[rowid][m]
                    for j in range(len(avgs)):
                        avgs[j]/=len(bestmatches[i])
                    clusters[i]=avgs
        coordinates = [[rows[index] for index in bestmatch] for bestmatch in bestmatches]
        return bestmatches,rows,coordinates

