Question 1: The count of the operating systems used to visit the site and the percentage of the total

Operating System Count:
 operating_systems
Windows     6596
MACOS       2676
Android     2584
iOS          385
ChromeOS      62
Ubuntu         9
Other          7
Name: count, dtype: int64

Operating System Percentage:
 operating_systems
Windows     53.543307
MACOS       21.722542
Android     20.975729
iOS          3.125254
ChromeOS     0.503288
Ubuntu       0.073058
Other        0.056823
Name: count, dtype: float64

Question 2: The amount of users visiting the site using mobile operating system and desktop operating systems.
Device Type Count:
 device_type
Desktop    9361
Mobile     2969
Name: count, dtype: int64

Device Type Percentage:
 device_type
Desktop    75.920519
Mobile     24.079481
Name: proportion, dtype: float64

Question 3: The most commonly used browsers and their breakdown on mobile versus desktop

operating_systems  Android  ChromeOS  MACOS  Other  Ubuntu  Windows  iOS
browser                                                                 
Android                116         0      1      0       0        4    0
Google Chrome         2437        17    254      0       1     4878  124
Internet Explorer       10         0      2      0       0      140    4
Microsoft Edge           5         3      6      0       0      557   11
Mozilla Firefox          5         0      0      1       0      816    8
Opera                    0         0      1      0       0      129    6
QQ                       7         0      0      0       0       45    1
Safari                   0         3   2269      6       8       15  225
Samsung Internet         0         0    139      0       0        0    6
Sogou Explorer           1        39      0      0       0        7    0
UC Browser               1         0      0      0       0        1    0
Undetermined             0         0      2      0       0        0    0
Yandex                   2         0      2      0       0        4    0

Google Chrome is used across various operating systems, with the highest count of users on Windows and Android.
Safari is predominantly used on MACOS and iOS.
Android is most frequently used with the Android browser.
Internet Explorer, Microsoft Edge, and other browsers show smaller counts across the various operating systems.

Based on this analysis of what are the most popular operating system, are there any regions where there is a discrepancy in what is popular? This could be an indication that users in that region are having technical issues that the tech team might want to investigate.

To answer this last question, we need to analyse the data to identify any discrepancies in operating system usage across regions. The idea is to compare the most popular operating systems by region, which could highlight areas where there may be a technical issue or unusual trends.

operating_systems  Android  ChromeOS  MACOS  Other  Ubuntu  Windows  iOS
region                                                                  
Africa                 131         1     99      0       1      514   23
Asia                   255         3    261      1       0      586   34
Eastern Europe         280         3    209      2       0      623   37
North America          925         9   1159      3       7     2598  162
Northern Africa         53        40     91      1       0      306    8
Oceania                 51         3     31      0       0      182    9
South America          221         0    182      0       0      476   34
Southern Africa        140         0     94      0       0      183    6
Western Europe         528         3    550      0       1     1128   72

Observations:
Android Usage:
North America: 925 users (Highest count in any region)
Western Europe: 528 users
Eastern Europe: 280 users
Asia: 255 users
Africa: 131 users
Southern Africa: 140 users
South America: 221 users
Oceania: 51 users
Northern Africa: 53 users
Conclusion: Android is widely used in many regions but is particularly prominent in North America, western Europe, Eastern Europe, and Asia. The higher count in North America could be due to more widespread mobile usage.
ChromeOS Usage:
Northern Africa: 40 users (Highest for ChromeOS)
Eastern Europe: 3 users
Asia: 3 users
North America: 9 users
Africa: 1 user
Oceania: 3 users
South America: 0 users
Southern Africa: 0 users
Western Europe: 3 users
Conclusion: Northern Africa shows a relatively high use of ChromeOS compared to other regions. This could indicate that ChromeOS is being used in that region more than expected, which might suggest limited access to other operating systems or different usage patterns.
Windows Usage:
North America: 2598 users (Dominant in this region)
Western Europe: 1128 users
Eastern Europe: 623 users
Asia: 586 users
Africa: 514 users
Southern Africa: 183 users
South America: 476 users
Oceania: 182 users
Northern Africa: 306 users
Conclusion: Windows is the most popular operating system in regions like North America, Western Europe, and Eastern Europe, confirming its strong presence in developed markets.
MACOS Usage:
North America: 1159 users (Dominant in this region)
Western Europe: 550 users
Eastern Europe: 209 users
South America: 182 users
Africa: 99 users
Southern Africa: 94 users
Asia: 261 users
Northern Africa: 91 users
Oceania: 31 users
Conclusion: MACOS is most commonly used in North America, followed by Western Europe and Eastern Europe, confirming its popularity in tech-savvy and affluent regions.
iOS Usage:
North America: 162 users (Highest count)
Western Europe: 72 users
South America: 34 users
Asia: 34 users
Eastern Europe: 37 users
Africa: 23 users
Oceania: 9 users
Northern Africa: 8 users
Southern Africa: 6 users
Conclusion: iOS is most frequently used in North America, with other regions like Western Europe and South America showing moderate usage.
Potential Issues and Regional Discrepancies:
Northern Africa: The notably high use of ChromeOS (40 users) compared to other regions (with other regions having 1-9 users) is unusual and could indicate a specific trend or limitation in accessing other operating systems. This might be due to limited access to hardware or specific regional preferences.
Africa and Oceania: Both regions show relatively low use of MACOS and Windows, which might suggest limitations in accessing these operating systems due to economic or infrastructure constraints. Android and iOS are more common in these regions, likely because of mobile-first usage patterns.
Southern Africa: This region shows relatively lower usage across most operating systems, indicating potential barriers to access or fewer users with the necessary technical setup.
Actionable Insights:
The tech team should investigate why ChromeOS has a higher presence in Northern Africa.
Africa, Oceania, and Southern Africa could benefit from a technical assessment of mobile versus desktop accessibility and whether there are any infrastructure challenges limiting access to operating systems like Windows or MACOS.