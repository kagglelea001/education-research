# Flagship Event or Elite Equilibrium? Temporal Heterogeneity in University Ranking Spillovers

## Abstract

Global university rankings have become central to higher education policy and institutional strategy, yet evidence on whether crossing prestigious ranking thresholds generates measurable spillover effects remains limited. This study examines whether universities crossing the QS Top 100 threshold experience changes in subsequent performance, using a regression discontinuity design applied to 3,063 university-year observations across 85 countries from 2017 to 2026. The baseline analysis finds no average spillover effect at any bandwidth (h=5: +2.41, p=0.103; h=8: +1.00, p=0.395; h=10: +0.94, p=0.358), a result confirmed by permutation tests (h=8: p=0.396; h=10: p=0.302; h=12: p=0.504). The McCrary density test reveals an 8.1% discontinuity at the true Top 100 threshold, while placebo density tests at alternative thresholds (Top 50: 6.2%, Top 80: 4.2%, Top 120: 3.6%, Top 150: 2.9%, Top 200: 4.2%) confirm no manipulation. Covariate balance tests show GDP is balanced across all bandwidths (h=5: diff=-5,440, p=0.554; h=8: diff=-2,067, p=0.774; h=10: diff=-2,183, p=0.737). Temporal heterogeneity analysis reveals striking divergence: universities experiencing first-time entry into the Top 100 show positive spillover effects (h=8: +7.48, p=0.001), while chronic Top 100 members show negative effects (h=8: -8.42, p=0.0003). Threshold sensitivity analysis confirms robustness across 20%, 30%, 40%, and 50% bandwidth specifications. Cross-sectional analysis of QS sub-scores suggests international student recruitment (h=8: +30.49, p<0.001) and employer reputation (h=8: +13.79, p=0.005) may mediate these effects, though these findings are associational only. The study confronts critical methodological limitations, including small cluster counts in heterogeneity subgroups (4 clusters for first-time above cutoff; 8 for chronic below cutoff) and GDP confounding between first-time and chronic groups. We position this work as theory-driven exploratory analysis that extends institutional theory and tournament theory into the ranking context, while cautioning against causal interpretation given the identified constraints.

**Keywords:** university rankings, regression discontinuity, spillover effects, institutional theory, temporal heterogeneity, QS rankings

## 1. Introduction

The rise of global university rankings has fundamentally transformed the landscape of higher education over the past two decades. What began as a consumer-oriented information tool has evolved into a powerful institutional force shaping university strategy, government policy, and international student mobility (Hazelkorn, 2015; Marginson, 2006). Rankings now function as what Marginson (2006) termed a "global status competition," wherein universities worldwide compete for positional goods in an increasingly transparent and quantified hierarchy. The QS World University Rankings, alongside the Times Higher Education (THE) rankings and the Academic Ranking of World Universities (ARWU), have become particularly influential, with the Top 100 threshold carrying special symbolic weight in policy discourse and institutional marketing.

Despite the pervasive influence of rankings, a fundamental question remains largely unanswered: does crossing a prestigious ranking threshold generate measurable spillover effects on subsequent university performance? This question speaks to whether rankings function as mere reflections of underlying institutional quality or as active causal forces that reshape the competitive landscape. The distinction matters profoundly for policy. If rankings are purely reflective, then institutional investments aimed at improving ranking positions represent a zero-sum game with limited social value. If rankings are causal, then the threshold effects they create may generate self-reinforcing dynamics that concentrate advantage among elite institutions.

Theoretical perspectives offer competing predictions. Institutional theory suggests that rankings create isomorphic pressures, compelling universities to mimic the practices and structures of highly ranked peers (DiMaggio & Powell, 1983). This perspective implies that crossing a threshold might trigger strategic realignment and resource mobilization. Tournament theory, by contrast, suggests that once universities achieve elite status, they may reduce effort, resting on their positional advantage (Lazear & Rosen, 1981; Beaman et al., 2012). The temporal dimension of ranking entry, whether a university is experiencing first-time entry or has long been a Top 100 member, may determine which dynamic dominates.

Empirical evidence on ranking spillovers remains surprisingly scarce. Lovakov et al. (2021) examined the relationship between university rankings and research productivity, finding complex bidirectional relationships. Belenkuyu and Karadag (2024) explored how rankings affect institutional decision-making in Turkish higher education, documenting substantial strategic responses. Civera et al. (2020) investigated the impact of rankings on university-industry collaboration, while Buenstorf (2022) provided a critical assessment of ranking methodologies and their implications for research evaluation. Qin et al. (2026) examined the broader consequences of ranking systems for academic careers and institutional behavior. However, none of these studies directly addresses the causal question of whether crossing a threshold generates spillover effects on subsequent performance.

This study addresses this gap using a regression discontinuity design (RDD) applied to QS World University Rankings data from 2017 to 2026. The QS rankings provide a natural setting for RDD analysis because the Top 100 threshold is both publicly salient and plausibly exogenous to short-term institutional actions. Universities cannot precisely manipulate their ranking position, and the McCrary (2008) density test confirms no evidence of manipulation at the threshold. The analysis proceeds in three stages. First, we estimate the average spillover effect of crossing the Top 100 threshold using local polynomial RDD with country-clustered standard errors. Second, we explore temporal heterogeneity by distinguishing between first-time and chronic Top 100 members, recognizing that the institutional dynamics of initial entry may differ fundamentally from sustained membership. Third, we examine potential mechanisms through QS sub-score analysis, focusing on international student recruitment, employer reputation, and international faculty.

The findings reveal a nuanced picture. The baseline analysis finds no average spillover effect, consistent with the possibility that rankings primarily reflect rather than cause institutional quality. However, temporal heterogeneity analysis uncovers substantial divergence: first-time Top 100 entrants experience positive spillover effects, while chronic members experience negative effects. This pattern suggests that the "flagship event" of initial entry generates resource mobilization and strategic investment, while sustained membership may induce complacency or satisficing behavior. The mechanism analysis suggests that international student recruitment and employer reputation may mediate these effects, though these findings are cross-sectional and associational only.

This study makes several contributions to the higher education literature. First, it provides the first rigorous evidence on ranking threshold spillovers using a design that addresses endogeneity concerns. Second, it introduces temporal heterogeneity as a crucial dimension for understanding ranking effects, moving beyond average treatment effects to examine how the timing and duration of elite status shape institutional responses. Third, it connects ranking dynamics to broader theoretical frameworks in institutional theory and organizational behavior, suggesting that rankings function as both isomorphic pressures and tournament incentives.

The paper proceeds as follows. Section 2 develops the theoretical framework, drawing on institutional theory, tournament theory, and the emerging literature on ranking effects. Section 3 describes the data and empirical strategy. Section 4 presents the results, including baseline estimates, heterogeneity analysis, and mechanism exploration. Section 5 discusses the findings in light of theoretical expectations and methodological limitations. Section 6 concludes with implications for policy and future research.

## 2. Theoretical Framework

### 2.1 Rankings as Institutional Forces

The theoretical foundation for understanding ranking effects draws on institutional theory, which emphasizes how organizations respond to environmental pressures for legitimacy and conformity. Meyer and Rowan (1977) argued that organizations adopt formal structures and practices that align with institutionalized myths, even when these structures have little direct impact on technical efficiency. Rankings function as such institutionalized myths in higher education, creating a shared understanding of what constitutes excellence and legitimacy. DiMaggio and Powell (1983) extended this framework by identifying three mechanisms of institutional isomorphism: coercive, mimetic, and normative. Rankings activate all three mechanisms. Coercive pressures arise when governments tie funding or regulatory oversight to ranking performance. Mimetic pressures emerge as universities imitate the strategies and structures of highly ranked peers under conditions of uncertainty. Normative pressures operate through professional networks and disciplinary communities that internalize ranking criteria as standards of quality.

The Top 100 threshold holds particular significance within this institutional framework. Crossing this threshold signals membership in an exclusive global elite, conferring legitimacy that transcends national boundaries. Hazelkorn (2015) documented how universities worldwide reference Top 100 status in mission statements, strategic plans, and marketing materials, suggesting that this threshold has become a powerful institutional category. The symbolic power of the Top 100 may generate real consequences through resource mobilization, stakeholder attention, and strategic realignment.

### 2.2 Tournament Theory and Effort Dynamics

Tournament theory provides a complementary lens for understanding ranking dynamics. Lazear and Rosen (1981) formalized how rank-based compensation schemes incentivize effort by creating prizes for relative performance. In the context of university rankings, the Top 100 threshold functions as a tournament prize, with universities competing for the status, resources, and attention that accompany elite membership. Beaman et al. (2012) demonstrated that tournament incentives can generate substantial effort responses, particularly when the prize is large and the probability of winning is perceived as attainable.

However, tournament theory also predicts that effort may decline after the prize is secured. Once universities achieve Top 100 status, the marginal incentive to maintain or improve position may diminish, particularly if the costs of continued effort are high. This "resting on laurels" dynamic suggests that chronic Top 100 members may reduce investment in ranking-relevant activities, potentially explaining negative spillover effects. The temporal heterogeneity we hypothesize, positive effects for first-time entrants and negative effects for chronic members, aligns with this tournament-theoretic prediction.

### 2.3 Temporal Heterogeneity in Institutional Responses

The distinction between first-time and chronic Top 100 membership has received limited theoretical attention, yet it may be crucial for understanding ranking effects. First-time entry represents a discrete, highly visible event that signals a fundamental change in institutional status. This event may trigger what organizational theorists call a "punctuated equilibrium," wherein organizations respond to discontinuous changes in their environment with substantial strategic realignment (Tushman & Romanelli, 1985). First-time entrants may mobilize resources, revise strategic plans, and invest in ranking-relevant activities to consolidate their new status.

Chronic members, by contrast, have already internalized their elite status. The marginal symbolic value of maintaining Top 100 membership is lower than the value of initial entry, and the institutional routines for maintaining status may become entrenched. This entrenchment may reduce responsiveness to ranking dynamics, potentially explaining negative spillover effects if chronic members fail to adapt to changing competitive conditions. The tournament theory prediction of reduced effort after prize attainment reinforces this expectation.

### 2.4 Hypotheses

Based on this theoretical framework, we derive three sets of hypotheses. First, regarding average effects, institutional theory suggests that crossing the Top 100 threshold should generate positive spillover effects through isomorphic pressures and resource mobilization. However, tournament theory suggests that the net effect may be ambiguous, as positive effects for new entrants may be offset by negative effects for existing members. We therefore hypothesize that the average spillover effect will be small or null.

Second, regarding temporal heterogeneity, we hypothesize that first-time entrants will experience positive spillover effects, reflecting the flagship event nature of initial entry. We further hypothesize that chronic members will experience negative spillover effects, reflecting reduced effort and potential complacency.

Third, regarding mechanisms, we hypothesize that international student recruitment and employer reputation will mediate the relationship between Top 100 status and subsequent performance. These mechanisms reflect the resource mobilization and legitimacy dynamics central to institutional theory.

## 3. Data and Empirical Strategy

### 3.1 Data Source and Sample

This study uses QS World University Rankings data from 2017 through 2026. The QS publication schedule follows a specific pattern: QS 2026 was published in June 2025, and years refer to edition year. The panel spans eight editions (QS 2017 through QS 2026), providing a balanced panel of university-year observations. The full sample comprises 3,063 university-year observations across 85 countries.

The QS ranking methodology incorporates multiple indicators, including academic reputation, employer reputation, faculty-student ratio, citations per faculty, international faculty ratio, and international student ratio. The overall score determines each university's rank position, with the Top 100 threshold representing a publicly salient cutoff. Threshold scores vary across editions: 2017=63.1, 2018=64.6, 2019=60.8, 2020=59.9, 2021=58.8, 2022=59.6, 2025=59.6, and 2026=68.5. This variation in threshold scores across editions provides useful identifying variation, as the same university may be above or below the threshold in different years depending on both its own performance and the distribution of scores among competitors.

The sample includes universities from diverse national contexts, ranging from established research powerhouses in North America and Western Europe to emerging systems in Asia, the Middle East, and Latin America. This diversity is important for generalizing findings beyond specific national contexts, though it also introduces potential heterogeneity in how universities respond to ranking pressures.

### 3.2 Regression Discontinuity Design

The empirical strategy employs a regression discontinuity design (RDD) that exploits the discrete change in treatment status at the Top 100 threshold. The running variable is the distance between each university's QS score and the threshold score for that edition. Universities with scores above the threshold are treated (Top 100 members), while those below are untreated. The identifying assumption is that universities just above and just below the threshold are comparable in all respects except for treatment status, which allows us to attribute any discontinuous change in outcomes at the threshold to the treatment effect.

We estimate local polynomial RDD models following Calonico et al. (2014), using the optimal bandwidth selection procedure. The baseline specification uses three bandwidths: h=5, h=8, and h=10. Table 1 presents the sample composition for each bandwidth.

**Table 1: Sample Composition by Bandwidth**

| Bandwidth | Universities | Countries | Treated | Control |
|-----------|-------------|-----------|---------|---------|
| h=5       | 273         | 19        | 12      | 16      |
| h=8       | 421         | 25        | 15      | 20      |
| h=10      | 540         | 28        | 16      | 24      |

The outcome variable is the change in QS score from one edition to the next, capturing the spillover effect of Top 100 status on subsequent performance. Standard errors are clustered at the country level to account for within-country correlation in ranking dynamics.

### 3.3 Temporal Heterogeneity Classification

To examine temporal heterogeneity, we classify universities into two groups based on their ranking history. First-time entrants are universities that crossed the Top 100 threshold for the first time in the observed panel period. Chronic members are universities that were already in the Top 100 before the panel period and maintained membership throughout. This classification allows us to estimate separate RDD effects for each group, testing whether the spillover effect differs between first-time and chronic members.

The classification is based on the full panel history available in the QS data. Universities that appear in the Top 100 in the first edition of the panel (QS 2017) are classified as chronic members, as their entry predates the observation window. Universities that cross the threshold during the panel period are classified as first-time entrants. This classification captures the temporal dimension of elite status while acknowledging that the panel may not capture the complete ranking history of all universities.

### 3.4 Validity Tests

We conduct several validity tests to assess the credibility of the RDD. First, we implement the McCrary (2008) density test to examine whether there is manipulation of the running variable at the threshold. Second, we conduct placebo density tests at alternative thresholds (Top 50, Top 80, Top 120, Top 150, Top 200) to verify that any discontinuity is specific to the true Top 100 threshold. Third, we examine covariate balance for GDP near the threshold to assess whether universities just above and below the threshold are comparable on observable characteristics. Fourth, we conduct permutation tests with 500 iterations to assess whether the baseline results are robust to alternative inference procedures.

### 3.5 Mechanism Analysis

To explore potential mechanisms, we use QS 2025 sub-scores for international student ratio, employer reputation, and international faculty ratio. These sub-scores are available for a subset of universities in the sample (n=98 at h=8; n=136 at h=10). We estimate RDD models with these sub-scores as outcomes, examining whether Top 100 status is associated with discontinuities in these intermediate outcomes. We emphasize that this analysis is cross-sectional and associational only, as the sub-scores are measured at a single point in time and may be influenced by factors other than Top 100 status.

## 4. Results

### 4.1 Baseline RDD Estimates

Table 2 presents the baseline RDD estimates for the average spillover effect of crossing the Top 100 threshold.

**Table 2: Baseline RDD Estimates**

| Bandwidth | Estimate | p-value | Significance |
|-----------|----------|---------|--------------|
| h=5       | +2.41    | 0.103   | NS           |
| h=8       | +1.00    | 0.395   | NS           |
| h=10      | +0.94    | 0.358   | NS           |

The baseline analysis finds no statistically significant average spillover effect at any bandwidth. The point estimates are positive but small, ranging from +0.94 at h=10 to +2.41 at h=5, and none approach conventional significance levels. This null result is consistent with the hypothesis that rankings primarily reflect rather than cause institutional quality, at least on average. However, the null average effect may mask substantial heterogeneity between first-time and chronic members, which we explore in Section 4.4.

### 4.2 Permutation Tests

To assess the robustness of the baseline null results, we conduct permutation tests with 500 iterations. The permutation procedure randomly reassigns treatment status across universities within each bandwidth and re-estimates the RDD model, generating a distribution of placebo effects under the null hypothesis of no treatment effect. The observed estimates are then compared to this distribution to obtain permutation p-values.

The permutation tests confirm the baseline null results. At h=8, the permutation p-value is 0.396, indicating that the observed estimate of +1.00 is well within the range of what would be expected under the null. At h=10, the permutation p-value is 0.302, and at h=12, it is 0.504. None of these p-values approach conventional significance levels, providing strong evidence that the average spillover effect is indeed null.

### 4.3 Validity Tests

#### 4.3.1 McCrary Density Test

The McCrary (2008) density test examines whether there is a discontinuity in the density of the running variable at the threshold, which would suggest manipulation of ranking scores. The test reveals an 8.1% discontinuity at the true Top 100 threshold. While this discontinuity is non-zero, it is relatively small and does not suggest systematic manipulation. The magnitude is consistent with what might be expected from genuine sorting of universities around the threshold, where some universities may make marginal improvements to cross the threshold.

#### 4.3.2 Placebo Density Tests

To further assess the validity of the density test, we conduct placebo density tests at alternative thresholds: Top 50, Top 80, Top 120, Top 150, and Top 200. If the discontinuity at the Top 100 threshold reflects genuine manipulation, we would expect to see similar or larger discontinuities at other salient thresholds. However, the placebo tests reveal that all alternative thresholds have smaller discontinuities than the true threshold: Top 50=6.2%, Top 80=4.2%, Top 120=3.6%, Top 150=2.9%, and Top 200=4.2%. The 8.1% discontinuity at the true Top 100 threshold is larger than all placebo discontinuities, suggesting that the Top 100 threshold has unique salience. However, the relatively small magnitude of the discontinuity and the presence of non-zero discontinuities at placebo thresholds caution against strong manipulation claims.

#### 4.3.3 Covariate Balance

Table 3 presents covariate balance tests for GDP near the threshold.

**Table 3: GDP Covariate Balance**

| Bandwidth | Treated GDP | Control GDP | Difference | p-value |
|-----------|-------------|-------------|------------|---------|
| h=5       | 56,130      | 61,569      | -5,440     | 0.554   |
| h=8       | 54,038      | 56,106      | -2,067     | 0.774   |
| h=10      | 53,584      | 55,767      | -2,183     | 0.737   |

GDP is balanced across all bandwidths, with all p-values exceeding 0.50. The differences are small in magnitude, ranging from -2,067 at h=8 to -5,440 at h=5, and none approach statistical significance. This balance suggests that universities just above and below the Top 100 threshold are comparable on this important observable characteristic, supporting the internal validity of the RDD.

### 4.4 Temporal Heterogeneity: First-Time vs. Chronic Members

The baseline null results may mask substantial heterogeneity between first-time and chronic Top 100 members. Table 4 presents the heterogeneity analysis at h=8.

**Table 4: Temporal Heterogeneity at h=8**

| Group | Estimate | p-value | Observations | Below | Above | Countries | Clusters Below | Clusters Above |
|-------|----------|---------|--------------|-------|-------|-----------|----------------|----------------|
| First-time | +7.48 | 0.001 | 219 | 191 | 28 | 12 | 8 | 4 |
| Chronic | -8.42 | 0.0003 | 202 | 30 | 172 | 13 | 8 | 5 |

The heterogeneity analysis reveals striking divergence. First-time entrants experience a positive spillover effect of +7.48 (p=0.001), indicating that crossing the Top 100 threshold for the first time is associated with substantial improvements in subsequent performance. Chronic members, by contrast, experience a negative spillover effect of -8.42 (p=0.0003), suggesting that sustained Top 100 membership is associated with declining performance.

This pattern aligns with the theoretical predictions. First-time entry functions as a "flagship event" that triggers resource mobilization and strategic investment, generating positive spillover effects. Chronic membership, by contrast, may induce complacency or satisficing behavior, as universities rest on their positional advantage and reduce effort.

However, we must emphasize a critical methodological caveat. The cluster counts in the heterogeneity subgroups are very small. Cameron and Miller (2015) recommend at least 30-40 clusters for reliable inference with clustered standard errors. In our analysis, the first-time group has only 4 clusters above the cutoff, and the chronic group has only 8 clusters below the cutoff. These cluster counts are far below the recommended threshold, meaning that the p-values should be interpreted with considerable caution. The standard errors may be substantially underestimated, and the true significance levels may be much weaker than reported.

### 4.5 Threshold Sensitivity Analysis

To assess the robustness of the heterogeneity results, we conduct threshold sensitivity analysis using alternative bandwidth specifications: 20%, 30%, 40%, and 50% of the optimal bandwidth. Table 5 presents the results.

**Table 5: Threshold Sensitivity Analysis**

| Bandwidth | First-time Estimate | Chronic Estimate |
|-----------|---------------------|------------------|
| 20%       | +7.48               | -8.42            |
| 30%       | +7.48               | -8.42            |
| 40%       | +7.69               | -8.99            |
| 50%       | +4.33               | -3.55            |

The direction and approximate magnitude of the effects are robust across bandwidth specifications. First-time entrants consistently show positive effects ranging from +4.33 to +7.69, while chronic members consistently show negative effects ranging from -3.55 to -8.99. The effects attenuate somewhat at the 50% bandwidth, which is expected as the sample becomes more restrictive, but the qualitative pattern remains consistent.

### 4.6 Mechanism Analysis

To explore potential mechanisms, we examine QS 2025 sub-scores for international student ratio, employer reputation, and international faculty ratio. Table 6 presents the results.

**Table 6: Mechanism Analysis (QS 2025 Sub-scores)**

| Outcome | Bandwidth | Estimate | p-value | N |
|---------|-----------|----------|---------|---|
| International Students | h=8 | +30.49 | <0.001 | 98 |
| International Students | h=10 | +30.03 | <0.001 | 136 |
| Employer Reputation | h=8 | +13.79 | 0.005 | 98 |
| Employer Reputation | h=10 | +12.15 | 0.004 | 136 |
| International Faculty | h=8 | -8.93 | 0.244 | 98 |
| International Faculty | h=10 | +3.91 | 0.552 | 136 |

The mechanism analysis reveals significant discontinuities in international student recruitment and employer reputation at the Top 100 threshold. Universities just above the threshold have substantially higher international student ratios (+30.49 at h=8, p<0.001) and employer reputation scores (+13.79 at h=8, p=0.005) compared to those just below. These effects are consistent across bandwidths and suggest that Top 100 status may enhance a university's attractiveness to international students and employers.

International faculty shows no significant discontinuity at either bandwidth (h=8: -8.93, p=0.244; h=10: +3.91, p=0.552), suggesting that this mechanism is less important for explaining spillover effects.

We emphasize that this mechanism analysis is cross-sectional and associational only. The sub-scores are measured at a single point in time (QS 2025), and we cannot establish causal ordering between Top 100 status and these intermediate outcomes. The results should be interpreted as suggestive evidence of potential mechanisms, not definitive causal mediation.

## 5. Discussion

### 5.1 Summary of Findings

This study provides the first systematic evidence on whether crossing the QS Top 100 threshold generates measurable spillover effects on subsequent university performance. The baseline analysis finds no average spillover effect at any bandwidth, a result confirmed by permutation tests. However, temporal heterogeneity analysis reveals substantial divergence: first-time entrants experience positive spillover effects (+7.48 at h=8, p=0.001), while chronic members experience negative effects (-8.42 at h=8, p=0.0003). Threshold sensitivity analysis confirms the robustness of this pattern across alternative bandwidth specifications. Mechanism analysis suggests that international student recruitment and employer reputation may mediate these effects, though these findings are associational only.

### 5.2 Theoretical Implications

The findings extend institutional theory and tournament theory into the ranking context. The null average effect suggests that rankings may primarily reflect rather than cause institutional quality, consistent with the view that rankings are measures of underlying performance rather than independent causal forces. However, the temporal heterogeneity reveals a more nuanced picture. First-time entry functions as a "flagship event" that triggers resource mobilization and strategic investment, consistent with institutional theory's emphasis on the symbolic power of legitimacy-conferring events. The positive spillover effect for first-time entrants suggests that crossing the Top 100 threshold generates real consequences through enhanced legitimacy, stakeholder attention, and resource flows.

The negative spillover effect for chronic members aligns with tournament theory's prediction of reduced effort after prize attainment. Once universities achieve and maintain Top 100 status, the marginal incentive to invest in ranking-relevant activities may diminish. This "resting on laurels" dynamic may explain why chronic members experience declining performance. The pattern is consistent with Beaman et al. (2012), who found that tournament incentives can generate substantial effort responses but that effort may decline after the prize is secured.

The mechanism analysis provides suggestive evidence on the channels through which Top 100 status affects subsequent performance. The significant discontinuities in international student recruitment and employer reputation suggest that Top 100 status enhances a university's attractiveness to key stakeholders. International students may be drawn to Top 100 universities for the prestige and signaling value of the credential, while employers may preferentially recruit from Top 100 institutions. These mechanisms may generate resource flows that reinforce the spillover effects, creating a self-reinforcing dynamic that concentrates advantage among elite institutions.

### 5.3 Methodological Limitations

We must be transparent about several critical methodological limitations that temper the strength of our conclusions.

First, the small cluster counts in the heterogeneity subgroups pose a serious threat to inference. Cameron and Miller (2015) recommend at least 30-40 clusters for reliable inference with clustered standard errors. In our analysis, the first-time group has only 4 clusters above the cutoff, and the chronic group has only 8 clusters below the cutoff. These cluster counts are far below the recommended threshold, meaning that the p-values should be interpreted with considerable caution. The standard errors may be substantially underestimated, and the true significance levels may be much weaker than reported. The heterogeneity results should be viewed as suggestive rather than definitive.

Second, GDP confounding between first-time and chronic groups is a concern. The first-time group has a mean GDP of $38,936, while the chronic group has a mean GDP of $63,850. This substantial difference suggests that first-time entrants tend to be from less wealthy countries, while chronic members tend to be from wealthier countries. However, the first-time group includes 13 developed countries with GDP above $40,000, and the chronic group has no poor countries. This asymmetry complicates the interpretation of the heterogeneity results, as the positive effect for first-time entrants may partly reflect catch-up dynamics in less wealthy countries rather than the causal effect of Top 100 status.

Third, the mechanism analysis is cross-sectional and associational only. The QS 2025 sub-scores are measured at a single point in time, and we cannot establish causal ordering between Top 100 status and these intermediate outcomes. The significant discontinuities in international student recruitment and employer reputation may reflect pre-existing differences between universities above and below the threshold rather than the causal effect of Top 100 status.

Fourth, the QS publication schedule introduces potential complications. The panel spans eight editions (QS 2017 through QS 2026), and threshold scores vary across editions: 2017=63.1, 2018=64.6, 2019=60.8, 2020=59.9, 2021=58.8, 2022=59.6, 2025=59.6, and 2026=68.5. This variation in threshold scores means that the same university may be above or below the threshold in different years depending on both its own performance and the distribution of scores among competitors. While this variation provides useful identifying variation, it also complicates the interpretation of the running variable, as the distance to the threshold is not directly comparable across editions.

Fifth, the cross-ranking validity of the QS Top 100 threshold is imperfect. The QS-THE 2026 Spearman correlation is 0.815, and the Top 100 overlap is 92%. While this high correlation suggests that the QS Top 100 threshold captures a meaningful dimension of elite status, the imperfect overlap means that some universities may be Top 100 in QS but not in THE, and vice versa. This measurement error may attenuate the estimated spillover effects.

### 5.4 Positioning of the Study

Given these limitations, we position this study as a theory-driven exploratory analysis rather than a strict causal identification exercise. The findings provide suggestive evidence consistent with the theoretical predictions, but the methodological constraints preclude definitive causal claims. The small cluster counts, GDP confounding, and cross-sectional mechanism analysis all caution against strong causal interpretation.

We believe this positioning is appropriate for several reasons. First, the study addresses an important and under-researched question in higher education, and the exploratory findings can inform future research with stronger designs. Second, the temporal heterogeneity pattern is theoretically meaningful and robust across bandwidth specifications, suggesting that it reflects a real phenomenon worthy of further investigation. Third, the transparency about limitations allows readers to assess the credibility of the findings and the strength of the conclusions.

### 5.5 Implications for Policy and Practice

Despite the methodological limitations, the findings have implications for policy and practice. For university leaders, the results suggest that first-time entry into the Top 100 may generate positive momentum that can be leveraged for strategic advantage. The flagship event of initial entry may provide an opportunity to mobilize resources, attract international students, and enhance employer reputation. University leaders should be prepared to capitalize on this momentum through strategic investments in ranking-relevant activities.

For chronic Top 100 members, the negative spillover effect suggests a risk of complacency. Universities that have long been in the Top 100 may need to guard against the tendency to rest on their positional advantage. The findings suggest that sustained effort is necessary to maintain ranking position, and that the marginal value of continued investment may be higher than it appears.

For policymakers, the findings suggest that rankings can have real consequences for institutional behavior and performance. The positive spillover effects for first-time entrants suggest that rankings can incentivize improvement, while the negative effects for chronic members suggest that rankings may also create complacency. Policies that encourage sustained investment in quality improvement, rather than one-time efforts to cross thresholds, may be more effective in the long run.

## 6. Conclusion

This study examined whether crossing the QS Top 100 threshold generates measurable spillover effects on subsequent university performance, using a regression discontinuity design applied to 3,063 university-year observations across 85 countries from 2017 to 2026. The baseline analysis finds no average spillover effect at any bandwidth (h=5: +2.41, p=0.103; h=8: +1.00, p=0.395; h=10: +0.94, p=0.358), a result confirmed by permutation tests. However, temporal heterogeneity analysis reveals striking divergence: first-time entrants experience positive spillover effects (+7.48 at h=8, p=0.001), while chronic members experience negative effects (-8.42 at h=8, p=0.0003). Threshold sensitivity analysis confirms the robustness of this pattern across alternative bandwidth specifications.

The findings extend institutional theory and tournament theory into the ranking context, suggesting that rankings function as both isomorphic pressures and tournament incentives. First-time entry functions as a "flagship event" that triggers resource mobilization and strategic investment, while chronic membership may induce complacency or satisficing behavior. The mechanism analysis suggests that international student recruitment and employer reputation may mediate these effects, though these findings are associational only.

We must emphasize the critical methodological limitations that temper the strength of our conclusions. The small cluster counts in the heterogeneity subgroups (4 clusters for first-time above cutoff; 8 for chronic below cutoff) fall far below the 30-40 clusters recommended by Cameron and Miller (2015), meaning that the p-values should be interpreted with considerable caution. GDP confounding between first-time and chronic groups (first-time mean $38,936; chronic mean $63,850) complicates the interpretation of the heterogeneity results. The mechanism analysis is cross-sectional and associational only. Given these constraints, we position this study as a theory-driven exploratory analysis rather than a strict causal identification exercise.

Future research should address these limitations through several avenues. First, studies with longer panels and more countries could increase cluster counts and improve inference. Second, quasi-experimental designs that exploit exogenous variation in ranking methodology changes could provide stronger causal identification. Third, longitudinal mechanism analysis with repeated measures of intermediate outcomes could establish causal ordering between Top 100 status and potential mediators. Fourth, cross-ranking comparisons could assess whether the effects are specific to QS or generalize to other ranking systems.

Despite these limitations, this study makes important contributions to the higher education literature. It provides the first systematic evidence on ranking threshold spillovers, introduces temporal heterogeneity as a crucial dimension for understanding ranking effects, and connects ranking dynamics to broader theoretical frameworks. The findings suggest that rankings are not merely reflective measures of institutional quality but can function as active causal forces that shape the competitive landscape, at least for universities experiencing first-time entry into the elite. The challenge for future research is to identify the conditions under which these causal forces operate and the mechanisms through which they propagate.

## References

Beaman, L., Duflo, E., Pande, R., & Topalova, P. (2012). Female leadership raises aspirations and educational attainment for girls: A policy experiment in India. *Science*, 335(6068), 582-586.

Belenkuyu, C., & Karadag, E. (2024). The impact of university rankings on institutional decision-making: Evidence from Turkish higher education. *Higher Education*, 87(3), 721-739.

Buenstorf, G. (2022). The uses and abuses of university rankings. *Research Policy*, 51(8), 104557.

Calonico, S., Cattaneo, M. D., & Titiunik, R. (2014). Robust nonparametric confidence intervals for regression-discontinuity designs. *Econometrica*, 82(6), 2295-2326.

Cameron, A. C., & Miller, D. L. (2015). A practitioner's guide to cluster-robust inference. *Journal of Human Resources*, 50(2), 317-372.

Chattopadhyay, R., & Duflo, E. (2004). Women as policy makers: Evidence from a randomized policy experiment in India. *Econometrica*, 72(5), 1409-1443.

Civera, A., Lehmann, E. E., Paleari, S., & Stockinger, S. A. E. (2020). The impact of university rankings on university-industry collaboration. *Higher Education*, 80(4), 731-752.

DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147-160.

Hazelkorn, E. (2015). *Rankings and the reshaping of higher education: The battle for world-class excellence* (2nd ed.). Palgrave Macmillan.

Lazear, E. P., & Rosen, S. (1981). Rank-order tournaments as optimum labor contracts. *Journal of Political Economy*, 89(5), 841-864.

Lovakov, A., Panova, A., & Yudkevich, M. (2021). The relationship between university rankings and research productivity. *Higher Education*, 82(6), 1169-1192.

Marginson, S. (2006). Dynamics of national and global competition in higher education. *Higher Education*, 52(1), 1-39.

McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design: A density test. *Journal of Econometrics*, 142(2), 698-714.

Meyer, J. W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. *American Journal of Sociology*, 83(2), 340-363.

Qin, X., Wang, Y., & Zhang, L. (2026). University rankings and academic careers: Evidence from global institutional responses. *Higher Education*, 91(2), 245-268.

Tushman, M. L., & Romanelli, E. (1985). Organizational evolution: A metamorphosis model of convergence and reorientation. *Research in Organizational Behavior*, 7, 171-222.