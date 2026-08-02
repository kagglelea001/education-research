

# Beyond the Flagship: Spillover Effects of Global University Rankings on National Higher Education Systems — A Regression Discontinuity Design

**Author 1**  
[Affiliation 1]  
[Email 1]  
[ORCID 1]

**Author 2**  
[Affiliation 2 – Chinese University]  
[Email 2]  
[ORCID 2]

**Author 3**  
[Affiliation 3 – Chinese University]  
[Email 3]  
[ORCID 3]

---

**Corresponding Author:** Author 1, [Affiliation 1], [Email 1]

**Acknowledgements:** The authors declare no conflicts of interest. This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Data Availability:** Replication materials and code will be made available upon publication.

---

*Manuscript prepared for submission to Studies in Higher Education*



**Background:** Global university rankings increasingly shape institutional strategy and national policy, yet whether the success of a top-ranked university generates spillover effects—positive or negative—on its domestic peers remains causally unidentified. Prior work documents isomorphic pressures (DiMaggio & Powell, 1983; Marginson, 2006) but cannot separate correlation from causation.

**Methods:** We exploit the discrete Top 100 cutoff in the QS World University Rankings (2017–2026) as a sharp regression discontinuity (RDD), comparing country-years where a domestic university marginally enters versus misses the threshold. Using 3,063 university-year observations across 85 countries and 307 country-year RDD observations, we estimate local polynomial models across five bandwidths (Calonico et al., 2014). McCrary (2008) tests confirm no manipulation (8.1%). Balance is achieved (152 treated vs. 155 control country-years). Panel DID-RDD robustness checks supplement the cross-sectional design.

**Results:** Ranking spillovers are Janus-faced. Market-facing outcomes improve significantly: international student scores rise +37.0 to +38.9 points (p<0.001, all bandwidths); faculty/student ratios gain +32.5 to +41.5 (p<0.001, all); employer reputation +8.8 to +12.3 (p<0.05, 4/5); employment outcomes +10.6 to +16.1 (p<0.01, 2/5). Conversely, research concentration emerges: citations diverge (+12.9 at h=5, p<0.05; −29 to −39 at wider bandwidths, p<0.001); sustainability (−21 to −25, p<0.01) and international research network (−10 to −17, p<0.06–p<0.001) decline. Of 45 estimates, 24 are significant (53%): 17 positive, 7 negative.

**Conclusions:** Top-100 entry triggers market-based prestige spillovers but simultaneously concentrates research resources, suggesting rankings produce stratified rather than uniformly elevating national systems.



## 1. Introduction

The global competition for world-class university (WCU) status has become one of the defining features of contemporary higher education policy. Over the past two decades, governments across more than 85 countries have committed well over $100 billion in cumulative public investment toward the explicit goal of elevating select institutions into the upper echelons of global university rankings (Hazelkorn, 2015; Marginson, 2006). Flagship initiatives—from China’s Double First-Class scheme and Germany’s Excellence Strategy to South Korea’s Brain Korea 21 and France’s Initiatives d’Excellence—share a common underlying logic: that concentrating resources in a small number of elite universities will generate benefits that diffuse to the broader national higher education system. Yet remarkably, despite this unprecedented scale of investment, there exists no causal evidence on whether the elevation of some institutions produces measurable spillover effects—positive or negative—on their peer institutions. This paper provides the first causal estimates of ranking-induced spillovers on non-ranked peer universities, using a regression discontinuity design (RDD) around the QS World University Rankings Top 100 threshold.

The theoretical motivation for this study extends a growing body of causal evidence on peer effects in educational settings. In a landmark field experiment, Beaman et al. (2012) demonstrated that the presence of female leaders in Indian villages changed aspirations and outcomes for adolescent girls, illustrating how role models can generate substantial spillover effects beyond their direct targets. More recently, Qin et al. (2026) provided causal evidence from Chinese classrooms that the assignment of high-ability peers to elite tracks generates positive spillovers on non-treated students through aspiration and information channels. These findings establish that in educational contexts, the treatment of a select group can meaningfully alter the behavior and outcomes of untreated peers. We extend this logic from the classroom to the institutional level: when a university crosses a salient global ranking threshold, does this event generate spillover effects on peer institutions in the same country? The mechanisms may operate through multiple channels—competitive emulation, resource reallocation, reputational externalities, and shifts in student and faculty mobility patterns—but the fundamental question is whether the WCU investment strategy generates system-level benefits or merely redistributes advantage.

The existing literature on university rankings has largely focused on the ranked institutions themselves. A substantial body of work has examined how rankings affect the behavior, resources, and reputations of the universities that appear in them (Hazelkorn, 2015; Marginson, 2006). Scholars have documented that rankings shape institutional strategy, influence student choice, and create isomorphic pressures toward conformity with ranking criteria (DiMaggio & Powell, 1983). However, this literature suffers from two critical limitations. First, it is overwhelmingly descriptive and correlational, lacking credible identification strategies to distinguish causal effects from selection and confounding. Second, and more importantly for our purposes, it has almost entirely ignored the question of spillover effects on non-ranked institutions. If rankings function as a positional good—where the value of being ranked depends on the distribution of rankings across institutions—then the treatment of universities near the threshold may have important consequences for those below it. The theoretical possibility of both positive spillovers (through demonstration effects, talent pool expansion, and reputational lift for the national system) and negative spillovers (through resource diversion, faculty poaching, and student concentration) remains entirely unexplored in the causal literature.

This paper addresses these gaps by exploiting a sharp discontinuity in the QS World University Rankings. The QS rankings, published annually since 2004, are among the most influential global university rankings, and the Top 100 threshold carries particular salience for policymakers, students, and institutional leaders. Crossing this threshold confers substantial reputational benefits and is frequently cited as a policy target in national WCU strategies. Using a cross-sectional RDD with panel robustness checks, we compare outcomes for universities in countries where a peer institution crossed the Top 100 threshold against those in countries where no such crossing occurred. Our primary dataset spans QS rankings from 2017 to 2026, encompassing 3,063 university-year observations across 85 countries, with 307 country-year observations at the RDD threshold. The cross-sectional design yields 152 treated country-years versus 155 control country-years, providing substantial statistical power. We supplement this with a cross-year analysis of the QS 2025 rankings, which identifies 54 countries with 25 treated and 29 control observations, and traces spillover effects on 532 non-ranked universities.

Our empirical strategy follows the robust RDD framework developed by Calonico et al. (2014), with manipulation testing following McCrary (2008). The McCrary test confirms no evidence of manipulation near the Top 100 threshold (8.1%, p>0.10), supporting the validity of the design. We examine nine outcome dimensions for peer universities: international student enrollment, employer reputation, faculty-student ratio, employment outcomes, research citations, sustainability performance, international research network, and overall QS scores. Across 45 total estimates (9 outcomes × 5 bandwidths), we find 24 statistically significant effects (53%), with 17 positive and 7 negative. The pattern of results reveals a Janus-faced spillover structure. On the positive side, we find large and robust increases in international student enrollment (+37.0 to +38.9 points, p<0.001 across all bandwidths), faculty-student ratios (+32.5 to +41.5 points, p<0.001 across all bandwidths), and employer reputation (+8.8 to +12.3 points, p<0.05 in 4 of 5 bandwidths). Employment outcomes also improve (+10.6 to +16.1 points), though with weaker statistical significance. On the negative side, we find significant declines in research citations at wider bandwidths (−29 to −39 points, p<0.001), sustainability performance (−21 to −25 points at narrow bandwidths, p<0.01), and international research network (−10 to −17 points, p<0.06 to p<0.001). These divergent effects suggest that the spillover mechanism operates through multiple, partially offsetting channels: while peer institutions benefit from enhanced international visibility and resource competition, they may suffer from resource diversion in research-intensive domains.

This paper makes three principal contributions. First, we provide the first causal evidence on ranking-induced spillover effects on peer institutions, extending the RDD approach from classroom settings (Qin et al., 2026) to the institutional level. Our findings demonstrate that the treatment of universities near salient ranking thresholds generates substantial and heterogeneous effects on non-ranked peers, with implications for the design of national higher education policies. Second, we uncover a Janus-faced mechanism structure: the same treatment that elevates some institutions generates both positive and negative spillovers on others, depending on the outcome dimension. This heterogeneity has important theoretical implications for understanding how positional competition operates in higher education systems. Third, our findings inform ongoing policy debates about the efficacy of WCU investment strategies. The large positive spillovers on international student recruitment and faculty-student ratios suggest that WCU policies may generate system-level benefits, while the negative effects on research citations and international research networks caution against assuming uniform positive externalities.

The remainder of the paper proceeds as follows. Section 2 reviews the relevant literature on rankings, peer effects, and higher education policy. Section 3 describes our data sources, variable construction, and empirical strategy. Section 4 presents the main results, including validity checks, baseline estimates, and heterogeneity analyses. Section 5 provides robustness checks and addresses potential threats to identification. Section 6 discusses the mechanisms underlying our findings and their policy implications. Section 7 concludes.



# Theoretical Framework

## Institutional Isomorphism and Ranking-Driven Convergence

The global proliferation of university ranking systems has fundamentally altered the competitive landscape of higher education. DiMaggio and Powell's (1983) seminal theory of institutional isomorphism provides a powerful lens for understanding how organizations respond to environmental uncertainty and external evaluation. Rankings, as highly visible and consequential evaluative instruments, generate precisely the conditions that precipitate mimetic isomorphism: organizations face ambiguous production functions, uncertain quality signals, and pressure to conform to externally validated models of excellence. When a peer institution crosses a salient status threshold—such as entering the global Top 100—it becomes a template for legitimate organizational form and strategy. This isomorphic pressure operates through three channels: coercive (government funding tied to ranking performance), mimetic (modeling successful peers under uncertainty), and normative (professional networks disseminating "best practices" associated with high-ranked institutions).

The higher education literature has extensively documented the pervasive influence of rankings on institutional behavior. Hazelkorn (2015) demonstrates that rankings shape strategic priorities, resource allocation, and even faculty hiring decisions across diverse national contexts. Marginson (2006) argues that rankings have created a global status hierarchy that transcends national systems, positioning universities within a competitive field where positional goods—prestige, selectivity, and reputation—are paramount. Within this framework, the entry of a peer institution into the Top 100 represents a discrete, observable event that recalibrates the competitive environment for all institutions in the same country. The mechanism is twofold: first, the ranked institution's success signals that the national system can produce world-class universities, potentially legitimizing the entire sector; second, the same event intensifies competitive pressure on peer institutions to emulate the successful model.

## Status Competition and Positional Dynamics

Marginson's (2006) analysis of status competition in global higher education emphasizes that universities operate within a zero-sum positional market where relative standing matters more than absolute quality. This perspective generates distinctive predictions about spillover effects. When a domestic peer enters the Top 100, the competitive equilibrium shifts: the successful institution captures a larger share of positional goods (elite students, star faculty, research funding, international partnerships), potentially at the expense of proximate competitors. This concentration dynamic is particularly acute for research-intensive outcomes, where resources are finite and prestige is inherently relative. The mechanism parallels status competition dynamics documented in other contexts: Beaman et al. (2012) show that exposure to successful role models can have heterogeneous effects depending on the domain and the observer's position in the status hierarchy.

The status competition framework suggests that spillover effects are not uniformly positive or negative but rather domain-dependent. Market-facing outcomes—international student recruitment, employer reputation, employment outcomes—may benefit from positive brand spillover as the national system's global visibility increases. However, research-intensive outcomes—citations, faculty productivity, research infrastructure—may suffer from concentration effects as the Top 100 institution attracts disproportionate resources and talent. This tension between brand spillover and resource concentration constitutes the theoretical core of our investigation.

## Role Model Effects and Behavioral Transmission

Qin et al. (2026) provide causal evidence that role model effects operate through four distinct mechanisms: aspiration (raising perceived feasibility of success), information (revealing effective strategies), demonstration (providing observable templates for action), and competition (intensifying rivalry through comparison). These mechanisms map directly onto our theoretical framework for ranking spillovers. Table 1 presents this mapping.

**Table 1: Mechanism Mapping Between Role Model Effects and Ranking Spillovers**

| Qin et al. (2026) Mechanism | Ranking Spillover Mechanism | Predicted Outcome Domain |
|---------------------------|---------------------------|-------------------------|
| Aspiration | Legitimacy signaling: Top 100 entry raises perceived ceiling for national peers | Market-facing outcomes (international students, employer reputation) |
| Information | Strategic disclosure: successful institution's practices become observable templates | Administrative and operational outcomes (faculty/student ratio) |
| Demonstration | Benchmarking: peer institutions adopt visible strategies of the ranked university | Employment outcomes, international recruitment |
| Competition | Resource concentration: Top 100 institution captures disproportionate positional goods | Research-intensive outcomes (citations, research network) |

This mapping reveals that the four mechanisms are not uniformly directional. Aspiration, information, and demonstration mechanisms generate positive spillovers by raising aspirations, transmitting knowledge, and providing templates. Competition mechanisms, however, generate negative spillovers through resource concentration and intensified rivalry for finite positional goods. The net effect for any given outcome depends on the relative strength of these opposing forces, which in turn depends on the outcome's position in the market-facing versus research-intensive spectrum.

## Hypotheses

Synthesizing these theoretical perspectives, we derive three testable hypotheses:

**H1 (Positive Brand Spillover):** A domestic peer's entry into the global Top 100 generates positive spillover effects on market-facing outcomes of non-ranked universities, including international student enrollment, employer reputation, and employment outcomes. This hypothesis follows from the aspiration and legitimacy mechanisms: the peer's success signals national system quality, raises global visibility, and enhances the positional value of all domestic degrees.

**H2 (Negative Concentration Effect):** The same Top 100 entry generates negative spillover effects on research-intensive outcomes, including citation performance and international research network strength. This hypothesis follows from the competition mechanism: the successful institution attracts disproportionate research funding, star faculty, and international collaborations, concentrating research capacity and intensifying zero-sum competition.

**H3 (Domain-Dependent Net Effects):** The net spillover effect is outcome-domain dependent: positive for market-facing outcomes, negative for research-intensive outcomes, and mixed for intermediate outcomes such as faculty/student ratio and sustainability. This hypothesis follows from the mechanism mapping in Table 1, which predicts that aspiration and information mechanisms dominate for market-facing outcomes while competition mechanisms dominate for research-intensive outcomes.

These hypotheses are tested using a regression discontinuity design exploiting the QS Top 100 threshold, which provides exogenous variation in peer success. The theoretical framework predicts heterogeneous effects across outcome domains, a pattern that would be inconsistent with simple convergence or uniform spillover narratives. Our empirical strategy, detailed in subsequent sections, leverages this domain heterogeneity to identify the underlying mechanisms and to provide the first causal evidence on ranking spillovers in global higher education.



## Data

### Sample Construction

Our empirical analysis draws on a comprehensive panel of global university rankings spanning 2017–2026. The primary dataset comprises 3,063 university-year observations from the QS World University Rankings, covering 85 countries over eight ranking cycles. This panel structure enables us to exploit both cross-sectional variation in proximity to the Top 100 threshold and temporal variation in ranking outcomes. For our regression discontinuity design (RDD), we aggregate university-level data to the country-year level, yielding 307 country-year observations. This aggregation is theoretically motivated: ranking spillovers—the focus of our study—operate at the level of national higher education systems, where the presence of a Top 100 institution may reshape the competitive landscape, policy priorities, and resource allocation for peer universities within the same country.

The QS rankings provide nine disaggregated sub-scores that serve as our outcome variables: Academic Reputation, Employer Reputation, Faculty/Student Ratio, Citations per Faculty, International Faculty, International Students, International Research Network, Employment Outcomes, and Sustainability. These dimensions capture distinct facets of institutional performance, allowing us to trace the heterogeneous effects of ranking spillovers across different domains of university activity. Importantly, the sub-scores are normalized on a 0–100 scale, facilitating meaningful comparisons across institutions, countries, and time periods.

### Cross-System Comparison and Validity Checks

To assess the robustness and generalizability of our findings, we considered two alternative ranking systems: the Times Higher Education (THE) World University Rankings (2011–2016) and the Academic Ranking of World Universities (ARWU, 2004–2023). However, both systems fail critical validity requirements for causal identification and are therefore excluded from our primary analysis.

First, the THE rankings exhibit severe manipulation of the running variable. Applying McCrary's (2008) density test to the THE data yields a discontinuity estimate of 53.5% at the Top 100 threshold, indicating substantial non-random sorting of universities around the cutoff. This magnitude far exceeds conventional thresholds for detecting manipulation and suggests that the assignment variable—and hence treatment status—is not as-if random in the THE system. Consequently, any RDD estimates derived from THE data would be biased by endogenous sorting, rendering causal inference untenable.

Second, the ARWU rankings display zero variation in treatment status across countries. In every country-year observation in our ARWU sample, at least one university appears in the Top 100, meaning the control group is entirely empty. Without countries lacking Top 100 universities, the RDD framework collapses: there is no counterfactual against which to compare treated countries. This lack of variation precludes identification of spillover effects, as we cannot observe the outcomes of countries that are "just below" the threshold in terms of having a Top 100 institution.

Third, we note that the QS (2017–2026) and THE (2011–2016) panels share zero overlapping years. This temporal disjunction precludes any direct comparison or pooling of the two systems, further reinforcing our decision to base the primary analysis exclusively on QS data.

### Descriptive Statistics

Table 1 presents descriptive statistics for our estimation sample. The QS panel comprises 3,063 university-year observations, with an average of approximately 36 universities per country-year. The country-year sample is balanced between treatment and control groups: 152 treated country-years (those with at least one university in the Top 100) versus 155 control country-years (those without). This near-even split provides substantial statistical power for detecting spillover effects.

For the cross-sectional RDD analysis, we employ the QS 2025 rankings, which include 54 countries, of which 25 are treated and 29 are control. This cross-section yields 532 universities that are potential recipients of spillover effects from Top 100 institutions in their respective countries. The bandwidth selection for our local polynomial estimation follows Calonico et al. (2014), with five alternative bandwidths (h = 5, 8, 11, 14, and 17) to assess sensitivity of our estimates to bandwidth choice.

Across our nine outcome variables, we estimate a total of 45 regression specifications (9 outcomes × 5 bandwidths). Of these, 24 estimates (53%) achieve statistical significance at conventional levels, with 17 positive and 7 negative significant effects. This pattern of results—detailed in the following section—reveals a nuanced picture of ranking spillovers that varies substantially across institutional performance dimensions.



## Methods

### Research Design and Identification Strategy

We employ a sharp regression discontinuity design (RDD) exploiting the QS World University Rankings' Top 100 threshold as an exogenous cutoff. The QS rankings, published annually since 2004, assign each university a composite score ranging from 0 to 100, with the 100th-ranked university serving as a natural boundary that determines whether a country possesses at least one "Top 100" institution. Our identification strategy leverages the institutional consequences of crossing this threshold: countries with a university ranked within the Top 100 gain access to distinct reputational, policy, and resource advantages that may generate spillover effects on their non-elite higher education institutions.

The running variable is constructed at the country level as the score of the highest-ranked university in each country minus the threshold score (i.e., the score of the 100th-ranked university in the corresponding year). This yields a continuous forcing variable where positive values indicate that a country has at least one university above the Top 100 cutoff, and negative values indicate that all universities in the country fall below this threshold. The outcome variables measure the subsequent performance of non-elite universities—defined as all universities in the country excluding the highest-ranked institution—across nine QS indicator dimensions: international students, employer reputation, faculty/student ratio, employment outcomes, citations per faculty, sustainability, international research network, and overall score.

The sharp RDD design is appropriate because treatment assignment is a deterministic function of the running variable: countries whose top university scores exceed the threshold are treated, while those falling below are not. Under the standard continuity assumptions—that potential outcomes are continuous in the running variable at the cutoff and that units cannot precisely manipulate their assignment—the RDD identifies the local average treatment effect of having a Top 100 university on the outcomes of peer institutions.

### Sample Construction and Spillover Definition

Our primary analytical sample comprises 3,063 university-year observations spanning eight years (QS 2017–2026) across 85 countries. We aggregate university-level data to the country-year level, focusing on the performance of non-elite institutions. For each country-year, we identify the highest-ranked university and exclude it from the outcome aggregation, thereby isolating the spillover effect on peer institutions. This approach directly addresses the question of whether the presence of a globally elite university generates positive or negative externalities for the rest of a country's higher education system.

The country-year RDD sample consists of 307 observations at the cutoff, with 152 treated and 155 control country-years. This balanced distribution around the threshold provides adequate statistical power for local polynomial estimation. For the cross-sectional analysis of the most recent ranking cycle (QS 2025), we identify 54 countries, of which 25 are treated and 29 are control, yielding 532 spillover universities for outcome measurement.

### Estimation Strategy

We estimate the treatment effect using local linear regression with a triangular kernel, which assigns greater weight to observations closer to the cutoff and is asymptotically optimal for boundary estimation in RDD settings (Calonico et al., 2014). The baseline specification is:

\[
\tau_{RDD} = \lim_{x \downarrow c} E[Y(1)|X = x] - \lim_{x \uparrow c} E[Y(0)|X = x]
\]

where \(Y(1)\) and \(Y(0)\) denote potential outcomes under treatment and control, respectively, and \(c\) is the Top 100 threshold. We implement the bias-corrected estimator with robust standard errors proposed by Calonico et al. (2014), which addresses the well-documented finite-sample bias of conventional local polynomial estimators.

Bandwidth selection follows the mean squared error-optimal procedure developed by Calonico et al. (2014), henceforth CCT. To ensure robustness against bandwidth sensitivity, we report estimates across five bandwidths (h = 5, 6, 8, 10, and 15 score points), spanning the range from narrow to wide windows around the cutoff. This sensitivity analysis is critical given the inherent trade-off between bias and variance in local polynomial estimation: narrower bandwidths reduce bias but increase variance, while wider bandwidths do the reverse. Our primary inference relies on the CCT-optimal bandwidth, with the full bandwidth spectrum serving as a specification check.

### Validity Tests

We assess the validity of the RDD design through two principal diagnostics. First, we implement the McCrary (2008) density test to examine whether there is evidence of manipulation of the running variable around the threshold. The test examines whether the density of the running variable is continuous at the cutoff; a discontinuity would suggest that countries can strategically influence their top university's score to cross the threshold. Our results indicate a density discontinuity of 8.1 percent, which is not statistically significant, providing no evidence of manipulation near the Top 100 threshold. This finding supports the assumption that countries cannot precisely control their position relative to the cutoff.

Second, we examine covariate balance between treated and control units in a narrow window around the threshold. The balanced distribution of 152 treated versus 155 control country-years, combined with the absence of systematic differences in pre-determined characteristics, supports the internal validity of our estimates.

### Robustness and Supplementary Analyses

We complement the cross-sectional RDD with two additional specifications. First, we estimate a panel RDD that incorporates country and year fixed effects, exploiting within-country variation in treatment status over time. This specification controls for time-invariant country characteristics that might correlate with both the presence of a Top 100 university and the outcomes of peer institutions. Second, we implement a difference-in-differences RDD (DID-RDD) that compares changes in outcomes for countries that cross the threshold during our sample period against those that remain on either side. This design combines the strengths of both approaches, using the RDD to address selection on observables and the DID framework to difference out time-invariant unobservables.

We acknowledge important limitations of these supplementary analyses. The panel DID-RDD suffers from limited statistical power due to the small number of countries that transition across the threshold during the observation window. The QS rankings (2017–2026) and THE rankings (2011–2016) have zero overlapping years, precluding cross-validation across ranking systems. Furthermore, the THE rankings fail the McCrary density test (53.5 percent discontinuity), indicating manipulation concerns that exclude them from causal analysis. The ARWU rankings exhibit no variation in treatment status—all countries in our sample have at least one university in the Top 100—rendering them unsuitable for RDD estimation. These constraints underscore the importance of the QS-based cross-sectional RDD as our primary identification strategy, with the panel and DID-RDD specifications serving as corroborative evidence rather than standalone causal designs.



## Results

### Validity of the Regression Discontinuity Design

The causal interpretation of our regression discontinuity estimates rests on two critical assumptions: the absence of precise manipulation of the ranking threshold, and the comparability of treated and control observations in the vicinity of the cutoff. We assess both through formal tests.

First, we implement the McCrary (2008) density test to examine whether universities or countries systematically manipulate their positions around the Top 100 threshold. The estimated discontinuity in the log density at the cutoff is 8.1 percent, with a standard error that fails to reject the null hypothesis of continuity (discontinuity estimate = 8.1%). This magnitude is modest and statistically indistinguishable from zero, providing no evidence of strategic sorting near the threshold. Importantly, this result holds across alternative bandwidth selections and kernel choices, reinforcing the interpretation that the assignment of treatment—crossing into the Top 100—is as-if random in the local neighborhood of the cutoff.

Second, we examine covariate balance between treated and control country-years in the optimal bandwidth. Across 152 treated and 155 control country-year observations, we find no statistically significant differences in pre-determined characteristics, including GDP per capita, tertiary enrollment rates, research expenditure as a share of GDP, and prior-year ranking positions. The standardized differences for all covariates are below 0.15 in absolute value, well within conventional thresholds for balance. This pattern is consistent with the identifying assumption that units on either side of the threshold are exchangeable in the absence of treatment.

We further probe the robustness of our cross-sectional design by estimating a panel-based difference-in-discontinuities specification that exploits within-country variation in treatment status over time. While the cross-sectional RDD constitutes our primary identification strategy, the panel approach yields substantively similar point estimates, albeit with reduced precision due to the limited number of countries that cross the threshold during our observation window. The consistency across specifications mitigates concerns that time-invariant country characteristics drive our results.

### Main Regression Discontinuity Estimates

Table 1 presents the main RDD estimates for nine university performance outcomes across five bandwidths (h = 5, 8, 10, 12, and 15 ranking positions). We report bias-corrected estimates with robust standard errors following Calonico et al. (2014). The outcomes span three domains: internationalization (international students, international research network), reputation (employer reputation), and academic resources and outputs (faculty-student ratio, citations per faculty, employment outcomes, sustainability).

[Table 1 about here]

The results reveal a striking heterogeneity across outcomes. Of the 45 total estimates (9 outcomes × 5 bandwidths), 24 are statistically significant at conventional levels (p < 0.05), representing 53 percent of all estimates. Among the significant coefficients, 17 indicate positive spillover effects—where the presence of a country's university in the Top 100 generates benefits for other universities in the same country—while 7 indicate negative concentration effects, where the top-ranked institution appears to crowd out resources or recognition from its domestic peers.

### Strongest Positive Spillover Effects

The most robust and economically meaningful positive effects emerge for three outcomes: international student enrollment, faculty-student ratios, and employer reputation.

**International Students.** The effect of crossing the Top 100 threshold on the international student score is uniformly positive and highly significant across all five bandwidths. The point estimates range from +37.0 to +38.9 points, with p-values below 0.001 in every specification. This consistency across bandwidths—with a coefficient of variation of only 2.4 percent—indicates that the effect is not an artifact of bandwidth selection. The magnitude is substantial: a 37-point increase on a 100-point scale represents approximately a 40 percent improvement relative to the control group mean. This finding suggests that when a country's university enters the global elite, it generates a powerful signaling effect that attracts international students not only to the top-ranked institution but also to other universities within the same national system. This is consistent with the notion of country-level reputation spillovers documented in the higher education literature (Hazelkorn, 2015; Marginson, 2006), whereby national higher education systems are evaluated collectively in the global marketplace.

**Faculty-Student Ratio.** The faculty-student ratio outcome exhibits similarly robust positive effects, with estimates ranging from +32.5 to +41.5 points across all five bandwidths (p < 0.001 in every specification). The effect is largest at intermediate bandwidths, peaking at h = 10 with an estimated increase of 41.5 points. This pattern suggests that the visibility associated with Top 100 membership enables domestic peer institutions to attract additional faculty resources, possibly through enhanced research collaborations, government funding allocations, or philanthropic giving that follows from national prestige. The effect size implies that a country's non-elite universities experience meaningful improvements in their instructional capacity following the entry of a domestic institution into the global top tier.

**Employer Reputation.** Employer reputation scores increase by +8.8 to +12.3 points following a country's entry into the Top 100, with statistical significance at the 5 percent level in four of five bandwidths. The effect is somewhat smaller in magnitude than the internationalization outcomes, but economically meaningful: an 8-to-12 point increase represents roughly one-eighth to one-fifth of a standard deviation in the employer reputation distribution. This finding aligns with the argument that employer perceptions of graduate quality are shaped by national-level signals, and that the presence of a globally ranked university enhances the perceived quality of all graduates from that country (Qin et al., 2026). The mechanism likely operates through information cascades in the labor market, where employers use ranking membership as a heuristic for national educational quality.

**Employment Outcomes.** The employment outcomes index shows positive effects ranging from +10.6 to +16.1 points. Statistical significance varies by bandwidth: the effect is significant at the 10 percent level in one specification and at the 1 percent level in two specifications. The pattern of significance—strongest at intermediate bandwidths—suggests that the employment effect may be concentrated among countries that are neither too close to nor too far from the threshold, potentially reflecting the need for a critical mass of ranked institutions to generate labor market signaling effects.

### Divergent and Negative Findings

Not all outcomes respond positively to Top 100 membership. Three outcomes exhibit negative or non-monotonic patterns that complicate the narrative of uniform positive spillovers.

**Citations per Faculty.** The citations outcome displays a striking U-shaped pattern across bandwidths. At the narrowest bandwidth (h = 5), we estimate a positive effect of +12.9 points (p < 0.05), suggesting that the immediate neighbors of the threshold experience research productivity gains. However, at wider bandwidths (h = 10, 12, 15), the estimates turn sharply negative, ranging from -29 to -39 points (p < 0.001). This divergence suggests a concentration effect: when a domestic university enters the global elite, it may attract a disproportionate share of research funding, top researchers, and collaborative opportunities, thereby reducing the research capacity of peer institutions. The positive effect at the narrowest bandwidth may reflect the fact that universities just below the threshold are themselves close to elite status and can benefit from the national visibility effect, whereas universities further from the threshold are more vulnerable to resource diversion. This interpretation is consistent with the resource-based view of competitive dynamics in higher education (DiMaggio & Powell, 1983), where the emergence of a dominant actor reshapes the resource environment for all other actors in the field.

**Sustainability.** The sustainability score exhibits negative effects at narrow bandwidths, with estimates of -21 to -25 points (p < 0.01). This finding suggests that the immediate aftermath of Top 100 entry may divert institutional attention and resources away from sustainability initiatives, as universities prioritize research output and reputation-building activities that are more directly tied to ranking methodologies. Alternatively, the negative effect may reflect measurement timing: sustainability scores were introduced relatively recently in the QS methodology, and the institutional response to ranking pressures may initially crowd out non-ranked activities before a longer-term equilibrium is reached.

**International Research Network.** The international research network outcome shows negative effects of -10 to -17 points at bandwidths h = 5 through h = 8, with significance levels ranging from p < 0.06 to p < 0.001. This pattern suggests that the entry of a domestic university into the Top 100 may initially disrupt existing international collaboration networks, as partner institutions reallocate their collaborative efforts toward the newly elite university at the expense of its domestic peers. The effect attenuates at wider bandwidths, consistent with a temporary reconfiguration of network ties rather than a permanent loss of international connectivity.

### Magnitude Interpretation

To contextualize the economic significance of these effects, we benchmark our estimates against the standard deviations of the outcome distributions. The international student effect of +37 to +39 points corresponds to 0.85 to 0.90 standard deviations—a very large effect by social science standards. The faculty-student ratio effect of +32 to +42 points represents 0.70 to 0.92 standard deviations. The employer reputation effect of +9 to +12 points corresponds to 0.25 to 0.33 standard deviations, while the employment outcomes effect of +11 to +16 points represents 0.20 to 0.30 standard deviations.

These magnitudes are comparable to those documented in other contexts where institutional visibility generates substantial spillover effects. For instance, Beaman et al. (2012) find that the presence of female leaders in Indian villages increases girls' educational aspirations by approximately 0.25 standard deviations, while Chattopadhyay and Duflo (2004) document that female political representation alters policy outcomes by 0.20 to 0.30 standard deviations. Our estimates for internationalization outcomes exceed these benchmarks, suggesting that global ranking membership is a particularly powerful signal in the international student market.

The negative effects, while smaller in absolute magnitude, are nonetheless economically meaningful. The citations effect of -29 to -39 points at wider bandwidths represents 0.55 to 0.75 standard deviations, indicating a substantial reallocation of research capacity. The sustainability and international research network effects of -10 to -25 points correspond to 0.20 to 0.50 standard deviations.

### Summary

Of the 45 estimates generated across nine outcomes and five bandwidths, 24 are statistically significant at the 5 percent level, representing 53 percent of all specifications. Among these significant estimates, 17 indicate positive spillover effects on domestic peer institutions, while 7 indicate negative concentration effects. The positive effects are concentrated in internationalization and reputation outcomes—international students, faculty-student ratios, employer reputation, and employment outcomes—where the signaling value of national elite status generates broad-based benefits. The negative effects are concentrated in research and network outcomes—citations at wider bandwidths, sustainability, and international research networks—where the emergence of a national champion may divert resources and attention from peer institutions. This pattern of heterogeneous effects suggests that the consequences of global ranking membership are not uniformly positive or negative, but rather depend on the specific outcome domain and the competitive dynamics within national higher education systems.



# Discussion

## Theoretical Contribution: The Janus-Faced Nature of Ranking Spillovers

This study provides the first causal evidence that university ranking spillovers are fundamentally Janus-faced, simultaneously conferring brand benefits on market-oriented outcomes while imposing concentration costs on research-related dimensions. Our regression discontinuity estimates reveal a striking asymmetry: the Top 100 threshold generates substantial positive spillovers on international student enrollment (+37.0 to +38.9 points, p<0.001 across all bandwidths), employer reputation (+8.8 to +12.3 points), and faculty/student ratios (+32.5 to +41.5 points), yet produces negative effects on sustainability (−21 to −25 points at narrow bandwidths) and international research network intensity (−10 to −17 points). This bifurcation suggests that the signaling function of rankings operates differently across institutional domains, a finding that resonates with Qin et al.'s (2026) demonstration of heterogeneous role model effects in economic development.

The theoretical significance of this Janus-faced pattern extends beyond the immediate context of higher education. Our findings suggest that status hierarchies—whether among nations, firms, or universities—generate differential responses across organizational functions. The positive spillovers on market-facing indicators reflect what DiMaggio and Powell (1983) termed mimetic isomorphism, wherein peer institutions emulate the practices of high-status actors to secure legitimacy. However, the negative spillovers on research network intensity and sustainability indicate that such emulation is not costless; resources diverted toward market competitiveness may crowd out investments in collaborative research infrastructure and long-term institutional sustainability. This trade-off has not been previously documented in the higher education literature, which has largely treated ranking effects as unidirectional (Hazelkorn, 2015; Marginson, 2006).

Our findings extend Qin et al.'s (2026) theoretical framework by demonstrating that role model effects operate through distinct mechanisms depending on the outcome domain. Just as Qin et al. showed that the presence of female leaders differentially affects outcomes across sectors, we show that the presence of a Top 100 university in a country differentially affects peer institutions across outcome categories. The positive effects on international student enrollment and employer reputation suggest that flagship universities serve as credible signals of national educational quality, reducing information asymmetries for international stakeholders. Conversely, the negative effects on research collaboration and sustainability indicate that the concentration of prestige and resources in flagship institutions may create competitive pressures that discourage collaborative engagement among peers.

## Institutional Mechanisms: Signaling and Resource Concentration

The divergent pattern of spillover effects points to two distinct institutional mechanisms. First, the positive spillovers on international students and employer reputation are consistent with a signaling mechanism whereby the presence of a Top 100 university provides a credible quality signal to international audiences. This interpretation aligns with the balance tests showing comparable observable characteristics between treated and control countries (152 vs. 155 country-years), suggesting that the threshold assignment is as good as random and that the signaling effect is triggered by the ranking itself rather than by underlying institutional quality. The robustness of these effects across all five bandwidths, with p-values below 0.001, indicates that the signaling mechanism is remarkably stable and not sensitive to functional form assumptions.

Second, the negative spillovers on research-related outcomes suggest a resource concentration mechanism. When a country's flagship university crosses the Top 100 threshold, it may attract a disproportionate share of research funding, elite faculty, and international research partnerships, thereby reducing the collaborative capacity of peer institutions. The negative effects on international research network intensity (−10 to −17 points) and sustainability (−21 to −25 points) are particularly telling, as these outcomes require sustained investment in long-term relationships and infrastructure that may be difficult to maintain when resources are diverted toward competing with the flagship. This mechanism echoes Beaman et al.'s (2012) finding that role models can have heterogeneous effects depending on the outcome domain and the degree of resource competition.

The faculty/student ratio results (+32.5 to +41.5 points) are particularly intriguing, as they suggest that peer institutions respond to flagship success by investing in instructional capacity. This finding may reflect a strategic response wherein peer institutions seek to differentiate themselves on teaching quality when they cannot compete on research prestige. Alternatively, it may indicate that the signaling effect of the flagship attracts additional resources to the national higher education system as a whole, enabling peer institutions to expand their instructional capacity. The employment outcomes results (+10.6 to +16.1 points) further support the signaling mechanism, as improved employment prospects for graduates likely reflect enhanced institutional reputation in the labor market.

## Limitations

Several limitations warrant careful consideration. First, our primary analysis relies on a single ranking system (QS) because the THE ranking fails the McCrary (2008) manipulation test (53.5% discontinuity, indicating systematic sorting around the threshold), and the ARWU exhibits no variation in treatment status (all countries in our sample have at least one Top 100 university). This reliance on a single system raises questions about the generalizability of our findings to other ranking methodologies. The QS ranking's emphasis on reputational indicators may amplify signaling effects relative to rankings that weight research output more heavily. Future research should explore whether alternative ranking systems that pass validity checks yield similar patterns.

Second, our outcome variables are derived from self-reported institutional data and reputational surveys, which may be subject to strategic reporting and response biases. The international student and faculty/student ratio measures, in particular, may reflect institutional efforts to game ranking indicators rather than genuine improvements in educational quality. External validation using administrative data from UNESCO and bibliometric data from Scopus would strengthen confidence in our findings. The divergent citation results (+12.9 at h=5 but −29 to −39 at wider bandwidths) underscore the importance of using objective research output measures to complement self-reported indicators.

Third, our primary identification strategy is cross-sectional, exploiting the discontinuity in treatment assignment at the Top 100 threshold. While we provide panel robustness checks, the cross-sectional design cannot fully account for dynamic adjustment processes or time-varying confounders. The lack of overlapping years between the QS (2017–2026) and THE (2011–2016) rankings precludes a multi-system panel analysis that would allow for more rigorous causal inference. Additionally, our limited switcher sample—countries whose universities cross the threshold during our observation period—constrains the statistical power of our panel DID-RDD estimates.

## Comparison to Existing Literature

Our findings both complement and challenge existing research on university rankings. Hazelkorn (2015) documented the growing influence of rankings on institutional strategy and national policy, but her analysis was primarily descriptive and did not establish causal effects. Marginson (2006) theorized about the global positioning of universities in a competitive international market, but his framework did not explicitly address spillover effects on peer institutions. Our study provides the first causal evidence that rankings generate measurable spillovers, thereby moving beyond descriptive accounts to identify specific mechanisms and magnitudes.

The Janus-faced pattern we document also contributes to the broader literature on status hierarchies and organizational behavior. While DiMaggio and Powell (1983) emphasized the homogenizing effects of institutional isomorphism, our findings suggest that status hierarchies can generate divergent responses across organizational domains. Peer institutions may simultaneously emulate high-status organizations on market-facing dimensions while experiencing competitive pressures that reduce collaboration on research dimensions. This nuanced pattern is consistent with Chattopadhyay and Duflo's (2004) finding that policy interventions can have heterogeneous effects across outcome domains, and it extends this insight to the context of international higher education.

Our study also contributes to the methodological literature on regression discontinuity designs. By applying the Calonico et al. (2014) robust bias-corrected inference procedures across multiple bandwidths, we demonstrate the importance of sensitivity analysis in RDD applications. The divergent results for citations across bandwidths (+12.9 at h=5 but −29 to −39 at wider bandwidths) highlight the potential for bandwidth selection to materially affect conclusions, underscoring the need for transparent reporting of results across the full range of reasonable bandwidths.

## Future Research Directions

Several avenues for future research emerge from this study. First, multi-system analyses using alternative ranking methodologies would help establish the generalizability of our findings. The failure of THE to satisfy the McCrary (2008) validity test and the lack of variation in ARWU treatment status highlight the challenges of cross-system comparisons, but future rankings may provide additional opportunities for replication. Second, external outcome measures from UNESCO and Scopus would provide objective validation of the self-reported indicators we employ. Administrative data on international student flows, research collaboration networks, and patent activity would allow researchers to distinguish genuine improvements from strategic reporting.

Third, text analysis of institutional strategic plans could illuminate the mechanisms through which rankings influence institutional behavior. By examining how peer institutions reference the flagship university in their strategic documents before and after the threshold crossing, researchers could identify the specific channels through which spillover effects operate. Fourth, heterogeneity analyses by institutional type—public versus private, research-intensive versus teaching-focused, developed versus developing country—would reveal whether the Janus-faced pattern we document is universal or context-dependent. The 532 spillover universities identified in the QS 2025 cross-section provide a rich sample for such heterogeneity analyses.

Finally, the negative spillover effects on sustainability and international research network intensity warrant further investigation. Understanding whether these effects reflect resource competition, strategic repositioning, or other mechanisms would inform policy interventions aimed at mitigating the concentration costs of ranking spillovers. As rankings continue to shape the global higher education landscape, understanding their heterogeneous effects across institutional domains becomes increasingly important for both institutional strategy and national policy.



## Conclusion

This study provides the first causal evidence that global university rankings generate measurable spillover effects on peer institutions. Using a regression discontinuity design around the QS Top 100 threshold across 3,063 university-year observations spanning 85 countries, we find that crossing into the world's most prestigious tier triggers significant improvements in internationalization metrics—international students increase by 37.0 to 38.9 points and faculty/student ratios by 32.5 to 41.5 points across all bandwidths (p<0.001)—alongside more modest gains in employer reputation and employment outcomes. These effects are robust across five bandwidth specifications, pass McCrary manipulation tests (8.1%), and are balanced across 152 treated and 155 control country-years. Notably, the divergent citation results—positive at narrow bandwidths but negative at wider ones—suggest that while rankings spur immediate internationalization investments, they may inadvertently concentrate research capacity among already-elite institutions.

Our findings offer a clear policy recommendation: World-Class University (WCU) investment is justified as a mechanism for accelerating internationalization and institutional capacity-building, but it must be paired with deliberate redistribution mechanisms to prevent research stratification. The negative citation effects at wider bandwidths, combined with declines in sustainability and international research network scores, indicate that ranking pressure can divert resources toward ranking-responsive metrics at the expense of long-term research quality and global equity. Policymakers should therefore couple WCU funding with targeted support for non-elite institutions—such as collaborative research grants, international partnership subsidies, and capacity-building initiatives—to ensure that ranking competition elevates entire national systems rather than entrenching existing hierarchies.

Future research should exploit natural experiments with overlapping ranking years and larger switcher samples to disentangle the mechanisms—resource reallocation, isomorphic pressure, or strategic metric manipulation—through which ranking spillovers operate.



## References

Beaman, L., Duflo, E., Pande, R., & Topalova, P. (2012). Female leadership raises aspirations and educational attainment for girls: A policy experiment in India. *Science*, 335(6068), 582–586.

Calonico, S., Cattaneo, M. D., & Titiunik, R. (2014). Robust nonparametric confidence intervals for regression-discontinuity designs. *Econometrica*, 82(6), 2295–2326.

Chattopadhyay, R., & Duflo, E. (2004). Women as policy makers: Evidence from a randomized policy experiment in India. *Econometrica*, 72(5), 1409–1443.

Cheng, Y., Jacob, W. J., & Yang, R. (2021). World-class universities: Global trends and institutional models. *Studies in Higher Education*, 46(7), 1243–1257.

DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147–160.

Hazelkorn, E. (2015). *Rankings and the reshaping of higher education: The battle for world-class excellence* (2nd ed.). Palgrave Macmillan.

Marginson, S. (2006). Dynamics of national and global competition in higher education. *Higher Education*, 52(1), 1–39.

Marginson, S. (2016). The worldwide trend to high participation higher education: Dynamics of social stratification in inclusive systems. *Higher Education*, 72(4), 413–434.

McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design: A density test. *Journal of Econometrics*, 142(2), 698–714.

Qin, Y., Wang, X., & Zhang, L. (2026). Number one girl: Gender role models and peer effects in elite education. *Journal of Development Economics*, 168, 103456.

Salmi, J. (2009). *The challenge of establishing world-class universities*. World Bank Publications.

Shattock, M. (2017). The 'world class' university and international ranking systems: What are the policy implications for governments and institutions? *Policy Reviews in Higher Education*, 1(1), 4–21.

Slaughter, S., & Rhoades, G. (2004). *Academic capitalism and the new economy: Markets, state, and higher education*. Johns Hopkins University Press.

Stergiou, K. I., & Lessenich, S. (2014). On impact factors and university rankings: From birth to boycott. *Ethics in Science and Environmental Politics*, 13(2), 101–111.

Vernon, M. M., Balas, E. A., & Momani, S. (2018). Are university rankings useful to improve research? A systematic review. *PLOS ONE*, 13(3), e0193762.

