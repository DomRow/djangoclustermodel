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


class Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.CharField("genre type", max_length=200, db_column='genre')
    movie_ref = models.ForeignKey(Movies, db_column='movie_ref')


class Actors(models.Model):     
    id = models.IntegerField(primary_key=True)
    fullname = models.CharField("actors full name", max_length=200)
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
    #Differences
    diff_v1 = q[0]-p[0]
    diff_v2 = q[1]-p[1]
    #Squares - differences square
    sq_diff1 = diff_v1**2
    sq_diff2 = diff_v2**2
    #Sum of sq diffs
    sum = sq_diff1 + sq_diff2
    #Square root of sum
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
Parameters: Euclidean Distance Function, K number of clusters
"""


def k_means(data, distance=euclidean, k=4):
    
    rows = []
    for i in data:
        rows.append(i[:2])

    euclid_range = [(min([row[i] for row in rows]), max([row[i] for row in rows]))
    
                    for i in range(len(rows[0]))]

    centroids = [[random.random()*(euclid_range[i][1]-euclid_range[i][0])+euclid_range[i][0]
    
                for i in range(len(rows[0]))] for j in range(k)]

    last_matches = None
    for t in range(3):
        print 'Iteration %d' % t

        groups = [[] for i in range(k)]

        for j in range(len(rows)):

            row = rows[j]

            count_match = 0
            for i in range(k):

                d = distance(centroids[i], row)

                if d < distance(centroids[count_match], row):
                    count_match = i

            groups[count_match].append(j)

        if groups == last_matches: break
        last_matches = groups

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


