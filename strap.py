#importing for all libs#
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import csv
import os
from pathlib import Path

import urllib
#displaying text#
st.write ("hi streamlit world")
st.header("--SUPER DEVELOPER--")
st.subheader("***-AHMED AWAD DEVELOPER***-")
st.title("-/-sp stores-/-")
#displaying interactive widgets#
btn=st.button("submit")
if btn:
    st.info("sp information")
chk=st.checkbox("mails")
if chk:
    st.exception("***sp results***")
st.text_input("enter a text")
st.text_area("enter a paragraph")
st.file_uploader("uplode a afile")
st.camera_input("taake a photo")
st.date_input("today")
st.time_input("now")
st.number_input("num")
st.color_picker("colors")
""" df = open('d:\\jpture.csv',"r")
print(df.read()) """
#df=open(r'jpture.csv',encoding="utf-8")  
ff=sns.load_dataset('taxis')
st.write(ff)
df=pd.read_csv(r'c:/mido.csv',encoding='utf-8')




#df = pd.read_csv(r'mido1.csv',encoding='unicode_escape')
#df=pd.read_csv (r"d:/mido1.csv",encoding='unicode_escape')
#df=pd.read_csv (r"C:\Users\mido.csv", sep='\t')
st.write(df)

q=df.groupby('supplier').sum()['TOTAL']
q
e=q
supp_large=q.nlargest(n=10)
supp_large
st.subheader("bar chart")
fig=px.bar(data_frame=supp_large,y='TOTAL')
#st.plotly_chart(fig)
w=df.groupby('STATEMENT').sum()['TOTAL']
w
state_large=w.nlargest(n=11)
state_large
fig=px.bar(data_frame=state_large,y='TOTAL')
e=df.groupby('supplier').sum()['DISC']
e
disc_large=e.nlargest(n=5)
disc_large
#m=df.groupby('DATE').sum()['TOTAL']



#st.plotly_chart(fig)
t=df['TOTAL'].sum()
st.subheader("GRAND TOTAL")
t

st.subheader("scatter plot")

selection=st.selectbox("bot",['STATEMENT','supplier','month','disc',],key='a')
if selection=='STATEMENT':
  fig=px.scatter(data_frame=state_large,y='TOTAL')
elif selection=='supplier':
   fig=px.scatter(data_frame=supp_large,y='TOTAL')
elif selection=='disc':
   fig=px.bar(data_frame=disc_large,y='DISC')
   #fig=px.scatter(data_frame=disc_large,x='DISC')
   
   

st.plotly_chart(fig) 



   
