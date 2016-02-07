from __future__ import unicode_literals
from math import sqrt
import random
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

def pearson(v1,v2):
        
    #sums
    #distance(clusters[i],row) are passed as v1,v2
    #row=rows(counter)
    #counter in clusters=[[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0]
    sum1=sum(v1)
    sum2=sum(v2)
    #print(sum1)
    #sums of the sqs
    sum1Sq=sum([pow(v,2) for v in v1])
    sum2Sq=sum([pow(v,2) for v in v2])
    
    #sum of products
    pSum=sum([v1[i]*v2[i] for i in range(len(v1))])
    
    #calculate pearson R
    ##NOTE CHANGED - after PSUM to +
    ##AND len(v1) changed to len(a)
    a=(1,2)
    num=pSum-(sum1*sum2/len(v1))
    den=sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
    if den==0: return 0
    
    return 1.0-num/den

def euclidean(p,q):
    dist=sqrt(q[0]-p[0])**2 + (q[1]-p[1])**2
    return dist


def kmeans(rows,distance=pearson,k=4):
    
    
    #ranges finds the min and max to use as initial partition
    ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows]))

    for i in range(len(rows[0]))] 
    print ranges



    #create k randomly placed centroids within len of 'data'
    clusters=[[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0]
    
    for i in range(len(rows[0]))] for j in range(k)]
    #print clusters
    
    lastmatches=None
    for t in range(5):
       # print 'Iteration %d' % t

        bestmatches=[[] for i in range(k)]

        #print bestmatches
        #find which centroid is the closts to each row
        for j in range(len(rows)):
            #print j
            ##STILL HOLDING VALUES
            row=rows[j]
            ##-------------------

            bestmatch=0
            for i in range(k):
                ##apply pearson to clusters[0],row
                d=distance(clusters[i],row)
                ##if pearson(randomInitCent) LESSTHAN pearson(cluster[0],row)
                ##iterate bestmatch :. 
                if d<distance(clusters[bestmatch],row):
                    bestmatch=i
                #print i
                #print 'iter'
                #print d
               # print distance(clusters[bestmatch],row)
               # print 'iter'
            bestmatches[bestmatch].append(j)

            #print j
            #print (row[j]
            

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
             #           print(avgs)
                    for j in range(len(avgs)):
                        avgs[j]/=len(bestmatches[i])
                    clusters[i]=avgs
           # for index,elem in enumerate(bestmatches):
            #    print(index,elem)
                
        return bestmatches

def postprocess(request):
    coordinates=[ [(1,1)], [], [3.5,5], [(1.5,2),(3,4),(5,7),(4.5,5),(3.5,4.5)]]
    