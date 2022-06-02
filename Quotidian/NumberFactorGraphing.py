import plotly.express as px
import sys

def PrimeFactors(n):
    primeFactors = []
    
    if n <= 0:
        print("Invalid number")
        return []
    else:
        primeFactors.append(1)
        i = 2

        while n != 1:
            dividedNumber = n / i

            if dividedNumber.is_integer() == False:
                i = i + 1
            
            elif dividedNumber.is_integer():
                primeFactors.append(i)
                n = n / i
                i = 2

    return primeFactors



def GraphFactorsRising(number):
    numberFactors = sorted(PrimeFactors(number))
    multipliedFactors = []
    n = 1
    for f in numberFactors:
        n = n * f
        multipliedFactors.append(n)
            
    fig = px.line(multipliedFactors)
    fig.show()

    return None


def GraphFactorsSinking(number):
    numberFactors = sorted(PrimeFactors(number), reverse=True)
    multipliedFactors = []
    n = 1
    for f in numberFactors:
        n = n * f
        multipliedFactors.append(n)
            
    fig = px.line(multipliedFactors)
    fig.show()

    return None


# either shows visualization of prime factorial multiplication graph by rising, sinking prime factorials, or both
if __name__ == "__main__":
    myNumber = int(sys.argv[1])
    graphingSequence = sys.argv[2]

    if graphingSequence.lower() in ["rising", "r", "-r"]:
        GraphFactorsRising(myNumber)
        exit()
    
    elif graphingSequence.lower() in ["both", "b", "-b"]:
        GraphFactorsRising(myNumber)
        GraphFactorsSinking(myNumber)
        exit()

    else:
        GraphFactorsSinking(myNumber)
        exit()
    