import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--input_file')
parser.add_argument('--out_path')
parser.add_argument('--pos', action='store_true')
args = parser.parse_args()

f = open(args.input_file).read()

lines = []
tags = []
for line in f.split('\n\n'):
    l = line.strip().split('\n')
    if len(l[0])==0:
        continue
    if args.pos:
        a = " ".join(i.split('\t')[0] for i in l)
        b = " ".join(i.split('\t')[2] for i in l)
        s = a+'\t'+b
        lines.append(s)
        t = [i.split('\t')[2] for i in l]
        for i in t:
            if i not in tags:
                tags.append(i)    
    else:    
        a = " ".join(i.split('\t')[0] for i in l)
        b = " ".join(i.split('\t')[1] for i in l)
        s = a+'\t'+b
        lines.append(s)
        t = [i.split('\t')[1] for i in l]
        for i in t:
            if i not in tags:
                tags.append(i)
    

tags = list(set(tags))

with open('{}.tsv'.format(args.out_path), 'w') as f:
    for line in lines:
        f.write('{}\n'.format(line))

with open('{}_tags.txt'.format(args.out_path), 'w') as f:
    for tag in tags:
        f.write('{}\n'.format(tag))

rand_lines = [random.choice(lines) for i in range(50)]

with open('{}_rand50.tsv'.format(args.out_path), 'w') as f:
    for line in rand_lines:
        f.write('{}\n'.format(line))

