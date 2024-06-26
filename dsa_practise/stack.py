# ------------------- 1. next greatest element to the right ------------------ #
array = [1,3,2,4]
answer = []
stack = []
for i in range(len(array)-1,-1,-1):
  while (len(stack)>0 and array[i]>stack[-1]):
    stack.pop()
  if (len(stack)==0):
    answer.append(-1)
  else:
    answer.append(stack[-1])
  stack.append(array[i])
print(answer[::-1])
# ------------------ 2. nearest greatest element to the left ----------------- #
array = [1,3,2,4]
answer = []
stack = []
for i in range(0,len(array)):
  while (len(stack)>0 and array[i]>stack[-1]):
    stack.pop()
  if (len(stack)==0):
    answer.append(-1)
  else:
    answer.append(stack[-1])
  stack.append(array[i])
print(answer)
# ---------------------- 3. nearest smaller element to the right --------------------- #
array = [1,3,2,5,4]
answer = []
stack = []
for i in range(len(array)-1,-1,-1):
  while (len(stack)>0 and array[i]<stack[-1]):
    stack.pop()
  if (len(stack)==0):
    answer.append(-1)
  else:
    answer.append(stack[-1])
  stack.append(array[i])
print(answer[::-1])
# ---------------------- 4. nearest smaller element to the left ---------------------- #
array = [1,3,2,5,4]
answer = []
stack = []
for i in range(0,len(array)):
  while (len(stack)>0 and array[i]<stack[-1]):
    stack.pop()
  if (len(stack)==0):
    answer.append(-1)
  else:
    answer.append(stack[-1])
  stack.append(array[i])
print(answer)
# --------------------------- 5. stock span problem -------------------------- #
array = [100,80,60,70,60,75,85]
answer = []
stack = []
for i in range(0,len(array)):
  consecutiveCount=1
  while (len(stack)>0 and array[i]>stack[-1][0]):
    consecutiveCount+=stack[-1][1]
    stack.pop()
  if (len(stack)==0):
    answer.append(1)
  else:
    answer.append(consecutiveCount)
  stack.append([array[i],consecutiveCount])
print(answer)
# ------------------------- 6. max area of histogram ------------------------- #
buildingHeights = [6,2,5,4,5,1,6]
nsr = []
nsl = []
stack = []
for i in range(len(buildingHeights)-1,-1,-1):
  while(len(stack)>0 and buildingHeights[i]<stack[-1][0]):
    stack.pop()
  index = None
  if(len(stack)==0):
    index = len(buildingHeights)
  else:
    index = stack[-1][1]
  nsr.append(index)
  stack.append([buildingHeights[i],i])
nsr = nsr[::-1]
stack = []
for i in range(0,len(buildingHeights)):
  while(len(stack)>0 and buildingHeights[i]<stack[-1][0]):
    stack.pop()
  index = None
  if(len(stack)==0):
    index=-1
  else:
    index = stack[-1][1]
  nsl.append(index)
  stack.append([buildingHeights[i],i])
maxArea = -1
for i in range(0,len(buildingHeights)):
  area = (nsr[i]-nsl[i]-1)*buildingHeights[i]
  maxArea = max(maxArea,area)
print(maxArea)
# ------------------ 7. max area reactangle in binary matrix ----------------- #
def maxAreaOfHistogram(heights): 
  stack = []
  nsr = []
  nsl = []
  maxArea = 0
  for i in range(len(heights)-1,-1,-1):
    index = len(heights)
    while(len(stack)>0 and heights[i]<=stack[-1][0]):
      stack.pop()
    if(len(stack)!=0):
      index = stack[-1][1]
    nsr.append(index)
    stack.append([heights[i],i])
  nsr = nsr[::-1]
  stack = []
  for i in range(len(heights)):
    index = -1
    while(len(stack)>0 and heights[i]<=stack[-1][0]):
      stack.pop()
    if(len(stack)!=0):
      index = stack[-1][1]
    nsl.append(index)
    stack.append([heights[i],i])
  for i in range(len(heights)):
    maxArea = max(maxArea, (nsr[i]-nsl[i]-1)*heights[i])
  return maxArea

def modifyData(rowIndex,matrix):
  baseRow = matrix[rowIndex]
  newHeights = []
  maxheight = len(matrix)
  for i in range(len(baseRow)):
    height = 0
    if(baseRow[i]!=0):
      for j in range (rowIndex,maxheight):
        if(matrix[j][i]==0):
          break
        else:
          height += 1
    newHeights.append(height)
  return newHeights
  
def maxAreaInBinaryMatrix(matrix):
  maxArea = 0
  for i in range(len(matrix)):
    modifiedData = modifyData(i,matrix)
    maxArea = max(maxArea,maxAreaOfHistogram(modifiedData))
  return maxArea
inputArray = [[1,1,0,1],[1,1,1,1],[1,1,1,1],[0,1,1,0]]
result = maxAreaInBinaryMatrix(inputArray)
print(result)
# -------------------------- 8. Rain water trapping -------------------------- #
def rainWaterTrapping(array):
  mxl = []
  mxr = []
  mxl[0] = array[0]
  for i in range(1, len(array)):
    mxl[i] = max(mxl[i-1],array[i])
  mxr[len(array)-1] = array[len(array)-1]
  for i in range(len(array)-2,-1,-1):
    mxr[i] = max(mxr[i+1],array[i])
  waterLevel = 0
  for i in range(len(array)):
    waterLevel+= min(mxl[i],mxr[i]) - array[i]
  return waterLevel
result = rainWaterTrapping([3, 0, 0, 2, 0, 4])
print(result)
# -------------------------- 9. min stack O(n) space ------------------------- #
stack = []
supportingStack = []
def push(elem):
  if(len(stack)==0):
    stack.append(elem)
    supportingStack.append(elem)
  else:
    stack.append(elem)
    currentMinElement = supportingStack[-1]
    if(elem<currentMinElement):
      supportingStack.append(elem)

def pop():
  if(len(stack)==0):
    print("Stack is empty")
    return
  topElement = stack.pop()
  if(topElement==supportingStack[-1]):
    supportingStack.pop()

def minElement():
  if(len(stack)==0):
    print("Stack is empty")
    return
  print(supportingStack[-1])

push(18)
push(19)
minElement()
push(29)
push(15)
minElement()
pop()
minElement()
# --------------------------- min stack O(1) space --------------------------- #
stack = []
minimumElement = -1

def push(elem):
  global minimumElement
  if(len(stack)==0):
    stack.append(elem)
    minimumElement = elem
  else:
    if(elem<minimumElement):
      prevMin = minimumElement
      newMin = elem
      flag = 2*newMin - prevMin
      stack.append(flag)
      minimumElement = newMin
    else:
      stack.append(elem)

def pop():
  global minimumElement
  if(len(stack)==0):
    print("Stack is empty")
    return
  top = stack.pop()
  if(top<minimumElement):
    prevMin = 2*minimumElement - top
    top = minimumElement
    minimumElement = prevMin
  print(top)

def minElement():
  if(len(stack)==0):
    print("Stack is empty")
    return
  print(minimumElement)

def top():
  if(len(stack)==0):
    print("Stack is empty")
    return
  top = stack[-1]
  if(top<minimumElement):
    top = minimumElement
  print(top)

push(18)
push(19)
minElement()
push(29)
push(15)
minElement()
pop()
minElement()
# ----------------------------- celebrity problem ---------------------------- #
matrix = [[0,1,1,0],
   [0,0,0,0],
   [0,1,0,0],
   [1,1,0,0]]

def celebrityProblem():
  stack = []
  for i in range(len(matrix)):
    stack.append(i)
  while(len(stack)>1):
    a = stack.pop()
    b = stack.pop()
    if matrix[a][b] == 1 and matrix[b][a]==0:
      stack.append(b)
    elif(matrix[b][a] == 1 and matrix[a][b]==0):
      stack.append(a)
  if(len(stack)==0):
    return -1
  probableCelebrity = stack.pop()
  row=0
  col=0
  for i in range(len(matrix)):
    row+=matrix[probableCelebrity][i]
    col+=matrix[i][probableCelebrity]
  if(row==0 and col==len(matrix)-1):
    return probableCelebrity
  else:
    return -1
result = celebrityProblem()
print(result)
# --------------------------- is valid parenthesis --------------------------- #
def isValidParentheses(string):
  stack = []
  if(len(string)==0):
    return True
  for i in range(len(string)):
    if string[i] in [')','}',']']:
      if(len(stack)==0):
        return False
      else:
        top = stack.pop()
        if(string[i]==')' and top=='('):
          continue
        elif(string[i]=='}' and top=='{'):
          continue
        elif(string[i]==']' and top=='['):
          continue
        else:
          return False
    else:
      stack.append(string[i])
  return len(stack)==0

s = "()[{}()]"
if isValidParentheses(s):
    print("True")
else:
    print("False")
x = "([)]"
if isValidParentheses(x):
  print("True")
else:
  print("False")
# ------------------------- longest valid parentheses ------------------------ #
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if(len(s)==0):
            return 0
        stack = []
        for i in range(len(s)):
            char = s[i]
            if(char==')'):
                if(len(stack)>0):
                    top = stack[-1][0]
                    if(top=='('):
                        stack.pop()
                    else:
                        stack.append([char,i])
                else:
                    stack.append([char,i])
            else:
                stack.append([char,i])
        if(len(stack)==0):
            return len(s)
        invalidIndexes = [-1]
        for j in range(len(stack)):
            invalidIndexes.append(stack[j][1])
        invalidIndexes.append(len(s))
        length = 0
        for k in range(0,len(invalidIndexes)-1):
            length = max(length,invalidIndexes[k+1]-invalidIndexes[k]-1)
        return length
# ------------------------- iterative tower of hanoi ------------------------- #
def moveDisk(fromRod, toRod, fromStack, toStack, move):
  if len(fromStack) == 0:
      fromStack.append(toStack.pop())
      print(f"Step {move}::Move disk from {toRod} to {fromRod}")
  elif len(toStack) == 0:
      toStack.append(fromStack.pop())
      print(f"Step {move}::Move disk from {fromRod} to {toRod}")
  elif fromStack[-1] > toStack[-1]:
      fromStack.append(toStack.pop())
      print(f"Step {move}::Move disk from {toRod} to {fromRod}")
  else:
      toStack.append(fromStack.pop())
      print(f"Step {move}::Move disk from {fromRod} to {toRod}")

def towerOfHanoiIterative(numberOfDiscs, source, destination, helper):
  totalMoves = 2 ** numberOfDiscs - 1
  sourceStack = list(range(numberOfDiscs, 0, -1))
  destinationStack = []
  helperStack = []

  mapping = {
      source: sourceStack,
      destination: destinationStack,
      helper: helperStack
  }

  if numberOfDiscs % 2 == 0:
      moveSeq = [(source, helper), (source, destination), (helper, destination)]
  else:
      moveSeq = [(source, destination), (source, helper), (helper, destination)]

  for i in range(1, totalMoves + 1):
      fromRod, toRod = moveSeq[(i - 1) % 3]
      moveDisk(fromRod, toRod, mapping[fromRod], mapping[toRod], i)

towerOfHanoiIterative(4, 's', 'd', 'h')
# ----------------------- class implementation of stack ---------------------- #
class Stack:

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def pop(self):
    print('Popped element is', self.items.pop())
    self.items.pop()

  def push(self, item):
    self.items.append(item)

  def top(self):
    print('Top of the stack is', self.items[-1])

  def size(self):
    print('Size of the stack is', len(self.items))


stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()


