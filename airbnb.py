import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


df = pd.read_csv("C:\\Users\\shiva\\Desktop\\Guvi\\Airbnb_Capstone\\airbnbcleaned.csv")


st.set_page_config(layout="wide")


with st.sidebar.title("OPTIONS"):
    select=option_menu("Main Menu",["HOME","ANALYSIS","ABOUT"])
    

if select == "HOME":
    
    st.title(":red[**WELCOME TO AIRBNB ANALYSIS**]")
    
    st.write("1." "Through meticulous data analysis, we uncover trends indicating a surge in urban bookings, suggesting a shift in traveler preferences towards vibrant city experiences.")

    st.write("2." "Examining user feedback reveals a growing demand for unique, culturally immersive stays, prompting Airbnb to expand its offerings to cater to diverse traveler interests.")

    st.write("3." "By dissecting regional booking patterns, we identify lucrative opportunities in emerging markets, guiding strategic expansion efforts and maximizing revenue potential.")

    st.write("4." "Utilizing advanced analytics, we pinpoint areas for optimization in the booking process, enhancing user experience and fostering long-term customer loyalty.")
    
    col1,col2=st.columns(2)
    with col1:   
        st.title(":red[ABOUT US]")
        
        st.write("**AIRBNB Analysis is one of the Travel Industry, Property Management and Tourism**")
        
       
        
        
    with col2:
        
        st.header(":red[DATA]")
        
        st.write("Where the data is got from mongodb sample database from **Airbnb**")
        
        st.image("E:\VS CODE files\.venv\Airbnb-Logo.jpg", width=500)
              
elif  select == "ANALYSIS":
    
    st.title(":red[ANALYSIS]")
    
    row = st.columns(1)
    
    with row[0]:
    
        analysis = st.selectbox("Exploratory Analysis of Airbnb Listing Data", ["Distribution of Listings by Country",
                                                                    "Price Variation by Selected Feature",
                                                                    "Frequency of Selected Feature",
                                                                    "Sum of Price and Beds by Number of Bedrooms",
                                                                    "Average Price by Cancellation Policy",
                                                                    "Sum of Price and Beds by Property Type",
                                                                    "Sum of Price and Guests Included by Cancellation Policy",
                                                                    "Sum of Price and Average Review Scores Rating by Number of Bathrooms"
                                                                    ])
    if analysis == "Distribution of Listings by Country":

        sub_columns = st.columns(2)

        with sub_columns[0]:

            country_counts = df['Country'].value_counts().reset_index()
            country_counts.columns = ['country', 'count']

            fig = px.pie(country_counts, values='count', names='country', title='Country Distribution')
            fig.update_layout(title_x=0.3)
            st.plotly_chart(fig)
        

    if analysis == "Price Variation by Selected Feature":

        sub_columns = st.columns(2)

        with sub_columns[1]:
                    sub_columns_1 = st.columns(2)

                    with sub_columns_1[1]:
                        yaxis = st.selectbox("", ['Price',
                                                  'Security_deposit',
                                                  'Cleaning_fee',
                                                  'Extra_people',
                                                ])

        with sub_columns[0]:
            fig = px.bar(df, x='Country', y = yaxis, title=f"{yaxis} by Country")
            fig.update_layout(xaxis_title='Country', yaxis_title = yaxis , xaxis_tickangle=-45, title_x=0.35)
            st.plotly_chart(fig)

    if analysis == "Frequency of Selected Feature":

        sub_columns = st.columns(2)

        with sub_columns[1]:
                    sub_columns_1 = st.columns(2)

                    with sub_columns_1[1]:
                        yaxis = st.selectbox("", ['Property_type',
                                                  "Country",
                                                  "Bed_type",
                                                ])

        with sub_columns[0]:
            property_type_counts = df[yaxis].value_counts().reset_index()
            property_type_counts.columns = [yaxis, 'count']

            fig = px.bar(property_type_counts, x='count', y=yaxis, title=f'Frequency of {yaxis}', orientation='h')
            fig.update_layout(xaxis_title='Frequency', yaxis_title= yaxis, xaxis_tickangle=-45, title_x=0.35)
            st.plotly_chart(fig)
    
    if analysis == "Sum of Price and Beds by Number of Bedrooms":

        agg_df = df.groupby('Total_bedrooms').agg({'Price': 'sum', 'Total_beds': 'sum'}).reset_index()

        
        fig = px.bar(agg_df, x='Total_bedrooms', y='Price', title='Sum of Price and Sum of Beds by Number of Bedrooms')
        fig.add_scatter(x=agg_df['Total_bedrooms'], y=agg_df['Total_beds'], mode='lines', name='Sum of Beds', yaxis='y2')

        
        fig.update_layout(
            xaxis_title='Number of Bedrooms',
            yaxis=dict(title='Sum of Price', side='left', color='blue'),
            yaxis2=dict(title='Sum of Beds', side='right', overlaying='y', color='green')
        )

       
        st.plotly_chart(fig)
    
    if analysis == "Average Price by Cancellation Policy":
        avg_price_by_cancellation = df.groupby('Cancellation_policy')['Price'].mean().reset_index()
        bar_fig = px.bar(avg_price_by_cancellation, x='Cancellation_policy', y='Price', title='Average Price by Cancellation Policy')
        bar_fig.update_xaxes(title='Cancellation Policy')
        bar_fig.update_yaxes(title='Average Price')
        st.plotly_chart(bar_fig)
    
    if analysis == "Sum of Price and Beds by Property Type":
       
        agg_property_df = df.groupby('Property_type').agg({'Price': 'sum', 'Total_beds': 'sum'}).reset_index()

       
        property_fig = px.bar(agg_property_df, x='Property_type', y='Price', title='Sum of Price and Sum of Beds by Property Type')
        property_fig.add_scatter(x=agg_property_df['Property_type'], y=agg_property_df['Total_beds'], mode='lines', name='Sum of Beds', yaxis='y2')

        
        property_fig.update_layout(
            xaxis_title='Property Type',
            yaxis=dict(title='Sum of Price', side='left', color='blue'),
            yaxis2=dict(title='Sum of Beds', side='right', overlaying='y', color='green')
        )
        st.plotly_chart(property_fig)

    if analysis == "Sum of Price and Guests Included by Cancellation Policy":
        
        agg_cancel_df = df.groupby('Cancellation_policy').agg({'Price': 'sum', 'Guests_included': 'sum'}).reset_index()

        
        cancel_fig = px.bar(agg_cancel_df, x='Cancellation_policy', y='Price', title='Sum of Price and Sum of Guests Included by Cancellation Policy')
        cancel_fig.add_scatter(x=agg_cancel_df['Cancellation_policy'], y=agg_cancel_df['Guests_included'], mode='lines', name='Sum of Guests Included', yaxis='y2')

       
        cancel_fig.update_layout(
            xaxis_title='Cancellation Policy',
            yaxis=dict(title='Sum of Price', side='left', color='blue'),
            yaxis2=dict(title='Sum of Guests Included', side='right', overlaying='y', color='green')
        )
        st.plotly_chart(cancel_fig)

    if analysis == "Sum of Price and Average Review Scores Rating by Number of Bathrooms":
       
        agg_bathroom_df = df.groupby('bathrooms').agg({'Price': 'sum', 'Review_scores': 'mean'}).reset_index()

        
        bathroom_fig = px.bar(agg_bathroom_df, x='bathrooms', y='Price', title='Sum of Price and Average Review Scores Rating by Number of Bathrooms')
        bathroom_fig.add_scatter(x=agg_bathroom_df['bathrooms'], y=agg_bathroom_df['Review_scores'], mode='lines', name='Average Review Scores Rating', yaxis='y2')

        
        bathroom_fig.update_layout(
            xaxis_title='Number of Bathrooms',
            yaxis=dict(title='Sum of Price', side='left', color='blue'),
            yaxis2=dict(title='Average Review Scores Rating', side='right', overlaying='y', color='green')
        )

       

        st.plotly_chart(bathroom_fig)

elif select == "ABOUT":
    
    st.title(":red[ABOUT]")
    
    st.subheader("Disruptive Innovation:") 
    
    st.text("Airbnb revolutionized the travel industry by introducing a peer-to-peer platform that allows individuals to rent out their properties to travelers")  
    st.text("offering unique and affordable accommodation options beyond traditional hotels.")       
    
    st.subheader("Shared Economy:")
    
    st.text("Airbnb embodies the concept of the shared economy") 
    st.text(" enabling property owners to monetize their underutilized space while providing travelers with more diverse and personalized lodging experiences.")
    
    st.subheader("Flexibility:")
    
    st.text("Airbnb offers a range of accommodation types, from private rooms to entire homes") 
    st.text(" catering to different traveler preferences and budgets, while also allowing for flexible booking arrangements and customization.") 
    
    st.subheader("Community Building:")
    
    st.text(" Airbnb fosters a sense of community among hosts and guests")
    st.text("facilitating connections, cultural exchange, and mutual respect")
    st.text("ultimately enriching the travel experience and promoting positive interactions worldwide.") 
       


 




