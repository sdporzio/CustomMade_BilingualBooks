import spacy
import numpy as np

def RemoveLines(text):
    text = text.replace('\n\n\n\n\n\n\n','\n\n')
    text = text.replace('\n\n\n\n\n\n','\n\n')
    text = text.replace('\n\n\n\n\n','\n\n')
    text = text.replace('\n\n\n\n','\n\n')
    text = text.replace('\n\n\n','\n\n')
    return text

def RebinPhrases(nlp,par,maxC=200):
    '''
    Rebin sentences in a paragraph, so that a group of sentences is not larger than maxC characters
    '''
    iGroup, temp_iGroup, lenGroup = [], [], []   

    # Divide the paragraph in sentences
    sents = nlp(par).sents
    sents = [s.string.strip() for s in sents]
    # Get the number of characters in each sentence
    lens = [len(s) for s in sents]
    # Keep adding to a bin until maxC lenght is reached
    count = 0
    i = 0
    for i in range(len(lens)):
        temp_count = count+lens[i]
        if temp_count<maxC:
            count += lens[i]
            temp_iGroup.append(i)
        else:
            temp_iGroup.append(i)
            iGroup.append(temp_iGroup)
            lenGroup.append(count)
            count = 0
            temp_iGroup = []
            count += lens[i]
            temp_iGroup.append(i)
    temp_iGroup.append(i+1)
    iGroup.append(temp_iGroup)
    lenGroup.append(count)
    # Bin the group of sentences together
    pars = []
    for i in range(len(iGroup)):
        start = iGroup[i][0]
        end = iGroup[i][-1]
        pars.append(sents[start:end])
    # Merge the sentences in each group
    new_pars = []
    for p in pars:
        new_pars.append(' '.join(p))        
    return new_pars


def GetDivisions(new_pars,div):
    maxL = len(new_pars)
    t = np.arange(0,maxL,div)
    s = [c for c in t]
    s.append(maxL)

    nr = []
    for i in range(len(s)-1):
        nr.append([s[i],s[i+1]])
    return nr