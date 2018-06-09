#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:10:21 2018

@author: vishal
"""

from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()

# bar chart for histogram


from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)
plt.bar([x - 4 for x in histogram.keys()],histogram.values(),8)

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])

plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()



# another example

mentions = [500, 505]
years = [2013, 2014]
plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")
           
plt.axis([2012.5,2014.5,499,506])
plt.title("Look at the 'Huge' Increase!")
plt.show()


plt.axis([2012.5,2014.5,0,550])
plt.title("Not So Huge Anymore")
plt.show()