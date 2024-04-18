from DecisionSet.Minds2 import Learn_DS
from DecisionSet.check import ConsistencyCheck
from DecisionSet.data import Data
def main():
    # featureset = [['v2 == 0', 'v2 == 1', 'v2 >= 0', 'v2 > 1', 'v1 == v2', 'v1 == 0', 'v1 == 1', 'v1 >= v2', 'v1 > 1', 'v1 >= 0', 'v2 >= v1', 'v2 > v1', 'v2 >= 1', 'v1 > v2', 'target'], ['1', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0'], ['0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '1', '0', '1'], ['0', '0', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '0', '1'], ['1', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1'], ['0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '0', '1'], ['0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0'], ['1', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1'], ['0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '0', '1'], ['0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '1']]
    # featureset = [['v2 == 0', 'v2 == 1', 'v2 >= 0', 'v2 > 1', 'v1 == v2', 'v1 == 0', 'v1 == 1', 'v1 >= v2', 'v1 > 1', 'v1 >= 0', 'v2 >= v1', 'v2 > v1', 'v2 >= 1', 'v1 > v2', 'target'], ['1', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0'], ['0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '1', '0', '1'], ['0', '0', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '0', '1'], ['1', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1'], ['0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '0', '1'], ['0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0'], ['1', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1'], ['0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '0', '1']]
    # featureset = [['v2 == 0', 'v2 == 1', 'v2 >= 0', 'v2 > 1', 'v1 == v2', 'v1 == 0', 'v1 == 1', 'v1 >= v2', 'v1 >= 0', 'v2 >= v1', 'v1 > 1', 'v2 > v1', 'v2 >= 1', 'v1 > v2', 'target'], ['1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0', '0', '1', '0', '1'], ['1', '0', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1'], ['0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '0', '1', '1', '0', '1'], ['0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0'], ['1', '0', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1'], ['0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '0', '1', '1', '0', '1'], ['0', '0', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '0', '1'], ['0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '1', '1', '1']]
    featureset =  [['v2 == 0', 'v2 == 1', 'v2 >= 0', 'v2 > 1', 'v1 == v2', 'v1 == 0', 'v1 == 1', 'v1 >= v2', 'v1 >= 0', 'v2 >= v1', 'v1 > 1', 'v2 > v1', 'v2 >= 1', 'v1 > v2', 'v1 == v1 + 1', 'v1 == v1 + v2', 'v1 == v2 + 1', 'v1 == v2 + v2', 'v1 == v2 - 1', 'v1 == 2', 'v2 == 2', 'v1 + 1 == v2 + v2', 'v1 + 1 == v2 - 1', 'v1 + v1 == v2 + 1', 'v1 + v2 == 1', 'v1 + v2 == 2', 'v2 + 1 == v1 - 1', 'v2 + 1 == v1 - v2', 'v2 + v2 == v1 - v2', 'v1 - 1 == 2', 'v1 >= v2 + 1', 'v1 >= v2 + v2', 'v1 >= v1 - 1', 'v1 >= v2 - 1', 'v1 >= 2', 'v2 >= v1 + 1', 'v2 >= v1 - 1', 'v2 >= v1 - v2', 'v2 >= 2', 'v1 + 1 >= v1 + v2', 'v1 + 1 >= v2 + v2', 'v1 + v2 >= 2', 'v2 + 1 >= v1 + v1', 'v2 + 1 >= v1 - 1', 'v2 + 1 >= v1 - v2', 'v2 + v2 >= v1 + 1', 'v1 - 1 >= v2 + 1', 'v1 - 1 >= v2 + v2', 'v1 + v1 > v2 + 1', 'v1 + v2 > 2', 'v2 + v2 > v1 + 1', 'v1 - 1 > v2 + 1', 'v1 - 1 > v2 + v2', 'v1%2 == 1', 'v2%2 == 0', 'v2%2 == 1', '(v1 + v2)%2 == 0', '(v1 + v2)%2 == 1', 'target'], ['1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '0', '1', '0'], ['0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '0', '1'], ['1', '0', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1'], ['0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1'], ['0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0'], ['0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '0', '1', '0'], ['0', '0', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '1', '0', '1'], ['1', '0', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1'], ['0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '0', '1'], ['0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1', '0', '0', '0', '1', '0', '1', '1', '0', '1']]
    data = Data(featureset)
    checker = ConsistencyCheck(data)
    if checker.status and checker.do() == False:
        checker.remove_inconsistent()
    # 检查完以后计算决策集
    minds2_DS, expr = Learn_DS(data).compute()
    print("expr", expr)

if __name__ == '__main__':
    main()