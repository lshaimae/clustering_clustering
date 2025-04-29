import streamlit as st
from streamlit.components.v1 import html

def home_page(go_to):
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        /* Reset complet - suppression de toutes les marges */
        html, body, [data-testid="stAppViewContainer"], 
        [data-testid="stAppViewBlockContainer"] {
            margin: 0 !important;
            padding: 0 !important;
            width: 100% !important;
            font-family: 'Poppins', sans-serif !important;
            overflow-x: hidden !important;
        }
        
        /* Animation de fond sur TOUTE la page */
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
        
        /* Contenu principal avec animations */
        .main-content {
            position: relative;
            z-index: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            height: calc(100vh - 100px);
            padding: 0 20px;
            color: white;
        }
        
        .hero-title {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            animation: fadeInDown 1s ease;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
            font-weight: 300;
            margin-bottom: 2.5rem;
            max-width: 800px;
            line-height: 1.6;
            opacity: 0.9;
            animation: fadeInUp 1s ease 0.3s both;
        }
        
        .cta-button {
            display: inline-block;
            background: white;
            color: #4a6cf7;
            padding: 0.8rem 2.5rem;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 50px;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            animation: fadeIn 1s ease 0.6s both;
            border: none;
            cursor: pointer;
        }
        
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Suppression des éléments Streamlit par défaut */
        [data-testid="stSidebar"],
        [data-testid="collapsedControl"],
        .stApp > header,
        .stApp > div:first-child > div:first-child > div {
            display: none !important;
            padding-top:0 !important;
        }
    </style>
    <script>
    function navigateToClustering() {
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: 'clustering'
        }, '*');
    }
    </script>
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
    
    <!-- Contenu principal -->
    <div class="main-content">
        <h1 class="hero-title">Welcome to Clustering App</h1>
        <p class="hero-subtitle">
            Simplify your data analysis with our clustering tool
        </p>
       <div style="text-align: center; margin-top: 2rem;">
        <a href="?page=clustering" style="
            background: white;
            color: #4a6cf7;
            padding: 0.8rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            display: inline-block;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        " target="_self">Start Clustering Now</a>
       </div>
    </div>

    <script>
    function handleNavClick(page) {
        // Méthode 1 : Pour Streamlit version récente
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            key: 'nav_change',
            value: page
        }, '*');
        
        // Méthode 2 : Alternative pour certaines configurations
        window.location.search = `?page=${page}`;
    }

    <script>
        // Script pour forcer le plein écran
        document.body.style.margin = '0';
        document.body.style.padding = '0';
    </script>
    """, unsafe_allow_html=True)