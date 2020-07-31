import unicodedata
from pickle import dump, load
from collections import Counter

def load_doc(filename):
    with open(filename, 'r', encoding='utf8') as f:
        text = f.read()
    return text

# pretty hacky and punctuation is totally ignored
def clean_doc(doc):
    doc = unicodedata.normalize('NFKD', doc).encode('ascii','ignore').decode('utf-8','ignore')
    doc = doc.lower().replace('--', ' ').replace('!','.').replace('...','.').replace('?','.').replace(':','.').replace("'",'').replace('mr.','mr').replace('mrs.','mrs').replace(' s ','s ')
    duds = ['(',')','*',',','-','>','\\','[',']']
    for d in duds:
        doc = doc.replace(d, ' ')
    doc = doc.replace('  ',' ')
    doc = doc.replace('. ', ' endofsentence ')
    # split into tokens by white space
    tokens = doc.split()
    tokens = [word for word in tokens if word.isalpha()]
    return tokens

def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()

def convert_to_sequences():
    print('importing books')
    all_text = ''
    for i in range(7):
        temp = load_doc('texts/book'+str(i+1)+'.txt')
        all_text += temp

    print('cleaning text')
    tokens = clean_doc(all_text)

    # replace words that occur infrequently
    print('removing infrequent words')
    temp = Counter(tokens)
    infreq_words = [x for x in temp if temp[x] <= 5]

    out_tokens = []
    for t in tokens:
        if t in infreq_words:
            out_tokens.append('unknownword')
        else:
            out_tokens.append(t)

    tokens = out_tokens

    length = 50 + 1
    sequences = list()
    for i in range(length, len(tokens)):
        seq = tokens[i-length:i]
        line = ' '.join(seq)
        sequences.append(line)

    print('saving sequences to file')
    save_doc(sequences, 'texts/hp_sequences.txt')

if __name__ == '__main__':
    convert_to_sequences()
