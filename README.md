# ADS_citibike_project


## Programs:

1) 01\_setup: prepares working directory and downloads data

2) 02\_create\_cb\_dist: Uses LEHD Origin-Destination table and Census Block level data to calculate the average commute distance for each Census Block. 

3) 03\_citibike\_cb: Calculate number of Citibike rides per Census Block. This is slow because it looks at over 8 million rides from 2014.

4) 04\_demographics: Read in and clean demographic data per Census Block Group.

5) 05\_model: Run the regression and conduct model evaluation.

