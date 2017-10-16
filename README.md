## Fake News NLP Project

### Project Overview

I have recently completed the 12-week Immersive Data Science course at General Assembly. For my final project I have chosen to look at the dataset from the first stage of a competition set up by a group of academics and professionals, called the [Fake News Challenge](http://www.fakenewschallenge.org). Although the competition is now over, I feel the topic is relevant and interesting so I wanted to explore the dataset and see what results I could get. 

Effectively evaluating the stance of a text in relation to another text is a useful step towards automating the fact-checking process. To give context of where this may be useful, fact-checking organisations have large databases of previously checked statements and facts and also continuously source up to date statistics and figures on important social, economic and political factors. A robust Stance Detection Classifier would be able to take a news article and identify which previously checked facts stored within the database are related to it and of those what the relationship is between the article and the checked statements. 


![diagram](https://github.com/hapenfold/Fake-News-NLP-Project/blob/master/Assets/diagram_afc_horizontal.png?raw=true)


As defined on the [Fake News Challenge website](http://www.fakenewschallenge.org), they have chosen the task of estimating the stance of a news article's body text relative to a headline. Specifically, the body text may `agree` with, `disagree` with, `discuss` or be `unrelated` to the headline. 

This project is contained in the Jupyter Notebook file named [capstone_project_fake_news](capstone_project_fake_news.ipynb) which includes a commentary on the methods, processes and results of the project. 

The data is contained in four CSV files (2 training and 2 test) contained in the [data](data/) folder. 

There is also a file `plotter_help.py` which contains some plotting functions which were used within the project. 




