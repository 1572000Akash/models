import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#plotting of madhya pradesh
avvmpn =pd.read_csv('NEWSOYAMP.csv')
import plotly.express as px
# iris = px.data.iris()
fig = px.scatter_3d(avvmpn, x=avvmpn['arrival_date'], y=avvmpn['modal_price/Quintol'], z=avvmpn['Sold_Amount'],color ='district')
fig.show()

#plotting of maharastra
avvmhn =pd.read_csv('NEWSOYAMH.csv')
import plotly.express as px
# iris = px.data.iris()
fig = px.scatter_3d(avvmhn, x=avvmhn['arrival_date'], y=avvmhn['modal_price/Quintol'], z=avvmhn['Sold_Amount'],color ='district')
fig.show()

#plotting of rajisthan
avvrjn =pd.read_csv('NEWSOYARJ.csv')
import plotly.express as px
# iris = px.data.iris()
fig = px.scatter_3d(avvrjn, x=avvrjn['arrival_date'], y=avvrjn['modal_price/Quintol'], z=avvrjn['Sold_Amount'],color ='district')
fig.show()
