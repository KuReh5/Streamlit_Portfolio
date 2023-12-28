from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie as sl
import requests
import json
from matplotlib import pyplot as plt
import numpy as np
#to run code: python -m streamlit run Port.py
st.set_page_config(page_title="Ku Reh Portfolio",layout="wide")

# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#images
#python_anim = load_lottieurl("https://lottie.host/ffaa1c88-8e1e-4a58-a7fd-dcce73b9f59c/1rOMigRSM1.json")
# propic = Image.open("ProPic.jpg")
# art_pic = Image.open("art.jpg")
# resume = open("Ku_Reh_Resume_ General.docx", 'r')
# riverland_logo = Image.open("riverland_logo.jpg")
# mnsu_logo = Image.open("mnsu_logo.jpg")

#Insert Image
def InsertIMG(path):
    img = Image.open(path)
    return img
#Inserting json animations
def Anim(path):
    with open(path, 'r') as file:
        name = json.load(file)
    return name

#navbar/tabs
tab = st.tabs(["About me","Skills","Projects", "Contact me"])

#region AboutMe
#About me page
with tab[0]:
    bioCol = st.columns([.6,.4])
    #CSS
    st.markdown("""
    <style>
    .normal-font {
    font-size:20px !important;
    font-family: "Lucida Console"
    }
    </style>
    """, unsafe_allow_html=True)

    with bioCol[0]:
        st.header("Hi 👋")
        st.markdown('<p class="normal-font">My name is Ku Reh. I am a developer proficient in Python.\
            With years of experience, I extend my learning in data analysis.\
            I am passionate about using technologies to better the lives of people.\
            I concentrate my studies on healthcare technologies.</p>', unsafe_allow_html=True)

        ('---')
        with st.expander("**Education**"):

            c = st.columns(2)
            with c[0]:
                'Riverland Community College'
                '**GPA**: 3.7'
                '**Degree**: AA'
                #st.image('riverland_logo.jpg',None,200,200)
            with c[1]:
                'Minnesota State University Mankato'
                '**GPA**: 3.8'
                '**Degree**: Health Informtics (BS)'
                #st.image('mnsu_logo.jpg',None,300,300)
        with st.expander("**Hobbies**"):
            col = st.columns(4)
            with col[0]:
                'Coding'

                sl(Anim('coding_anim.json'))
            with col[1]:
                'Volleyball'
                sl(Anim('Vol_anim.json'))
            with col[2]:
                'Piano, guitar, drum'
                sl(Anim('piano_anim.json'))
            with col[3]:
                'Draw'
                #st.image('art.jpg',None, 150)
        #ResumeDownload

    with bioCol[1]:
        #st.image('ProPic.jpg',None, 350)
        ''


    st.write("---")
    col = st.columns([.7,.3])
    #left col
    with col[0]:
        st.write("[Github](https://github.com/KuReh5) [Linkedin](https://www.linkedin.com/in/ku-reh-8211661b5/)")



    #right col
    #with col[1]:
        #sl(python_anim)
#endregion
#region Skills page
with tab[1]:
    topcol = st.columns(3)
    with topcol[0]:
        col = st.columns([.4,.6])
        with col[0]:
            '**Developing**'
            '-.Net MAUI app'
            'Streamlit web app'
        with col[1]:
            sl(Anim('python_anim.json'), height=100, width=100)

    with topcol[1]:
        col = st.columns([.6,.4])
        
        with col[0]:
            '**Database Management**'
            '-MySQL & MS SQL Server'
            '-Diagrams(ERD,FDD)'
        with col[1]:
            sl(Anim('sql_anim.json'),height=100, width=100)
    with topcol[2]:
        col = st.columns([.4,.6])
        with col[0]:
            '**Object Oriented(C#)**'
            '-Unity'
            '-Data Structures'
        with col[1]:
            #st.image(InsertIMG('csharp.png'),None, 100)
            ''
    ('---')
    bottomcol = st.columns(3)
    with bottomcol[0]:
        col = st.columns([.4,.6])
        with col[0]:
            '**Data Analysis**'
            '-Train/Test models'
            '-Predict outcomes'
        with col[1]:
            sl(Anim('analysis1.json'),height=100, width=100)
    with bottomcol[1]:
        col = st.columns([.4,.6])
        with col[0]:
            '**Data Visualization**'
            '-Tableau'
            '-Matplotlib, Seaborn'
        with col[1]:
            sl(Anim('analysis.json'),height=100, width=100)

    with bottomcol[2]:
        col = st.columns([.4,.6])
        with col[0]:
            '**ArcGis**'
            '-Create Maps'
            '-Predict trends'
        with col[1]:
            #st.image(InsertIMG('gis.jpg'),None, 100)
            ''
    ('---')
    thirdcol = st.columns(3)
    with thirdcol[0]:
        col = st.columns([.6,.4])
        with col[0]:
        
            '**Security**'
            ' -Vulnerability scans'
            ' -Firewalls'
        with col[1]:
            sl(Anim('firewall_anim.json'),height=100, width=100)

    ('---')
    with st.expander('Frequency of languages used'):
        languages = ['Python','C#','SQL','HTML','JavaScript','CSS']
        languagePercent = [80,10,5,3,1,1]
        explode = [0.1,0,0,0,0,0]
        fig, ax = plt.subplots()
        ax = plt.pie(languagePercent,labels=languages,wedgeprops={'edgecolor':'black'}, explode=explode, autopct='%1.1f%%')
        ax = plt.title("Programming languages")
   
        st.pyplot(fig)
#endregion
#region Projects page
with tab[2]:
    #DiabetesProj
    with st.container(border=True):
        col = st.columns([.7,.3])
        with col[0]:
            'Diabetes prediction'
            '''-In this data analysis project, me and my partner(Nuri) trained models to predict which types of factors increases a person's chance
                of acquiring diabetes. First, we cleaned the data that was in csv format. Many of the data had nulls and we replaced them with zeros.
                We then visualize them with Matplotlib and Seaborn. With the model that we tested, we can be sure that glucose is the most prominent factor for 
                diabetes.'''
            '[Jupyter Notebook](https://github.com/KuReh5/Diabetes/blob/main/Diabetes443.ipynb)'
        with col[1]:
            #st.image('diabetes.png',None, 350)
            ''

    #MAUIProj
    with st.container(border=True):
        
        'Charting App'
        '''-Using .Net MAUI app builder, I created a charting app for nurses. I integrated the Model-View-ViewModel method. 
        I learned about the importance of object-oriented when creating an app.
        I created UI screens for all the pages with navigation. With a database connected, the app
        be complete.
        '''
        col = st.columns(3)
        with col[0]:
            #st.image(InsertIMG('maui1.png'),None, 350)
            #st.image('maui1.png',None, 350)
            ''
        with col[1]:
            #st.image('maui2.png',None, 150)
            ''
        with col[2]:
            #st.image('maui3.png',None, 150)
            ''
        '[Github](https://github.com/KuReh5/GoChart)'
    #UnityProj
    with st.container(border=True):
        col = st.columns([.7,.3])
        with col[0]:
            'Unity Game(Nikana)'
            '''-In this group project, I used Unity Engine to create a 2D platformer game. I learn how to use scipts
            and apply physics to characters. Github was crucial to the success of the project as multiple people
            were working on it. I learn how to push and pull from Github as well as creating backups. Testing our
            scripts was done to make sure it works with the other scripts.
            
            '''
        
            '[Nikana](https://github.com/ZacharySkinner/Nikana)'
        with col[1]:
             #st.image('unity.png',None, 300)
             ''
         
    #TableuProj
    with st.container(border=True):
        col = st.columns([.7,.3])
        with col[0]:
            'Tableau'
            '''-In this tableau, I looked at Covid-19 and its numbers in 2023. We can see that Europe had the most cases
            by population. 
            With a basic analysis, 42% of South Korea will be infected with Covid by Oct 2024 at current rate. 
            '''
            '[Dashboard](https://public.tableau.com/app/profile/ku.reh/viz/Portfolio_17017144621630/Dashboard1)'
        with col[1]:
             #st.image('tableau.png',None, 300)
             ''
         
#endregion
#region Contact page
with tab[3]:
    st.header('**Get in touch with me**')
    contact_form = ''' <form action="https://formsubmit.co/76afb1d056ba41731e5c8b210ecb7c1a " method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder='Your Message Here' required></textarea>
     <button type="submit">Send</button>
</form>'''
    st.markdown(contact_form, unsafe_allow_html=True)
    local_css('style.css')
#endregion


