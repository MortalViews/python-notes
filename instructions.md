# Financial Platform - FPG Squad Intern Code Challenge

Global businesses like MediaMath deal with large amounts of data on a daily basis. Often, these data must be processed in certain ways - aggregated, divided, or combined in various manners - before they can be consumed or analyzed. MediaMath recently received a bill for its New Year Party, but accounting thinks that some prices on the bill don't add up. MediaMath would like to understand how each item on the bill is calculated. Fortunately, from the bill, the ingredients of each dish can be recognized, so the first step to understand if MediaMath was charged correctly, is to understand how each ingredient plays in the final price of a dish.

The following sample data set is part of the bill:

***Table 1***

| Ingredient 1 | Ingredient 2 | Price |
| ------------ | ------------ | ------|
| Chicken Breast | Parsley | $25.00 |
| Chicken Breast | Red Sauce | $20.00 |
| Pasta | Parsley | $17.00 |
| Pasta | Red Sauce | $12.00 |

Your job is to write a program that can analyze the data and calculate how much each ingredient costs independently. There can be many possibilities when separating ingredients like this. As an example, one possible way to transform the above data set is presented in the following table, so that the combination of two ingredients will add up to the price in the above table. Note that the order is not important.

***Table 2***

| Ingredient | Price |
| ---------- | ----- |
| Chicken Breast | $15.00 |
| Pasta | $7.00 |
| Parsley | $10.00 |
| Red Sauce | $5.00 |

To make the workflow more organized and the system flexible, you're recommended to follow the steps below to complete this task. Keep your solutions to all these problems in a single directory, and write down your explanations in a separate README file.

## Step 1

Create a program to read data from either command line or a file in the format that complies with Table 1, above. The sample comma-delimited data is provided in the appendix below.  If you choose to input the data through command line, separate each column with a comma (','). Load the data into a data structure that will help you complete the overall task.

## Step 2

Create an algorithm to calculate the price of each ingredient as demonstrated in Table 2. You may assume that every ingredient is priced within the range of \[$1, $40\], in $1 increments. Print your results into a file. There is no limit to the number of ingredients that may show up in the final bill to be processed by your program. In the case that more than one possible solutions exist, output all possibilities into different files.

Explain how the amount of data will affect the time and space consumption of your algorithm.

## Step 3

Instead of reading data from command line or a file, as you did in Step 1, create a separate program that runs continuously and takes input from command line. Input into this separate program must also comply with the format of data in Table 1. As soon as this service receives a new line of data, it should pass the data on to your algorithm created in Problem 2. Your algorithm should take the new data into account and recalculate results based on all historical data.

## Appendix

### Sample Data

```
Ingredient 1,Ingredient 2,Price
Chicken Breast,Parsley,$25.00
Chicken Breast,Red Sauce,$20.00
Pasta,Parsley,$17.00
Pasta,Red Sauce,$12.00
```

