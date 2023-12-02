import pandas as pd
import matplotlib.pyplot as plt 
import statistics as stat

surveydata = pd.read_csv('Guestbook Testing Survey.csv')
output = open("Stats.txt", "w")

profile = surveydata['UnderstandProfile'].mean()
party = surveydata['EnterParty'].mean()
output.write("Understood Profile mean: " + str(profile) + "\n")
output.write("Understood if entered party mean: " + str(party) + "\n\n")

sus1 = surveydata['SUS1'].mean()
sus2 = surveydata['SUS2'].mean()
sus3 = surveydata['SUS3'].mean()
sus4 = surveydata['SUS4'].mean()
sus5 = surveydata['SUS5'].mean()
sus6 = surveydata['SUS6'].mean()
sus7 = surveydata['SUS7'].mean()
sus8 = surveydata['SUS8'].mean()
sus9 = surveydata['SUS9'].mean()
sus10 = surveydata['SUS10'].mean()

output.write("SUS Question 1 mean: " + str(sus1-1) + "\n")
output.write("SUS Question 2 mean: " + str(5-sus2) + "\n")
output.write("SUS Question 3 mean: " + str(sus3-1) + "\n")
output.write("SUS Question 4 mean: " + str(5-sus4) + "\n")
output.write("SUS Question 5 mean: " + str(round(sus5-1,2)) + "\n")
output.write("SUS Question 6 mean: " + str(5-sus6) + "\n")
output.write("SUS Question 7 mean: " + str(sus7-1) + "\n")
output.write("SUS Question 8 mean: " + str(5-sus8) + "\n")
output.write("SUS Question 9 mean: " + str(sus9-1) + "\n")
output.write("SUS Question 10 mean: " + str(5-sus10) + "\n")

positiveSUS = ["SUS1", "SUS3", "SUS5", "SUS7", "SUS9"]
negativeSUS = ["SUS2", "SUS4", "SUS6", "SUS8", "SUS10"]
output.write("\nUser Total SUS Scores: \n")
SUSscores = []

for i in range(5):
    temptotal = 0
    for x in positiveSUS:
        temptotal += surveydata[x].values[i] - 1
    for y in negativeSUS:
        temptotal += 5 - surveydata[y].values[i]
    temptotal = temptotal*2.5
    output.write("User " + str(i + 1) + ": " + str(temptotal) + "\n")
    SUSscores.append(temptotal)

scoremean = round(stat.mean(SUSscores),2)
output.write("\nMean of Final Scores: " + str(scoremean))
scoredev = round(stat.stdev(SUSscores),2)
output.write("\nStandard Deviation of Final Scores: " + str(scoredev))
## mean, standard deviation, dot plot(sus question results)

left = [1,2,3,4,5,6,7,8,9,10]
height = [sus1-1, 5-sus2, sus3-1, 5-sus4, sus5-1, 5-sus6, sus7-1, 5-sus8, sus9-1, 5-sus10]
tick_label = ["SUS1","SUS2","SUS3","SUS4","SUS5","SUS6","SUS7","SUS8","SUS9","SUS10"]
plt.bar(left, height, tick_label=tick_label, width=1, color=['dodgerblue','lime'])
plt.xlabel("Question")
plt.ylabel("Mean")
plt.title("System Usability Scale (SUS) Score Means")
plt.savefig('SUSplot.png') 


output.close()