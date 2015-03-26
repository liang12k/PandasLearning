import pandas

"""
DataFrame loading csv
 - olympicmedals.csv
"""

medals = pandas.read_csv("olympicmedals.csv")
print medals # [29216 rows x 10 columns]

# print medals.head()
# print medals.tails()

# print medals.NOC.value_counts() # Length: 138, dtype: int64

print medals.Sport.value_counts() # 
"""
Aquatics             3828
Athletics            3448
Rowing               2523
Gymnastics           2214
Fencing              1547
Football             1387
Hockey               1325
Wrestling            1140
Shooting             1105
Sailing              1061
Cycling              1025
Canoe / Kayak        1002
Basketball            940
Volleyball            910
Equestrian            894
Handball              886
Boxing                842
Weightlifting         548
Judo                  435
Baseball              335
Archery               305
Tennis                272
Rugby                 192
Softball              180
Modern Pentathlon     174
Badminton             120
Table Tennis          120
Tug of War             94
Taekwondo              80
Polo                   66
Lacrosse               59
Golf                   30
Skating                27
Ice Hockey             27
Cricket                24
Triathlon              18
Rackets                10
Croquet                 8
Water Motorsports       5
Basque Pelota           4
Roque                   3
Jeu de paume            3
dtype: int64
"""
