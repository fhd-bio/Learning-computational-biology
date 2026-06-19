import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/gbm_tcga,cell_pub2013_clinical_data.csv')
df = df.dropna(subset=['Disease Free (Months)', 'TMB (nonsynonymous)'])

x = df['Disease Free (Months)']
y = df['TMB (nonsynonymous)']
plt.scatter(x, y)
plt.xlabel('Disease Free (Months)')
plt.ylabel('TMB (nonsynonymous)')
plt.title('Glioblastoma Disease free status in months vs Total mutational burden (TBM)')
plt.show()
