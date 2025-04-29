import streamlit as st

def about_page():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        /* Styles globaux */
        html, body, [data-testid="stAppViewContainer"] {
            margin: 0 !important;
            padding: 0 !important;
            font-family: 'Poppins', sans-serif !important;
        }
        
        /* Animation de fond */
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
        /* Styles spécifiques à la page About */
        .about-container {
            background: rgba(255,255,255,0.85);
            backdrop-filter: blur(10px);
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        
        .about-title {
            color: #4a6cf7;
            text-align: center;
        }
        
        .highlight {
            color: #4a6cf7;
            font-weight: 600;
        }
        /* Masquer les éléments par défaut de Streamlit */
        [data-testid="stSidebar"],
        [data-testid="stHeader"] {
            display: none !important;
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
    <!-- Contenu About -->
    <div class="about-container">
        <h1 class="about-title">About Clustering App</h1>
        <div style="margin-bottom: 2rem;">
            <h2>What is this app?</h2>
            <p>A simple tool to <span class="highlight">group your data automatically</span>.</p>
        </div>
        <div style="margin-bottom: 2rem;">
            <h2>Key Features</h2>
            <ul>
                <li>Works with <span class="highlight">Excel</span> files</li>
                <li>Two clustering methods <span class="highlight">K-means & CHA</span></li>
            </ul>
        </div>
        <div>
            <h2>Who made this?</h2>
            <p>Created by <span class="highlight">Chaimae Likouk</span>.</p>
        </div>
    </div>
    
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
        " target="_self">Try It Now</a>
    </div>
    <script>
        // Script pour gérer la navigation
        document.querySelectorAll('.navbar-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                window.history.pushState({}, '', e.target.href);
                window.dispatchEvent(new Event('popstate'));
            });
        });
    </script>
    """, unsafe_allow_html=True)
