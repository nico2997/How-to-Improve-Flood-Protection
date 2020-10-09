import matplotlib.pyplot as plt
import pandas as pd
from pip._vendor.distlib.compat import raw_input

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'


river = raw_input("Enter your river name:")
print("your river is, %s." %river)
print(river)

def name1(y):
    return y['Day']

def name2(x):
    return x['Flowrate']

def name3(y):
    return y['Riverheight']

if river == "don":
    river1 = pd.read_csv('Don data.csv')
elif river == "calder":
    river1 = pd.read_csv('Calder data.csv')
elif river == "aire":
    river1 = pd.read_csv('Aire data.csv')
elif river == "thames":
    river1 = pd.read_csv('Thames data.csv')

# aire = pd.read_csv('Aire data.csv')
# calder = pd.read_csv('Calder data.csv')
# thames = pd.read_csv('Thames data.csv')

day = name1(river1)
flow = name2(river1)
height = name3(river1)

print(day)

#CHANGE WITH EACH GRAPH
if river =="aire":
    ht = 3.9
    a = [0.156, 0.028, 0.153]
    b = [1.115, 1.462, 1.502]
    c = [30.69, 27.884, 30.127]
    lowlims = [0.2, 0.685, 1.917]
    uplims = [0.685, 1.917, 4.17]
elif river == "calder":
    a = [0.342, 0.826, -0.856]
    b = [2.239, 1.37, 2.515]
    c = [8.459, 21.5, 2.086]
    lowlims = [0, 2.107, 3.088]
    uplims = [2.107, 3.088, 5.8]
    ht = 4.5
elif river =="don":
    a = [0.223, 0.3077, 0.34, -0.5767]
    b = [1.7742, 1.3803, 1.2967, 1.1066]
    c = [78.4407, 77.2829, 79.5956, 41.3367]
    lowlims = [0, 0.52, 0.931, 1.436]
    uplims = [0.52, 0.931, 1.436, 3.58]
    ht = 2.9

def scale(x):
    return ((x-min(x))/(max(x)-min(x)))

scaledday = scale(day)
#print(scaledday)
scaledflow = scale(flow)
scaledheight = scale(height)
negday = -(scaledday)
negheight = -(scaledheight)

#Finding HM from HT
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)
print(hm)

#Finding qt and qm.
if river == "don":
    def Q(x):
        if x<=uplims[0] and x>=lowlims[0]:
            y = (c[0]*((x-a[0])**b[0]))
        elif x<=uplims[1] and x>lowlims[1]:
            y = (c[1]*((x-a[1])**b[1]))
        elif x<=uplims[2] and x>lowlims[2]:
            y = (c[2]*((x-a[2])**b[2]))
        elif x<=max(height) and x>lowlims[3]:
            y = (c[3]*((x-a[3])**b[3]))
        return(y)
else:
    def Q(x):
        if x<=uplims[0] and x>=lowlims[0]:
            y = (c[0]*((x-a[0])**b[0]))
        elif x<=uplims[1] and x>lowlims[1]:
            y = (c[1]*((x-a[1])**b[1]))
        elif x<=max(height) and x>lowlims[2]:
            y = (c[2]*((x-a[2])**b[2]))
        return(y)

qt = Q(ht)
qm = Q(hm)
print(qt ,qm)

#Rating Curve
if river == "don":
    Flow = []
    for i in height:
        if i<=uplims[0] and i>=lowlims[0]:
            Flow.append(c[0]*((i-a[0])**b[0]))
        elif i<=uplims[1] and i>lowlims[1]:
            Flow.append(c[1]*((i-a[1])**b[1]))
        elif i<=uplims[2] and i>lowlims[2]:
            Flow.append(c[2]*((i-a[2])**b[2]))
        elif i<=max(height) and i>lowlims[3]:
            Flow.append(c[3]*((i-a[3])**b[3]))
else:
    Flow = []
    for i in height:
        if i <= uplims[0] and i >= lowlims[0]:
            Flow.append(c[0] * ((i - a[0]) ** b[0]))
        elif i <= uplims[1] and i > lowlims[1]:
            Flow.append(c[1] * ((i - a[1]) ** b[1]))
        elif i <= max(height) and i > lowlims[2]:
            Flow.append(c[2] * ((i - a[2]) ** b[2]))

scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))

print(scaledFlow)
#Plot the Rating Curve using Q NOT the Flow Rate.
negheight = -scaledheight
# ax.plot(negheight,scaledFlow,'black',linewidth=2)
# ax.plot([0,-1],[0,1],'black',linestyle='--', marker='', linewidth=2)
#Originally the dotted line was wrong because it went to the positional origin
#and not the actual origin.

#Plot the Flow Rate and Height against the Date.
negday = -(scaledday)
# ax.plot(scaledday, scaledFlow, 'black', linewidth=2)
# ax.plot(negheight, negday, 'black', linewidth=2)

# if river == "don":
#     scaledht = (2.9-min(height))/(max(height)-min(height))
#     scaledhm = (4.06-min(height))/(max(height)-min(height))
#     scaledqm = (225.9-min(flow))/(max(flow)-min(flow))
#     scaledqt = (164.1-min(flow))/(max(flow)-min(flow))
# elif river == "calder":
#     scaledht = (4.5 - min(height)) / (max(height) - min(height))
#     scaledhm = (5.25 - min(height)) / (max(height) - min(height))
#     scaledqm = (197.5 - min(flow)) / (max(flow) - min(flow))
#     scaledqt = (142 - min(flow)) / (max(flow) - min(flow))
# elif river == "aire":
#     scaledht = (3.9 - min(height)) / (max(height) - min(height))
#     scaledhm = (4.77 - min(height)) / (max(height) - min(height))
#     scaledqm = (300.2 - min(flow)) / (max(flow) - min(flow))
#     scaledqt = (219.1 - min(flow)) / (max(flow) - min(flow))
# elif river == "thames":
#     scaledht = (4.8 - min(height)) / (max(height) - min(height))
#     scaledhm = (5.5 - min(height)) / (max(height) - min(height))
#     scaledqm = (350 - min(flow)) / (max(flow) - min(flow))
#     scaledqt = (300 - min(flow)) / (max(flow) - min(flow))

#Scaling ht,hm,qt and qm.
scaledht = (ht-min(height))/(max(height)-min(height))
scaledhm = (hm-min(height))/(max(height)-min(height))
scaledqt = (qt-min(Flow))/(max(Flow)-min(Flow))
scaledqm = (qm-min(Flow))/(max(Flow)-min(Flow))

print(scaledht, scaledhm, scaledqt, scaledqm)

a = ((max(height)-min(height))/(max(height)-min(height))) #1
print(a)
b = ((max(flow)-min(flow))/(max(flow)-min(flow))) #1

fig, ax = plt.subplots()

ax.plot(scaledday, scaledFlow, 'black', linewidth=2) # Q-t
ax.plot(negheight, negday, 'black', linewidth=2) # H-t
ax.plot(negheight, scaledFlow, 'black', linewidth=2) # rating curve

ax.plot([0,-1*a], [0,b], 'black', linestyle='--', marker='', linewidth=2)

ax.plot([-scaledht,-scaledht],[-1,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,-scaledhm],[-1,scaledqm], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledht,1],[scaledqt,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,1],[scaledqm,scaledqm], 'black', linestyle='--', linewidth=1)

if river == "don":
    ax.plot([1 / 8, 1 / 8, 1 / 8], [scaledqt, scaledqm, -1 / 5], 'black', linestyle='--', linewidth=1)
    ax.plot([107 / 400, 107 / 400, 107 / 400], [scaledqt, scaledqm, -1 / 5], 'black', linestyle='--', linewidth=1)
    ax.plot([1 / 8, 107 / 400], [-1 / 5, -1 / 5], 'black', linewidth=1)
    ax.plot([1 / 8, 1 / 8], [scaledqm, scaledqt], 'black', linewidth=1.5)
    ax.plot([1 / 8, 107 / 400], [scaledqm, scaledqm], 'black', linewidth=1.5)
    ax.plot([1 / 8, 107 / 400], [scaledqt, scaledqt], 'black', linewidth=1.5)
    ax.plot([107 / 400, 107 / 400], [scaledqm, scaledqt], 'black', linewidth=1.5)
#
    ticks_x = [-4481 / 4156, -3481 / 4156, -2481 / 4156, -1481 / 4156, -481 / 4156, 1 / 4, 2 / 4, 3 / 4, 1]
    # done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be positioned on the axis.
    ticks_y = [-1, -3 / 4, -2 / 4, -1 / 4, 1024 / 6249, 758 / 2083, 3524 / 6249, 4774 / 6249, 2008 / 2083, 1.164026244]
    ax.set_xticks(ticks_x)
    ax.set_yticks(ticks_y)
    Ticks_x = [5, 4, 3, 2, 1, 26, 27, 28, 29]
    Ticks_y = [29, 28, 27, 26, 50, 100, 150, 200, 250, 300]
    ax.set_xticklabels(Ticks_x)
    ax.set_yticklabels(Ticks_y)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
    ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

    ax.fill_between(scaledday, scaledFlow, scaledqt, where=scaledflow >= scaledqt, facecolor='gray')
    #
    plt.title('Don Graph')

    plt.text(-0.57, -1, '$h_t$')
    plt.text(-0.85, -1, '$h_m$')
    plt.text(1, scaledqm, '$Q_m$')
    plt.text(1, scaledqt, '$Q_t$')
    plt.text(0.3, 0.73, 'F.E.V.', size=15)
    plt.text(0.185, -0.19, '$T_f$')
    plt.text(0.12, -0.212, '<')
    plt.text(0.25, -0.212, '>')

    plt.text(0, 1.05, 'Flow $[m^3/s]$', size=10)
    plt.text(0.75, -0.13, 'Day in December', size=10)
    plt.text(-0.35, -1.09, 'Day in December', size=10)
    plt.text(-1.1, 0.02, 'Height $[m]$', size=10)

    plt.text(-0.015, 1.07, '^')
    plt.text(-0.011, -1.11, 'v')
    plt.text(1.08, -0.015, '>')
    plt.text(-1.1, -0.015, '<')

    plt.text(0.4, -0.4, '$F.E.V.≈3.00Mm^3$', size=15)
    plt.text(0.4, -0.475, '$T_f=13.50hrs$', size=15)
    plt.text(0.4, -0.55, '$h_t=2.90m$', size=15)
    plt.text(0.4, -0.625, '$h_m=4.06m$', size=15)
    plt.text(0.4, -0.7, '$Q_t=164.1m^3/s$', size=15)
    plt.text(0.4, -0.775, '$Q_m=225.9m^3/s$', size=15)

elif river == "aire":
    ax.plot([71 / 250, 71 / 250, 71 / 250], [scaledqt, scaledqm, -1 / 5], 'black', linestyle='--', linewidth=1)
    ax.plot([69 / 125, 69 / 125, 69 / 125], [scaledqt, scaledqm, -1 / 5], 'black', linestyle='--', linewidth=1)
    ax.plot([71 / 250, 69 / 125], [-1 / 5, -1 / 5], 'black', linewidth=1)
    ax.plot([71 / 250, 71 / 250], [scaledqm, scaledqt], 'black', linewidth=1.5)
    ax.plot([71 / 250, 69 / 125], [scaledqm, scaledqm], 'black', linewidth=1.5)
    ax.plot([71 / 250, 69 / 125], [scaledqt, scaledqt], 'black', linewidth=1.5)
    ax.plot([69 / 125, 69 / 125], [scaledqm, scaledqt], 'black', linewidth=1.5)

    ticks_x = [-4874 / 4091, -3874 / 4091, -2874 / 4091, -1874 / 4091, -874 / 4091, 1 / 5, 2 / 5, 3 / 5, 4 / 5, 1]
    # done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be positioned on the axis.
    ticks_y = [-1, -4 / 5, -3 / 5, -2 / 5, -1 / 5, 3 / 52, 17 / 78, 59 / 156, 7 / 13, 109 / 156, 67 / 78, 53 / 52]
    ax.set_xticks(ticks_x)
    ax.set_yticks(ticks_y)
    Ticks_x = [6, 5, 4, 3, 2, 26, 27, 28, 29, 30]
    Ticks_y = [30, 29, 28, 27, 26, 50, 100, 150, 200, 250, 300, 350]
    ax.set_xticklabels(Ticks_x)
    ax.set_yticklabels(Ticks_y)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
    ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

    ax.fill_between(scaledday, scaledflow, scaledqt, where=scaledflow >= scaledqt, facecolor='gray')

    plt.title('Aire Graph')

    plt.text(-4 / 6, -1, '$h_t$')
    plt.text(-13 / 15, -1, '$h_m$')
    plt.text(1, 187 / 210, '$Q_m$')
    plt.text(1, 87 / 140, '$Q_t$')
    plt.text(0.34, 0.70, 'F.E.V.', size=15)
    plt.text(0.4, -0.18, '$T_f$')
    plt.text(0.27, -0.213, '<')
    plt.text(0.535, -0.213, '>')

    plt.text(0, 1.05, 'Flow $[m^3/s]$', size=10)
    plt.text(0.75, -0.13, 'Day in December', size=10)
    plt.text(-0.35, -1.09, 'Day in December', size=10)
    plt.text(-1.1, 0.02, 'Height $[m]$', size=10)

    plt.text(-0.015, 1.07, '^')
    plt.text(-0.011, -1.11, 'v')
    plt.text(1.08, -0.015, '>')
    plt.text(-1.1, -0.015, '<')

    plt.text(0.4, -0.4, '$F.E.V.≈9.34Mm^3$', size=15)
    plt.text(0.4, -0.475, '$T_f=32.00hrs$', size=15)
    plt.text(0.4, -0.55, '$h_t=3.90m$', size=15)
    plt.text(0.4, -0.625, '$h_m=4.77m$', size=15)
    plt.text(0.4, -0.7, '$Q_t=219.1m^3/s$', size=15)
    plt.text(0.4, -0.775, '$Q_m=300.2m^3/s$', size=15)

elif river == "calder":
    ax.plot([67 / 200, 67 / 200, 67 / 200], [scaledqt, scaledqm, -1 / 5], 'black', linestyle='--', linewidth=1)
    ax.plot([67 / 160, 67 / 160, 67 / 160], [scaledqt, scaledqm, -1 / 5], 'black', linestyle='--', linewidth=1)
    ax.plot([67 / 200, 67 / 160], [-1 / 5, -1 / 5], 'black', linewidth=1)
    ax.plot([67 / 200, 67 / 200], [scaledqm, scaledqt], 'black', linewidth=1.5)
    ax.plot([67 / 200, 67 / 160], [scaledqm, scaledqm], 'black', linewidth=1.5)
    ax.plot([67 / 200, 67 / 160], [scaledqt, scaledqt], 'black', linewidth=1.5)
    ax.plot([67 / 160, 67 / 160], [scaledqm, scaledqt], 'black', linewidth=1.5)

    ticks_x = [-4731 / 4466, -533 / 638, -2731 / 4466, -1731 / 4466, -731 / 4466, 1 / 4, 2 / 4, 3 / 4, 1]
    # done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be positioned on the axis.
    ticks_y = [-1, -3 / 4, -2 / 4, -1 / 4, 2413 / 11593, 4643 / 11593, 7143 / 11593, 9643 / 11593, 1.047442422]
    ax.set_xticks(ticks_x)
    ax.set_yticks(ticks_y)
    Ticks_x = [6, 5, 4, 3, 2, 26, 27, 28, 29]
    Ticks_y = [29, 28, 27, 26, 50, 100, 150, 200, 250]
    ax.set_xticklabels(Ticks_x)
    ax.set_yticklabels(Ticks_y)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
    ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

    ax.fill_between(scaledday, scaledflow, scaledqt, where=scaledflow >= scaledqt, facecolor='gray')

    plt.title('Calder Graph')

    plt.text(-0.7, -1, '$h_t$')
    plt.text(-13 / 15, -1, '$h_m$')
    plt.text(1, scaledqm, '$Q_m$')
    plt.text(1, scaledqt, '$Q_t$')
    plt.text(0.45, 0.675, 'F.E.V.', size=15)
    plt.text(0.363, -0.19, '$T_f$')
    plt.text(0.331, -0.212, '<')
    plt.text(0.4, -0.212, '>')

    plt.text(0, 1.05, 'Flow $[m^3/s]$', size=10)
    plt.text(0.75, -0.13, 'Day in December', size=10)
    plt.text(-0.35, -1.09, 'Day in December', size=10)
    plt.text(-1.1, 0.02, 'Height $[m]$', size=10)

    plt.text(-0.015, 1.07, '^')
    plt.text(-0.011, -1.11, 'v')
    plt.text(1.08, -0.015, '>')
    plt.text(-1.1, -0.015, '<')

    plt.text(0.4, -0.4, '$F.E.V.≈1.65Mm^3$', size=15)
    plt.text(0.4, -0.475, '$T_f=8.25hrs$', size=15)
    plt.text(0.4, -0.55, '$h_t=4.5m$', size=15)
    plt.text(0.4, -0.625, '$h_m=5.25m$', size=15)
    plt.text(0.4, -0.7, '$Q_t=142.0m^3/s$', size=15)
    plt.text(0.4, -0.775, '$Q_m=197.5m^3/s$', size=15)

elif river == "thames":
    ax.plot([111 / 200, 111 / 200, 111 / 200], [scaledqt, scaledqm, -1 / 5], 'black', linestyle='--', linewidth=1)
    ax.plot([127 / 160, 127 / 160, 127 / 160], [scaledqt, scaledqm, -1 / 5], 'black', linestyle='--', linewidth=1)
    ax.plot([111 / 200, 127 / 160], [-1 / 5, -1 / 5], 'black', linewidth=1)
    ax.plot([111 / 200, 111 / 200], [scaledqm, scaledqt], 'black', linewidth=1.5)
    ax.plot([111 / 200, 127 / 160], [scaledqm, scaledqm], 'black', linewidth=1.5)
    ax.plot([111 / 200, 127 / 160], [scaledqt, scaledqt], 'black', linewidth=1.5)
    ax.plot([125 / 160, 127 / 160], [scaledqm, scaledqt], 'black', linewidth=1.5)

    ticks_x = [-1, -0.8, -0.6, -0.4, -0.2, 0, 1 / 3, 2 / 3, 1]
    # done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be positioned on the axis.
    ticks_y = [-1, -2/3, -1/3, 0.03,0.19,0.35,0.51,0.67,0.83,1]

    ax.set_xticks(ticks_x)
    ax.set_yticks(ticks_y)
    Ticks_x = [5.5, 5, 4.5, 4, 3.5, 16, 29, 10, 23]
    Ticks_y = [23, 10, 29, 50, 100, 150, 200, 250, 300, 350]
    ax.set_xticklabels(Ticks_x)
    ax.set_yticklabels(Ticks_y)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
    ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

    ax.fill_between(scaledday, scaledflow, scaledqt, where=scaledflow >= scaledqt, facecolor='gray')

    plt.title('Thames Graph')

    plt.text(-0.68, -1.05, '$h_t$')
    plt.text(-15 / 15, -1.05, '$h_m$')
    plt.text(1, scaledqm, '$Q_m$')
    plt.text(1, scaledqt, '$Q_t$')
    plt.text(0.6, 0.74, 'F.E.V.', size=15)
    plt.text(0.65, -0.19, '$T_f$')
    plt.text(0.54, -0.215, '<')
    plt.text(0.79, -0.215, '>')

    plt.text(0.02, 1.05, 'Flow $[m^3/s]$', size=10)
    plt.text(1, -0.19, 'Day in December', size=10)
    plt.text(-0.23, -1.15, 'Day in December', size=10)
    plt.text(-1.2, 0.04, 'Height $[m]$', size=10)

    plt.text(-0.0095, 1.07, '^')
    plt.text(-0.0095, -1.125, 'v')
    plt.text(1.09, -0.015, '>')
    plt.text(-1.12, -0.015, '<')

    plt.text(0.4, -0.4, '$F.E.V.≈28.00Mm^3$', size=15)
    plt.text(0.4, -0.475, '$T_f=229.75hrs$', size=15)
    plt.text(0.4, -0.55, '$h_t=4.8m$', size=15)
    plt.text(0.4, -0.625, '$h_m=5.5m$', size=15)
    plt.text(0.4, -0.7, '$Q_t=300m^3/s$', size=15)
    plt.text(0.4, -0.775, '$Q_m=350m^3/s$', size=15)

plt.show()