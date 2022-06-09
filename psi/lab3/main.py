import random
# set random weight and offset
w1 = random.uniform(0, 1)
w2 = random.uniform(0, 1)
b  = random.uniform(0, 1)

# data for training
data_set = [
    [-8,20],  #1
    [4,25],   #2
    [5,9],    #3
    [2,20],   #4
    [1,-10],  #5
    [-6,-5],  #6
    [4,-16],  #7
    [-6,-25], #8
    [-9,-10], #9
    [-2,-10]  #10
]

# answer key to data
answer_set = [
    1, #1
    1, #2
    0, #3
    1, #4
    0, #5
    1, #6
    0, #7
    0, #8
    1, #9
    0, #10
]

def train(data, answer_key):
    global w1
    global w2
    global b
    for i in range(len(data)):
        e = 1
        while e != 0:
            activation = 0
            x = data[i][0]
            y = data[i][1]
            print "\nx", x, "y", y
            answer = (w1*x) + (w2*y) + b
            if answer > 0:
                activation = 1
            e = answer_key[i] - activation
            print "answer", round(answer,2), "=", activation

            if e != 0:
                print "wrong answer, change w1, w2, b and repeat"
                w1 = w1 + (e * x)
                w2 = w2 + (e * y)
                b = b + e

def check(x, y):
    global w1
    global w2
    global b
    activation = 0
    answer = (w1*x) + (w2*y) + b
    if answer > 0:
        activation = 1
    print "\nx", x, "y", y
    print round(answer,2), "answer", activation

train(data_set, answer_set)

print "\ncheck perceptron after training"
check(-2,5)
check(1,4)
check(8,8)