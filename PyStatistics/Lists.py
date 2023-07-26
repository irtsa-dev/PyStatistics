# PyStatistics | List Functions






#Imports
from NumberTypes import *






#Private Functions
def __ConvertData(Data: list[WeightedNumber, Fraction, Decimal, int, float] | tuple[WeightedNumber, Fraction, Decimal, int, float]):
    return [i.floatForm if type(i) in [WeightedNumber, Fraction] else i for i in Data]




#Public Functions
def Mode(Data: list[WeightedNumber, Fraction, Decimal, int, float] | tuple[WeightedNumber, Fraction, Decimal, int, float]) -> int | float:
    Data = __ConvertData(Data)
    Data = {i: Data.count(i) for i in Data}

    return max(Data, key = Data.get)



def Median(Data: list[WeightedNumber, Fraction, Decimal, int, float] | tuple[WeightedNumber, Fraction, Decimal, int, float]) -> int | float:
    Data = __ConvertData(Data)

    if len(Data) == 0: return None
    if len(Data) == 1: return Data[0]

    Data = sorted(Data)
    x = int(len(Data) / 2)

    if len(Data) % 2 == 0: return round(((Data[x] + Data[x + 1]) / 2.0), 2)
    return Data[x]



def Mean(Data: list[WeightedNumber, Fraction, Decimal, int, float] | tuple[WeightedNumber, Fraction, Decimal, int, float]) -> float:
    Data = __ConvertData(Data)
    return round((sum(Data) / len(Data)), 2)



def QuartileFirst(Data: list[WeightedNumber, Fraction, Decimal, int, float] | tuple[WeightedNumber, Fraction, Decimal, int, float]) -> float:
    Data = sorted(__ConvertData(Data))
	
    x = int(len(Data) / 2)
    return Mean(Data[:(x + 1)])



def QuartileThird(Data: list[WeightedNumber, Fraction, Decimal, int, float] | tuple[WeightedNumber, Fraction, Decimal, int, float]) -> float:
    Data = sorted(__ConvertData(Data))
	
    x = int(len(Data) / 2)
    return Mean(Data[x:])



def InterQuartileRange(Data: list[WeightedNumber, Fraction, Decimal, int, float] | tuple[WeightedNumber, Fraction, Decimal, int, float]) -> float:
    q1 = QuartileFirst(Data)
    q3 = QuartileThird(Data)
	
    return q3 - q1



def Range(Data: list[WeightedNumber, Fraction, Decimal, int, float] | tuple[WeightedNumber, Fraction, Decimal, int, float]) -> float:
	return float(max(Data) - min(Data))



def Outliers(Data: list[WeightedNumber, Fraction, Decimal, int, float] | tuple[WeightedNumber, Fraction, Decimal, int, float]) -> list:
    Data = __ConvertData(Data)

    iqr = InterQuartileRange(Data)

    upperBound = QuartileThird(Data) + (1.5 * iqr)
    lowerBound = QuartileFirst(Data) - (1.5 * iqr)

    return [i for i in Data if i > upperBound or i < lowerBound]