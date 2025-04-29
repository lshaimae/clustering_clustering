import streamlit as st
from pages.k_means import kmeans_tab
from pages.cahclust import cah_tab
import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler ,MinMaxScaler
def get_data():
    """Function to import data"""
    st.header("Data Import")
    data=None
    upload_file=st.file_uploader("Upload an Excel file :",type=["xls","xlsx"])
    manual_input=st.text_area("Enter Data manually :",help="Each row ,values separated by spaces \n All rows must have the same number of columns.")
    if upload_file is not None:
        try:
            df = pd.read_excel(upload_file, header=None)
            df = df.dropna(axis=1, how='all').dropna(how='all')
            df = df.apply(pd.to_numeric, errors='coerce')
            df = df.iloc[:, 1:] if df.shape[1] > 1 else df
            df = df.dropna()
            data = df.to_numpy()
            st.success("Data imported successfully!")
        except Exception as e:
            st.error(f"Error while importing: {e}")
    elif manual_input :
        try:
            lines=manual_input.strip().split('\n')
            matrix=[list(map(float,line.strip().split())) for line in lines if line.strip()]
            data=np.array(matrix)
            if not all(len(row)==len(data[0]) for row in data):
                raise ValueError("All rows must have the same numbers of columns.")  
            st.success("Manual Data entry successful !")
        except Exception as e:
            st.error(f"Input error :{e}")
    if data is not None:
        with st.expander("View data"):
            st.write("Shape :",data.shape)
            st.dataframe(pd.DataFrame(data))
    return data
def normalization_tab(data):
    st.header("Preprocessing")
    if data is None:
        st.warning("Please import data first !")
        return None
    normalize = st.radio("Normalize Dta ?",
                        ["Yes", "No"],
                        index=1,
                        key="normalize_choice")
    if normalize == "Yes":
        method = st.selectbox("Normalization Method",
                            ["Standard Scaler (mean=0, std=1)",
                             "MinMax Scaler (0-1 range)"],
                            key="norm_method")
            
        if method == "Standard Scaler (mean=0, std=1)":
                scaler = StandardScaler()
        else:
                scaler = MinMaxScaler()
        
        processed_data = scaler.fit_transform(data)
        scaler_used = method
        st.subheader("After normalization :")
        st.dataframe(pd.DataFrame(processed_data).head(len(processed_data)))
    else:
        processed_data = data
        scaler_used = "No Normalization"
        
    return processed_data,scaler_used
def clustering_page(go_to):
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
            
            /* Animation de fond identique à home_page */
            .stApp {
                background: linear-gradient(135deg, #6e8efb 0%, #4a6cf7 100%) !important;
                min-height: 100vh;
                position: relative;
                overflow: hidden;
            }
            
            .stApp::before {
                content: "";
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
                animation: pulse 15s infinite linear;
                z-index: 0;
            }
            
            @keyframes pulse {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            /* Styles pour le contenu */
            .stApp > div:first-child > div:first-child > div:first-child > div:first-child {
                background: rgba(255,255,255,0.85);
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 2rem;
                margin: 2rem auto;
                max-width: 95%;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            }
            
            /* Navbar style */
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px 10% !important;
                width: 100%;
                box-shadow:none !important;
                position: relative;
                background: transparent !important;
                backdrop-filter: none !important;
                margin-top:0 !important;
            }
            
            .navbar-name {
                font-weight: 700;
                font-size: 1.3rem;
                color: white;
            }
            
            .navbar-links {
                display: flex;
                gap: 20px !important;
            }
            
            .navbar-link {
                color: white !important;
                font-weight: 500;
                font-size: 1.1rem;
                transition: all 0.3s;
            }
            
            .navbar-link:hover {
                opacity: 0.8;
                text-decoration:underline;
                color :white !important;
            }
            
            /* Suppression des éléments Streamlit par défaut */
            [data-testid="stSidebar"],
            [data-testid="stHeader"] {
                display: none !important;
            }
            
            /* Style pour les tabs */
            .stTabs [role="tablist"] {
                background: rgba(255,255,255,0.9);
                border-radius: 10px;
                padding: 5px;
            }
            
            .stTabs [role="tab"] {
                color: #4a6cf7;
                font-weight: 600;
            }
            
            .stTabs [aria-selected="true"] {
                background-color: #4a6cf7;
                color: white !important;
            }
        </style>
        
        <!-- Navbar -->
        <nav class="navbar">
            <div class="navbar-name">By LIKOUK Chaimae</div>
            <div class="navbar-links">
                <a href="?page=home" class="navbar-link" target="_self">Home</a>
                <a href="?page=clustering" class="navbar-link" target="_self">Clustering</a>
                <a href="?page=about" class="navbar-link" target="_self">About</a>
                <a href="?page=contact" class="navbar-link" target="_self">Contact</a>
            </div>
        </nav>
        """,
        unsafe_allow_html=True
    )
    
    st.title("Clustering Analysis")
    
    tab1, tab2,tab3 = st.tabs(["Data Import", "Preprocessing","Clustering"])
    with tab1:
         data=get_data()
         if data is not None:
             st.session_state['raw_data']=data
    with tab2:
        if 'raw_data' in st.session_state:
            processed_data,scaler_info=normalization_tab(st.session_state['raw_data'])
            if processed_data is not None:
                st.session_state['processed_data']=processed_data
                st.session_state['scaler_info']=scaler_info
            else:
                st.warning("Please import data first in 'Data Import' to start Clustering ")
    with tab3:
        if 'raw_data' not in st.session_state and 'processed_data' not in st.session_state:
            st.warning("Please import data in the 'Data Import' tab first")
        else:
            current_data = st.session_state.get('processed_data', st.session_state.get('raw_data'))
            
            if current_data is not None:
                st.subheader("Clustering Methods")
                st.info(f"Data preparation: {st.session_state.get('scaler_info', 'Raw data (no normalization)')}")
                
                tab_kmeans, tab_hierarchical = st.tabs(["K-means", "Hierarchical Clustering"])
                
                with tab_kmeans:
                    kmeans_tab(current_data)
                
                with tab_hierarchical:
                    cah_tab(current_data)
            else:
                st.warning("Please import data first in 'Data Import' to strat Clustering")


            