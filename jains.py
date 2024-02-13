import sys
import math

def JFI(throughputs):
    top = math.pow(sum(throughputs),2)
    bot = len(throughputs) * sum([math.pow(x,2) for x in throughputs])
    return top / bot

if __name__ == "__main__":
    if len(sys.argv) == 2 and ".txt" not in sys.argv[1]:
        try:
            throughputs = [int(x) for x in sys.argv[1].strip('[]').split(',')]
            print("Jains Fairness index is: "+ str(JFI(throughputs)))
        except:
            print("There was a problem.\nUsage: python3 jains.py [10,10,10] // prints 1") 
    

    elif len(sys.argv) == 2 and ".txt" in sys.argv[1]:
        try:
            # Hashmap of prefixes, so M = a million
            prefix = {"G": math.pow(10, 9), "M" : math.pow(10,6), "K" : math.pow(10,3)}

            with open(sys.argv[1], "r") as f:
                file = f.read().split("\n")
                throughputs = []
                for line in file:
                    tmp = line.split(" ")
                    prefix_letter = prefix[tmp[1][0]]
                    throughput_calculated = int(tmp[0]) * prefix_letter 
                    
                    throughputs.append(throughput_calculated) 

                print(f"Jains Fairness index of {sys.argv[1]} is: {JFI(throughputs)}")

        except:
            print("Could not find file.")
