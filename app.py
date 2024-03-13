import streamlit as st
from pathlib import Path

#-------------PATH SETTINGS------------

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "resume.pdf"

#------------LOAD FILE----------------
with open(resume_file, "rb") as pdf_file: 
    PDFbyte = pdf_file.read()

st.set_page_config(
    page_title="CV",
    page_icon=":brain:",
    )


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("headphone.jpg")
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"] {
right: 1rem;
}

[data-testid="stSidebar"] {    
background-image: url("")
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#---------------SIDEBAR--------------------------

with st.sidebar:
    container = st.container(border=True)
    st.image("picc.png", width=200)
    #st.write("###")
    #st.markdown(" > **Data analyst asisting enterprises and organizations by supporting data driven decsisions towards growth**")

with st.sidebar:
    container = st.container(border=True)
    #container.write("###")
    container.header("**HARD SKILLS**")
    container.markdown('''
    - Data Analysis
    - Machine Learning
    - Web development
    - 3D Rendering. 
    - Graphic Design and Videography
    - Marketting Content Creation''')

with st.sidebar:
    container = st.container(border=True)
    #st.sidebar.write(" ###")
    container.header("**SOFT SKILLS**")
    container.markdown('''
    - Microsoft office packages. 
    - Proposal Writing.
    - Communication skills 
    - Problem solving skills
    - Team work and adaptability
     ''')

with st.sidebar:
    container = st.container(border=True)
    #st.sidebar.write("###")
    container.header("**LANGUAGE**")
    container.write('''
    - Swahili 
    - English (Written & Spoken)''')

with st.sidebar:
    container = st.container(border=True)
    container.header("CONTACTS")
    container.markdown(":telephone_receiver:(+255) 625 232 734")
    container.write((":envelope: williamjohnie61@gmail.com"))
    container.markdown(":round_pushpin: Dar es Salaam, Tanzania")


#------------------PAGE SETUP---------------

st.title(" :green[JOHN NDELEMBI] :crown: ")
#st.markdown("**Data Scientist | Developer | Graphic Designer**")
st.markdown("**Data Analyst. Developer advocate at Py.Hub. Python instructor at Py.Hub. Data enthusiat supporting data-driven decisions.**")

st.download_button(
    label="Download CV",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)

st.write("###")
col1, col2, col3, col4 = st.columns(4)

link = '[LinkedIn](https://www.linkedin.com/in/john-ndelembi/)'
col1.markdown(link, unsafe_allow_html=True)

link1 = '[Github](https://github.com/dashboard)'
col2.markdown(link1, unsafe_allow_html=True)

link2 = '[Twitter](https://twitter.com/Johnwills171)'
col3.markdown(link2, unsafe_allow_html=True)

link3 = '[Portfolio](https://tome.app/fx-3c4/johns-portfolio-cllaidgc700wkoe5qqmitxx1q)'
col4.markdown(link3, unsafe_allow_html=True)




st.write("---")

st.subheader(" :green[PROFILE] ")
st.markdown(''' 
    *I have 2 years of experience working with data, strong hands on experience with Python, Excell and STATA. I have completed 4 data science projects with an 85% efficiency in my lifetime. I have good understanding of statistics principles and their respective applications. I am a hard worker with a team-work oriented mindset. data driven decision-maker
    It would be an honor to work under your organization/company and drive growth with data driven decision.*''')

st.write("###")

st.subheader(" :orange[VOLUNTEER EXPERIENCE] ")

st.write(" :orange[PSSSF], *Geita*")
st.write("July 2023 - September 2023")
st.markdown('''
    - Participated in PSSSF volunteer training of the institution
    - Assisted in operations department office work
    - Worked with Excell spreadsheets of members perfoming data wrangling and missing values treatment ''')

st.write("###")
st.write(" :orange[ENNOVATE VENTURES], Dar es Salaam")
st.write("April 2023 - June 2023")
st.markdown('''
    - Worked as a developer tasked to design a web app with the aim to solve a problem in the community
    - Completed the task by 90% and submitted the project on time''')

st.subheader(" :red[WORK EXPERIENCE] ")
st.write(" :red[EVERYDAY MANIFESTATIONS],  *Dar es Salaam — C.E.O Personal Assistant*")
st.markdown("April 2022 - July 2022")
st.markdown('''
    - Worked with the C.E.O in launching multiple marketing campaigns. 
    - Performed 65% of back office activities of the company.''')

st.write("###")    

st.write(" :red[BRENDALICIOUS FRESH JUICE],  *Mbeya — Business analyst, Graphics designer.*")
st.markdown("December 2022 - January 2023")
st.markdown('''
    - Helped in re-establishing the the company into the business world by making better decisions in marketing and sales department which brought about the growth of the company by 75% from before i started working with.
    - Worked as an assistant social media manager, ran considerable number of online based marketing campaigns.
    - Established a stable system for business flow and operations.''')

st.write("###")

st.write(" :red[AIESEC IN UDSM], *Dar es Salaam -- Team member of Business and Patners development department*")
st.markdown("June 2023 - Present")
st.markdown('''
    - Participated in organizing AIESEC International Relations event with EwA members
    - Worked towards patnerships establishment for specific AIESEC Events and  for the entity at large
    - Participated and worked in Campus held AIESEC events''')

st.write("###")

st.subheader(":blue[EDUCATION AND TRAINING]")
st.write("**:blue[University of Dar es Salaam]** | B.A in Economics and Statisitcs")
st.write(" *November 2021 - September 2023*")
st.markdown('''
    - Leadership skills
    - Learned Economics, Statistics Principles''')

st.write("**:blue[MSUFINI HIGH SCHOOL]** , Hai - Kilimanjaro")
st.write(" *April 2020 - May 2021*")
st.write('''
         - EGM - Economics, Geography and Mathematics''')

col7, col8 = st.columns([0.5,5])
col8.header("PROJECTS AND ACCOMPLISHMENTS")

c1, c2, c3 = st.columns(3)

c1.metric(label="Completed", value="5", delta="1")
c2.metric(label="Currently Working on", value="2", delta="1")
c3.metric(label="Declined", value="0", delta="-5")

#style_metric_cards(border_left_color="#1E1E1E")

with st.expander("PROJECTS AND ACCOMPLISHMENTS"):
    proj1, proj2 = st.columns(2)
    container = st.container(border=False)

    with st.container():
        proj1.video("academic.webm")  
        proj1.caption("Academic results analysis")
        proj1.write("###") 
        proj1.write("###")
        link4 = '[:trophy: **ACADEMIC RESULTS DASHBOARD** - Comparing Performances, relationships and causality across different subjects](https://dataproject.streamlit.app/)'
        proj2.markdown(link4, unsafe_allow_html=True)
        proj2.markdown("I workshopped a data dashboard presenting data from examination results of diploma students from a certain university(name reserved) in year 2021/2022 and highlighted the basic statistics analytical oroceedures ")
        proj2.write("###")
        proj1.write("###")
        proj2.write("###")

    with st.container(border=True):
        proj1.video("DATA_PROJECT.mp4")
        proj1.caption("Data analysis app")
        proj1.write("###")
        link5 = '[:trophy: **DATA ANALYSIS APP** - created a tool capable of providing descriptive analysis of a dataframe regardless of size using python code](https://dataproject.streamlit.app/)'
        proj2.markdown(link5, unsafe_allow_html=True )
        proj2.markdown("I developed a tool capable of performing descriptive analysis of uploaded data. you just have to upload your data and the app will analyse your data for you with a single click ")
        proj2.write("###")
        proj2.write("###")
        proj2.write("###")
        
    with st.container():
        proj1.video("legends.mp4")
        proj1.caption("Graphic designs collection")
        link6 = '[:trophy: **MY GRAPHIC DESIGNS COLLECTION** - some of my graphic designs from different times](https://tally.so/r/n0dEVQ)'
        proj2.markdown(link6, unsafe_allow_html=True)
        proj2.markdown("check out my art portfolio to and view my graphic designs collection over the years")

st.write("---")


#----------------FOOTER----------------------------------
col10, col11 = st.columns([2,5])
col11.header("**REFERENCES**")

cols1, cols2 = st.columns(2)

cols1.subheader("Evelyn Mchau")
cols1.caption("*EVERYDAY MANIFESTATIONS / CEO* ")
cols1.markdown(":telephone_receiver: (+255) 768 180 503")
cols1.write(":envelope: goodlyne23@gmail.com")

cols2.subheader("Doreen Daffa")
cols2.caption("*AIESEC IN UDSM*")
cols2.markdown(":telephone_receiver: (+255) 684 327 666 ")
cols2.write(":envelope: doreen.daffa@aiesec.net")
