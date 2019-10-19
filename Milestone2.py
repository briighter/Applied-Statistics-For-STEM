####### Milestone 2 Python Script
import pandas as pd
import scipy.stats as st
from snhu_MAT243 import prop_1samp_ztest
from snhu_MAT243 import means_1samp_ttest
from statsmodels.stats.proportion import proportions_ztest


##Step 1: Import your data set
##-----------------------------------------------------------------------------
manchesterweather = pd.read_csv('ManchesterWeather.csv')

####### Step 2: Perform hypothesis test for the difference of two population proportions
##-------------------------------------------------------------------------------------------------

print ('Hypothesis test for the difference of two population proportions - Step 2')
n1 = manchesterweather.loc[manchesterweather['Month'] == 7]['EMXT'].count()
n2 = manchesterweather.loc[manchesterweather['Month'] == 8]['EMXT'].count()
x1 = (manchesterweather.loc[manchesterweather['Month'] == 7]['EMXT'] > 325).values.sum()
x2 = (manchesterweather.loc[manchesterweather['Month'] == 8]['EMXT'] > 325).values.sum()
counts = [x1, x2]
n = [n1, n2]
print (proportions_ztest(counts, n))
print ('')

####### Step 3: Perform hypothesis test for the difference of two population proportions
##-------------------------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population proportions - Step 3')
n1 = manchesterweather.loc[manchesterweather['Month'] == 2]['EMXP'].count()
n2 = manchesterweather.loc[manchesterweather['Month'] == 8]['EMXP'].count()
x1 = (manchesterweather.loc[manchesterweather['Month'] == 2]['EMXP'] > 200).values.sum()
x2 = (manchesterweather.loc[manchesterweather['Month'] == 8]['EMXP'] > 200).values.sum()
counts = [x1, x2]
n = [n1, n2]
print (proportions_ztest(counts, n))
print ('')

####### Step 4: Perform hypothesis test for the difference of two population means
##----------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population means - Step 4')
jul_data = manchesterweather.loc[manchesterweather['Month'] == 7]['EMXT']
aug_data = manchesterweather.loc[manchesterweather['Month'] == 8]['EMXT']
print (st.ttest_ind(jul_data, aug_data, equal_var=False))
print ('')


####### Step 5: Perform hypothesis test for the difference of two population means
##----------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population means - Step 5')
feb_data = manchesterweather.loc[manchesterweather['Month'] == 2]['EMXP']
aug_data = manchesterweather.loc[manchesterweather['Month'] == 8]['EMXP']
print (st.ttest_ind(feb_data, aug_data, equal_var=False))
print ('')
