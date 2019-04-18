# link_prediction

This repository is aimed at doing link prediction in investors-startup bipartite graph.

■ [Illustrating paper](https://github.com/malaville/link_prediction/blob/master/illustrating_paper.ipynb) illustrates Zheng's paper
![Illustrating one small graph that is growing](https://github.com/malaville/link_prediction/blob/master/content/gifexample_data.gif)



■ [Preparing Real Data](https://github.com/malaville/link_prediction/blob/master/preparing_real_data.ipynb) prepares the data and puts it in a **utils.p** file that can be used to work.

■ [Generate Dataframes and Predict II](https://github.com/malaville/link_prediction/blob/master/generate-dataframes-and-predict-II.ipynb) shows how with prepared data, we generate dataframes and begin to predict and compare predictions
![Results are better than Zheng's](https://github.com/malaville/link_prediction/blob/master/content/2019-4-18-14h47-1.9pc-featuresnb-12.png)

■ [Investors profile from year to another](https://github.com/malaville/link_prediction/blob/master/generate-investor-investing-profile.ipynb)
In this part we show that similarity between firm is not random when an investor make choices. Start-ups invested in year+1 are closer (word2vec cosine distance) to that of the year before.
![Results are better than Zheng's](https://github.com/malaville/link_prediction/blob/master/content/K5_Investor_profiles.png)

The paper I inspire of is [Zheng's](https://github.com/malaville/link_prediction/blob/master/base_papers/zheng.pdg) which you can find in /base_papers


