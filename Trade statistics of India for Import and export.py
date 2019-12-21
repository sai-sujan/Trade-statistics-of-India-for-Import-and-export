#!/usr/bin/env python
# coding: utf-8

# In[67]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go


# In[68]:


import_india=pd.read_csv('2018-2010_import.csv')
export_india=pd.read_csv('2018-2010_export.csv')


# In[69]:


country_list=list(import_india.country.unique())


# In[70]:


country_group=import_india.groupby('country')
ls=[]
for country_name in country_list:
    ls.append([country_name, country_group.get_group(str(country_name)).value.sum() ])

total = pd.DataFrame(ls, columns = ['country', 'total_imports']) 


# In[71]:


total.loc[total.total_imports==0]


# In[72]:


largest_importers_dataframe=total.nlargest(5,['total_imports'])
largest_importers_dataframe['total_imports']=largest_importers_dataframe['total_imports']/1000 

plt.figure(figsize=(10,10))
sns.set_style('whitegrid')
largest_importers_bar=sns.barplot(x=largest_importers_dataframe['country'],y=largest_importers_dataframe['total_imports'])
plt.xlabel('COUNTRIES',size=18)
plt.ylabel('Total Imports in Billion $',size=18)
plt.title('LARGEST IMPORTERS TO INDIA 2010-2018',SIZE=20)


# In[73]:


top_5_importers_sum=largest_importers_dataframe.total_imports.sum() 

rest_of_the_world=total.sort_values('total_imports',ascending=False)[5:].total_imports.sum()/1000 

labels=['Rest of the world','Top 5']

colors = ['#99ff99','#ffcc99']

sizes=[rest_of_the_world,top_5_importers_sum]

explode = [ 0.1, 0.3]
plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(sizes, labels = labels, colors = colors, explode = explode, shadow = True,autopct='%1.2f')
plt.title('Top 5 Importers vs Rest of The world', fontsize = 20)
plt.legend()
plt.show()


# In[74]:


total.nlargest(5,['total_imports'])


# In[75]:


china=country_group.get_group('CHINA P RP')
imports_per_year_china=[]

for i in list(china['year'].unique())[::-1]:
    imports_per_year_china.append(china.sort_values('year').loc[china.year==i].value.sum()/1000)

year_china=list(china['year'].unique())[::-1]


plt.plot(year_china,imports_per_year_china,alpha=1,color='red',marker='o')

plt.xlabel('YEAR',size=17)
plt.ylabel('IMPORTS IN BILLION $',size=17)
plt.fill_between(year_china,imports_per_year_china,facecolor='#99ff99')
plt.title('TRADE TRENDS',size=20)


# In[76]:


fig, ax = plt.subplots()

UAE=country_group.get_group('U ARAB EMTS')
imports_per_year_uae=[]

for i in list(UAE['year'].unique())[::-1]:
    imports_per_year_uae.append(UAE.sort_values('year').loc[UAE.year==i].value.sum()/1000)

year_uae=list(UAE['year'].unique())[::-1]



saudi=country_group.get_group('SAUDI ARAB')
imports_per_year_saudi=[]

for i in list(saudi['year'].unique())[::-1]:
    imports_per_year_saudi.append(saudi.sort_values('year').loc[saudi.year==i].value.sum()/1000)

year_saudi=list(saudi['year'].unique())[::-1]


uae_line, = ax.plot(year_uae,imports_per_year_uae,alpha=0.99,color='green',marker='o',label='United Arab Emirates')

saudi_line, = ax.plot(year_saudi,imports_per_year_saudi,alpha=0.7,color='blue',marker='o',label='Saudi Arabia')

plt.xlabel('YEAR',size=17)
plt.ylabel('IMPORTS IN BILLION $',size=17)
plt.title('TRADE TRENDS',size=20)


ax.legend()
plt.show()


# In[77]:


china_detail=country_group.get_group('CHINA P RP')

c=china_detail.groupby('HSCode')

item_value_china=[]

for item in list(set(china_detail.HSCode)):
    item_value_china.append([item,
                             round(c.get_group(item).value.sum()/1000,5),
                             list(china_detail.loc[china_detail.HSCode==item].Commodity)[0]]),
          
df_china = pd.DataFrame(item_value_china, columns = ['HScode','Total_value', 'Name'])      

print(df_china.sort_values('Total_value',ascending=False)[:5])
df_china=df_china.sort_values('Total_value',ascending=False)

rest_of_the_imports_china=df_china.sort_values('Total_value',ascending=False)[5:].Total_value.sum() 

labels=['Rest of the imports','ELECTRICAL MACHINERY AND EQUIPMENT AND PARTS','NUCLEAR REACTORS, BOILERS, MACHINERY'
,'ORGANIC CHEMICALS','FERTILISERS','PROJECT GOODS; SOME SPECIAL USES']

colors = ['red','orange','yellow','green','grey','blue']

sizes=[rest_of_the_imports_china,df_china.Total_value[83],df_china.Total_value[82],df_china.Total_value[28],df_china.Total_value[30],df_china.Total_value[96]]


explode = [ 0.03, 0.03,0.1,0.1,0.1,0.3]
plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(sizes, labels = labels, colors = colors, explode = explode, shadow = True,autopct='%1.2f')
plt.title('Top Imported Items from China', fontsize = 20)
plt.show()


# In[78]:


export_india.head()
export_india.dtypes
export_india.isnull().sum()


# In[79]:


export_india.dropna(inplace=True)
export_india.drop_duplicates(keep="first",inplace=True)


# In[80]:


country_export_list=list(export_india.country.unique())


# In[81]:


export_india.loc[export_india.country=='UNSPECIFIED']


# In[82]:


country_export_group=export_india.groupby('country')
ls=[]
for country_name in country_export_list:
    ls.append([country_name, country_export_group.get_group(str(country_name)).value.sum() ])

total_exports = pd.DataFrame(ls, columns = ['country', 'total_exports'])
total_exports.loc[total_exports.total_exports==0]


# In[83]:


largest_exporters_dataframe=total_exports.nlargest(5,['total_exports'])
largest_exporters_dataframe['total_exports']=largest_exporters_dataframe['total_exports']/1000

plt.figure(figsize=(10,10))
sns.set_style('whitegrid')
largest_exporters_bar=sns.barplot(x=largest_exporters_dataframe['country'],y=largest_exporters_dataframe['total_exports'])
plt.xlabel('COUNTRIES',size=18)
plt.ylabel('Total exports in Billion $',size=18)
plt.title('LARGEST EXPORTERS OF INDIA 2010-2018',SIZE=20)


# In[84]:


usa_detail=country_export_group.get_group('U S A')

u=usa_detail.groupby('HSCode')

item_value_usa=[]

for item in list(set(usa_detail.HSCode)):
    item_value_usa.append([item,
                             round(u.get_group(item).value.sum()/1000,5),
                             list(usa_detail.loc[usa_detail.HSCode==item].Commodity)[0]]),
          
df_usa = pd.DataFrame(item_value_usa, columns = ['HScode','Total_value', 'Name'])      

print(df_usa.sort_values('Total_value',ascending=False)[:5])
df_usa=df_usa.sort_values('Total_value',ascending=False)

rest_of_the_imports_usa=df_usa.sort_values('Total_value',ascending=False)[5:].Total_value.sum() 

labels=['Rest of the imports','NATURAL OR CULTURED PEARLS','PHARMACEUTICAL PRODUCTS'
,'MINERAL FUELS, MINERAL OILS AND PRODUCTS','OTHER MADE UP TEXTILE ARTICLES','NUCLEAR REACTORS, BOILERS, MACHINERY']

colors = ['red','blue','orange','green','yellow','violet']

sizes=[rest_of_the_imports_usa,df_usa.Total_value[70],df_usa.Total_value[29],df_usa.Total_value[26],df_usa.Total_value[62],df_usa.Total_value[82]]

explode = [ 0.03, 0.03,0.1,0.1,0.1,0.3]
plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(sizes, labels = labels, colors = colors, explode = explode, shadow = True,autopct='%1.2f')
plt.title('Top Imported Items to USA', fontsize = 20)
plt.show()


# In[85]:


total_imports_per_year=import_india.groupby('year').agg({'value':'sum'})
total_exports_per_year=export_india.groupby('year').agg({'value':'sum'})
trade_deficit=[round(list(total_imports_per_year.value/1000)[i]-list(total_exports_per_year.value/1000)[i],2) for i in range(len(total_exports_per_year.index))]

trade_deficit=pd.Series(trade_deficit,index=total_exports_per_year.index)
sns.set_style('whitegrid')
trade_deficit.plot(kind='bar',color=['green','red'])
plt.xlabel('COUNTRIES',size=18)
plt.ylabel('TRADE DEFICIT in Billion $',size=18)
plt.title('YEARS',SIZE=20)


# In[86]:


df5 = import_india.groupby('country').agg({'value':'sum'})
df5 = df5.sort_values(by='value', ascending = False)
df5 = df5[:10]

df6 = export_india.groupby('country').agg({'value':'sum'})
df6 = df6.sort_values(by='value', ascending = False)
df6 = df6[:10]
sns.set(rc={'figure.figsize':(10,6)})
ax1 = plt.subplot(121)

sns.barplot(df5.value,df5.index).set_title('Country Wise Import')

ax2 = plt.subplot(122)
sns.barplot(df6.value,df6.index).set_title('Country Wise Export')
plt.tight_layout()
plt.show()


# In[87]:


df3 = import_india.groupby('Commodity').agg({'value':'sum'})
df3 = df3.sort_values(by='value', ascending = False)
df3 = df3[:10]

df4 = export_india.groupby('Commodity').agg({'value':'sum'})
df4 = df4.sort_values(by='value', ascending = False)
df4 = df4[:10]
sns.set(rc={'figure.figsize':(15,10)})

sns.barplot(df3.value,df3.index).set_title('Commodity Wise Import')
plt.show()

sns.barplot(df4.value,df4.index).set_title('Commodity Wise Import')
plt.show()


# In[88]:


expensive_import = import_india[import_india.value>1000]
expensive_import.head(10)


# In[ ]:





# In[89]:


plt.figure(figsize=(15,9))
ax = sns.boxplot(x="HSCode", y="value", data=expensive_import).set_title('Expensive Imports HsCode distribution')
plt.show()


# In[ ]:





# In[ ]:




