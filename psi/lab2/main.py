import random
import math
# user defined
n = 10
gens = 5
# 0 - no debug
# 1 - debug
debug = 0

def select_parents(input_data):
    summary = 0
    new_data = []
    new_gen = []
    for i in range(len(input_data)):
        summary += input_data[i][1]
        temp = []
        temp.append(input_data[0])
        temp.append(input_data[1])
        temp.append(summary)
        new_data.append(temp)

    for i in range(len(new_data)):
        new = random.randint(1,summary)
        for j in range(len(new_data)):
            if new <= new_data[j][2]:
                new_gen.append(input_data[j][0])
                break
    return new_gen

def mix_parents(input_data):
    new_data = []
    for i in range(len(input_data)/2):
        locus = random.randint(1,9)
        par1 = list(format(input_data[i], '08b'))
        par2 = list(format(input_data[len(input_data)-i-1], '08b'))
        if debug > 0:
            print "\nparents", input_data[i], input_data[len(input_data)-i-1], \
                "locus:", locus
            print par1
            print par2
        for i in range(len(par1)):
            if i >= locus:
                tmp = par1[i]
                par1[i] = par2[i]
                par2[i] = tmp
        if debug > 0:
            print "after crossing"
            print par1
            print par2
        mutation = random.randint(0,7)
        par1[mutation] = str(1 - int(par1[mutation],10))
        mutation = random.randint(0,7)
        par2[mutation] = str(1 - int(par2[mutation],10))
        if debug > 0:
            print "after mutation"
            print par1
            print par2
        tmp_par1 = "".join(par1)
        tmp_par2 = "".join(par2)
        new_data.append(int(tmp_par1, 2))
        new_data.append(int(tmp_par2, 2))
    return new_data

def print_data(input_data):
    print "chromos", "name", "result"
    best = []
    for i in range(n):
        best.append(input_data[i][0])
        print format(input_data[i][0], '08b'), format(input_data[i][0], '3d'), input_data[i][1]
    print "best unit:", max(best)

# f(x) = 2(x +1), where x => <1...127>
def calc_fun(input_data):
    result = []
    for i in input_data:
        temp = []
        temp.append(i)
        temp.append(2*(math.pow(i,2)+1))
        result.append(temp)
    return result

generation = []
for k in range(n):
    generation.append(random.randint(1,128))

for i in range(gens - 1):
    print "\ngeneration",i+1
    ret = calc_fun(generation)
    print_data(ret)
    breed = select_parents(ret)
    generation = mix_parents(breed)
print "\nfinal generation"
ret = calc_fun(generation)
print_data(ret)