from logic import TruthTable

print('Problem #1')
myTable = TruthTable(['a'],['-a'])
myTable.display()
print('')

myTable2 = TruthTable(['a','b'],['a and b'])
myTable2.display()
print('')

myTable3 = TruthTable(['a','b'],['a or b'])
myTable3.display()
print('')

myTable4 = TruthTable(['a','b'],['a -> b'])
myTable4.display()
print('')

myTable5 = TruthTable(['a','b'],['a <-> b'])
myTable5.display()
print('')

print('')
print('')

print('Problem #2')
Case1 = input("Enter the first propostion: ")
PropTable1 = TruthTable (['p','q'],[Case1])
PropTable1.display()
print('')

Case2 = input("Enter the second proposition: ")
PropTable2 = TruthTable(['p','q'],[Case2])
PropTable2.display()
print('')

List1 = PropTable1.table
List2 = PropTable2.table

Arr1 = []
Arr2 = []

for row in List1:
    propList1 = row
    Arr1.append(propList1[1])

for row in List2:
    propList2 = row
    Arr2.append(propList2[1])

equiv = 1
for i in range (0, len(Arr1)):
    if Arr1[i] != Arr2[i]:
        equiv = 0
        print("The propositions are not equivalent.")
        break

if equiv == 1:
    print("The propositions are equivalent.")


