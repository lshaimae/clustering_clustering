import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
import scipy.cluster.hierarchy as sch 
from sklearn.metrics import silhouette_score , silhouette_samples   
from mpl_toolkits.mplot3d import Axes3D

def euclidean_dist(a,b):
  """ Compute the Euclidean distance between points"""
  return np.sqrt(np.sum((a-b)**2,axis=1))

def manhattan_dist(a,b):
  """ Compute the Manhattan distance between points"""
  return np.sum(np.abs(a-b),axis=1)

def chebychev_dist(a,b):
  """ Compute the Chebychev distance between points"""
  return np.max(np.abs(a-b),axis=1)

def minkowski_dist(a,b,p=2):
  """ Compute the Minkowski distance between points"""
  return np.sum(np.abs(a-b)**p,axis=1)**(1/p)

def cosine_dist(a,b):
  """ Compute the cosine distance between points"""
  return 1 - np.dot(a,b)/((np.linalg.norm(a,axis=1)*(np.linalg.norm(b,axis=1))))

def choose_k(data):
  """ Asking the user of the number of clusters K"""
  while True:
    try:
      #choose the number of clusters K
      k=int(input("Choose the number of clusters K :"))
      if k>len(data):
        print("The number of clusters should be less than the number of data points {len(data)}!")
        continue
      return k
    except ValueError :
      print("Please enter a valid number ")
 
def initialize_centroides(k,data):
  """Initialize centroides randomly"""
  indices=np.random.choice(len(data),k,replace=False) #randomly select k centroides from 0 to len(data)-1 making sure we don't select the same point multiple time
  centroides=data[indices]
  return centroides

def choose_distance():
  """ Asking the user of the distance metric to use"""
  #choose a distance metric 
  print("choose a distance metric :\n1 -Euclidien\n2 -Manhattan\n3 -Chebychev\n4 -Minkowski\n5 -Cosine")
  choice=int(input("enter 1,2 or 3:"))
  if choice==1:
    return euclidean_dist,"euclidean"
  elif choice==2:
    return manhattan_dist,"manhattan"
  elif choice==3:
    return chebychev_dist,"chebychev"
  elif choice==4:
    return minkowski_dist,"minkowski"
  elif choice==5:
    return cosine_dist,"cosine"
  else:
    print("Invalid choice,defaulting to Euclidean distance.")
    return euclidean_dist,"euclidean"
  
def assign_clusters(data, centroids, distance_func):
    """Assign each data point to the nearest cluster using the chosen distance"""
    clusters = []
    for point in data:
        # Compute the distance between the point and each centroid
        distance = np.array([distance_func(point[np.newaxis, :], centroid[np.newaxis, :])[0] for centroid in centroids])
        cluster_index = np.argmin(distance)  # Find the nearest centroid
        clusters.append(cluster_index)
    return np.array(clusters)


def update_centroids(centroides,data,clusters,distance_type):
  """Update the centroids of each cluster"""
  new_centroids=[]#list of new centroids
  for cluster_index in range(len(centroides)):
    #select all points belonging to the current cluster
    clusters_point=data[clusters==cluster_index]
    #if the cluster has points we recalculate the centroid
    if len(clusters_point)>0:
      if distance_type in["euclidean","manhattan","minkowski"]:
       nv_centroid=np.mean(clusters_point,axis=0)
      elif distance_type in ["chebychev","cosine"]:
        nv_centroid=np.median(clusters_point,axis=0)
      else :
        #if distance type is invalid,default to mean
        nv_centroid=np.mean(clusters_point,axis=0)
    else:
    #if the cluster is empty ,we keep the old centroid
      nv_centroid=centroides[cluster_index]

    new_centroids.append(nv_centroid)
  return np.array(new_centroids)
   
def k_means(data, k, distance_func, distance_type="euclidean", max_iters=100):
  #initialization 
  centroids=initialize_centroides(k,data)
  for i in range(max_iters):
    #assign clusters 
    clusters=assign_clusters(data, centroids, distance_func)
    #update centroids
    new_centroides=update_centroids(centroids,data,clusters,distance_type)
    #check for convergence 
    if np.allclose(new_centroides,centroids,atol=1e-4):
      convergence_msg=f"convergence reached after {i+1} iterations."
      break
    centroids=new_centroides
  else :
    convergence_msg=f"No convergence after {max_iters} iterations."
  return centroids,clusters,convergence_msg

def plot_clusters(data, clusters, centroids):
    """Plot the data points and centroids"""
    fig, ax = plt.subplots(figsize=(3, 3))
    # Plot des points
    scatter = ax.scatter(data[:, 0], data[:, 1], c=clusters, cmap='magma', marker='o', s=40, alpha=0.6,label="observation")
    # Plot des centroïdes
    ax.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=15, label="Centroids")
    ax.set_title("K-means clustering (2D)")
    ax.legend()
    return fig  

from mpl_toolkits.mplot3d import Axes3D

def plot_kmeans_3d(data, clusters, centroids=None):
    """Plot clusters in 3D if data has 3 dimensions"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    colors = plt.cm.get_cmap("Blues", len(np.unique(clusters)))
    
    for i in np.unique(clusters):
        cluster_points = data[clusters == i]
        ax.scatter(cluster_points[:, 0], cluster_points[:, 1], cluster_points[:, 2], 
                   label=f"Cluster {i+1}", alpha=0.7, s=60, color=colors(i))
    
    if centroids is not None:
        ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], 
                   marker='X', c='red', s=200, label='Centroids')
    
    ax.set_title("K-means Clustering (3D)")
    ax.legend()
    fig.tight_layout()
    return fig

def find_best_k(data, distance_func, distance_type="euclidean", k_max=10):
    """Return the best number of clusters K using silhouette score (no plot)."""
    k_range = range(2, min(len(data), k_max))
    best_k, best_score = 2, -1
    for k_val in k_range:
        centroids, labels, _ = k_means(data, k_val, distance_func, distance_type)
        try:
            score = silhouette_score(data, labels, metric=distance_type)
            if score > best_score:
                best_k, best_score = k_val, score
        except Exception:
            continue  # sometimes silhouette_score fails 
    return best_k, best_score


