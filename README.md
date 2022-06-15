# DPS_Challenge
This repo is for DSP challenge.

## Create model
I utilize LinearRegression model to do the prediction task.  

First, I do some visualization to analyse the distribution and relationshop of the data. 
![image](https://github.com/MingyuLiu1/DPS_Challenge/blob/main/figs/num_acc_cat.png)

![image](https://github.com/MingyuLiu1/DPS_Challenge/blob/main/figs/num_acc_00-20.png)

Then after preprocessing, only the values of Month and Year are input to the predit model. The following is the prediction results for year 2021.
![iamge](https://github.com/MingyuLiu1/DPS_Challenge/blob/main/figs/predict_res_2021.png)

## Create website
The interface of the website is shown in the followed figure.
![image](https://github.com/MingyuLiu1/DPS_Challenge/blob/main/figs/web.png)

## How to use
1. Download the whole project
2. Under the project folder
    `cd DPS_Challenge`
3. Run `app.py`
    `python app.py`
4. Open the generated links, input the year and month that you want to predict, like
  `202101` --- 2021 January
