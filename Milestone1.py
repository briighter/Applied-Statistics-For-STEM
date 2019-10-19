####### Milestone 1 Python Script
import pandas as pd
import scipy.stats as st
from snhu_MAT243 import prop_1samp_ztest
from snhu_MAT243 import means_1samp_ttest



##Step 1: Import your data set
##-----------------------------------------------------------------------------
manchesterweather = pd.read_csv('ManchesterWeather.csv')


##Step 2: Calculate descriptive statistics 
##-----------------------------------------------------------------------------
print ('Descriptive Statistics - Step 2')
print ('')

print ('Mean')
print (manchesterweather[['EMXT']].mean())
print ('')

print ('Median')
print (manchesterweather[['EMXT']].median())
print ('')

print ('Mode')
print (manchesterweather[['EMXT']].mode())
print ('')

print ('Minimum')
print (manchesterweather[['EMXT']].min())
print ('')

print ('Maximum')
print (manchesterweather[['EMXT']].max())
print ('')

print ('Variance')
print (manchesterweather[['EMXT']].var())
print ('')

print ('Standard Deviation')
print (manchesterweather[['EMXT']].std())
print ('')

print ('Describe')
print (manchesterweather[['EMXT']].describe())
print ('')

print ('')

##Step 3: Calculate descriptive statistics
##-----------------------------------------------------------------------------
print ('Descriptive Statistics - Step 3')
print ('')

print ('Mean')
print (manchesterweather[['EMXP']].mean())
print ('')

print ('Median')
print (manchesterweather[['EMXP']].median())
print ('')

print ('Mode')
print (manchesterweather[['EMXP']].mode())
print ('')

print ('Minimum')
print (manchesterweather[['EMXP']].min())
print ('')

print ('Maximum')
print (manchesterweather[['EMXP']].max())
print ('')

print ('Variance')
print (manchesterweather[['EMXP']].var())
print ('')

print ('Standard Deviation')
print (manchesterweather[['EMXP']].std())
print ('')

print ('Describe')
print (manchesterweather[['EMXP']].describe())
print ('')


##Step 4: Construct confidence interval for population proportion
##-----------------------------------------------------------------------------
print ('Confidence Interval - Step 4')
n = manchesterweather[['EMXT']].count()
x = (manchesterweather[['EMXT']] > 190).values.sum()
p = x/n*1.0
stderror = (p * (1 - p)/n)**0.5
print (st.norm.interval(0.99, p, stderror))
print ('')



##Step 5: Construct confidence interval for population mean
##-----------------------------------------------------------------------------
print ('Confidence Interval - Step 5')
n = manchesterweather[['EMXP']].count()
df = n - 1
mean = manchesterweather[['EMXP']].mean()
stdev = manchesterweather[['EMXP']].std()
stderror = stdev/(n**0.5)
print (st.t.interval(0.95, df, mean, stderror))
print ('')



##Step 6: Perform hypothesis test for population proportion
##-----------------------------------------------------------------------------
print ('Hypothesis Test - Step 6')
n = manchesterweather[['EMXT']].count()
x = (manchesterweather[['EMXT']] > 190).values.sum()
null_value = 0.67
alternative = 'not-equal'
print (prop_1samp_ztest(x, n, null_value, alternative))
print ('')



##Step 7: Perform hypothesis test for population mean
##-----------------------------------------------------------------------------
print ('Hypothesis Test - Step 7')
n = manchesterweather[['EMXP']].count()
df = n - 1
mean = manchesterweather[['EMXP']].mean()
std_dev = manchesterweather[['EMXP']].std()
null_value = 280
alternative = 'not-equal'
print (means_1samp_ttest(mean, std_dev, n, null_value, alternative))
print ('')