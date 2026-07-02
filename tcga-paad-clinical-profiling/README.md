## Overview
This project profiles clinical records from the TCGA Pancreatic Adenocarcinoma (PAAD) cohort to isolate survival trends across tumor grades, stages, and radiation therapy regimens using `pandas`.
## **Methodology:**

- Ingested 184 patient records from the TCGA PanCancer Atlas.
- Grouped cohorts by Histologic Grade (G1-G3), AJCC Tumor Stage, and Radiation Therapy status.
- Filtered out smaller cohorts (n < 10) to ensure valid findings
## **Key Insights

- Well-differentiated tumors (G1) predictably outperformed poorly differentiated tumors (G3) at the same staging.
    
- Within the G3/Stage IIB cohort, patients receiving radiation therapy showed a higher mean survival (22.1 months, n=12) compared to those who did not (13.2 months, n=27).
- 
- Whilst these findings indicate a correlation between radiation therapy and enhanced PAAD survival, further statistical modeling is required to establish therapeutic efficacy, as the effects of confounders (Ex: survivorship bias) were uncontrolled in this project.