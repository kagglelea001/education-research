# RDD Analysis with REAL Kaggle QS Data
Generated: 2025-07-31

## Data
- Source: Kaggle (padhmam/qs-2017-2022 + melissamonfared/qs-2025)
- Years: [np.int64(2017), np.int64(2018), np.int64(2019), np.int64(2020), np.int64(2021), np.int64(2022), np.int64(2025)]
- Universities: 3,408 rows
- Countries: 71

## RDD Summary
- Country-level obs: 315
- Treated: 152, Control: 163
- McCrary discontinuity: 8.6%

## RDD Results
 bandwidth    n  n_below  n_above  est   se    t      p sig  mean_outcome
         5  401      166      235 1.29 1.91 0.68 0.4999              41.1
         8  633      229      404 2.84 1.27 2.24 0.0254   *          41.2
        10  775      303      472 3.43 1.48 2.31 0.0213   *          41.0
        12  969      383      586 1.57 1.13 1.39 0.1655              41.4
        15 1219      504      715 1.30 1.02 1.28 0.2020              41.3

## Top 10 Universities (Latest Year)
-   1. Massachusetts Institute of Technology (MIT)   (United States       ) 100.0
-   2. Imperial College London                       (United Kingdom      ) 98.5
-   3. University of Oxford                          (United Kingdom      ) 96.9
-   4. Harvard University                            (United States       ) 96.8
-   5. University of Cambridge                       (United Kingdom      ) 96.7
-   6. Stanford University                           (United States       ) 96.1
-   7. ETH Zurich - Swiss Federal Institute of Techn (Switzerland         ) 93.9
-   8. National University of Singapore (NUS)        (Singapore           ) 93.7
-   9. UCL                                           (United Kingdom      ) 91.6
-  10. California Institute of Technology (Caltech)  (United States       ) 90.9
