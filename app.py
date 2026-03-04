import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Dashboard", layout="wide")

st.title("🎓 Student Performance Dashboard")

st.write("Student data analysis project using Python")

df = pd.read_csv("students.csv")

df["Average"] = df[["Math","Science","English"]].mean(axis=1)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)

st.sidebar.header("Filters")

grade_filter = st.sidebar.multiselect(
    "Select Grade",
    df["Grade"].unique(),
    default=df["Grade"].unique()
)

df = df[df["Grade"].isin(grade_filter)]

col1,col2,col3 = st.columns(3)

col1.metric("Total Students",len(df))
col2.metric("Average Score",round(df["Average"].mean(),2))
col3.metric("Highest Score",round(df["Average"].max(),2))

st.subheader("Student Data")

st.dataframe(df)

fig = px.bar(df,x="Name",y="Average",color="Grade",title="Student Performance")
st.plotly_chart(fig,use_container_width=True)

fig2 = px.pie(df,names="Grade",title="Grade Distribution")
st.plotly_chart(fig2,use_container_width=True)

fig3 = px.scatter(df,x="Attendance",y="Average",color="Grade",hover_name="Name")
st.plotly_chart(fig3,use_container_width=True)
