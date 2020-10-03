# EECS 731 Project 4: Major Leagues
Submission by Benjamin Wyss

## Project Overview

Examining fivethirtyeight soccer power index (spi) data sets to build a regression model which predicts the scores of soccer matches.

### Data Sets Used

fivethirtyeight Soccer SPI Ratings - Taken from: https://github.com/fivethirtyeight/data/tree/master/soccer-spi on 10/1/20

Only the spi_matches dataset is examined because it contains all of the match information and historical spi data needed to build the target regression model. The spi_matches_latest data set is a subset of the spi_matches dataset, and thus it can be discarded without losing any additional match data samples. The remaining data sets include information about current spi ratings, but the target regression model should perform better at predicting match scores based on ratings from when a match occured rather than from current ratings, so these data sets are discarded as well.

### Results

By utilizing feature engineering, I was able to construct a regression model which performs better than the baseline models which I tested.

Despite the fact that feature engineering aided my final regression model, the model performed poorly overall, with predicted match scores having validation testing coefficients of determination equal to 0.092 and 0.068 when rounded to 3 decimal places. This is likely because the final regression model utilizes spi scores to predict match scores, and while there does exist a correlation between these two scores, the correlation coefficient is small and the variance between these features is high. Both of these factors limit the overall performance of the final regression model.
