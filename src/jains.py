import sys
# using math might be a mistake here, code might break with really large values.
import math

def JFI(throughputs):
    '''
    takes in input of list of throughputs and returns their calculated JFI
    '''
    top = math.pow(sum(throughputs),2)
    bot = len(throughputs) * sum([math.pow(x,2) for x in throughputs])
    return top / bot

def converts_throughput_value_to_number(line):
    '''
    Takes in the line in throughtputs_values.txt
    It splits line, and converts the prefix in to an actual number.
    Then it returns the first number times the prefix.
    '''
    # Hashmap of prefixes, so G = billion, M = a million, K = a thousand
    prefix = {"G": math.pow(10, 9), "M" : math.pow(10,6), "K" : math.pow(10,3)}
    tmp = line.split(" ")
    
    # converts the 7 in for example 7 Mbits into just 7
    first_num = int(tmp[0])
    
    # converts the M in fir example 7 Mbits into a number, in this case a million.
    prefix = prefix[tmp[1][0]]

    # in this case does 7 * a million so we retun 7 million which is equal to 7 Mbits.
    return first_num * prefix


if __name__ == "__main__":
    #if user has not asked for a file
    if len(sys.argv) == 2 and ".txt" not in sys.argv[1]:
        try:
            throughputs = [int(x) for x in sys.argv[1].strip('[]').split(',')]
            print("Jains Fairness index is: "+ str(JFI(throughputs)))
        except:
            print("There was a problem.\nUsage: python3 jains.py [10,10,10] // prints 1") 
    
    #if user has asked for a file
    elif len(sys.argv) == 2 and ".txt" in sys.argv[1]:
        try:
            
            with open(sys.argv[1], "r") as f:
                file = f.read().split("\n")
                throughputs = []

                for line in file:
                    throughput_calculated = converts_throughput_value_to_number(line)
                    throughputs.append(throughput_calculated) 

                print(f"Jains Fairness index of {sys.argv[1]} is: {JFI(throughputs)}")

        except:
            print("Could not find file.")
    
    #if user forgot to do either
    else:
        print("There was an error.\nUsage: python3 jains.py [10,10,10] // prints 1")
