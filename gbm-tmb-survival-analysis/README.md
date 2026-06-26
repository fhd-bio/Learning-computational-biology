## Interpretation:
Consistent with current oncological research, the majority of datapoints were found to possess lower TMBs, which makes sense for glioblastoma as its known to be a low TMB cancer. The datapoints do not point to any particularly strong or weak correlation between TMB and disease free status in months, meaning GBM patients with the same TMB could hypothetically stay disease free for vastly different periods of time.

## Methodology
Dataset: TCGA Glioblastoma Cohort (Cell, 2013) via cBioPortal.
Variables : Non-synonymous Tumor Mutational Burden vs. Disease-Free Survival (Months).

## Technical Stack
pandas: Dataframe structuring and missing-value isolation.
matplotlib: Visual data distribution mapping.
numpy: correlation coefficient calculation.
