def Sort(array):  # insertion sort
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1


def GetSum(array):
    summa = 0
    for el in array:
        summa += el.value
    return summa


class Node:  # tree node
    left = None
    right = None
    parent = None
    value = None

    def __init__(self, num):  # constructor
        self.value = num


class BinarySearchTree:  # binary search tree
    root = None  # root node
    pos = 0  # position in array, used in InorderRebuild

    def LoadTree(self, sourceArray):
        currentParent = None  #
        isLeft = True

        for element in sourceArray:  # iterating elements in array
            if self.root is None:  # if tree is empty, creating node and making it head
                newNode = Node(int(element))
                self.root = newNode
                currentParent = self.root
            else:
                if element == "0":  # if element is NIL, choosing for right place
                    if isLeft:  # if the last element was left, this element is right
                        isLeft = False
                    else:  # if last element was right, going upwards, to parent
                        while currentParent.parent and currentParent.parent.right == currentParent:
                            currentParent = currentParent.parent
                        currentParent = currentParent.parent
                else:
                    newNode = Node(int(element))  # creating new node
                    newNode.parent = currentParent  # setting references
                    if isLeft:  # if there is no left leaf, setting new node as left of current node
                        currentParent.left = newNode
                    else:  # else setting new node as right
                        currentParent.right = newNode
                    currentParent = newNode  # setting new node as parent for next node
                    isLeft = True  # setting flag for next node
                if not currentParent:
                    break

    def InorderAddValuesToArray(self, array, x):  # function that writes values of tree in array
        if x is not None:
            self.InorderAddValuesToArray(array, x.left)
            array.append(x.value)
            self.InorderAddValuesToArray(array, x.right)

    def InorderSetSortedValues(self, array, x):  # function that sets sorted values to nodes
        if x is not None:
            self.InorderSetSortedValues(array, x.left)
            x.value = array[self.pos]
            self.pos += 1
            self.InorderSetSortedValues(array, x.right)

    def InorderRebuild(self):  # function that rebuilds binary tree to binary search tree
        values = []
        self.InorderAddValuesToArray(values, self.root)  # getting all values in tree
        Sort(values)  # sorting values

        self.pos = 0
        self.InorderSetSortedValues(values, self.root)  # setting values to tree inorder

    def InorderGetSequence(self, tempArray, summa, x):  # function that get array of nodes that contains sum
        if x is not None:
            tempArray.append(x)  # adding node to current list
            self.InorderGetSequence(tempArray, summa, x.left)  # adding left element to current list and check
            if GetSum(tempArray) == summa:  # if sum of values of current nodes == summa, end
                return
            self.InorderGetSequence(tempArray, summa, x.right)  # adding right element to current list and check
            if GetSum(tempArray) == summa:  # if sum of values of current nodes == summa, end
                return
            tempArray.pop()  # deleting last element of current list

    def InorderFindSums(self, answers, summa, x):  # function that gets arrays of nodes that contains sum
        if x is not None:
            self.InorderFindSums(answers, summa, x.left)  # going to left subtree

            tempArray = []  # creating new sequence that starts on current node
            self.InorderGetSequence(tempArray, summa, x)  # and checking it for sum
            if len(tempArray) != 0:  # if temp array is not empty, adding it to answers
                answers.append(tempArray)

            self.InorderFindSums(answers, summa, x.right)  # going to right subtree


if __name__ == "__main__":
    file_name = input("Type file name: ")  # reading data from file
    with open(file_name, "r") as file:
        bigString = file.readlines()

    source = bigString[0].split()  # splitting values

    tree = BinarySearchTree()  # creating binary tree
    tree.LoadTree(source)  # building tree using start array
    tree.InorderRebuild()  # rebuilding tree to binary search tree

    summ = int(input("Type S: "))
    answers = []
    tree.InorderFindSums(answers, summ, tree.root)  # finding all sets of nodes with sum

    with open("is03_diordiev_02_output.txt", "w") as file:  # writing results to file
        for seq in answers:
            for node in seq:
                file.write(str(node.value) + " ")
            file.write("\n")
