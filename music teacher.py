'''A music teacher has developed a new technique to teach the students in which each 
unique node is identified by a lower character of english alphabet. In total there are
 26 nodes in this technique from 'a' to 'z'. To teach a new song the music teacher first 
 converts the song to string consisting of a to z then breaks it into melodies. 
 A melody is a collection of nodes in which the frequency of each node present in that
   melody is same. He strictly teaches one melody in one day. You are given the song 
   string and your task is to find and return the minimum number of days in which he
     can teach the whole song. input specification:input1: A string representing the 
     song string. for example if input1: abbaabed then output:2 and if the input: abcd 
     then output: 1 '''



from math import gcd
from functools import reduce
from collections import Counter

def min_days_to_teach(song):
    unique_nodes = set(song)
    frequencies = {node: song.count(node) for node in unique_nodes}
    days_required = len(set(frequencies.values()))

    return days_required

# Example usage:
input_str = "abbaabed"
output = min_days_to_teach(input_str)
print(output)  # Output: 2

input_str = "abcd"
output = min_days_to_teach(input_str)
print(output)  # Output: 1
