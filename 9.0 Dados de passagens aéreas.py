
# coding: utf-8

# # Análise de Dados - Passagens Aéreas

# In[130]:


# Importar biblioteca
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


# Ler o arquivo e criar DataFrame
df = pd.read_excel('201710_EmissaoPassagens_SCDP.xlsx', skiprows=3, skipfooter=3)


# In[36]:


df.columns = ['Código do órgão superior', 'Nome do órgão superior', 'Código do órgão solicitante da viagem', 
              'Nome do órgão solicitante da viagem', 'N. PCDP', 'N. Reserva/Localizador', 'Data Emissão Bilhete',
              'Data Embarque', 'Valor Tarifa Comercial', 'Percentual Desconto Aplicado', 'Valor Tarifa Governo',
              'Valor Tarifa Embarque', 'Valor Bilhete', 'Companhia Aérea', 'Classe Tarifária Bilhete', 'Regra Tarifária',
              'No Show', 'Remarcado', 'Cancelado', 'Valor Multas', 'Valor Reembolso', 'Diferença de Tarifa',
              'Situação Final Bilhete']


# In[37]:


df.info()


# In[48]:


df.shape


# In[81]:


df.sample(5)


# In[44]:


# Identificar as situacoes finais dos bilhetes.
df['Situação Final Bilhete'].unique()


# In[59]:


# Identificar as companhias aereas.
df['Companhia Aérea'].unique()


# In[65]:


# Distribuicao das situacoes finais dos bilhetes.
df['Situação Final Bilhete'].value_counts()


# In[101]:


# GRAFICO: Distribuicao das situacoes finais dos bilhetes.
df['Situação Final Bilhete'].value_counts().plot.bar()


# In[93]:


# Qual a Companhia com a maior valor de multa?
df[df['Valor Multas'] == df['Valor Multas'].max()]


# In[180]:


# GRAFICO: Qual a Companhia com a maior valor de multa?
df.groupby('Companhia Aérea')['Valor Multas'].max().plot.barh()


# In[182]:


# Qual a Companhia com a maior quantidade de multas?
df.groupby('Companhia Aérea')['Valor Multas'].sum()


# In[181]:


# GRAFICO: Qual a Companhia com a maior quantidade de multas?
df.groupby('Companhia Aérea')['Valor Multas'].sum().plot.barh()


# In[175]:


# Qual a Companhia com a maior Valor Tarifa Comercial?
df[df['Valor Tarifa Comercial'] == df['Valor Tarifa Comercial'].max()]


# In[176]:


# GRAFICO: # Qual a Companhia com a maior Valor Tarifa Comercial?
df.groupby('Companhia Aérea')['Valor Tarifa Comercial'].max().plot.barh()


# In[179]:


# GRAFICO: Passagens aereas por companhias.
df['Companhia Aérea'].value_counts().plot.barh()


# In[171]:


# Qual a Companhia com o maior Valor Tarifa Governo?
df[df['Valor Tarifa Governo'] == df['Valor Tarifa Governo'].max()]


# In[172]:


# GRAFICO: Qual a Companhia com o maior Valor Tarifa Governo?
df.groupby('Companhia Aérea')['Valor Tarifa Governo'].max().plot.barh()


# In[147]:


# Qual a Companhia com o maior Percentual Desconto Aplicado?
df[df['Percentual Desconto Aplicado'] == df['Percentual Desconto Aplicado'].max()]


# In[174]:


# GRAFICO: Qual a Companhia com o maior Percentual Desconto Aplicado?
df.groupby('Companhia Aérea')['Percentual Desconto Aplicado'].max().plot.barh()

