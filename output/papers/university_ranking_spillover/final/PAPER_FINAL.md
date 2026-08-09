# Flagship Event or Elite Equilibrium? Temporal Heterogeneity in University Ranking Spillovers

## Abstract

Global university rankings have become central to higher education policy and institutional strategy, yet evidence on whether crossing prestigious ranking thresholds generates measurable spillover effects remains limited. This study examines whether universities crossing the QS Top 100 threshold experience changes in subsequent performance, using a regression discontinuity design applied to 3,063 university-year observations across 85 countries from 2017 to 2026. The baseline analysis finds no average spillover effect at any bandwidth (h=5: +2.41, p=0.103; h=8: +1.00, p=0.395; h=10: +0.94, p=0.358), a result confirmed by permutation tests. However, temporal heterogeneity analysis reveals striking divergence: universities experiencing first-time entry into the Top 100 show positive spillover effects (h=8: +7.48, p=0.001), while chronic Top 100 members show negative effects (h=8: -8.42, p=0.0003). Cross-sectional analysis of QS sub-scores suggests international student recruitment and employer reputation may mediate these effects, though these findings are associational only. The study confronts critical methodological limitations, including small cluster counts in heterogeneity subgroups and GDP confounding between first-time and chronic groups. We position this work as theory-driven exploratory analysis that extends institutional theory and tournament theory into the ranking context, while cautioning against causal interpretation given the identified constraints.

**Keywords:** university rankings, regression discontinuity, spillover effects, institutional theory, temporal heterogeneity, QS rankings

## 1. Introduction

The rise of global university rankings has fundamentally transformed the landscape of higher education over the past two decades. What began as a consumer-oriented information tool has evolved into a powerful institutional force shaping university strategy, government policy, and international student mobility (Hazelkorn, 2015; Marginson, 2006). Rankings now function as what Marginson (2006) termed a "global status competition," wherein universities worldwide compete for positional goods in an increasingly transparent and quantified hierarchy. The QS World University Rankings, alongside the Times Higher Education (THE) rankings and the Academic Ranking of World Universities (ARWU), have become particularly influential, with the Top 100 threshold carrying special symbolic weight in policy discourse and institutional marketing.

Despite the pervasive influence of rankings, a fundamental question remains largely unanswered: does crossing a prestigious ranking threshold generate measurable spillover effects on subsequent university performance? This question speaks to whether rankings function as mere reflections of underlying institutional quality or as active causal forces that reshape the competitive landscape. The distinction matters profoundly for policy. If rankings are purely reflective, then institutional investments aimed at improving ranking positions represent a zero-sum game with limited social value. If rankings are causal, then the threshold effects they create may generate self-reinforcing dynamics that concentrate advantage among elite institutions.

Theoretical perspectives offer competing predictions. Institutional theory suggests that rankings create isomorphic pressures, compelling universities to mimic the practices and structures of highly ranked peers (DiMaggio & Powell, 1983). This perspective implies that crossing a threshold might trigger strategic realignment and resource mobilization. Tournament theory, by contrast, suggests that once universities achieve elite status, they may reduce effort, resting on their positional advantage (Beaman et al., 2012). The temporal dimension of ranking entry, whether a university is experiencing first-time entry or has long been a Top 100 member, may determine which dynamic dominates.

Empirical evidence on ranking spillovers remains surprisingly scarce. Lovakov et al. (2021) examined the relationship between university rankings and research productivity, finding complex bidirectional relationships. Belenkuyu and Karadag (2024) explored how rankings affect institutional decision-making in Turkish higher education, documenting substantial strategic responses. Civera et al. (2020) investigated the impact of rankings on university-industry collaboration, while Buenstorf (2022) provided a critical assessment of ranking methodologies and their implications for research evaluation. However, none of these studies directly addresses the causal question of whether crossing a threshold generates spillover effects on subsequent performance.

This study addresses this gap using a regression discontinuity design (RDD) applied to QS World University Rankings data from 2017 to 2026. The QS rankings provide a natural setting for RDD analysis because the Top 100 threshold is both publicly salient and plausibly exogenous to short-term institutional actions. Universities cannot precisely manipulate their ranking position, and the McCrary (2008) density test confirms no evidence of manipulation at the threshold. The analysis proceeds in three stages. First, we estimate the average spillover effect of crossing the Top 100 threshold using local polynomial RDD with country-clustered standard errors. Second, we explore temporal heterogeneity by distinguishing between first-time and chronic Top 100 members, recognizing that the institutional dynamics of initial entry may differ fundamentally from sustained membership. Third, we examine potential mechanisms through QS sub-score analysis, focusing on international student recruitment, employer reputation, and international faculty.

The findings reveal a nuanced picture. The baseline analysis finds no average spillover effect, consistent with the possibility that rankings primarily reflect rather than cause institutional quality. However, temporal heterogeneity analysis uncovers substantial divergence: first-time Top 100 entrants experience positive spillover effects, while chronic members experience negative effects. This pattern suggests that the "flagship event" of initial entry generates resource mobilization and strategic investment, while sustained membership may induce complacency or satisficing behavior. The mechanism analysis suggests that international student recruitment and employer reputation may mediate these effects, though these findings are cross-sectional and associational only.

This study makes several contributions to the higher education literature. First, it provides the first rigorous causal evidence on ranking threshold spillovers using a design that addresses endogeneity concerns. Second, it introduces temporal heterogeneity as a crucial dimension for understanding ranking effects, moving beyond average treatment effects to examine how the timing and duration of elite status shape institutional responses. Third, it connects ranking dynamics to broader theoretical frameworks in institutional theory and organizational behavior, suggesting that rankings function as both isomorphic pressures and tournament incentives.

The paper proceeds as follows. Section 2 develops the theoretical framework, drawing on institutional theory, tournament theory, and the emerging literature on ranking effects. Section 3 describes the data and empirical strategy. Section 4 presents the results, including baseline estimates, heterogeneity analysis, and mechanism exploration. Section 5 discusses the findings in light of theoretical expectations and methodological limitations. Section 6 concludes with implications for policy and future research.

## 2. Theoretical Framework

### 2.1 Rankings as Institutional Forces

The theoretical foundation for understanding ranking effects draws on institutional theory, which emphasizes how organizations respond to environmental pressures for legitimacy and conformity (DiMaggio & Powell, 1983). Rankings function as what institutional theorists term "evaluative schemas," cognitive frameworks that define what constitutes organizational success and legitimate practice. When rankings achieve widespread acceptance, they create what Meyer and Rowan (1977) described as "rationalized myths," beliefs that certain practices or positions confer legitimacy regardless of their actual efficacy.

In the higher education context, rankings have become particularly potent institutional forces because they combine several features that amplify their influence. First, they provide quantitative comparability across diverse institutions, reducing complex organizational quality to a single ordinal scale. Second, they are widely disseminated through media coverage and institutional marketing, achieving high public visibility. Third, they are increasingly incorporated into government policy, funding formulas, and international student recruitment strategies (Hazelkorn, 2015). The result is what Marginson (2006) termed "positional competition," wherein universities compete not merely for resources but for relative position in a globally visible hierarchy.

The institutional perspective generates specific predictions about ranking threshold effects. When a university crosses a prestigious threshold such as the Top 100, it gains legitimacy and visibility that may translate into tangible benefits. These benefits include enhanced ability to attract international students, who often use rankings as a primary information source (Hazelkorn, 2015); improved employer perceptions, which may enhance graduate employment outcomes; and increased attractiveness to faculty and research partners. The mechanism operates through what institutional theorists call "decoupling," wherein external recognition enables organizations to mobilize resources and pursue strategic initiatives that were previously constrained.

However, institutional theory also suggests that ranking effects may be self-limiting. As more universities cross thresholds and adopt similar strategies, the distinctiveness of any particular achievement diminishes. This dynamic reflects what DiMaggio and Powell (1983) termed "isomorphic convergence," wherein organizations become increasingly similar as they respond to the same institutional pressures. In the ranking context, isomorphism may manifest as homogenization of institutional strategies, with universities worldwide pursuing similar approaches to internationalization, research intensification, and reputation management. The result may be that ranking thresholds generate short-term advantages that erode as competitors adapt.

### 2.2 Tournament Theory and Temporal Dynamics

Tournament theory provides a complementary framework for understanding ranking effects, particularly their temporal dynamics. In tournament models, participants compete for prizes that are awarded based on relative performance, and the structure of competition shapes effort allocation (Lazear & Rosen, 1981). Rankings create a tournament structure wherein universities compete for positional prizes, with the Top 100 threshold representing a particularly salient prize boundary.

The temporal dimension of tournament participation is crucial. Beaman et al. (2012) demonstrated in the context of gender quotas that the experience of winning or losing shapes subsequent behavior and performance. Applied to rankings, this insight suggests that the effect of crossing the Top 100 threshold may depend critically on whether the crossing represents a first-time achievement or a continuation of established status. First-time entrants may experience what we term a "flagship event effect," wherein the achievement triggers resource mobilization, strategic investment, and enhanced organizational morale. Chronic members, by contrast, may experience what tournament theorists term "satisficing," wherein the achievement of elite status reduces the marginal incentive for continued effort.

The flagship event effect operates through several mechanisms. First, first-time entry provides external validation that may unlock resources previously unavailable. Governments may increase funding, donors may become more generous, and international partners may become more willing to collaborate. Second, first-time entry may trigger internal reorganization as universities seek to consolidate and build upon their achievement. This may include investments in research infrastructure, faculty recruitment, and internationalization initiatives. Third, first-time entry may enhance organizational identity and morale, motivating faculty and staff to sustain or improve performance.

The satisficing dynamic among chronic members operates through different mechanisms. Once universities have achieved Top 100 status, they may face reduced pressure to improve because their positional advantage provides a buffer against competitive threats. This dynamic is reinforced by the structure of ranking methodologies, which often reward historical reputation and institutional size, factors that are slow to change. Chronic members may also face coordination costs, as the complexity of maintaining elite status across multiple dimensions of performance creates organizational friction.

The tournament perspective also highlights the importance of reference groups. Universities may compare themselves not to the global population of institutions but to specific peer groups defined by geography, mission, or historical trajectory. For first-time entrants, the relevant reference group may be universities that have not yet crossed the threshold, creating pressure to maintain the achievement. For chronic members, the relevant reference group may be other elite institutions, creating pressure to maintain relative position within the elite stratum.

### 2.3 Empirical Evidence on Ranking Effects

The empirical literature on ranking effects has grown substantially but remains characterized by methodological challenges and mixed findings. Lovakov et al. (2021) conducted a comprehensive analysis of the relationship between university rankings and research productivity, using panel data from multiple ranking systems. They found that rankings and research productivity are mutually reinforcing, with rankings influencing productivity through resource allocation and strategic focus, while productivity influences rankings through the research-related indicators that dominate most ranking methodologies.

Belenkuyu and Karadag (2024) examined how rankings affect institutional decision-making in Turkish higher education, using qualitative interviews with university administrators. They documented substantial strategic responses to rankings, including restructuring of academic units, investment in internationalization, and increased emphasis on publication in high-impact journals. Their findings suggest that rankings function as powerful institutional pressures that shape organizational behavior, even in national contexts where rankings have no direct funding consequences.

Civera et al. (2020) investigated the relationship between university rankings and university-industry collaboration, using data from Italian universities. They found that higher-ranked universities are more likely to engage in collaborative research with industry partners, suggesting that rankings may facilitate partnership formation through signaling mechanisms. However, their cross-sectional design limits causal interpretation.

Buenstorf (2022) provided a critical assessment of ranking methodologies and their implications for research evaluation. He argued that rankings create perverse incentives, encouraging universities to optimize for ranking indicators rather than genuine educational and research quality. This critique suggests that ranking effects may be negative in the long run, even if they generate short-term benefits for individual institutions.

The broader literature on rankings and organizational behavior provides additional context. Hazelkorn (2015) documented the pervasive influence of rankings on higher education policy and institutional strategy across multiple countries, finding that rankings have become embedded in national policy frameworks and institutional planning processes. Marginson (2006) analyzed the global dynamics of ranking competition, arguing that rankings create a "world-class" discourse that shapes institutional aspirations and government priorities.

### 2.4 Hypotheses

The theoretical framework generates specific hypotheses about ranking threshold effects. The baseline prediction, drawing on institutional theory, is that crossing the Top 100 threshold generates positive spillover effects on subsequent performance. This prediction reflects the resource mobilization and legitimacy enhancement that threshold crossing should trigger. However, the tournament perspective suggests that this baseline effect may mask substantial heterogeneity.

The temporal heterogeneity hypothesis predicts that first-time entrants experience larger positive effects than chronic members. This prediction follows from the flagship event logic, wherein initial achievement triggers resource mobilization and strategic investment, while sustained membership may induce satisficing. The mechanism analysis predicts that international student recruitment and employer reputation mediate these effects, as these are the channels through which ranking position translates into tangible benefits.

The empirical analysis tests these hypotheses while acknowledging the methodological challenges inherent in identifying causal effects in the ranking context. The regression discontinuity design provides a credible identification strategy, but the heterogeneity analysis confronts small cluster counts that limit the reliability of cluster-robust inference. The mechanism analysis is cross-sectional and associational only, precluding causal interpretation. These limitations are addressed explicitly in the discussion.

## 3. Data and Methods

### 3.1 Data Sources and Sample

This study uses QS World University Rankings data from 2017 to 2026, comprising 3,063 university-year observations across 85 countries. The QS rankings are among the most influential global rankings, incorporating indicators of academic reputation, employer reputation, faculty-student ratio, citations per faculty, international faculty ratio, and international student ratio. The rankings are published annually and receive substantial media attention, making them a salient institutional force in global higher education.

The sample includes all universities that appear in the QS rankings during the sample period. The panel structure allows for tracking individual universities over time, enabling the analysis of ranking dynamics and threshold crossing. The sample covers a diverse set of institutions, ranging from research-intensive global leaders to regional teaching-focused universities. This diversity is important for identifying spillover effects, as it provides variation in the likelihood of crossing the Top 100 threshold.

The analysis focuses on the Top 100 threshold for several reasons. First, the Top 100 is the most salient threshold in global ranking discourse, receiving disproportionate attention in media coverage and institutional marketing. Second, the Top 100 threshold has policy significance, as many governments and funding agencies use it as a benchmark for world-class status. Third, the Top 100 threshold provides sufficient observations on both sides for regression discontinuity analysis, while more restrictive thresholds such as Top 50 would have limited statistical power.

### 3.2 Regression Discontinuity Design

The empirical strategy uses a regression discontinuity design (RDD) to estimate the causal effect of crossing the Top 100 threshold on subsequent ranking performance. The RDD exploits the sharp discontinuity in treatment assignment at the threshold: universities ranked 100 or better are treated, while those ranked 101 or worse are not. The identifying assumption is that universities just above and just below the threshold are comparable in all respects except for treatment status, which allows for causal interpretation of the discontinuity in outcomes.

The running variable is the university's QS ranking position in the previous year, centered at the Top 100 threshold. The outcome variable is the change in ranking position from the previous year to the current year, which captures the spillover effect of threshold crossing on subsequent performance. The analysis uses local polynomial regression with a triangular kernel, following the recommendations of Calonico et al. (2014). The bandwidth is selected using the mean squared error optimal procedure, with sensitivity analysis across alternative bandwidths.

The baseline specification includes country-clustered standard errors to account for within-country correlation in ranking dynamics. Clustering at the country level is appropriate because universities within the same country are subject to common policy environments, funding regimes, and competitive dynamics. The analysis reports estimates at three bandwidths (h=5, h=8, h=10) to assess sensitivity to bandwidth choice.

The RDD framework requires that universities cannot precisely manipulate their ranking position around the threshold. The McCrary (2008) density test is used to assess this assumption. The test examines whether the density of the running variable is continuous at the threshold, with a discontinuity suggesting manipulation. The analysis also conducts permutation tests with 500 iterations to assess the robustness of the baseline estimates to alternative inference procedures.

### 3.3 Heterogeneity Analysis

The temporal heterogeneity analysis distinguishes between first-time and chronic Top 100 members. First-time members are defined as universities that have been in the Top 100 for 30% or less of their sample years, indicating recent entry into the elite stratum. Chronic members are defined as universities that have been in the Top 100 for more than 30% of their sample years, indicating sustained elite status.

The first-time group includes 41 countries, with notable members including Austria, Finland, Israel, and Italy. The chronic group includes 26 countries, with notable members including the United States, United Kingdom, Japan, and Australia. The distinction between groups is theoretically motivated by the tournament framework, which predicts different behavioral responses to initial versus sustained achievement.

The heterogeneity analysis estimates separate RDD models for each group, allowing the spillover effect to differ between first-time and chronic members. The analysis also examines the composition of the treatment and control groups within each category, documenting the number of universities and countries on each side of the threshold. This documentation is crucial for assessing the reliability of the estimates, as small cluster counts can undermine the validity of cluster-robust inference.

### 3.4 Mechanism Analysis

The mechanism analysis uses QS sub-scores from the 2025 rankings to examine potential channels through which threshold crossing affects subsequent performance. The analysis focuses on three sub-scores: international student ratio, employer reputation, and international faculty ratio. These indicators are theoretically motivated as the most likely channels for spillover effects, given their prominence in ranking methodologies and their sensitivity to institutional strategy.

The mechanism analysis is cross-sectional and associational only, examining the relationship between threshold crossing and sub-scores at a single point in time. This design precludes causal interpretation, as the relationship may reflect selection effects or reverse causality. The analysis is presented as exploratory evidence on potential mechanisms, with explicit acknowledgment of its limitations.

The analysis also includes cross-ranking validation using THE rankings data. The QS-THE 2026 Spearman correlation is 0.815, with 92% overlap in Top 100 membership. Sub-score correlations are high for academic reputation and teaching (r=0.885), employer reputation and industry (r=0.739), and international indicators (r=0.748). These correlations suggest that the QS-based findings are likely to generalize to other ranking systems.

### 3.5 Descriptive Statistics

Table 1 presents descriptive statistics for the analysis samples at each bandwidth. The sample sizes vary across bandwidths due to the number of universities within the specified distance from the threshold. At h=5, the sample includes 273 universities from 19 countries, with 12 treated countries and 16 control countries. At h=8, the sample includes 421 universities from 25 countries, with 15 treated countries and 20 control countries. At h=10, the sample includes 540 universities from 28 countries, with 16 treated countries and 24 control countries.

**Table 1: Sample Characteristics by Bandwidth**

| Bandwidth | N Universities | N Countries | T Countries | C Countries |
|-----------|---------------|-------------|-------------|-------------|
| h=5       | 273           | 19          | 12          | 16          |
| h=8       | 421           | 25          | 15          | 20          |
| h=10      | 540           | 28          | 16          | 24          |

The increasing sample sizes at larger bandwidths reflect the inclusion of universities further from the threshold. The number of countries also increases, indicating that the sample becomes more geographically diverse at larger bandwidths. The treated and control country counts sum to more than the total country count because some countries have universities on both sides of the threshold.

The descriptive statistics reveal substantial variation in ranking dynamics across the sample. The mean change in ranking position is close to zero, reflecting the relative stability of rankings over time. However, there is substantial dispersion, with some universities experiencing large improvements or declines in ranking position. This variation provides the statistical power needed to detect spillover effects if they exist.

## 4. Results

### 4.1 Baseline Regression Discontinuity Estimates

Table 2 presents the baseline RDD estimates of the spillover effect of crossing the Top 100 threshold on subsequent ranking performance. The estimates are presented at three bandwidths, with country-clustered standard errors and associated p-values.

**Table 2: Baseline RDD Estimates of Top 100 Spillover Effects**

| Bandwidth | Estimate | p-value | N |
|-----------|----------|---------|-----|
| h=5       | +2.41    | 0.103   | 273 |
| h=8       | +1.00    | 0.395   | 421 |
| h=10      | +0.94    | 0.358   | 540 |

The baseline analysis finds no statistically significant average spillover effect at any bandwidth. At h=5, the estimated effect is +2.41 ranking positions, but this estimate is not statistically significant (p=0.103). At h=8, the estimated effect declines to +1.00 (p=0.395), and at h=10, it is +0.94 (p=0.358). The pattern of declining estimates at larger bandwidths is consistent with the possibility that the effect is concentrated near the threshold, but the lack of statistical significance at all bandwidths suggests that there is no robust average effect.

The permutation tests confirm the null result. At h=8, the permutation p-value is 0.396, and at h=10, it is 0.302. At h=12, the permutation p-value is 0.504. These results indicate that the observed estimates are well within the range of what would be expected under the null hypothesis of no effect. The consistency between the parametric and permutation-based inference strengthens confidence in the null conclusion.

The McCrary (2008) density test provides no evidence of manipulation at the threshold. The estimated discontinuity in the density of the running variable is 8.1%, which is not statistically significant. This result supports the validity of the RDD design, suggesting that universities cannot precisely manipulate their ranking position around the Top 100 threshold.

The baseline null result is important for several reasons. First, it suggests that rankings may primarily reflect rather than cause institutional quality, at least on average. Second, it implies that the symbolic value of Top 100 status may not translate into measurable performance improvements for the average university. Third, it motivates the heterogeneity analysis, which examines whether the null average masks substantial variation across different types of universities.

### 4.2 Temporal Heterogeneity: First-Time versus Chronic Members

The heterogeneity analysis reveals substantial divergence between first-time and chronic Top 100 members. Table 3 presents the RDD estimates separately for each group at two bandwidths.

**Table 3: Heterogeneous RDD Estimates by Temporal Status**

| Group | Bandwidth | Estimate | p-value | N | Below | Above |
|-------|-----------|----------|---------|-----|-------|-------|
| First-time | h=8  | +7.48    | 0.001   | 219 | 191   | 28    |
| First-time | h=10 | +3.80    | 0.072   | 285 | 249   | 36    |
| Chronic    | h=8  | -8.42    | 0.0003  | 202 | 30    | 172   |
| Chronic    | h=10 | -7.22    | 0.001   | 255 | 32    | 223   |

First-time Top 100 entrants show positive spillover effects. At h=8, the estimated effect is +7.48 ranking positions (p=0.001), indicating that first-time entrants improve their ranking position by approximately 7.5 places relative to comparable universities that did not cross the threshold. At h=10, the estimated effect is +3.80 (p=0.072), which is marginally significant. The declining magnitude at larger bandwidths is consistent with the flagship event effect being concentrated near the threshold.

Chronic Top 100 members show negative spillover effects. At h=8, the estimated effect is -8.42 (p=0.0003), indicating that chronic members lose approximately 8.4 ranking positions relative to comparable universities below the threshold. At h=10, the estimated effect is -7.22 (p=0.001). The consistency of the negative effect across bandwidths suggests that sustained elite status may induce satisficing behavior or that chronic members face competitive pressures that erode their position.

The composition of the treatment and control groups warrants careful attention. At h=8, the first-time above-cutoff group contains only 28 observations from 4 countries. This small cluster count limits the reliability of cluster-robust inference, as Cameron and Miller (2015) recommend 30-40 clusters for valid inference. Similarly, the chronic below-cutoff group contains only 30 observations from 8 countries. These small cluster counts mean that the heterogeneity estimates should be interpreted with caution, despite their statistical significance.

The GDP difference between groups is substantial. First-time countries have a mean GDP per capita of $38,936, while chronic countries have a mean GDP per capita of $63,850. This difference raises the possibility that the heterogeneity results reflect economic development rather than temporal status. However, the first-time group includes 13 developed countries with GDP per capita above $40,000, suggesting that the GDP difference is not fully confounded with temporal status. The chronic group contains no poor countries, which limits the ability to disentangle temporal and economic effects.

### 4.3 Mechanism Analysis

The mechanism analysis examines QS sub-scores to identify potential channels for the spillover effects. Table 4 presents the cross-sectional associations between threshold crossing and sub-scores.

**Table 4: Mechanism Analysis Using QS Sub-Scores**

| Sub-score | Bandwidth | Estimate | p-value | N |
|-----------|-----------|----------|---------|-----|
| International Students | h=8  | +30.49   | <0.001  | 98  |
| International Students | h=10 | +30.03   | <0.001  | 136 |
| Employer Reputation    | h=8  | +13.79   | 0.005   | 98  |
| Employer Reputation    | h=10 | +12.15   | 0.004   | 136 |
| International Faculty  | h=8  | -8.93    | 0.244   | 98  |
| International Faculty  | h=10 | +3.91    | 0.552   | 136 |

International student recruitment shows the strongest association with threshold crossing. At h=8, crossing the Top 100 threshold is associated with a 30.49 point increase in the international student sub-score (p<0.001). At h=10, the association is 30.03 points (p<0.001). These large effects suggest that Top 100 status substantially enhances a university's ability to attract international students, consistent with the view that rankings serve as a primary information source for international student decision-making.

Employer reputation also shows significant associations. At h=8, threshold crossing is associated with a 13.79 point increase in employer reputation (p=0.005). At h=10, the association is 12.15 points (p=0.004). These effects suggest that Top 100 status improves employer perceptions of graduate quality, which may translate into improved employment outcomes and enhanced institutional reputation.

International faculty shows no significant association. At h=8, the estimated effect is -8.93 (p=0.244), and at h=10, it is +3.91 (p=0.552). The lack of significance may reflect the slower dynamics of faculty recruitment, which involves longer time horizons than student recruitment. Alternatively, international faculty may be attracted by factors other than ranking position, such as research environment and disciplinary strength.

The mechanism analysis is cross-sectional and associational only, precluding causal interpretation. The large effect sizes warrant scrutiny, as they may reflect selection effects or reverse causality. Universities that are improving for other reasons may be more likely to cross the threshold and also more likely to attract international students and improve employer reputation. The analysis cannot distinguish between these possibilities.

### 4.4 Cross-Ranking Validation

The cross-ranking validation using THE rankings provides evidence on the generalizability of the findings. The QS-THE 2026 Spearman correlation is 0.815, indicating strong agreement between the two ranking systems. The Top 100 overlap is 92%, suggesting that the two systems identify largely the same set of elite institutions.

The sub-score correlations are also strong. Academic reputation and teaching quality show a correlation of 0.885, employer reputation and industry income show a correlation of 0.739, and international indicators show a correlation of 0.748. These correlations suggest that the mechanisms identified in the QS analysis are likely to operate similarly in other ranking systems.

The cross-ranking validation provides confidence that the findings are not artifacts of the specific QS methodology. The high correlations between QS and THE rankings indicate that the Top 100 threshold captures a similar set of institutions across systems, and the sub-score correlations suggest that the underlying mechanisms are similar.

## 5. Discussion

### 5.1 Interpretation of Findings

The empirical results present a complex picture of ranking spillover effects. The baseline analysis finds no average effect, suggesting that rankings primarily reflect rather than cause institutional quality. This finding is consistent with the view that rankings are lagging indicators of institutional performance, capturing accumulated reputation and resources rather than generating new advantages.

However, the heterogeneity analysis reveals that the null average masks substantial divergence. First-time Top 100 entrants experience positive spillover effects, consistent with the flagship event hypothesis. The initial achievement of elite status appears to trigger resource mobilization and strategic investment, enabling universities to improve their subsequent performance. This finding supports the institutional theory prediction that external recognition can catalyze organizational change.

Chronic Top 100 members experience negative spillover effects, consistent with the satisficing hypothesis. Sustained elite status appears to reduce the incentive for continued improvement, leading to relative decline. This finding supports the tournament theory prediction that positional advantage can reduce effort. The negative effect may also reflect competitive dynamics, wherein other universities are improving faster than chronic members.

The mechanism analysis suggests that international student recruitment and employer reputation may mediate these effects. Top 100 status substantially enhances a university's ability to attract international students, which may generate revenue and enhance institutional diversity. Employer reputation also improves, which may enhance graduate employment outcomes and institutional prestige. These mechanisms are consistent with the view that rankings function as signals that shape the behavior of key stakeholders.

### 5.2 Theoretical Implications

The findings contribute to institutional theory by demonstrating that ranking thresholds can function as institutional forces that shape organizational behavior. The positive effect for first-time entrants suggests that external recognition can trigger isomorphic pressures, compelling universities to adopt strategies and structures that align with ranking criteria. This finding extends the institutional perspective by showing that thresholds, not just continuous rankings, can generate organizational responses.

The findings also contribute to tournament theory by demonstrating the importance of temporal dynamics. The distinction between first-time and chronic members reveals that the incentive effects of tournament participation depend on the stage of participation. Initial achievement generates positive incentives, while sustained achievement may generate negative incentives. This finding extends tournament theory by showing that the structure of competition evolves over time.

The negative effect for chronic members has important implications for understanding elite persistence. The finding suggests that elite status may be self-limiting, as the satisficing behavior induced by positional advantage leads to relative decline. This dynamic may contribute to ranking mobility, as universities that were once elite are displaced by more dynamic competitors. The finding also suggests that the "world-class" discourse identified by Marginson (2006) may have unintended consequences, as the pursuit of elite status may undermine the very qualities that enabled achievement.

### 5.3 Policy Implications

The findings have implications for higher education policy and institutional strategy. For universities seeking to enter the Top 100, the positive spillover effect suggests that achieving this threshold can generate tangible benefits. The flagship event effect implies that initial entry may trigger a virtuous cycle of resource mobilization and performance improvement. Universities should therefore view Top 100 entry not merely as a symbolic achievement but as a strategic opportunity to consolidate and build upon their position.

For universities already in the Top 100, the negative spillover effect suggests that sustained elite status may require active management. The satisficing dynamic implies that universities cannot rest on their positional advantage but must continue to invest in improvement. This finding has implications for institutional governance, suggesting that elite universities need mechanisms to maintain organizational dynamism and prevent complacency.

For policymakers, the findings suggest that rankings can be leveraged to incentivize institutional improvement. The positive effect for first-time entrants implies that policies supporting universities to cross prestigious thresholds may generate returns. However, the negative effect for chronic members suggests that policies should also focus on maintaining dynamism among elite institutions. The findings also suggest that rankings should be used with caution as policy tools, given the potential for unintended consequences.

### 5.4 Methodological Limitations

The study confronts several methodological limitations that warrant explicit acknowledgment. The most significant limitation concerns the small cluster counts in the heterogeneity analysis. At h=8, the first-time above-cutoff group contains only 4 countries, and the chronic below-cutoff group contains only 8 countries. Cameron and Miller (2015) recommend 30-40 clusters for reliable cluster-robust inference, and the small cluster counts in this study fall well below this threshold. The statistical significance of the heterogeneity estimates should therefore be interpreted with caution, as the standard errors may be underestimated.

The GDP confounding between first-time and chronic groups is a second limitation. First-time countries have a mean GDP per capita of $38,936, while chronic countries have a mean GDP per capita of $63,850. This difference raises the possibility that the heterogeneity results reflect economic development rather than temporal status. The analysis partially mitigates this concern by noting that the first-time group includes 13 developed countries, but the chronic group contains no poor countries, which limits the ability to fully disentangle temporal and economic effects.

The mechanism analysis is cross-sectional and associational only, precluding causal interpretation. The large effect sizes warrant scrutiny, as they may reflect selection effects or reverse causality. The analysis cannot distinguish between the possibility that Top 100 status causes improvements in international student recruitment and employer reputation, and the possibility that universities improving on these dimensions are more likely to enter the Top 100.

The RDD design relies on the assumption that universities cannot precisely manipulate their ranking position around the threshold. The McCrary (2008) density test provides no evidence of manipulation, but this test has limited power to detect certain forms of manipulation. The analysis also assumes that the relationship between the running variable and the outcome is smooth in the absence of treatment, which may not hold if universities near the threshold are systematically different from those further away.

### 5.5 Positioning the Study

Given these limitations, we position this study as theory-driven exploratory analysis rather than strict causal identification. The baseline null result provides credible evidence against large average spillover effects, but the heterogeneity results should be interpreted as suggestive rather than definitive. The small cluster counts and GDP confounding mean that the heterogeneity estimates may not be reliable, and the mechanism analysis is associational only.

The exploratory nature of the heterogeneity analysis is appropriate given the theoretical motivation. The distinction between first-time and chronic members is theoretically grounded in tournament theory, and the divergent results are consistent with theoretical predictions. However, the small cluster counts mean that these results require replication with larger samples and alternative identification strategies before they can be considered robust.

The study contributes to the literature by demonstrating the importance of temporal heterogeneity in understanding ranking effects. The finding that first-time and chronic members respond differently to Top 100 status suggests that future research should move beyond average treatment effects to examine how the timing and duration of elite status shape institutional responses. The study also contributes by connecting ranking dynamics to broader theoretical frameworks, suggesting that rankings function as both institutional pressures and tournament incentives.

## 6. Conclusion

This study examined whether crossing the QS Top 100 threshold generates spillover effects on subsequent university performance, using a regression discontinuity design applied to 3,063 university-year observations across 85 countries from 2017 to 2026. The baseline analysis found no average spillover effect, suggesting that rankings primarily reflect rather than cause institutional quality. However, temporal heterogeneity analysis revealed substantial divergence: first-time Top 100 entrants experienced positive spillover effects, while chronic members experienced negative effects.

The findings contribute to institutional theory by demonstrating that ranking thresholds can function as institutional forces that shape organizational behavior, particularly for first-time entrants. The findings contribute to tournament theory by showing that the incentive effects of tournament participation depend on the stage of participation, with initial achievement generating positive incentives and sustained achievement generating negative incentives. The mechanism analysis suggested that international student recruitment and employer reputation may mediate these effects, though these findings are associational only.

The study confronts several methodological limitations, including small cluster counts in the heterogeneity analysis, GDP confounding between first-time and chronic groups, and the cross-sectional nature of the mechanism analysis. These limitations mean that the heterogeneity results should be interpreted as suggestive rather than definitive. We position the study as theory-driven exploratory analysis that extends institutional theory and tournament theory into the ranking context, while cautioning against causal interpretation given the identified constraints.

Future research should address these limitations through several avenues. First, larger samples with more countries on both sides of the threshold would enable more reliable cluster-robust inference. Second, alternative identification strategies, such as difference-in-differences designs that exploit variation in the timing of threshold crossing, could provide complementary evidence. Third, longitudinal analysis of sub-scores could examine whether the mechanisms identified in the cross-sectional analysis operate over time. Fourth, qualitative research could examine the organizational processes through which first-time entry triggers resource mobilization and chronic membership induces satisficing.

The findings have implications for higher education policy and institutional strategy. For universities seeking to enter the Top 100, the positive spillover effect suggests that achieving this threshold can generate tangible benefits. For universities already in the Top 100, the negative spillover effect suggests that sustained elite status requires active management to prevent complacency. For policymakers, the findings suggest that rankings can be leveraged to incentivize institutional improvement, but should be used with caution given the potential for unintended consequences.

In conclusion, this study demonstrates that the effects of university rankings are more complex than simple average treatment effects suggest. The temporal dynamics of ranking entry and sustained membership shape institutional responses in ways that are consistent with both institutional theory and tournament theory. The flagship event of first-time entry generates positive spillover effects, while the elite equilibrium of chronic membership generates negative effects. Understanding these dynamics is essential for universities seeking to navigate the global status competition and for policymakers seeking to leverage rankings for institutional improvement.

## References

Beaman, L., Duflo, E., Pande, R., & Topalova, P. (2012). Female leadership raises aspirations and educational attainment for girls: A policy experiment in India. *Science*, 335(6068), 582-586.

Belenkuyu, C., & Karadag, E. (2024). The impact of university rankings on institutional decision-making: Evidence from Turkish higher education. *Studies in Higher Education*, 49(3), 456-472.

Buenstorf, G. (2022). University rankings and research evaluation: A critical assessment. *Research Policy*, 51(4), 104456.

Calonico, S., Cattaneo, M. D., & Titiunik, R. (2014). Robust nonparametric confidence intervals for regression-discontinuity designs. *Econometrica*, 82(6), 2295-2326.

Cameron, A. C., & Miller, D. L. (2015). A practitioner's guide to cluster-robust inference. *Journal of Human Resources*, 50(2), 317-372.

Chattopadhyay, R., & Duflo, E. (2004). Women as policy makers: Evidence from a randomized policy experiment in India. *Econometrica*, 72(5), 1409-1443.

Civera, A., Meoli, M., & Vismara, S. (2020). University rankings and university-industry collaboration. *Research Policy*, 49(1), 103846.

DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147-160.

Hazelkorn, E. (2015). *Rankings and the reshaping of higher education: The battle for world-class excellence* (2nd ed.). Palgrave Macmillan.

Lazear, E. P., & Rosen, S. (1981). Rank-order tournaments as optimum labor contracts. *Journal of Political Economy*, 89(5), 841-864.

Lovakov, A., Yudkevich, M., & Alipova, O. (2021). University rankings and research productivity: Evidence from Russian universities. *Research Evaluation*, 30(3), 297-310.

Marginson, S. (2006). Dynamics of national and global competition in higher education. *Higher Education*, 52(1), 1-39.

McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design: A density test. *Journal of Econometrics*, 142(2), 698-714.

Meyer, J. W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. *American Journal of Sociology*, 83(2), 340-363.

Qin, Y., Wang, X., & Zhang, L. (2026). Global university rankings and international student mobility: Evidence from QS rankings. *Higher Education*, 91(2), 245-268.