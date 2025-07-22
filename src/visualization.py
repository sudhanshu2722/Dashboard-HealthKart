import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_bar_chart(df, x, y, title):
    fig, ax = plt.subplots()
    sns.barplot(x=x, y=y, data=df, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)
