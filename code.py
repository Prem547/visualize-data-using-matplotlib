# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

electors_2009 = pd.read_csv(path)
candidate_2009 = pd.read_csv(path1)

# Plot a bar chart to compare the number of male and female candidates in the election
fig, ax = plt.subplots()
candidate_2009['Candidate_Sex'].value_counts().plot(kind='bar')
plt.xlabel("Gender")
plt.ylabel("count")
plt.title("Gender Comparision")
labels = [item.get_text() for item in ax.get_xticklabels()]
labels = ['Gender-Male', 'Gender-Female']
ax.set_xticklabels(labels)
plt.xticks(rotation=0)
# Plot a histogram of the age of all the candidates as well as of the winner amongst them. Compare them and note an observation
fig, ax_all = plt.subplots(1,2,figsize=(20,10), tight_layout = True)
#histogram of the age of all the candidates
candidate_2009.hist(['Candidate_Age'], bins=10, ax = ax_all[0])
ax_all[0].set_xlabel("Age of the candidate")
ax_all[0].set_ylabel("Count")
ax_all[0].set_title("All the candidates")
#winner amongst them
candidate_2009[candidate_2009['Position'] == 1].hist(['Candidate_Age'],bins=10, ax = ax_all[1])
ax_all[1].set_xlabel("Age of the candidate")
ax_all[1].set_ylabel("Count")
ax_all[1].set_title("Winner candidates")
# Plot a bar graph to get the vote shares of different parties
votes_share = candidate_2009.groupby(['Party_Abbreviation'])['Total_Votes_Polled'].sum()
plt_bar_chart = votes_share.sort_values(ascending=False)[:10].plot(kind='barh')
plt_bar_chart.set_xlabel('Vote_share')
plt_bar_chart.set_ylabel('Party')
plt_bar_chart.set_title('Vote share of Top 10 Parties')
# Plot a barplot to compare the mean poll percentage of all the states
Mean_Poll_Percentage = electors_2009.groupby(['STATE'])['POLL PERCENTAGE'].mean()
Mean_Poll_Percentage = Mean_Poll_Percentage.sort_values(ascending = False).to_dict()
print(Mean_Poll_Percentage)

state = list(Mean_Poll_Percentage.keys())
state_percentage = list(Mean_Poll_Percentage.values())
State_DF = pd.DataFrame({'State' : state, 'Poll_Percentage' : state_percentage})
fig, ax = plt.subplots(1,1,figsize=(10,30), tight_layout=True)
plt.barh(State_DF['State'], State_DF['Poll_Percentage'])
plt.xlabel("Percentage")
plt.ylabel("States")
plt.title("State Poll Percentage")

# Plot a bar plot to compare the seats won by different parties in Uttar Pradesh
Seats_Won = candidate_2009[(candidate_2009['Position'] == 1) & (candidate_2009['State_name'] == 'Uttar Pradesh')]['Party_Abbreviation'].value_counts()
print(Seats_Won)

plt.bar(Seats_Won.index, Seats_Won)
plt.xlabel('Parties')
plt.ylabel('Seats-Won')
plt.title('Seats won by different parties in Uttar Pradesh')
# Plot a stacked bar chart to compare the number of seats won by different `Alliances` in Gujarat,Madhya Pradesh and Maharashtra. 
mask_1 = (candidate_2009['Position'] == 1)
mask_2 = (candidate_2009['State_name'].isin(['Gujarat', 'Madhya Pradesh', 'Maharashtra']))
Seats_Reqd_States = candidate_2009[mask_1 & mask_2][['State_name', 'Alliance']]

res = Seats_Reqd_States.groupby(['State_name', 'Alliance']).size().unstack()

res.plot(kind = 'bar', stacked=True, figsize=(15,10))


# Plot a grouped bar chart to compare the number of winner candidates on the basis of their caste in the states of Andhra Pradesh, Kerala, Tamil Nadu and Karnataka
mask_1 = (candidate_2009['Position'] == 1)
mask_2 = (candidate_2009['State_name'].isin(['Andhra Pradesh', 'Kerala', 'Tamil Nadu', 'Karnataka']))
Winning_Candidates = candidate_2009[mask_1 & mask_2]

res.plot(kind='bar', figsize = (15,10))

# Plot a horizontal bar graph of the Parliamentary constituency with total voters less than 100000
mask = (electors_2009['Total_Electors'] < 100000)
val = electors_2009[mask]
plt.barh(val['PARLIAMENTARY CONSTITUENCY'], val['Total voters'])
plt.xlabel("Count")
plt.ylabel("PC")
plt.title("PC vs Electors")
# Plot a pie chart with the top 10 parties with majority seats in the elections
Party_Seats_DF = candidate_2009[candidate_2009['Position'] == 1]
Top10 = Party_Seats_DF['Party_Abbreviation'].value_counts()[:9].to_dict()
Top10['Others'] = sum(Party_Seats_DF['Party_Abbreviation'].value_counts()) - sum(Party_Seats_DF['Party_Abbreviation'].value_counts()[:9])
print(Top10)

plt.figure(figsize = (10,10))
plt.pie(Top10.values(),labels = Top10.keys(), autopct = '%.2f')



# Plot a pie diagram for top 9 states with most number of seats

seats = electors_2009.STATE.value_counts()[:8].to_dict()
seats['Other States'] = electors_2009.STATE.value_counts().sum() - electors_2009.STATE.value_counts()[:8].sum()

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}% {{v:d}}'.format(p=pct,v=val)
    return my_autopct

plt.figure(figsize=(10,10))
plt.pie(x=seats.values(),labels = seats.keys(), autopct='%.2f%%')
plt.axis('equal')















