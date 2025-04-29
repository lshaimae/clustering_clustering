import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
import scipy.cluster.hierarchy as sch 
from kmeans import (euclidean_dist,chebychev_dist,minkowski_dist,manhattan_dist,cosine_dist)

def single_linkage_distance(cluster1,cluster2,data,distance_func):
  """ Compute the single linkage distance between two clusters """
  min_dist=float('inf')
  for i in cluster1:
    for j in cluster2:
      dist=distance_func(data[i][np.newaxis,:],data[j][np.newaxis,:])[0]#to access to numeric value only
      min_dist=min(min_dist,dist)
  return min_dist

def complete_linkage_distance(cluster1,cluster2,data,distance_func):
  """ Compute the complete linkage distance between two clusters"""
  max_dist=-float('inf')
  for i in cluster1:
    for j in cluster2:
      dist=distance_func(data[i][np.newaxis,:],data[j][np.newaxis,:])[0]
      max_dist=max(max_dist,dist)
  return max_dist

def average_linkage_distance(cluster1,cluster2,data,distance_func):
  """ Compute the average linkage distance between two clusters """
  sum_dist=0
  count=0
  for i in cluster1:
    for j in cluster2:
      dist=distance_func(data[i][np.newaxis,:],data[j][np.newaxis,:])[0]
      sum_dist+=dist
      count+=1
  return sum_dist/count

def ward_liaison(cluster1,cluster2,data,distance_func):
  """ Compute the Ward linkage distance between two clusters"""
  #extract points from clusters 
  points1=[data[i] for i in cluster1]
  points2=[data[i] for i in cluster2]
  #calcul clusters centroids 
  centroid1=np.mean(points1,axis=0)
  centroid2=np.mean(points2,axis=0)
  #calcul the length of clusters 
  size1=len(cluster1)
  size2=len(cluster2)
  #calcul the distance between centroids
  dist = distance_func(centroid1[np.newaxis, :], centroid2[np.newaxis, :])[0]
  #calcul Ward distance 
  ward_dist=(size1*size2)/(size1+size2) *(dist**2)
  return ward_dist

def initialize_clusters(data):
  """ Initialize each observation as a unique cluster """
  #create a cluster for each observation 
  clusters=[[i] for i in range(len(data))]
  return clusters

def merge_clusters(clusters, data,linkage_func, distance_func,centroids=None):
    """ Merge nearest clusters depending on the chosen distance """
    min_dist = float('inf')
    pair_to_merge = (None, None)
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            dist = linkage_func(clusters[i], clusters[j], data,distance_func)
            if dist < min_dist:
                min_dist = dist
                pair_to_merge = (i, j)
    
    i, j = pair_to_merge
    new_clusters = clusters[i] + clusters[j]  # Combine the two clusters
    
    # Update centroids if using Ward linkage
    if linkage_func == ward_liaison and centroids is not None:
        size1 = len(clusters[i])
        size2 = len(clusters[j])
        centroid1 = np.mean([data[idx] for idx in clusters[i]], axis=0)
        centroid2 = np.mean([data[idx] for idx in clusters[j]], axis=0)
        new_centroid = update_centroids_after_merging(centroid1, centroid2, size1, size2)
    else:
        # Merging without updating centroids
        pass 
    
    # Remove the old clusters and add the new one
    clusters.pop(max(i, j))  # Remove the larger index first
    clusters.pop(min(i, j))  # Remove the smaller index second
    clusters.append(new_clusters)  # Add the new merged cluster
    
    return clusters

def update_centroids_after_merging(centroid1,centroid2,size1,size2):
  """ Update the centroids of the two clusters after merging if using Ward linkage """
  new_centroid=(size1*centroid1+size2*centroid2)/(size1+size2)
  return new_centroid

def hierarchical_clustering(data,linkage_func,distance_func,max_clusters=1):
  """ Perform hierarchical clustering on the data"""
  #initialize the clusters
  clusters=initialize_clusters(data)
  #loop until only one cluster is left
  while len(clusters)>max_clusters:
    #merge the nearest two clusters
    clusters=merge_clusters(clusters,data,linkage_func,distance_func,centroids=None)
  return clusters

def plot_dendrogram(data,method='ward'):
  """ Plot a dendrogram of the clusters depending on the chosen distance"""
  method_map={
    "Single Linkage":"single",
    "Complete Linkage":"complete",
    "Average Linkage":"average",
    "Ward Linkage" :"ward"
  }
  scipy_method=method_map.get(method,"ward")
  fig,ax=plt.subplots(figsize=(4.5,4.5))
  #plot the dendrogram
  dendro=sch.dendrogram(sch.linkage(data,method=scipy_method),ax=ax)
  ax.set_title(f"Dendrogram using {method} ")
  ax.set_xlabel("Index of points")
  ax.set_ylabel("Distance")
  return fig
