import csv
import pandas as pd

top50ResultsDict = {
    'top50Results': {'diogo e ricardo e diogo': ['4D', '7H', '9J', '10K', '8I', '1A', '5F', '2B', '6G'],
                     'madureira palavra': ['10K', '3C', '8I', '4D', '1A', '5F', '7H', '9J', '6G']},
    'top20Results': {'diogo e ricardo e diogo': ['4D', '7H', '9J', '10K', '8I'],
                     'madureira palavra': ['10K', '3C', '8I', '4D', '1A']},
    'top10Results': {'diogo e ricardo e diogo': ['4D', '7H'],
                     'madureira palavra': ['10K', '3C']}}

arrDict = {}

with open('queries.relevance.txt', 'r') as csvfile:
    csvReader = csv.reader(csvfile, delimiter='\t')
    for row in csvReader:
        if not (row):
            continue
        else:
            if row[0].startswith("Q:"):
                key = row[0]
                newKey = str(key.replace('Q:', ''))
                arrDict.update({newKey: {}})
            else:
                arrDict[newKey].update({row[0]: row[1]})

print("arrDict ->", arrDict, "\n")

metricsDict = {}

def metrics():

    for key, value in arrDict.items():
        print(key)
        tp = 0
        fp = 0
        for a, b in top50ResultsDict.items():
            print("a->", a, "b->", b)
            if key in b.keys():
                for x in b[key]:
                    if x in arrDict[key].keys():
                        #print(x, "in", arrDict[key].keys())
                        tp += 1
                    else:
                        #print(x, "not in", arrDict[key].keys())
                        fp += 1

            fn = len(x) - fp

            precision = round(tp/(tp + fp), 3)
            recall = round(tp/(tp + fn), 3)
            fMeasure = round(
                ((2 * recall * precision)/(recall + precision)), 3)

            arrayMeasures = {}
            arrayMeasures.update({"precision": precision})
            arrayMeasures.update({"recall": recall})
            arrayMeasures.update({"fMeasure": fMeasure})

            if key not in metricsDict:
                metricsDict.update({key: {a: arrayMeasures}})
            else:
                if a not in metricsDict[key]:
                    metricsDict[key].update({a: arrayMeasures})


metrics()

print("\n\n")
#print(metricsDict)

df = pd.DataFrame(metricsDict).T
df.fillna(0, inplace=True)
print(df)

with open('testeFinal.txt', 'a') as f:
    dfAsString = df.to_string(header=True, index=True)
    f.write(dfAsString)