# garbage-chain-generator
A simple generator for making nonsense text based on an input .txt file.
Not much to say here.

## Requirements
Python 3.12.3 or greater.

Note: Don't input absolutely massive text files, this might cause issues.

## How do I use this?
Run the script, providing command line arguments as needed. 
You can run it with the -h flag to get a list of required args if you forget them.

### Arguments
```
-file [YOUR_FILE_NAME_OR_PATH_HERE]
```
*Input name or path of the text file for the script to use.*

```
-length [INTEGER]
```
*The length (in words) of the string to output, as in integer.*

### What kind of text should I use?
Generally anything that has words should ideally work. 
So, a file of random values would not work, but the entirety of the bee movie script would.

A few sample text files are included with this repo, if you desire to use them for the program. (or are too lazy to find your own, which is fair)

*Provided files:*

**sample_patchnotes.txt** A sample of recent patch notes from *ULTRAKILL*.

**sample_cave.txt** Select Cave Johnson transcribed dialouge from *Portal 2*.

**sample_ultrapoems.txt** Select short poems from *ULTRAKILL.*

**sample_missile.txt** "The missile knowsh where it is" copypasta.

## How do I install this?
Clone this repository via your desired method.

*Example:*
```
git clone https://github.com/a3oYzmN4fGhm7rA4ob/garbage-chain-generator
```
Move via your preferred method to the repository folder.

*Example:*
```
cd garbage-chain-generator
```
Run the script, again via your preferred method. See the section on usage for more details on the specifics.

*Example*
```
python3 chain.py -file sample_patchnotes -length 100
```
