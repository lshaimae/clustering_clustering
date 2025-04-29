import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
import scipy.cluster.hierarchy as sch 
from sklearn.metrics import silhouette_score , silhouette_samples   
from mpl_toolkits.mplot3d import Axes3D
from fpdf import FPDF
import io
import tempfile
import os
from kmeans import k_means
from clustering_heirarchie import hierarchical_clustering 
def export_results(data, clusters=None, fig=None, centroids=None,fig_dendro3d=None,method="kmeans",msg=None,best_k=None,best_score=None):
    df = pd.DataFrame(data)
    if clusters is not None:
     df["cluster"] = np.array(clusters) + 1
     df["cluster"] = df["cluster"].astype(int)
    else:
     df["cluster"] = -1  

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    #data before clustering
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 102, 255)
    pdf.cell(0,10,"Before Clustering :",ln=True,align="C")
    pdf.set_font("Arial",size=11)
    pdf.set_text_color(0,0,0)
    intro_text=(
       "The following table presents the raw data prior to any clustering analysis.\n"
"Each observation is described by its corresponding variables, representing the original features of the dataset without any transformation or grouping.\n"
"At this stage, no clustering algorithm has been applied, and therefore no cluster assignment has been made yet.\n"
"This raw view allows us to understand the structure and distribution of the data in its initial form, which serves as a reference point before any pattern discovery or segmentation takes place.\n\n"
    )
    pdf.multi_cell(0,7,intro_text)
    pdf.ln(2)
    for i,row in enumerate(data):
      row_str=",".join([f"{x:.2f}" for x in row])
      pdf.multi_cell(0,6,f"Observation {i+1:2d} : [{row_str}]")
    pdf.ln(10)
    #page results of clustering
    pdf.set_font("Arial","B",12)
    pdf.set_text_color(0,102,255)
    pdf.cell(0, 10, "Results of Clustering", ln=True, align="C")
    pdf.set_font("Arial", "I", 11)
    pdf.set_text_color(80, 80, 80)
    intro_text=("After reviewing the initial dataset, we proceed with a clustering analysis to uncover hidden patterns and reveal natural groupings within the data.")
    pdf.multi_cell(0, 7,
    "Clustering is an unsupervised learning technique that enables the identification of similarities among observations based on their features, without relying on predefined labels.\n"
    "This process helps to segment the dataset into distinct groups, each sharing common characteristics, which can be valuable for interpretation, decision-making, or further analysis.\n"
    "The 2D plot presents a simplified view of the clusters, typically using dimensionality reduction techniques such as PCA, "
    "to highlight how observations are grouped. \n\n" 
)
    pdf.ln(3)
    pdf.add_page()
    #save temporary the plot
    if fig:  # Vérifie si le graphique 2D existe
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_img:
            fig.savefig(tmp_img.name, format='png')
            tmp_img_path = tmp_img.name
        pdf.set_font("Arial", "B", 16)
        pdf.set_text_color(0, 102, 255)

        # Choisir le titre en fonction de la méthode (K-means ou CAH)
        if method == "Kmeans":
            pdf.cell(0, 10, "2D Plot (K-means Clusters)", ln=True)
        elif method == "CAH":
            pdf.cell(0, 10, "2D Plot (CAH Clusters)", ln=True)

        pdf.image(tmp_img_path, x=10, y=5, w=180)  # Position y=30 pour le graphique 2D
        os.remove(tmp_img_path)
    pdf.ln(85)
    # 3D plot (dendrogramme ou autre, juste en dessous du graphique 2D)
    if fig_dendro3d:  # Si tu as un graphique 3D
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_img_3d:
            fig_dendro3d.savefig(tmp_img_3d.name, format='png')
            tmp_img_path_3d = tmp_img_3d.name
        pdf.set_font("Arial", "B", 16)
        pdf.set_text_color(0, 102, 204)

        # Choisir le titre en fonction de la méthode
        if method == "Kmeans":
            pdf.cell(0, 10, "3D Plot (K-means Clusters)", ln=True)

        pdf.image(tmp_img_path_3d, x=10,y=140,w=180)  # Position y=140 pour le graphique 3D, juste en dessous du 2D
        os.remove(tmp_img_path_3d)
  
    # Results of clusters — only if multiple clusters exist
    if clusters is not None and len(set(clusters)) > 1:
        pdf.add_page()
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(0, 102, 255)
        pdf.cell(0,10, "Observations and Clusters:", ln=True,align="C")
        pdf.set_font("Arial", size=10)
        pdf.set_text_color(0, 0, 0)

        for i , row in df.iterrows():
            observation=[round(val,3) for val in row[:-1].tolist()]
            line=f"Observation {i+1:2d} : {observation} -> Cluster {row['cluster']}"
            pdf.multi_cell(0,6,line)


    # Centroids
    if centroids is not None and method.lower()=="kmeans":
        centroids_df = pd.DataFrame(centroids)
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(0, 102, 255)
        pdf.cell(0,10, "Centroids of Clusters:", ln=True,align="C")
        pdf.set_font("Arial", size=10)
        pdf.set_text_color(0, 0, 0)
        for i ,row in centroids_df.iterrows():
            centroid=[round(val,3) for val in row.tolist()]
            pdf.multi_cell(0,6,f"Cluster {i+1} :\n{centroid}")
    elif method.lower() == "cah":
       pdf.ln(50)
       pdf.set_font("Arial", "I", 10)
       pdf.set_text_color(255, 0, 0)
       pdf.multi_cell(0, 7, "Note: Centroids are not calculated for hierarchical clustering (CAH).")

    if msg:
      pdf.set_font("Arial", "I", 10)
      pdf.set_text_color(255, 0, 0)
      pdf.ln(3)
      pdf.multi_cell(0, 7, f"Clustering info: {msg}")

    if method == "kmeans" and best_k is not None and best_score is not None:
        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(0, 153, 0)  # Vert pour la réussite
        pdf.cell(0, 10, "Optimal Number of Clusters (Silhouette Score)", ln=True, align="C")
        pdf.set_font("Arial", "", 11)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 7, f"Best K (based on silhouette score): {best_k} with score {best_score:.4f}")
    # Save the PDF with a given filename
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    pdf_output = io.BytesIO(pdf_bytes)
    return pdf_output
   
