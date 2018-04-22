# %% imports
import numpy as np
import pandas as pd
import matplotlib
import pprint
import os
import sklearn

# %%


os.chdir(r'C:\Users\Administrator\Documents\kiva\data')

loans = pd.read_csv(r"C:\Users\Administrator\Documents\kiva\data\kiva_loans.csv")
display(loans.head(n=1))
display(loans.head(n=20))
loans.axes[1]
loans[5:6]
len(loans[loans.funded_amount<loans.loan_amount])/len(loans)
globals()
who
whos
tuple((loans.columns))
# %% IMPORT DATA
theme_ids=pd.read_csv('loan_theme_ids.csv')
themes_by_region=pd.read_csv('loan_themes_by_region.csv')
mpi_locs=pd.read_csv('kiva_mpi_region_locations.csv')
# %%

who

display(mpi_locs[mpi_locs.ISO=='AFG'])
display(theme_ids.head(n=3))
len(theme_ids)
len(loans)
len(themes_by_region)
len(mpi_locs)
display(themes_by_region.head(n=3))
