# garbage-chain-generator
A simple generator for making nonsense text based on an input .txt file.
Not much to say here.

## Requirements:
Python 3.12.3 or greater.

## How do I use this?
Run the script, providing command line arguments as needed. 
You can run it with the -h flag to get a list of required args if you forget them.

### Arguments
```
-file
```
*Input name or path of the text file for the script to use.*

```
-length
```
*The length (in words) of the string to output, as in integer.*

### What kind of text should I use?
Generally anything that has words should ideally work. 
So, a file of random values would not work, but the entirety of the bee movie script would.

A few sample text files are included with this repo, if you desire to use them for the program. (or are too lazy to find your own, which is fair)

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
