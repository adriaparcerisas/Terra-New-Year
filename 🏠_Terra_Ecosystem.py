#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
import pandas as pd
import numpy as np
from shroomdk import ShroomDK
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker as ticker
import numpy as np
import altair as alt
sdk = ShroomDK("7bfe27b2-e726-4d8d-b519-03abc6447728")


# In[9]:


st.title('Terra Ecosystem Dashboard')


# In[10]:


st.markdown("Fueled by a passionate community and deep developer talent pool, the Terra blockchain is fully community-owned and built to enable the next generation of Web3 products and services [[1]](https://www.terra.money/).")
st.markdown("The events that happened in May 2022 in the world of cryptocurrencies were unprecedented in the history of this asset class; More than 40 billion dollars of capital was lost and many small investors from billion dollar funds suffered losses.")
st.markdown("In the first quarter of 2022, with the collapse of the crypto market, Anchor had become a serious problem for Terra. Billions of dollars that could have been put to other uses and used in other platforms and even in the real world were wasted only to make profit in Anchor smart contracts. Such an attractive profit was even a hindrance to other beneficial projects of the Terra ecosystem. The bear market had reduced demand for loans, and Anchor's reserves were dwindling daily at an alarming rate.")
st.markdown("The holidays and New Year are often chaotic in the crypto and DEFI space, as users make a spree of new transactions and wallets as they receive (and give) some cash and coins as holiday gifts. Has this flurry of winter activity impacted the Terra ecosystem? Are users creating new wallets or buying tokens with their newfound holiday wealth? Are they staking all those new tokens once they get them? Or are they selling tokens to pay for their own gifts and holiday travel?")

# In[11]:
st.markdown("The main idea of this app is to show an overview of how the entire **Terra Ecosystem** community respond to this new 2023 year and how all sectors changed during this first days. You can find information about each different section by navigating on the sidebar pages.")


# In[12]:


st.markdown("These includes:") 
st.markdown("1. **_Activity_**") 
st.markdown("2. **_Supply_**")
st.markdown("3. **_Staking_**")
st.markdown("4. **_Development_**")

