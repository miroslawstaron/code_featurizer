#!/usr/bin/env python3
"""
Example demonstrating how to use the code featurizer on a Python calculator program.

This script shows:
1. How to load code from a CSV file
2. How to find features using the featurizer
3. How to generate feature vectors for each line of code
4. How to save the results to a CSV file

Author: Code Featurizer Example
"""

import re
import pandas as pd
import time
from collections import Counter

# ===== Classes from the featurizer =====

class FeatureMaker:
    """Class makes a feature vector based on the set of features defined in the class parameters"""

    def __init__(self):
        """The initial state of the feature vector is actually an empty vector"""
        self.featureVector = []

    def addNewFeature(self, newFeature):
        """Adds just one feature to the list of features"""
        self.featureVector.append(newFeature)

    def addNewFeatures(self, newFeatures):
        """Adds a list of features"""
        self.featureVector = self.featureVector + newFeatures
    
    def getFeatureVector(self):
        return self.featureVector

    def featurize(self, line):
        """Counts the frequency of each feature in a given line"""
        self.features = []
        for feature in self.featureVector:
            self.features.append(str(line.count(feature)))
        return self.features
    
    def featurize2(self, line):
        """Counts the frequency of each feature in a given line"""
        self.features = []
        counter = Counter(line)
        for feature in self.featureVector:
            self.features.append(str(counter[feature]))
        return self.features
    
    def featurize3(self, line):
        """Counts the frequency of each feature in a given line"""
        self.features = []
        for feature in self.featureVector:
            self.features.append(str(len(re.findall(str(feature), line))))
        return self.features
    
    def featuresToString(self):
        strFeatures = '$'.join(str(e) for e in self.features)
        return strFeatures
    
    def findNewFeatures(self, lstTokens):
        newElements = list(set(lstTokens) - set(self.featureVector))
        return newElements

def tokenizeString(myString):
    """This function takes a line and returns a set of strings; empty strings are removed"""
    tokenList = '[\\(|"|,|.|;|\\)|\\[|\\]|{|}| ,|\\n|\\t:]'
    tokens = re.split(tokenList, myString)
    tokens = list(filter(None, tokens))
    return tokens

class DataSet:
    """The class makes the connection between the code and its features"""

    def __init__(self):
        self.dictRows = {}
        self.featureVector = []
    
    def addFeatureVector(self, lstFeatureVector):
        self.featureVector = lstFeatureVector

    def addNewLine(self, strLine, lstFeatures):
        self.dictRows[lstFeatures] = strLine 

    def hasLine(self, lstFeatures):
        return (lstFeatures in self.dictRows.keys())
            
    def getLine(self, lstFeatures):
        return self.dictRows[lstFeatures]

    def toCSV(self, strFilename):
        fFile = open(strFilename, 'w', encoding='utf8')
        strFirstLine = 'line$'
        strFirstLine += '$'.join(self.featureVector) + '\n'
        fFile.write(strFirstLine)
        for key, value in self.dictRows.items():
            value = value.replace("\n", "").replace("$","").replace("\r","").replace("\t","")
            strToFile = f'{value}${key}\n'
            fFile.write(strToFile)
        fFile.close()
    
    def flush(self):
        self.dictRows = {}
        self.featureVector = []

# ===== Main featurizer functions =====

def findFeatureListIterative(lstLines, strOutputFeatureFile):
    """
    Recursively finds a minimal set of features that can distinguish all lines.
    
    Args:
        lstLines: List of code lines to analyze
        strOutputFeatureFile: File to save the feature list to
    
    Returns:
        List of features found
    """
    start_time = time.time()
    
    featurizer = FeatureMaker()
    featureList = []

    if len(lstLines) > 0:
        initialFeatures = tokenizeString(' '.join(lstLines))
        featurizer.addNewFeature(initialFeatures[0])
        featureList.append(initialFeatures[0])
    else:
        return featureList

    featureAdded = True

    while featureAdded:
        dictLinesUnique = {}
        lstNotUnique = []
        featureAdded = False

        # featurizing all lines in this iteration
        for line in lstLines:
            mFeatures = featurizer.featurize(line)
            strFeatures = '$'.join(mFeatures)
            if not (strFeatures in dictLinesUnique.keys()):
                dictLinesUnique[strFeatures] = line
            else:
                lstNotUnique.append(line)
                lstNotUnique.append(dictLinesUnique[strFeatures])
        
        lstNotUnique = list(set(lstNotUnique))
        strTime = f'{(time.time() - start_time):.2f} sec.'
        start_time = time.time()
        print(f'Non-unique lines remaining: {len(lstNotUnique)}, features found: {len(featureList)} in {strTime}')
        
        # Save features periodically
        if len(featureList) % 10 == 0:
            print('Saving feature list...')
            fFile = open(strOutputFeatureFile, 'w', encoding='utf8')
            strFirstLine = '$'.join(featureList) + '\n'
            fFile.write(strFirstLine)
            fFile.close()
            print('Done...')

        # Continue if there are non-unique lines
        if len(lstNotUnique) > 0:
            allLines = lstNotUnique
            getTokens = tokenizeString(' '.join(allLines))
            for oneToken in getTokens:
                if not oneToken in featureList:                    
                    featureList.append(oneToken)
                    featurizer.addNewFeature(oneToken)
                    featureAdded = True
                    break
            if featureAdded:
                lstLines = lstNotUnique
        
    return featureList

def featurizeListPredefined(lstLines, lstFeatures):
    """
    Featurizes lines using a predefined list of features.
    
    Args:
        lstLines: List of code lines to featurize
        lstFeatures: Predefined list of features to use
    
    Returns:
        DataSet object containing the featurized lines
    """
    dtLines = DataSet()
    
    featurizer = FeatureMaker()
    featurizer.addNewFeatures(lstFeatures)

    foundNewFeature = True
    i = 1
    while foundNewFeature:
        foundNewFeature = False
        print(f'Pass number: {i}')
        i += 1
        iLine = 0
        total = len(lstLines)
        for line in lstLines:
            iLine += 1
            if not foundNewFeature: 
                mFeatures = featurizer.featurize(line)  
                if not all(v == '0' for v in mFeatures):    
                    strFeatures = featurizer.featuresToString()
                    if not dtLines.hasLine(strFeatures):
                        dtLines.addNewLine(line, strFeatures)
                    else:
                        strLine = dtLines.getLine(strFeatures)
                        if strLine != line:
                            lineTokens = tokenizeString(line)
                            oldLineTokens = tokenizeString(strLine)
                            newFeatures = featurizer.findNewFeatures(lineTokens+oldLineTokens)
                            if len(newFeatures) > 0:
                                featurizer.addNewFeature(newFeatures[0])
                                foundNewFeature = True
                                dtLines.flush()
                                dtLines.addFeatureVector(featurizer.featureVector)
                                print(f'Found new feature at line {iLine} of {total}')                           

    return dtLines

# ===== Example Usage =====

def main():
    """Main function demonstrating the featurizer usage"""
    
    print("=" * 60)
    print("Code Featurizer Example - Python Calculator")
    print("=" * 60)
    print()
    
    # Step 1: Load the code from CSV
    print("Step 1: Loading code from CSV file...")
    dfCode = pd.read_csv('./example_calculator.csv', 
                        sep='$', 
                        on_bad_lines='skip',
                        header=0, 
                        index_col=False,
                        engine='python')
    
    mLines = [line for line in dfCode['code_content'] if str(line) != 'nan']
    print(f'Total lines loaded: {len(mLines)}')
    
    # Remove duplicate lines to speed up processing
    mLines = list(set(mLines))
    print(f'Unique lines: {len(mLines)}')
    print()
    
    # Step 2: Find features
    print("Step 2: Finding optimal feature set...")
    print("This may take a moment for larger codebases...")
    print()
    features = findFeatureListIterative(mLines, './feature_list_calculator.csv')
    print()
    print(f"Total features found: {len(features)}")
    print(f"Features: {features[:10]}..." if len(features) > 10 else f"Features: {features}")
    print()
    
    # Step 3: Featurize all lines using the found features
    print("Step 3: Generating feature vectors for all lines...")
    dtLines = featurizeListPredefined(mLines, features)
    dtLines.addFeatureVector(features)
    
    # Step 4: Save results to CSV
    output_file = './output_example_calculator.csv'
    print(f"Step 4: Saving results to {output_file}...")
    dtLines.toCSV(output_file)
    
    print()
    print("=" * 60)
    print("Featurization complete!")
    print(f"Output saved to: {output_file}")
    print("=" * 60)
    print()
    print("The output CSV contains:")
    print("- First column: original line of code")
    print("- Remaining columns: frequency of each feature in that line")
    print()

if __name__ == "__main__":
    main()
