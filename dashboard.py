### author : M Z Muhammed Jaabir
### python version : Python 3.8.2

import streamlit as st 
import plotly.express as px
import pandas as pd 
import numpy as np
from yahoofinancials import YahooFinancials
import scipy
import plotly.figure_factory as ff
import os
from about import Contents, info


def get_yr(company, gdf, col = 'yor'):
  dat = gdf.get_group(company)
  yr_list = dat[col].unique()
  return yr_list

def line_split(df):
  df['y'] = df.date.apply(lambda x : x.split('-')[0])
  years = []
  for y,rdf in df.groupby('y'):
    date = sorted(rdf.date.values)
    years.append(date[-1])
  return years

def plot_prices_yahf(df, company, start, end, title):
  yahoo_financials = YahooFinancials(company)
  data = yahoo_financials.get_historical_price_data(start_date=start, 
                                                    end_date=end, 
                                                    time_interval='monthly')
  df = pd.DataFrame(data[company]['prices'])
  df = df.drop('date', axis=1).set_index('formatted_date')
  df = df[["close"]]
  df['date'] = df.index
  df.index = np.arange(df.shape[0])
  yrs = line_split(df)
  fig = px.line(df, x = 'date', y = 'close', title = title)
  for yr in yrs[:-1]:
    fig.add_vline(x = yr, line_color = 'green')
  
  h = df[df.close == df.close.max()].reset_index(drop = True)
  m = df.close.mean()
  l = df[df.close == df.close.min()].reset_index(drop = True)

  return fig, h,m,l

def plot_px_line(df, x, y, title, yrs):
    fig = px.line(df, x = x, y = y, title = title)
    for yr in yrs:
        fig.add_vline(x = yr, line_color = "green" )
    h = df[df[y] == df[y].max()].reset_index(drop = True)
    m = df[y].mean()
    l = df[df[y] == df[y].min()].reset_index(drop = True)   
    
    st.plotly_chart(fig, use_container_width = True)
    _, col1, col2 = st.columns(3)
    col1.metric(f"Price ({h[x][0]})", round(h[y][0], 3), f"+{round(h[y][0] - m, 3)}")
    col2.metric(f"Price ({l[x][0]})", round(l[y][0], 3), f"{round(l[y][0] - m, 3)}") 
    
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def main():
    menu = ["Dataset", 'Hypothesis I', 'Hypothesis II', 'Hypothesis III', 'About us', 'Source links']
    choice = st.sidebar.selectbox("Menu", menu)
    if 'df' not in st.session_state:
        st.session_state.df = pd.read_csv(os.path.join('datasets', 'final_data.csv'))
    
    if choice == 'Dataset':
        st.header('Carbon Footprint Dataset')
        df = st.session_state.df
        st.write(df.head())
        st.download_button('Download dataset', data = convert_df(df), file_name = 'carbon_footprint.csv', mime='text/csv')
    elif choice == 'Hypothesis I':
        st.markdown('<h3 style="color:#2d87ad">Hypothesis</h3>', unsafe_allow_html=True)
        st.markdown("##### Companies which have high carbon emission don't flourish that much")
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Measurement idea</h3>', unsafe_allow_html=True)
        st.markdown("##### Compare stock prices between high emitting companies and low emitting companies ")
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Measurables</h3>', unsafe_allow_html=True)
        df = st.session_state.df
        comp_df = df.dropna(subset = ['company'])
        dets = sorted([[ind, rdf.cfp.sum()] for ind, rdf in comp_df.groupby('company')], reverse = False, key = lambda x : x[-1])
        dets = np.array(dets)
        dets = pd.DataFrame({
            'company' : dets[:, 0],
            'carbon footprint'     : dets[:, 1]
        })
        fig = px.bar(dets.iloc[-5:], x = 'company', y = 'carbon footprint', title = 'Top 5 companies producing high carbon emission for their products')
        st.plotly_chart(fig, use_container_width = True)
        fig = px.bar(dets.iloc[0:5], x = 'company', y = 'carbon footprint', title = 'Top 5 companies producing low carbon emission for their products')
        st.plotly_chart(fig, use_container_width = True)
        
        st.markdown('<h3 style="color:#2d87ad">High carbon footprint producing companies</h3>', unsafe_allow_html=True)
        
        fig, h, m, l = plot_prices_yahf(df, 'MT', '2012-01-11', '2014-12-30', 'Arcelor Mittal (2012 - 2014)')
        st.plotly_chart(fig, use_container_width = True)
        _, col1, col2 = st.columns(3)
        col1.metric(f"Price ({h.date[0]})", round(h.close[0], 3), f"+{round(h.close[0] - m, 3)}")
        col2.metric(f"Price ({l.date[0]})", round(l.close[0], 3), f"{round(l.close[0] - m, 3)}")
        
        fig, h, m, l = plot_prices_yahf(df, '7205.T', '2015-01-11', '2017-12-30', 'Hino motors (2012 - 2017)')
        st.plotly_chart(fig, use_container_width = True)
        _, col1, col2 = st.columns(3)
        col1.metric(f"Price ({h.date[0]})", round(h.close[0], 3), f"+{round(h.close[0] - m, 3)}")
        col2.metric(f"Price ({l.date[0]})", round(l.close[0], 3), f"{round(l.close[0] - m, 3)}")
        
        st.markdown('<h3 style="color:#2d87ad">Low carbon footprint producing companies</h3>', unsafe_allow_html=True)
        
        fig, h, m, l = plot_prices_yahf(df, 'CNX', '2015-01-11', '2017-12-30', 'CNX : (2015 - 2017)')
        st.plotly_chart(fig, use_container_width = True)
        _, col1, col2 = st.columns(3)
        col1.metric(f"Price ({h.date[0]})", round(h.close[0], 3), f"+{round(h.close[0] - m, 3)}")
        col2.metric(f"Price ({l.date[0]})", round(l.close[0], 3), f"{round(l.close[0] - m, 3)}")
        
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Insights</h3>', unsafe_allow_html=True)
        st.markdown('''
                    <h6 style="color:#7646e8">
                    The hypothesis of 'Companies which have high carbon emission don't flourish that much' has been affirmed positively and from the measureables it has been inferred that the data supports our claim. 
                    </h6>
                ''', unsafe_allow_html=True)
           
    elif choice == 'Hypothesis II':
        st.markdown('<h3 style="color:#2d87ad">Hypothesis</h3>', unsafe_allow_html=True)
        st.markdown("##### people gravitate towards companies which have less carbon footprint")
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Measurement idea</h3>', unsafe_allow_html=True)
        st.markdown("##### analysis of products which have less carbon emission based on their revenues")
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Measurables</h3>', unsafe_allow_html=True)
        kellog_dict = { 
                       'year'  : ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
                       'Revenue in $ (m)' : [13547,12854,12965,13525,14580,14792,14197][::-1]
                    }
        df_kel = pd.DataFrame(kellog_dict)
        plot_px_line(df_kel, 'year', 'Revenue in $ (m)', 'kellogg revenue in millions ($)', ['2014', '2015'])
        
        logitech_dict = { 
                        'year' : ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
                        'Revenue in $ (m)' : [2316, 2099, 2008, 2006, 2018, 2221, 2567]
                    }
        df_logi = pd.DataFrame(logitech_dict)
        plot_px_line(df_logi, 'year', 'Revenue in $ (m)', 'Logitech revenue in billions ($)', ['2014', '2015'])
        
        pep_dict = { 
                    'year' : ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
                    'Revenue in $ (m)' : [64661,63525,62799,63056,66683,66415,65492][::-1]
                }
        df_pep = pd.DataFrame(pep_dict)
        plot_px_line(df_pep, 'year', 'Revenue in $ (m)', 'Pepsi.Co revenue in millions ($)', ['2013','2014', '2015'])
        
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Insights</h3>', unsafe_allow_html=True)
        st.markdown('''
                    <h6 style="color:#7646e8">
                    The carborn footprint of a company doesn't impact the company's annual revenue and the trend is uncertain. hence the hypothesis is not tested to be entirely true      
                    </h6>
                ''', unsafe_allow_html=True)
        
    elif choice == 'Hypothesis III':
        st.markdown('<h3 style="color:#2d87ad">Hypothesis</h3>', unsafe_allow_html=True)
        st.markdown("##### To check whether products whose countries which emit high and low carbon footprint contributes to the national emission index as well as align with it")
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Measurement idea</h3>', unsafe_allow_html=True)
        st.markdown("##### extract products whose countries produce high and low carbon footprint")
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Measurables</h3>', unsafe_allow_html=True)
        df = st.session_state.df
        dets = sorted([[ind, np.sum(rdf.cfp)] for ind, rdf in df.groupby('country/region')], reverse = False, key = lambda x : x[1])
        dets = np.array(dets)
        dets = pd.DataFrame({
            'country' : dets[:, 0],
            'carbon footprint (m)'   : dets[:, 1],
        })
        
        # dist_cfp = pd.to_numeric(dets["carbon footprint (m)"], downcast="float")
        # fig = ff.create_distplot([dist_cfp], ['carbon footprint'], bin_size = .2)
        # fig.add_vline(x = dist_cfp.values.mean(), line_color = 'green')
        # st.plotly_chart(fig, use_container_width = True)
        
        fig = px.bar(dets.iloc[-10:], x = 'country', y = 'carbon footprint (m)', title = 'Top 10 countries producing highest carbon emission')
        st.plotly_chart(fig, use_container_width = True)
        
        # fig = px.imshow(plt.imread(os.path.join('assets', 'h3_high.jfif')))/
        # st.plotly_chart(fig, use_container_width = True)
        st.image(os.path.join('assets', 'h3_high.jfif'), caption = 'Source : OECD (2021), CO2 emission emobodied in international trade : http://oe.cd/io-co2')
        # _, col2 = st.columns(2)
        # col2.markdown("<p style='margin-top:-50px'><i><a href='http://oe.cd/io-co2'>Source : OECD (2021), CO<sub>2</sub> emission emobodied in international trade</a></i></p>", unsafe_allow_html = True)
        
        st.markdown('<h5 style="color:#2ac96a">Most of the countries align with the global chart of co2 production and consumption</h5>', unsafe_allow_html = True)
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Countries producing low carbon footprint</h3>', unsafe_allow_html = True)
        dets = sorted([[ind, np.sum(rdf.cfp)] for ind, rdf in df.groupby('country/region')], reverse = False, key = lambda x : x[1])
        dets = np.array(dets)
        dets = pd.DataFrame({
            'country' : dets[:, 0],
            'carbon footprint'   : dets[:, 1],
        })
        fig = px.bar(dets.iloc[:10,:], x = 'country', y = 'carbon footprint', title = 'Top 10 countries producing lowest carbon emission')
        st.plotly_chart(fig, use_container_width = True)
        
        st.image(os.path.join('assets', 'wmap.png'), caption = 'Source : https://worldpopulationreview.com/country-rankings/carbon-footprint-by-country')
        st.markdown('''<h5 style="color:#2d87ad">let's have a look at 3 countries</h5>''', unsafe_allow_html = True)
        st.image(os.path.join('assets', 'france.png'), caption = 'Carbon Footprint for France')
        st.image(os.path.join('assets', 'ukraine.png'), caption = 'Carbon Footprint for Ukraine')
        st.image(os.path.join('assets', 'serbia.png'), caption = 'Carbon Footprint for Serbia')
        
        st.markdown('---')
        st.markdown('<h3 style="color:#2d87ad">Insights</h3>', unsafe_allow_html=True)
        st.markdown('''
                    <h6 style="color:#7646e8">
                    The hypothesis is tested to be positive as the global index of the countries for both low and high carbon footprint aligns with our claims which is based on our dataset  
                    </h6>
                ''', unsafe_allow_html=True)
    elif choice == 'About us':
        st.markdown('''
                    <center><h2>Team - 99</h2></center>
                    ''', unsafe_allow_html = True)
        st.markdown(Contents, unsafe_allow_html=True)
        st.markdown('---')
        
        info('Abdelmalek Boughris (Frontend)', 'https://github.com/Boughris-Abdelmalek', 'https://www.linkedin.com/in/abdelmalek-boughris/', 'assets/mal.jfif')
        info('Talha abdurrahmaan (Backend/Dev-Ops)', 'https://github.com/Talha-Altair', 'https://www.linkedin.com/in/talhaabdurrahman/', 'assets/alt.jfif')
        info('M Z Muhammed Jaabir (AI/ML)', 'https://github.com/jaaabir', 'https://www.linkedin.com/in/muhammed-jaabir-94022019b/', 'assets/jab.jpg')
        info('Sashank Gs (AI/ML)', 'https://github.com/sashank24', 'https://www.linkedin.com/in/sashank-gs-97b1b91a4/', 'assets/sas.jpg')
    
    else:
        nlinks = [
            ('Structuring the datasets', os.path.join('.', 'structuring.ipynb')),
            ('Exploratory data analysis', os.path.join('.', 'eda.ipynb')),
        ]
        
        st.markdown('<h3>Notebook source</h3>', unsafe_allow_html=True)
        for cap,path in nlinks:
            st.markdown(f'''
                    <a href='{path}'>
                        <h4><p>{cap}</p></h4>
                    </a>
                    ''', unsafe_allow_html=True)
        
        st.markdown('<h3>App demo link</h3>', unsafe_allow_html=True)
        # st.markdown(f'''
        #             <a href='{path}'>
        #                 <h4><p>FLOOD</p></h4>
        #             </a>
        #             ''', unsafe_allow_html=True)
        
if __name__ == "__main__":
    streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Catamaran:wght@200&display=swap');
			html, body, [class*="css"]  {
			font-family: 'Catamaran', sans-serif;
			}
			</style>
			"""
    st.markdown(streamlit_style, unsafe_allow_html=True)
    main()
    
    