#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st


# In[6]:


data = pd.read_csv(r"C:\Documents\pythondata\Pandas-Data-Science-Tasks-master\SalesAnalysis\all_datax.csv")


# In[7]:


data.head()


# In[8]:


nan_df=data[data.isna().any(axis=1)]


# In[9]:


datae = data[data != data.isin(nan_df)]


# In[10]:


datae


# In[11]:


datae.isnull().sum()


# In[12]:


data.rename(columns = {'Quantity Ordered':'Quantity_Ordered'},inplace= True)
data.rename(columns = {'Price Each':'Price'},inplace=True)


# In[13]:


#data['stop_duration']=data['stop_duration'].map({'0-15 Min':7.5,'16-30 Min':23,'30+ Min':45})
data['Order Date'].str[0:2].value_counts()


# In[14]:


data['Order Date'].str


# In[15]:


data['month']=data['Order Date'].str[0:2].map({'01':'janvier','02':'fevrier','03':'mars','04':'avril','05':'mai','06':'juin','07':'juillet','08':'out','09':'ceptember','10':'october','11':'november','12':'december'})


# In[16]:


data.dropna(how='all',inplace=True)


# In[17]:


data['data_spec']=data['Order Date'].str[0:6]



# In[18]:


data


# # janvier
# 

# In[19]:


data[data['month'] =='janvier'].head()
janvier=data[data['month'] =='janvier']


# In[20]:


janvier


# In[21]:


data.rename(columns = {'Quantity Ordered':'Quantity_Ordered'},inplace= True)
data.rename(columns = {'Price Each':'Price'},inplace=True)


# In[ ]:





# In[22]:


element=janvier.groupby('Product').Quantity_Ordered.count()


# In[23]:


element


# In[24]:


janvier.groupby('Product').Price.describe()


# In[25]:


janvier.groupby('Product').Quantity_Ordered.describe()


# In[26]:


janvier['Quantity_Ordered'].value_counts()


# In[27]:


janvier.groupby('Product').Quantity_Ordered.value_counts()


# In[28]:


janvier.head()


# In[29]:


janvier['Quantity_Ordered'].value_counts()


# # fevrier

# In[30]:


fevrier=data[data['month'] =='fevrier']


# In[31]:


fevrier.head()


# In[32]:


fevrier.groupby('Product').Price.describe()


# In[33]:


mars=data[data['month'] == 'mars']


# In[34]:


mars.head()


# In[35]:


mars.groupby('Product').Price.describe()


# In[36]:


avril=data[data['month']== 'avril']


# In[37]:


avril.head()


# In[38]:


avril.groupby('Product').Price.describe()


# In[39]:


mai=data[data['month'] == 'mai']
mai


# In[40]:


mai.groupby('Product').Price.describe()


# In[41]:


juin=data[data['month'] == 'juin']
juin.head()


# In[42]:


juin.groupby('Product').Price.describe()


# In[43]:


juillet=data[data['month'] == 'juillet']


# In[44]:


juillet.head()


# In[45]:


juillet.groupby('Product').Price.describe()


# In[46]:


out=data[data['month'] == 'out']


# In[47]:


out.head()


# In[48]:


out.groupby('Product').Price.describe()


# In[49]:


ceptember=data[data['month'] == 'ceptember']


# In[50]:


ceptember.head()


# In[51]:


ceptember.groupby('Product').Price.describe()


# In[52]:


october=data[data['month'] == 'october']


# In[53]:


october.groupby('Product').Price.describe()


# In[54]:


november=data[data['month'] == 'november']


# In[55]:


november.groupby('Product').Price.describe()


# In[56]:


december=data[data['month'] == 'december']
december.groupby('Product').Price.describe()


# In[57]:


allsal=pd.read_excel(r"C:\Documents\pythondata\Pandas-Data-Science-Tasks-master\SalesAnalysis\allales.xlsx")


# In[58]:


allsal


# In[59]:


chifre_affaire=pd.read_excel(r"C:\Documents\pythondata\Pandas-Data-Science-Tasks-master\SalesAnalysis\chifre_permonth.xlsx")


# In[60]:


chifre_affaire


# In[61]:


chifre_affaire[chifre_affaire['chiffre'] == np.max(chifre_affaire['chiffre'])]


# In[ ]:





# In[62]:


chifre_affaire[chifre_affaire['chiffre'] == np.min(chifre_affaire['chiffre'])]


# In[63]:


chifre_affaire['chiffre'].mean()


# In[ ]:





# ## janvier

# In[64]:


permonth = pd.read_excel(r"C:\Documents\pythondata\Pandas-Data-Science-Tasks-master\SalesAnalysis\chifre_permonth.xlsx")


# In[65]:


permonth


# In[66]:


plt.style.use( 'Solarize_Light2')

#1
plt.figure(figsize=(32,5))
plt.subplot(121)
plt.title('chiffre d affaire du notre companie')
plt.plot(permonth['month'],permonth['chiffre'],color='b',marker='o',linestyle='--',label='chifre')
plt.xticks(ticks=permonth['month'])
plt.xlabel('month')
plt.ylabel('chifre')
plt.legend()
plt.tight_layout()
#2
plt.figure(figsize=(34,5))
plt.subplot(122)
plt.title('par nomber de pieces')
plt.plot(permonth['month'],permonth['nbr_piece'],color='r',marker='o',linestyle='--',label='par nomber de pieces')
plt.xticks(ticks=permonth['month'])
plt.xlabel('month')
plt.ylabel('nombre de oiece')
plt.legend()
plt.tight_layout()


# In[67]:


janvier.head()


# In[ ]:





# In[68]:


janvier.groupby('Product').Price.describe()


# In[69]:


janvier_describe=janvier.groupby('Product').Price.describe()
fevrier_describe=fevrier.groupby('Product').Price.describe()
mars_describe=mars.groupby('Product').Price.describe()
avril_describe=avril.groupby('Product').Price.describe()
mai_describe=mai.groupby('Product').Price.describe()
juin_describe=juin.groupby('Product').Price.describe()
juillet_describe=juillet.groupby('Product').Price.describe()
out_describe=out.groupby('Product').Price.describe()
ceptember_describe=ceptember.groupby('Product').Price.describe()
october_describe=october.groupby('Product').Price.describe()
november_describe=november.groupby('Product').Price.describe()
december_describe=december.groupby('Product').Price.describe()


# In[70]:


janvier_describe[janvier_describe['count'] ==1174]


# In[71]:


janvier_describe[janvier_describe['count'] ==39]


# In[72]:


janvier_describe['count'].mean()


# In[73]:


janvier_describe['count'].var()


# In[74]:


janvier_describe['count'].agg(['max','min','sum','mean','std'])


# In[75]:


janvier.head()


# In[76]:


janvier.groupby('data_spec').month.count()


# In[77]:


print('max', janvier.groupby('data_spec').month.count().max() ,'min',janvier.groupby('data_spec').month.count().min() ,
      'mean', janvier.groupby('data_spec').month.count().mean()
     )


# # fevrier

# In[78]:


fevrier.groupby('Product').Price.describe()


# In[79]:



fevrier_describe[fevrier_describe['count']==1514]


# In[80]:



print(fevrier.groupby('Product').Price.describe()['count'].min(),fevrier.groupby('Product').Price.describe()['count'].max())


# In[81]:


fevrier_describe[fevrier_describe['count']==38]


# In[82]:


fevrier_describe['count'].agg(['max','min','sum','mean','std'])


# In[83]:


fevrier_describe.drop(columns={'new'},inplace=True)


# In[85]:


fevrier_describe


# In[86]:


print('max', fevrier.groupby('data_spec').month.count().max() ,'min',fevrier.groupby('data_spec').month.count().min() ,
      'mean' ,fevrier.groupby('data_spec').month.count().mean()
     )


# # mars

# In[87]:


mars.groupby('Product').Price.describe()


# In[88]:


mars_describe[mars_describe['count']==1770]


# In[89]:


print(mars.groupby('Product').Price.describe()['count'].min(),mars.groupby('Product').Price.describe()['count'].max())


# In[90]:


mars_describe[mars_describe['count']==49]


# In[92]:


#nombre d achats pour les produits

mars_describe['count'].agg(['max','min','sum','mean','std'])


# In[91]:



#chifre d affaire pour 1 jours

print('max', mars.groupby('data_spec').month.count().max() ,'min',mars.groupby('data_spec').month.count().min() ,

      'mean' ,mars.groupby('data_spec').month.count().mean()
     )


# # avril

# april.groupby('Product').Price.describe()

# In[93]:


avril.groupby('Product').Price.describe()


# In[94]:


print(avril.groupby('Product').Price.describe()['count'].min(),avril.groupby('Product').Price.describe()['count'].max())


# In[95]:


avril_describe[avril_describe['count']==2203]


# In[96]:


avril_describe[avril_describe['count']==61]


# In[97]:


#nombre d achats pour les produits
avril_describe['count'].agg(['max','min','sum','mean','std'])


# In[98]:


#chifre d affaire pour 1 jours
print('max', avril.groupby('data_spec').month.count().max() ,'min',avril.groupby('data_spec').month.count().min() ,
      'mean' ,avril.groupby('data_spec').month.count().mean()
     )


# # mai

# In[99]:


mai.groupby('Product').Price.describe()


# In[100]:


print(mai.groupby('Product').Price.describe()['count'].min(),mai.groupby('Product').Price.describe()['count'].max())


# In[101]:


mai_describe[mai_describe['count']==1930]


# In[ ]:


mai_describe[mai_describe['count']==64]


# In[102]:



#nombre d achats pour les produits
mai_describe['count'].agg(['max','min','sum','mean','std'])


# In[103]:


#chifre d affaire pour 1 jours
print('max', mai.groupby('data_spec').month.count().max() ,'min',mai.groupby('data_spec').month.count().min() ,
      'mean' ,mai.groupby('data_spec').month.count().mean()
     )


# # juin

# In[104]:


juin.groupby('Product').Price.describe()


# In[105]:


print(juin.groupby('Product').Price.describe()['count'].min(),juin.groupby('Product').Price.describe()['count'].max())


# In[106]:


juin_describe[juin_describe['count']==1564]


# In[107]:


juin_describe[juin_describe['count']==43]


# In[113]:


#nombre d achats pour les produits
juin_describe['count'].agg(['max','min','sum','mean','std'])


# In[114]:


#chifre d affaire pour 1 jours
print('max', juin.groupby('data_spec').month.count().max() ,'min',juin.groupby('data_spec').month.count().min() ,
      'mean' ,juin.groupby('data_spec').month.count().mean()
     )


# # juillet

# In[115]:


juillet.groupby('Product').Price.describe()


# In[116]:


print(juillet.groupby('Product').Price.describe()['count'].min(),juillet.groupby('Product').Price.describe()['count'].max())


# In[120]:


juillet_describe[juillet_describe['count']==1695]


# In[124]:


juillet_describe[juillet_describe['count']==52]


# In[125]:


#nombre d achats pour les produits
juillet_describe['count'].agg(['max','min','sum','mean','std'])


# In[126]:


#chifre d affaire pour 1 jours
print('max', juillet.groupby('data_spec').month.count().max() ,'min',juillet.groupby('data_spec').month.count().min() ,
      'mean' ,juillet.groupby('data_spec').month.count().mean()
     )


# # Aout

# In[127]:


out.groupby('Product').Price.describe()


# In[128]:


print(out.groupby('Product').Price.describe()['count'].min(),out.groupby('Product').Price.describe()['count'].max())


# In[129]:


out_describe[out_describe['count']==1357]


# In[130]:


out_describe[out_describe['count']==46]


# In[131]:


#nombre d achats pour les produits
out_describe['count'].agg(['max','min','sum','mean','std'])


# In[132]:


#chifre d affaire pour 1 jours
print('max', out.groupby('data_spec').month.count().max() ,'min',out.groupby('data_spec').month.count().min() ,
      'mean' ,out.groupby('data_spec').month.count().mean()
     )


# # ceptember

# In[133]:


ceptember.groupby('Product').Price.describe()


# In[134]:


print(ceptember.groupby('Product').Price.describe()['count'].min(),ceptember.groupby('Product').Price.describe()['count'].max())


# In[135]:


ceptember_describe[ceptember_describe['count']==1454]


# In[136]:


ceptember_describe[ceptember_describe['count']==30]


# In[137]:


#nombre d achats pour les produits
ceptember_describe['count'].agg(['max','min','sum','mean','std'])


# In[138]:


#chifre d affaire pour 1 jours
print('max', ceptember.groupby('data_spec').month.count().max() ,'min',ceptember.groupby('data_spec').month.count().min() ,
      'mean' ,ceptember.groupby('data_spec').month.count().mean()
     )


# In[139]:


data['month'].value_counts()


# # october

# In[162]:


october.groupby('Product').Price.describe()


# In[141]:


print(october.groupby('Product').Price.describe()['count'].min(),october.groupby('Product').Price.describe()['count'].max())


# In[142]:


october_describe[october_describe['count']==2442]


# In[143]:


october_describe[october_describe['count']==50]


# In[144]:


#nombre d achats pour les produits
october_describe['count'].agg(['max','min','sum','mean','std'])


# In[145]:


#chifre d affaire pour 1 jours
print('max', october.groupby('data_spec').month.count().max() ,'min',october.groupby('data_spec').month.count().min() ,
      'mean' ,october.groupby('data_spec').month.count().mean()
     )


# # november

# In[146]:


november.groupby('Product').Price.describe()


# In[147]:


print(november.groupby('Product').Price.describe()['count'].min(),november.groupby('Product').Price.describe()['count'].max())


# In[148]:


november_describe[november_describe['count']==2062]


# In[149]:


november_describe[november_describe['count']==53]


# In[150]:


#nombre d achats pour les produits
november_describe['count'].agg(['max','min','sum','mean','std'])


# In[151]:


#chifre d affaire pour 1 jours
print('max', november.groupby('data_spec').month.count().max() ,'min',november.groupby('data_spec').month.count().min() ,
      'mean' ,november.groupby('data_spec').month.count().mean()
     )


# # december

# In[152]:


december.groupby('Product').Price.describe()


# In[154]:


print(december.groupby('Product').Price.describe()['count'].min(),december.groupby('Product').Price.describe()['count'].max())


# In[155]:


december_describe[december_describe['count']==2980]


# In[156]:


december_describe[december_describe['count']==80]


# In[157]:


#nombre d achats pour les produits
december_describe['count'].agg(['max','min','sum','mean','std'])


# In[158]:


#chifre d affaire pour 1 jours
print('max', december.groupby('data_spec').month.count().max() ,'min',december.groupby('data_spec').month.count().min() ,
      'mean' ,december.groupby('data_spec').month.count().mean()
     )


# # end
# 

# In[ ]:





# In[ ]:





# In[ ]:




