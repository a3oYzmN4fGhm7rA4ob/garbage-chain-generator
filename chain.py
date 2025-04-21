import collections, random, textwrap, argparse


# Parse arguments from user on command line interface
def parse_args():
    parser = argparse.ArgumentParser(description='Generate nonsense text based on in input text file.', usage='chain.py -file [YOUR_FILE_NAME_HERE].txt -length [INTEGER_HERE]')
    parser.add_argument('-file', required=True, help='The name of the .txt file input. Place it in the same directory as the script, or provide a path.')
    parser.add_argument('-length', required=True, help='The length (in words) of the string to output, as in integer.')
    args = parser.parse_args()
    return args

# Run the program
def main():
    args = parse_args()
    path = str(args.file)
    with open(path, 'r') as gorp:
        content = str(gorp.read())

    word_1 = word_2 = ''
    ops = collections.defaultdict(list)
    for line in content:
        for thing in content.split():
            ops[word_1, word_2].append(thing)
            word_1, word_2 = word_2, thing

    ops[word_1, word_2].append('')
    ops[word_2, ''].append('')

    word_1, word_2 = random.choice([k for k in ops if k[0][:1].isupper()])
    output = [word_1, word_2]
    for _ in range(int(args.length)):
        thing = random.choice(ops[word_1, word_2])
        output.append(thing)
        word_1, word_2 = word_2, thing
    print(textwrap.fill(' '.join(output)))

print("-| a3's garbage text chain generator |- \n please wait, this may take a moment based on the size of the file\n")
main()