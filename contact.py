import streamlit as st
def contact_page():
    st.markdown(
        """
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
            
            /* Animation de fond identique à home_page */
            .stApp {
                background: linear-gradient(135deg, #6e8efb 0%, #4a6cf7 100%) !important;
                min-height: 100vh;
                position: relative;
                overflow: hidden;
                color:white;
                padding-top:8rem;
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
            
            
            .contact-title {
                color:white;
                font-size: 2rem;
                margin-bottom: 1.5rem;
            }
            
            .contact-subtitle {
                color: white;
                font-size: 2.5rem;
                margin-bottom: 2rem;
                z-index:1;
                position:relative;
            }
            
            .contact-links {
                display: flex;
                flex-direction: column;
                gap: 20px;
            }
            
            .contact-links a {
                text-decoration: none;
                color: #ffffff;
                font-weight: 600;
                display: flex;
                align-items: center;
                gap: 10px;
                transition: all 0.3s;
            }
            
            .contact-links a:hover {
                color: #d0d7ff;
                transform: translateX(5px);
            }
            .contact-links img {
                filter: brightness(0) invert(1);
                width: 30px;
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
        
        """, 
        unsafe_allow_html=True
    )
    st.markdown(
        """
         <!-- Contenu Contact -->
            <h1 class="contact-title">📞 Contact</h1>
            <p class="contact-subtitle">You can find me on these platforms:</p>
            <div class="contact-links">
                <a href="chaimalikouk@gmail.com">
                    <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" >
                    Email
                </a>
                <a href="https://www.linkedin.com/in/chaimae-likouk-13477a271/" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" >
                    LinkedIn
                </a>
                <a href="https://github.com/lshaimae" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
                    GitHub
                </a>
            </div>
        """,unsafe_allow_html=True
    )