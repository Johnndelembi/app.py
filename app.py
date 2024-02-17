import streamlit as st
from pathlib import Path

#-------------PATH SETTINGS------------

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "resume.pdf"

#------------LOAD FILE----------------
with open(resume_file, "rb") as pdf_file: 
    PDFbyte = pdf_file.read()

st.set_page_config(
    page_title="JOHN NDELEMBI CV",
    page_icon="📄",
    )

#---------------SIDEBAR--------------------------

st.sidebar.image("picc.png", width=200)

st.sidebar.write("###")
st.sidebar.header("**HARD SKILLS**")
st.sidebar.markdown('''
    - Data Management & Analysis (Competent in Python,R,STATA and Excell)
    - Python Programming for Web app designs and development
    - 3D Rendering (Beginners level)
    - Graphic Design and Videography
    - Marketting Content Creation''')

st.sidebar.write(" ###")
st.sidebar.header("**SOFT SKILLS**")
st.sidebar.markdown('''
    - Communication and Problem solving skills
    - Team work, collaboration and adaptability
    - Microsoft office packages. 
    - Proposal Writing. ''')


st.sidebar.write("###")
st.sidebar.header("**LANGUAGE**")
st.sidebar.write('''
    - Swahili 
    - English (Written & Spoken)''')

st.sidebar.subheader("CONTACT ME")
st.sidebar.markdown(":telephone_receiver:(+255) 625 232 734")
st.sidebar.write((":envelope: williamjohnie61@gmail.com"))
st.sidebar.markdown(":round_pushpin: Dar es Salaam, Tanzania")


#------------------PAGE SETUP---------------

st.title(" :green[JOHN NDELEMBI] ")
st.sidebar.markdown(**'Data analyst asissting enterprises and organizations by supporting data-driven decsisions towards growth'**)
st.download_button(
    label="📝 Download CV.pdf",
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
    > I have 2 years of experience working with data, strong hands on experience with Python, Excell and STATA. I have completed 4 data science projects with an 85% efficiency in my lifetime. I have good understanding of statistics principles and their respective applications. I am a hard worker with a team-work oriented mindset. data driven decision-maker
    It would be an honor to work under your organization/company and drive growth with data driven decision.''')

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

st.subheader("PROJECTS AND ACCOMPLISHMENTS")

link4 = '[:trophy: **ACADEMIC RESULTS DASHBOARD** - Comparing Performances, relationships and causality across different subjects](https://dataproject.streamlit.app/)'
st.markdown(link4, unsafe_allow_html=True)

link5 = '[:trophy: **DATA ANALYSIS APP** - created a tool capable of providing descriptive analysis of a dataframe regardless of size using python code](https://dataproject.streamlit.app/)'
st.markdown(link5, unsafe_allow_html=True )

link6 = '[:trophy: **MY GRAPHIC DESIGNS COLLECTION** - some of my graphic designs from different times](https://tally.so/r/n0dEVQ)'
st.markdown(link6, unsafe_allow_html=True)

st.write("---")



#----------------FOOTER----------------------------------
st.header("**REFERENCES**")

cols1, cols2 = st.columns(2)

cols1.subheader("Evelyn Mchau")
cols1.caption("*EVERYDAY MANIFESTATIONS / CEO* ")
cols1.markdown(":telephone_receiver: (+255) 768 180 503")
cols1.write(":envelope: goodlyne23@gmail.com")

cols2.subheader("Doreen Daffa")
cols2.caption("*AIESEC IN UDSM*")
cols2.markdown(":telephone_receiver: (+255) 684 327 666 ")
cols2.write(":envelope: doreen.daffa@aiesec.net")
