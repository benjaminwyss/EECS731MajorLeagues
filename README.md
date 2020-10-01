# EECS 731 Project 4: Major Leagues
Submission by Benjamin Wyss

## Project Overview

Examining fivethirtyeight soccer power index (spi) data sets to build a regression model which predicts the scores of soccer matches.

### Data Sets Used

fivethirtyeight Soccer SPI Ratings - Taken from: https://github.com/fivethirtyeight/data/tree/master/soccer-spi on 10/1/20

Only the spi_matches dataset is examined because it contains all of the match information and historical spi data needed to build the target regression model. The spi_matches_latest data set is a subset of the spi_matches dataset, and thus it can be discarded without losing any additional match data samples. The remaining data sets include information about current spi ratings, but the target regression model should perform better at predicting match scores based on ratings from when a match occured rather than from current ratings, so these data sets are discarded as well.

### Results

Put your results here
