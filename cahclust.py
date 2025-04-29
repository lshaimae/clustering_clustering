import streamlit as st
from clustering_heirarchie import (
    single_linkage_distance,complete_linkage_distance,average_linkage_distance,ward_liaison
    ,plot_dendrogram,hierarchical_clustering
)
from kmeans import (
    euclidean_dist,manhattan_dist,minkowski_dist,chebychev_dist,cosine_dist
)
from export_results import export_results

def cah_tab(data):
    """Handle all Hierarchical Clustering functionality"""
    st.header("Hierarchical Clustering (CAH)")
    
    # Distance and linkage mappings
    dist_map = {
        "Euclidean": euclidean_dist,
        "Manhattan": manhattan_dist,
        "Chebychev": chebychev_dist,
        "Minkowski": minkowski_dist,
        "Cosine": cosine_dist,
    }
    
    linkage_map = {
        "Single Linkage": single_linkage_distance,
        "Complete Linkage": complete_linkage_distance,
        "Average Linkage": average_linkage_distance,
        "Ward Linkage": ward_liaison
    }
    
    col1, col2 = st.columns(2)
    with col1:
        dist_choice = st.selectbox("Distance Metric", list(dist_map.keys()),key="distance_metric_selector", help=
         "- Euclidean: Straight-line distance\n"
         "- Manhattan: Sum of absolute differences\n"
         "- Chebychev: Max coordinate difference\n"
         "- Minkowski: Generalized distance \n"
         "- Cosine: Based on the angle between vectors")
    with col2:
        linkage_method = st.selectbox("Linkage Method", list(linkage_map.keys()),key="cah_linkage_method", help=
         "- Single Linkage: Minimum distance between points in clusters\n"
         "- Complete Linkage: Maximum distance between points in clusters\n"
         "- Average Linkage: Average of all pairwise distances\n"
         "- Ward Linkage: Minimizes variance within clusters ")
    
    if st.button("Run Hierarchical Clustering"):
        distance_func = dist_map[dist_choice]
        method_func = linkage_map[linkage_method]
        
        # Perform clustering
        hierarchical_clustering(data, method_func, distance_func)
        
        # Visualization
        st.subheader("Dendrogram")
        fig = plot_dendrogram(data, linkage_method)
        st.pyplot(fig,use_container_width=False)
        
        # Export
        pdf = export_results(data, None, fig, None, method="CAH")
        st.download_button("Download PDF Report", data=pdf, file_name="cah_results.pdf")