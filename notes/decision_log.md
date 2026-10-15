# Sector Slection

## Decision:
Use the sector categories provided by the "Ministry for Primary Industries":
- Dairy
- Meat & wool
- Horticulture
- Forestry
- Seafood
- Arable
- Processed food and other products


## Reason:
I could not find a reliable external definition of which sectors should be considered "major".  
Therefore, I decided to keep the official MPI sector categories unchanged rather than creating my own classification.  


## Possible Limitation:
"Processed food and other priducts" may represent a broader category than the other sectors.


## Inspection before cleaning:
Missing values were found in the raw worksheet, but they occurred outside the data required for this analysis.  
No missing values were identified in the selected 2016-2025 sector export data.  

The first column -> 7 missing values  
Other columns -> 16 missing values  


## Dara cleaning:
Try to reshape a DataFrame and create an analysis-friendly format.  
An analysis-friendly format is a structure that makes it easy for landas to filter, group, calculate, and plot the data.  

sector              year    export_value
Dairy               2016       13289
Dairy               2017       14638
Dairy               2018       16655
...
Meat & wool         2016        9207
Meat & wool         2017        8361
...  
-> This is the better format.