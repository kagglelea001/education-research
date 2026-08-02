# Empirical Analysis Report
## "Beyond the Flagship" — University Ranking Spillovers

### Data
- Systems: QS, THE, ARWU
- Panel: 6,737 obs, 100 countries
- Years: [np.int64(2005), np.int64(2006), np.int64(2007), np.int64(2008), np.int64(2009), np.int64(2010), np.int64(2011), np.int64(2012), np.int64(2013), np.int64(2014), np.int64(2015), np.int64(2016), np.int64(2017), np.int64(2018), np.int64(2019), np.int64(2020), np.int64(2021), np.int64(2022), np.int64(2025), np.int64(2026)]

### Cross-System Validation
- QS-THE overlap: 0 country-years
- QS Top 100: 156 | THE Top 100: 95

### RDD Causal Estimates
system  h   n  effect   se     t      p  mean_y
    QS  5 276    2.82 1.34  2.11 0.0354    37.3
    QS  8 421    1.08 1.11  0.98 0.3287    38.1
    QS 10 540    1.14 0.97  1.18 0.2397    38.0
    QS 12 694    0.42 0.85  0.49 0.6250    39.1
    QS 15 882    1.13 0.75  1.52 0.1299    39.1
   THE  5 207   -6.86 3.38 -2.03 0.0436    11.0
   THE  8 418  -14.77 2.31 -6.39 0.0000    13.0
   THE 10 466  -10.71 2.14 -5.01 0.0000    14.0
   THE 12 583    4.84 1.85  2.62 0.0090    15.2
   THE 15 786   12.25 1.54  7.95 0.0000    16.1

### Heterogeneity
- Developing country Top 100 share: 3.8%
- Developed country Top 100 share: 9.3%