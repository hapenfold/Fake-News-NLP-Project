## Fake News Challenge (FNC-1)

### Introduction

I have recently completed the 12-week Immersive Data Science course at General Assembly. For my final project I have chose to look at the dataset from the first stage of a competition set up by a group of academics and professionals, called the [Fake News Challenge](http://www.fakenewschallenge.org). Although the competition is now over, I feel the topic is particularly interesting so I wanted to explore the dataset and see what results I could get. 

Effectively evaluating the stance of a text in relation to another text is a useful step towards automating the fact-checking process. To give context of where this may be useful, fact-checking organisations have large databases of previously checked statements and facts and also continuously source up to date statistics and figures on important social, economic and political factors. A robust Stance Detection Classifier would be able to take a news article and identify which previously checked facts stored within the database are related to it and of those what the relationship is between the article and the checked statements. 

As defined on the FNC website, for the first part of the challenge (FNC-1) they have chosen the task of estimating the stance of a body text from a news article relative to a headline. Specifically, the body text may agree, disagree, discuss or be unrelated to the headline.

The training dataset provided contains 50,000 pairs of headline and body text with the appropriate class label for each. 
<br/>
<br/>
<br/>

|**EXAMPLE HEADLINE**|   |
|:-------- | ----- |
|“Robert Plant Ripped up `$`800M Led Zeppelin Reunion Contract”| |
|<br/>  |<br/>    |
|**Example Snippets From Body Texts** | **Correct Classification** |
|“… Led Zeppelin’s Robert Plant turned down £500 MILLION to reform supergroup...”| **Agree**|
|“… No, Robert Plant did not rip up an `$`800 million deal to get Led Zeppelin back together...”| **Disagree**|
|“… Robert Plant reportedly tore up an `$`800 million Led Zeppelin reunion deal...”|**Discusses**|
|“… Richard Branson’s Virgin Galactic is set to launch SpaceShipTwo today..."| **Unrelated** |

<br/>
<br/>

