import operator
import itertools
import sys

def main(desired_number):
    f = open('condensed_files.txt','r')
    s = f.readlines()
    metrics_per_study = [x.replace('\t',';').replace('\n','').replace(' ','_').replace('#','').lower().split(';')
          for x in s if not (x.startswith('==>' ) or x.startswith('\n' ))]

    def get_all(x):
        for i in x:
            for j in i:
                yield(j)
                
    x = [j for j in get_all(metrics_per_study)]

    wordcount={}
    for word in x:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
                

    best_words = sorted(wordcount.items(), key=operator.itemgetter(1),reverse=True)[0:25]


    def get_best_combo(n):
        n_word_combos = list(itertools.combinations(range(len(best_words)), n))
        words_frequencies={}
        
        for i in n_word_combos:
            words = []
            for k in range (n):
                words.append(best_words[i[k]][0])
            word_string = ''
            for l in words:
                word_string += l
                word_string += '    '
            word_string=word_string.rstrip("    ")
            for j in metrics_per_study:
                if set(words).issubset(set(j)):
                    if word_string in words_frequencies:
                        words_frequencies[word_string] += 1
                    else:
                        words_frequencies[word_string] =1
        for key, value in words_frequencies.items():
            words_frequencies[key] = round(value / len(metrics_per_study),2)

        sorted_combo_frequencies = sorted(words_frequencies.items(), key=operator.itemgetter(1),reverse=True)
        return sorted_combo_frequencies



    # just call this to see how often a combination of attribute names appear in studies
    # eg in this case
    print("\n\n\n\n\n")
    print("This is a dictionary where:")
    print("-Key is the combination of attributes")
    print("-Value is the frequency of that combination of attributes in attributes of medical studies data")
    print()
    j = 0
    for i in get_best_combo(int(desired_number)):
        if (j < 20):
            j+=1
            print(i)


if __name__ == "__main__":
    main(sys.argv[1])
