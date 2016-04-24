from __future__ import unicode_literals
from django.db import models
from math import sqrt
import random


class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    imid = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    year = models.IntegerField()
    series_id = models.CharField(max_length=30)
    series_name = models.CharField(max_length=300)
    series_episode = models.IntegerField()
    series_season = models.IntegerField()
    rating = models.DecimalField(max_digits=11, decimal_places=10)
    rating_count = models.IntegerField()
    release_date = models.CharField(max_length=30)
    plot = models.CharField(max_length=1000)
    

class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=200)
    movie_ref = models.ForeignKey(Movies, db_column='movie_ref')


"""
To Use this call ActorManager.objects.count_avg()
django.db connection is representing the db connection
The connection.cursor creates a cursor object on which 
the raw SQL query is executed
Results(count,avg,fullname) are appended to an empty list
"""
class ActorManager(models.Manager):
    def count_avg(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT COUNT(*),
            AVG(clusterapp_movies.rating),
            fullname 
            FROM clusterapp_actors 
            INNER JOIN clusterapp_movies 
            ON clusterapp_actors.movie_ref = clusterapp_movies.id 
            GROUP BY `fullname` having COUNT(*) >1
            """)
        result_set=cursor.fetchall()
        print type(result_set)
        return result_set
        #result_list = []
        #for item in cursor.fetchall():
            # p = self.model(fullname=item[2])
            # p.count = item[0]
            # p.avg = int(item[1])
            # result_list.append(p)
        #return result_list    


class Actors(models.Model):     
    id = models.IntegerField(primary_key=True)
    fullname = models.CharField("actors full name", max_length=200)
    movie_ref = models.ForeignKey(Movies, db_column='movie_ref')
    objects = ActorManager()


class Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.CharField("genre type", max_length=200, db_column='genre')
    movie_ref = models.ForeignKey(Movies, db_column='movie_ref')


class Iris(models.Model):
    sepal_length = models.IntegerField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    species = models.CharField(max_length=15)

"""Get all
Stored reference to a get all objects query for each Model
"""

Movies_all = Movies.objects.all()
Directors_all = Director.objects.all()
Actors_all = Actors.objects.all()
Genres_all = Genres.objects.all()
Iris_all = Iris.objects.all()


"""Get Euclidean Distance between Points
Euclidean function is used to get the Euclidean distance between two samples, or centroids and samples.
It is used to measure membership of elements to a given cluster based on proximity to calculated centroid.
Input: Two points/sets of values (p0,p1) (q0,q1)
Output: Distance between Points
"""


def euclidean(p,q):
    diff_v1 = q[0]-p[0]
    diff_v2 = q[1]-p[1]
    sq_diff1 = diff_v1**2
    sq_diff2 = diff_v2**2
    sum = sq_diff1 + sq_diff2
    sqsum = sqrt(sum)
    return sqsum


"""Normalise List of Values
Normalise function takes values from an list/array of values and
Input: List of values
Output: New array with all values normalised to values between 0 and 1
"""


def norm(d):
        min_X = min(d)
        max_X = max(d)
        new_values = []
        for i,val in enumerate(d):
            top = float(val-min_X)
            bottom = float(max_X-min_X)
            normalized = float(top/bottom)
            new_values.append(normalized)
        return new_values

"""K means Algorithm
k_means takes a list of paired values and assigns them to groups(clusters) based on their proximity to calculated
centroids.
Firstly the data is parsed to find the range of values in the distribution, from this a set of centroids are calculated.
Then the algorithm gets the Euclidean distance between each centroid and a row in the data, compares it to the
 and assigns membership to a list.
The second part of the algorithm calculates an average of the members

Due to the fact that the data is static, a list comprehension 
Input: List of paired values from database
Parameters: Euclidean Distance Function, K number of clusters - provided by user input
Step 1: Choose number of clusters (K; provided by user)
Step 2: Set the initial partition, and centroids
Step 3: Repeat until convergence:
    Step 4: 
"""


def k_means(data, distance=euclidean, k=4):
    #Basic preprocessing
    rows = []
    for i in data:
        rows.append(i[:2])

    #Create initial partition using the upper and lower bounds of the data
    euclid_range = [(min([row[i] for row in rows]), max([row[i] for row in rows]))
    
                    for i in range(len(rows[0]))]
    #Initial mean vectors/centroids                
    centroids = [[random.random()*(euclid_range[i][1]-euclid_range[i][0])+euclid_range[i][0]
    
                for i in range(len(rows[0]))] for j in range(k)]
    #Assignment Step            
    last_matches = None
    for t in range(29):
        print 'Iteration %d' % t
        #Create list of lists for each K
        groups = [[] for i in range(k)]

        for j in range(len(rows)):
            #create counter through data items
            row = rows[j]

            count_match = 0
            for i in range(k):

                d = distance(centroids[i], row)

                if d < distance(centroids[count_match], row):
                    count_match = i

            groups[count_match].append(j)

        if groups == last_matches: break
        last_matches = groups
        """Update Step
           The goal of this step is to reduce the total sum of squared distances          
        """
        for i in range(k):

            averages = [0.0]*len(rows[0])

            if len(groups[i])>0:

                for rowid in groups[i]:

                    for m in range(len(rows[rowid])):
                        averages[m] += rows[rowid][m]

                        mean=len(groups[i])
                for j in range(len(averages)):

                    averages[j] /= mean

                centroids[i] = averages
        coordinates = [[data[index] for index in count_match] for count_match in groups]

    return coordinates


