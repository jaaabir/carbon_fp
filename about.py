import streamlit as st

Contents = '''
<p>Our goal : To encourge people to use products with less carbon footprint for the better future.</p>
<p>We have made this project to let our users know about the carbon footprint of the products scanned in our app along with the other product details.</p>
'''

contributors = '''
<h3>Contibutors:</h3>

<div>
    <h4>Abdelmalek Boughris (frontend)</h4>
    <a href="https://github.com/Boughris-Abdelmalek" target="_blank"><img src="assets/mal.jfif" alt="Malek"></a>
    <a href="https://www.linkedin.com/in/abdelmalek-boughris/" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 34 34" class="global-nav__logo">
    <g>
        <path d="M34,2.5v29A2.5,2.5,0,0,1,31.5,34H2.5A2.5,2.5,0,0,1,0,31.5V2.5A2.5,2.5,0,0,1,2.5,0h29A2.5,2.5,0,0,1,34,2.5ZM10,13H5V29h5Zm.45-5.5A2.88,2.88,0,0,0,7.59,4.6H7.5a2.9,2.9,0,0,0,0,5.8h0a2.88,2.88,0,0,0,2.95-2.81ZM29,19.28c0-4.81-3.06-6.68-6.1-6.68a5.7,5.7,0,0,0-5.06,2.58H17.7V13H13V29h5V20.49a3.32,3.32,0,0,1,3-3.58h.19c1.59,0,2.77,1,2.77,3.52V29h5Z" fill="currentColor"></path>
    </g>
    </svg>
    </a> 
</div>

<div>
    <h4>Talha abdurrahmaan (backend)</h4>
    <a href="https://github.com/Talha-Altair" target="_blank"><img src="assets/alt.jfif" alt="Talha"></a>
    <a href="https://www.linkedin.com/in/talhaabdurrahman/" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 34 34" class="global-nav__logo">
    <g>
        <path d="M34,2.5v29A2.5,2.5,0,0,1,31.5,34H2.5A2.5,2.5,0,0,1,0,31.5V2.5A2.5,2.5,0,0,1,2.5,0h29A2.5,2.5,0,0,1,34,2.5ZM10,13H5V29h5Zm.45-5.5A2.88,2.88,0,0,0,7.59,4.6H7.5a2.9,2.9,0,0,0,0,5.8h0a2.88,2.88,0,0,0,2.95-2.81ZM29,19.28c0-4.81-3.06-6.68-6.1-6.68a5.7,5.7,0,0,0-5.06,2.58H17.7V13H13V29h5V20.49a3.32,3.32,0,0,1,3-3.58h.19c1.59,0,2.77,1,2.77,3.52V29h5Z" fill="currentColor"></path>
    </g>
    </svg>
    </a> 
</div>

<div>
    <h4>M Z Muhammed Jaabir (ai/ml)</h4>
    <a href="https://github.com/jaaabir" target="_blank"><img src="assets/jab.jfif" alt="Jaabir"></a>
    <a href="https://www.linkedin.com/in/muhammed-jaabir-94022019b/" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 34 34" class="global-nav__logo">
    <g>
        <path d="M34,2.5v29A2.5,2.5,0,0,1,31.5,34H2.5A2.5,2.5,0,0,1,0,31.5V2.5A2.5,2.5,0,0,1,2.5,0h29A2.5,2.5,0,0,1,34,2.5ZM10,13H5V29h5Zm.45-5.5A2.88,2.88,0,0,0,7.59,4.6H7.5a2.9,2.9,0,0,0,0,5.8h0a2.88,2.88,0,0,0,2.95-2.81ZM29,19.28c0-4.81-3.06-6.68-6.1-6.68a5.7,5.7,0,0,0-5.06,2.58H17.7V13H13V29h5V20.49a3.32,3.32,0,0,1,3-3.58h.19c1.59,0,2.77,1,2.77,3.52V29h5Z" fill="currentColor"></path>
    </g>
    </svg>
    </a>
</div>

<div>
<h4>Sashank GS (ai/ml)</h4>
    <a href="https://github.com/sashank24" target="_blank"><img src="assets/sas.jpeg" alt="Sashank"></a>
    <a href="https://www.linkedin.com/in/sashank-gs-97b1b91a4/" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" width="54" height="34" viewBox="0 0 54 34" class="global-nav__logo">
    <g>
        <path d="M34,2.5v29A2.5,2.5,0,0,1,31.5,34H2.5A2.5,2.5,0,0,1,0,31.5V2.5A2.5,2.5,0,0,1,2.5,0h29A2.5,2.5,0,0,1,34,2.5ZM10,13H5V29h5Zm.45-5.5A2.88,2.88,0,0,0,7.59,4.6H7.5a2.9,2.9,0,0,0,0,5.8h0a2.88,2.88,0,0,0,2.95-2.81ZM29,19.28c0-4.81-3.06-6.68-6.1-6.68a5.7,5.7,0,0,0-5.06,2.58H17.7V13H13V29h5V20.49a3.32,3.32,0,0,1,3-3.58h.19c1.59,0,2.77,1,2.77,3.52V29h5Z" fill="currentColor"></path>
    </g>
    </svg>
    </a>
</div>

<div>

'''

def info(name, git, link, pho):
    
    st.markdown(f'<h5>{name}</h5>', unsafe_allow_html = True)
    st.image(pho, width = 200)
    col = st.columns(8)
    col[0].markdown(f'''
                <a href="{git}" target="_blank">
                    <svg xmlns="http://www.w3.org/2000/svg"  width="49" height="49" enable-background="new 0 0 24 24" viewBox="0 0 24 24"><path fill="#b2b1ff" d="M8.854 21.57a9.91 9.91 0 0 0 6.29.001.493.493 0 0 1-.644-.475c0-.338.013-1.413.013-2.75a2.368 2.368 0 0 0-.675-1.85c2.225-.25 4.562-1.1 4.562-4.938a3.87 3.87 0 0 0-1.025-2.687 3.594 3.594 0 0 0-.1-2.65s-.838-.275-2.75 1.025a9.427 9.427 0 0 0-5 0C7.612 5.958 6.775 6.22 6.775 6.22a3.593 3.593 0 0 0-.1 2.65 3.892 3.892 0 0 0-1.025 2.687c0 3.825 2.325 4.688 4.55 4.938-.368.354-.594.829-.638 1.337a2.137 2.137 0 0 1-2.91-.82l-.002-.005a2.001 2.001 0 0 0-1.538-1.025c-.837.013-.337.475.013.663.451.38.803.865 1.025 1.412.2.563.85 1.638 3.362 1.175 0 .838.013 1.625.013 1.863 0 .259-.185.551-.67.475z"/><path fill="#6563ff" d="M12 2.083c-5.523 0-10 4.477-10 10 0 4.423 2.875 8.169 6.855 9.488.485.075.67-.216.67-.475 0-.238-.012-1.025-.012-1.863-2.513.463-3.163-.612-3.363-1.175a3.637 3.637 0 0 0-1.025-1.412c-.35-.188-.85-.65-.013-.663.65.07 1.223.453 1.538 1.025l.003.006a2.137 2.137 0 0 0 2.91.82c.043-.51.27-.984.637-1.338-2.225-.25-4.55-1.113-4.55-4.938a3.892 3.892 0 0 1 1.025-2.687 3.594 3.594 0 0 1 .1-2.65s.837-.263 2.75 1.025a9.427 9.427 0 0 1 5 0c1.912-1.3 2.75-1.025 2.75-1.025.37.838.406 1.786.1 2.65a3.87 3.87 0 0 1 1.025 2.687c0 3.838-2.338 4.688-4.562 4.938.482.49.729 1.164.675 1.85 0 1.337-.013 2.412-.013 2.75a.493.493 0 0 0 .643.476C19.124 20.253 22 16.507 22 12.083c0-5.523-4.477-10-10-10z"/></svg>
                </a>
                ''', unsafe_allow_html=True)
    col[1].markdown(f'''
                <a href="{link}" target="_blank">
                    <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 34 34" class="global-nav__logo" style='margin-top:10'>
                    <g>
                        <path d="M34,2.5v29A2.5,2.5,0,0,1,31.5,34H2.5A2.5,2.5,0,0,1,0,31.5V2.5A2.5,2.5,0,0,1,2.5,0h29A2.5,2.5,0,0,1,34,2.5ZM10,13H5V29h5Zm.45-5.5A2.88,2.88,0,0,0,7.59,4.6H7.5a2.9,2.9,0,0,0,0,5.8h0a2.88,2.88,0,0,0,2.95-2.81ZM29,19.28c0-4.81-3.06-6.68-6.1-6.68a5.7,5.7,0,0,0-5.06,2.58H17.7V13H13V29h5V20.49a3.32,3.32,0,0,1,3-3.58h.19c1.59,0,2.77,1,2.77,3.52V29h5Z" fill="currentColor"></path>
                    </g>
                    </svg>
                </a>
                ''', unsafe_allow_html=True)
    
    st.markdown('---')