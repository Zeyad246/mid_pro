import streamlit as st
import plotly.express as px
import pandas as pd
st.set_page_config(layout='wide')
df=pd.read_csv('mid project')
tab1 , tab2 , tab3 ,tab4 ,tab5=st.tabs(['work_year', 'jobs' , 'salary' , 'countries' , 'Contracts'])
with tab1:
    col1 , col2 , col3 =st.columns(3)
    with col1:
        st.plotly_chart(px.histogram(data_frame=df , x='work_year' , y='salary_in_usd' ,text_auto=True , histfunc='avg', color='work_year' , title='Average salary in 3 years in usd'))
    with col2:
        st.plotly_chart(px.histogram(data_frame=df , x='work_year' , y='salary_in_usd' ,text_auto=True, barmode='group' , histfunc='avg', color='job_title' , title='Average salary in 3 years in usd').update_xaxes(categoryorder = 'total descending'))
    with col3:
        st.plotly_chart(px.histogram(data_frame=df , x='work_year' , color='job_title' , text_auto=True , barmode='group' , title="Jobs"))
        st.plotly_chart(px.histogram(data_frame=df , x='work_year' , color='employment_type' , text_auto=True , barmode='group', title = 'employment type for each year'))
with tab2:
    col1,col2,col3=st.columns(3)
    with col1:
        st.plotly_chart(px.histogram(data_frame=df , x='job_title' , text_auto=True , color = 'job_title' , title='Jobs').update_xaxes(categoryorder = 'total descending'))
    with col2:
        st.plotly_chart(px.histogram(data_frame=df , x='job_category' , text_auto=True ,color ='employment_type',barmode='group',title='employment_type for each job').update_xaxes(categoryorder = 'total descending'))
    with col3:
        st.plotly_chart(px.histogram(data_frame=df , x =['job_title'],color='experience_level' , title='Experience in every job',barmode='group' ,text_auto=True).update_xaxes(categoryorder = 'total descending'))
        st.plotly_chart(px.histogram(data_frame=df , x= 'job_title' , y='salary_in_usd' , text_auto=True , histfunc='avg', color='job_title',title=' avg salary jobs in dollar').update_xaxes(categoryorder = 'total descending'))
with tab3:
    col1,col2,col3=st.columns(3)
    with col1:
        st.plotly_chart(px.histogram(data_frame =  df , x='salary_currency' , text_auto=True , color='salary_currency' , title='salary_currency' ).update_xaxes(categoryorder = 'total descending'))
        st.plotly_chart(px.histogram(data_frame=df, x='job_title', y='salary_in_usd', color='work_setting' , text_auto=True,histfunc='avg', barmode='group',title='The average salary for each job work_setting').update_xaxes(categoryorder = 'total descending'))
    with col2:
        st.plotly_chart(px.histogram(data_frame=df, x='company_size', y='salary_in_usd', color='job_title' , text_auto=True,histfunc='avg', barmode='group',title='The average salary for each job depends on the size of the company').update_xaxes(categoryorder = 'total descending'))
        st.plotly_chart(px.histogram(data_frame=df, x='job_title', y='salary_in_usd', color='experience_level' , text_auto=True,histfunc='avg', barmode='group',title='The average salary for each job depends on experience').update_xaxes(categoryorder = 'total descending'))
    with col3:
        st.plotly_chart(px.histogram(data_frame=df , x='employment_type' , y='salary_in_usd' , text_auto=True , histfunc='avg',title='Salary  in dollars depends on employment_type').update_xaxes(categoryorder = 'total descending'))
with tab4:
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.plotly_chart(px.histogram(data_frame=df , x=['company_location'] , color='job_title' ,barmode='group', text_auto=True , title='Percentage of jobs in each country' ).update_xaxes(categoryorder = 'total descending'))
    with col2:
        st.plotly_chart(px.pie(data_frame=df , names='company_location' , facet_col='work_setting').update_traces(textinfo='label+value+percent'))
    with col3:
        st.plotly_chart(px.pie(data_frame=df , names='company_location' , facet_col='company_size' ).update_traces(textinfo='label+value+percent'))
        st.plotly_chart(px.pie(data_frame=df , names ='company_location'  , title=' Number of companies in each country').update_traces(textinfo='label+value+percent'))
    with col4:
        st.plotly_chart(px.histogram(data_frame=df , y='salary_in_usd' , x= 'company_location' , text_auto=True , histfunc='avg' ,title='Average salaries in countries').update_xaxes(categoryorder = 'total descending'))
with tab5:
    col1,col2=st.columns(2)
    with col1:
        st.plotly_chart(px.histogram(data_frame=df , x='employment_type' , text_auto=True , title=' contracts' ).update_xaxes(categoryorder = 'total descending'))
        st.plotly_chart(px.histogram(data_frame=df , x='company_location' , text_auto=True ,color ='employment_type',barmode='group').update_xaxes(categoryorder = 'total descending'))
    with col2:
        st.plotly_chart(px.histogram(data_frame=df , x='experience_level' , text_auto=True ,color ='employment_type',barmode='group').update_xaxes(categoryorder = 'total descending'))
        st.plotly_chart(px.histogram(data_frame=df , x='salary_currency' , text_auto=True ,color ='employment_type',barmode='group',title='The most currencies in contracts').update_xaxes(categoryorder = 'total descending'))



    
