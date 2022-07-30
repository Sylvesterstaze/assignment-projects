import streamlit as st
import pandas as pd 
# from matplotlib import pyplot as plt
# from plotly import graph_objs as go
import numpy as np
from PIL import Image
import plotly.express as px
st.title("HIPER AUTOMOTIVE TASK")
first,second,last=st.columns(3)
ass=first.selectbox("SELECT MANUFACTURER",('AL','TATA'))
ass1=second.selectbox("SELECT MODEL",(1615,1618))
ass2=last.selectbox("SELECT SUBSYSTEMS",("Fuel", "MeteringUnit", "CM","none"))
ass4=st.selectbox("SELECT plx",('IQ','Metering Unit','Common Rail'))
if ass2=='none':
    if ass=='AL' and ass1==1618:
        image = Image.open('Background MH 12 PQ 5841.png')
        st.image(image, caption='AL 1618')
    elif ass=='AL' and ass1==1615:
        image1= Image.open('Background TN 34 AB 7345.png')
        st.image(image1, caption='AL 1615')
elif ass2=="Fuel" and ass=='AL' and ass1==1618:
        images = ['Background MH 12 PQ 5841.png', 'Injector.png']
        st.image(images)
        
elif ass2=="MeteringUnit" and ass=='AL' and ass1==1618:
        images = ['Background MH 12 PQ 5841.png', 'Metering Unit.png']
        st.image(images)
elif ass2=="CM" and ass=='AL' and ass1==1618:
        images = ['Background MH 12 PQ 5841.png', 'Common Rail.png']
        st.image(images)
elif ass2=="Fuel" and ass=='AL' and ass1==1615:
        images = ['Background TN 34 AB 73451.png', 'Injector.png']
        st.image(images)
elif ass2=="MeteringUnit" and ass=='AL' and ass1==1615:
        images = ['Background TN 34 AB 73451.png', 'Metering Unit.png']
        st.image(images)
elif ass2=="CM" and ass=='AL' and ass1==1615:
        images = ['Background TN 34 AB 73451.png', 'Common Rail.png']
        st.image(images)
if ass4=='Metering Unit'and ass1==1618:
        df=pd.read_csv("BC 12 CD 3456.csv")
        # daf=pd.read_csv("AB 12 BC 3456.csv")
        msk = df['mu_pred']
        fig=px.line(msk)
        st.write(fig)
elif ass4=="IQ"and ass1==1618:
        df=pd.read_csv("BC 12 CD 3456.csv")
        # daf=pd.read_csv("AB 12 BC 3456.csv")
        msk = df['iq_pred']
        fig=px.line(msk)
        st.write(fig)
elif ass4=='Common Rail'and ass1==1618:
        df=pd.read_csv("BC 12 CD 3456.csv")
        # daf=pd.read_csv("AB 12 BC 3456.csv")
        msk = df['rp_pred']
        fig=px.line(msk)
        st.write(fig)
if ass4=='Metering Unit'and ass1==1615:
        # df=pd.read_csv("BC 12 CD 3456.csv")
        df=pd.read_csv("AB 12 BC 3456.csv")
        msk = df['mu_pred']
        fig=px.line(msk)
        st.write(fig)
elif ass4=="IQ"and ass1==1615:
        # df=pd.read_csv("BC 12 CD 3456.csv")
        df=pd.read_csv("AB 12 BC 3456.csv")
        msk = df['iq_pred']
        fig=px.line(msk)
        st.write(fig)
elif ass4=='Common Rail'and ass1==1615:
        # df=pd.read_csv("BC 12 CD 3456.csv")
        df=pd.read_csv("AB 12 BC 3456.csv")
        msk = df['rp_pred']
        fig=px.line(msk)
        st.write(fig)
