# Goals 

With this project we will assess your capacity to solve problems on your own and 
present a fully working solution to a data science problem mirroring the ones we are 
working on daily at Artefact. 

You will be given a chance to show your skills in data science: code, design, autonomy, 
rigor, etc. 
At Artefact, we are helping our client solve their business problems, and machine learning models are a tool to achieve this.

The data transformation, preprocessing, training and validation will be handled by your 
code. The data and its underlying trends is close to real data of our customers. 


# Description of the problem

Our client is a major household hardware company.
Their end goal is to better understand their customers and in identifying the most representative customer profiles, to improve their marketing & sales initiatives. This will be useful to:
- launch better targeted marketing actions with the right message to the right customer (depending on who he or she is) on the right channel
- optimize local communication (according to customer profile per store...)
- etc ...

In order to do that, we have to **create a customer segmentation** and **define customer profiles** to describe how each type of customers behave.


# Data Description 

With this instruction notice, you have been given a .tgz folder containing 3 CSV files:
- client.csv​ : table with customers information


|        Column        |                                            Description                                           |
|:--------------------:|:------------------------------------------------------------------------------------------------:|
|       client_id      |                                            Client unique ID                                      |
|      client_date     |                                       Client account creation date                               |
|          age         |                                               Client age                                         |
|      client_type     |                                   Client type (individual or company)                            |
|         zipcode      |                                             Customer zipcode                                     |
|         country      |                                             Customer country                                     |



- products.csv : table with products information

|        Column        |                                            Description                                           |
|:--------------------:|:------------------------------------------------------------------------------------------------:|
|      product_id      |                                           Product unique ID                                      |
|      product_cat     |                                           Product category                                       |



- transactions.csv : table with transactions information

|        Column        |                                            Description                                           |
|:--------------------:|:------------------------------------------------------------------------------------------------:|
|       ticket_id      |                                          Transaction unique ID                                   |
|      product_id      |                                          Product unique ID                                       |
|       store_id       |                                             Store unique ID                                      |
|       client_id      |                                            Client unique ID                                      |
|         date         |                                          Transaction date                                        |
|         hour         |                                             Transaction hour                                     |
|      n_products      |                                          Product quantities                                      |
|       price_ttc      |                                              Price amount                                        |


# Requirements

## Solution

You are asked to write a clear approach solving the challenge described above, by combining **three components**: **Exploratory Data Analysis (EDA), modeling and results interpretation**.

## Code & Frameworks

The programming language is **Python**, you are free to organize your code the way 
you want with the tools/frameworks you feel comfortable.
You should follow common best practices regarding naming conventions and formation and do not hesitate to add clear
comments to explain your ideas. 

The three parts of your approach should be easily identified and separated in your code.

## Metrics

Evaluate your model given a set of metrics (quantitative/qualitative) that are up to you to choose. 
Indeed, one of your missions once in the team will be to define accurate and relevant metrics that mimic the business needs of our clients. 

Therefore, **we will also assess your metrics’ choice** as a proxy of the understanding of the business problem. 

We intentionally are not giving any strict instructions on how the EDA, 
modeling or interpretation should be performed to let you explore and think about each 
problem. 

Given the time you have, you will not be able to implement all of your 
ideas, do the most important ones and add a "Next steps" section in your code with your eventual follow 
ups. 


## Evaluation Criteria

For this test, more than the relevance or architecture of your model, what we want to 
assess is the quality of your code in terms of readability, organization 
and ease of extension.

The second goal of this test is to see how well you understood the problems at play with the given data and what you have done or would do to solve them. You are asked to write down what you have discovered in the way you feel the most appropriate, this can be a markdown, a few slides, a clear detailed notebook etc. We will evaluate the content of the document, not the design of it. 

**Do not spend too much time making this document too beautiful, this is not the intended goal. The most important thing are the insights that you are going to find on the customers' profiles.**


# Expected Deliverables

<<<<<<< HEAD
We expect you to send us a link to a **private repository** (github, gitlab, bitbucket...). Your repository must be composed of :
- your main code (e.g. jupyter notebook)
=======
We expect you to send us a link to a **private repository** (github, gitlab, bitbucket...). Your repository must, at least, be composed of :
- your main code (e.g. jupyter notebooks, script files in folders, etc.)
>>>>>>> d6a8a173b0db90d954a73b1fcc142af2000fd85a
- a readme file containing an summary of your work
- any other file or folder you think may be relevant

You will be asked to present your work, code and findings in the next technical interview. The interview will allow you to explain your technical decisions, and the problems you encountered. 

Good luck!
