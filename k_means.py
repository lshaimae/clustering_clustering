import streamlit as st
import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
from kmeans import (plot_clusters, plot_kmeans_3d,euclidean_dist,
                    manhattan_dist,chebychev_dist,minkowski_dist,cosine_dist,k_means,find_best_k
                    ) 
from export_results import export_results

def kmeans_tab(data):
    """Handle all K-means clustering functionality"""
    st.header("K-means Clustering")
    
    # Distance metrics mapping
    dist_map = {
        "Euclidean": euclidean_dist,
        "Manhattan": manhattan_dist,
        "Chebychev": chebychev_dist,
        "Minkowski": minkowski_dist,
        "Cosine": cosine_dist,
    }
    
    col1, col2 = st.columns(2)
    with col1:
        k = st.slider("Number of Clusters (K)", 2, len(data), 2)
    with col2:
        dist_choice = st.selectbox("Distance Metric", list(dist_map.keys()),key="mertric_dist_kmeans", help=
         "- Euclidean: Straight-line distance\n"
         "- Manhattan: Sum of absolute differences\n"
         "- Chebychev: Max coordinate difference\n"
         "- Minkowski: Generalized distance \n"
         "- Cosine: Based on the angle between vectors")
    if st.button("Find Optimal K"):
            best_k, best_score = find_best_k(data, dist_map[dist_choice], dist_choice.lower())
            st.success(f"Best K (based on silhouette score): {best_k} with score {best_score:.4f}")
    if st.button("Run K-means"):
        centroids, clusters, msg = k_means(data, k, dist_map[dist_choice], dist_choice.lower())
        st.success(msg)
        
        st.subheader("2D Cluster Plot")
        fig_2D=plot_clusters(data, clusters, centroids)
        st.pyplot(fig_2D,use_container_width=False)
        
        fig_3d = plot_kmeans_3d(data, clusters, centroids)
        
        
       

        best_k=None
        best_score=None
        pdf = export_results(data, clusters,fig_2D, centroids, fig_3d, method="kmeans", msg=msg,best_k=best_k,
        best_score=best_score)
        st.download_button("Download PDF Report", data=pdf, file_name="kmeans_results.pdf")
