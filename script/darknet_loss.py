import argparse
import sys
import matplotlib.pyplot as plt
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("log_file",  help = "path to log file"  )
    parser.add_argument( "option", help = "0 -> loss vs iter"  )
    args = parser.parse_args()
    f = open(args.log_file)
    lines  = [line.rstrip("\n") for line in f.readlines()]
    # skip the first 3 lines
    lines = lines[3:]
    numbers = {'1','2','3','4','5','6','7','8','9','0'}
    iters = []
    loss = []
    for line in lines:
        if len(line)> 10 and line[0]==' ' and line[1] in numbers:
            args = line.split(" ")
            if len(args) >3 and args[1][len(args[1])-1]==':':
                iters.append(int(args[1][:-1]))
                loss.append(float(args[3]))

    plt.plot(iters,loss)
    plt.xlabel('iters')
    plt.ylabel('loss')
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main(sys.argv)
    
   # [len(args[1])