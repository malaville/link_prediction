# Link Prediction Investor-Startup 

This repository is aimed at doing link prediction in investors-startup bipartite graph.

I began with the work of [Zheng](https://github.com/malaville/link_prediction/blob/master/base_papers/zheng.pdg) which I illustrate and compare to my results. Basically, Zheng's work is just predicting with Preferential Attachement (Degree(venture) x Degree(investor)).

I wanted to leverage the information of graphs which I believe to represent - to a certain extent - the social interactions which drive venture capitalists, which bounded rationality and bounded geographical influence should push towards **closer** ventures. To measure this closeness, I computed the *LENGTH* feature, which represent the geodesic distance in the graph between the two nodes. In a second part I computed also the **textual closeness** of start-up to investor's portfolio using cosine distance on W2V features.

As expected, this feature shows strong tendance to make the model predict a *match* between venture and investors. We show that the model with LENGTH is globally stronger than without on PR-curves, and also that LENGTH is the SHAP-most-important feature (see B.2).

Along with that, quite uncorrelated, we added information about ventures descriptions. Those descriptions were converted to vectors thanks to W2V and then compared with cosine distance. We see that the startups invested in YEAR+1 by an investor are on average semantically closer to the previous YEAR portfolio of this same investor. This is a hint that investor are specialized in some areas (which we know of course). Inspired from [Basole's work](https://doi.org/10.1109/TEM.2018.2855435). 

■ [Illustrating paper](https://github.com/malaville/link_prediction/blob/master/illustrating_paper.ipynb) illustrates Zheng's paper
![Illustrating one small graph that is growing](https://github.com/malaville/link_prediction/blob/master/content/gifexample_data.gif)


■ [Preparing Real Data](https://github.com/malaville/link_prediction/blob/master/preparing_real_data.ipynb) prepares the data and puts it in a **utils.p** file that can be used to work.

■ [Generate DFA](https://github.com/malaville/link_prediction/blob/master/generate-DFA.ipynb) prepares the DataFrame to be used in later steps.

■ [Predictions](https://github.com/malaville/link_prediction/blob/master/test-different-models.ipynb) tests a fine-tuned RandomForestClassifier and gives Precision-Recall Curves for it with different features. We can see a good improvement with LENGTH and W2V features.
![Results are better than Zheng's](https://github.com/malaville/link_prediction/blob/master/content/2019-4-18-14h47-1.9pc-featuresnb-12.png)

# B - Insights

### ■ 1 Investors knowledge

Investors tend to invest in firms which description looks like the one it invested in before. By comparing the DIST_MEAN to a RANDOM distance we see that the start-up in the portfolio on the second half of the dataset is correlated to the first half (before and after 2016). If an investor was investing in random firms then it would be around RANDOM which was calculated by picking randomly 10 000 couples (Di, Dj) of start-ups i and j in the dataset.

See : [Investors profile from year to another](https://github.com/malaville/link_prediction/blob/master/generate-investor-investing-profile.ipynb)
![Investor profiles](https://github.com/malaville/link_prediction/blob/master/content/K5_Investor_profiles.png)

### ■ 2 Feature importance

[Investors profile from year to another](https://github.com/malaville/link_prediction/blob/master/test-feature-importance.ipynb) shows that the most impactful feature is LENGTH according to [SHAP feature importance](https://github.com/slundberg/shap).
![Most Impactful Features](https://github.com/malaville/link_prediction/blob/master/content/SHAP_values.png)
![Most Impactful Features 2](https://github.com/malaville/link_prediction/blob/master/content/SHAP_values2.png)
![The PR-curve comparison)](https://github.com/malaville/link_prediction/blob/master/content/pr-curve-comparison-1.png)

The paper I inspire of is [Zheng's](https://github.com/malaville/link_prediction/blob/master/base_papers/zheng.pdg) which you can find in /base_papers


