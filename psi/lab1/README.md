# **Rozwiązywanie problemów poprzez przeszukiwanie przestrzeni stanów**
## **1. Cel ćwiczenia**
Przedmiotem ćwiczenia jest analiza efektywności różnych metod rozwiązywanie problemu poprzez przeszukiwanie przestrzeni rozwiązań (stanów). Analiza ta realizowana ma być na przykładzie problemu komiwojażera.

## **2. Rozwiązanie**

### ***Brute Force***
- Metoda siłowa - polega na analizie wszystkich potencjalnych rozwiązań zadania w celu wybrania tego, które spełnia warunki zadania:  

    *Utwórz zbiór wszystkich permutacji bez powtórzeń dla N miast, policz łączną długość każdej drogi (permutacji) łącznie z powrotem do punktu startowego i wybierz najkrótszą.*

```python
def bruteForce(inputData):
    start = time.time()
    paths = finalizePath(createAllPermutations(dataSize), startingCity)
    result = 0
    bestPath = 0
    print "================="
    print "bruteForce"
    for i in range(len(paths)):
        fullPathLen = 0
        for j in range(len(paths[0]) - 1):
            fullPathLen += calcDist(inputData[paths[i][j]], \
                inputData[paths[i][j+1]])
            if debug >= 2:
                print "[", inputData[paths[i][j]][0], ",", \
                    inputData[paths[i][j+1]][0], "]=", \
                    round(calcDist(inputData[paths[i][j]], \
                    inputData[paths[i][j+1]]), 2)
        if debug >= 2:
            print paths[i], " = ", round(fullPathLen, 2)
        if (result == 0) or (result > fullPathLen):
            result = round(fullPathLen, 2)
            bestPath = paths[i]
    print "answer:", bestPath, "=", result
    end = time.time()
    print "time:", round((end - start), 5), "s"
```

<div class="page"/>

### ***Greedy***
- Metoda zachłanna - polegaja na wybraniu w każdym kroku najlepiej rokującego w danym momencie rozwiązania, według strategii działania:  

    *Począwszy od punktu startu, jako następny punkt wybierz ten w którym jeszcze nie byłeś, a który leży najbliżej miejsca w którym się znajdujesz.*

```python
def greedy(inputData):
    start = time.time()
    result = 0
    print "================="
    print "greedy"

    visited = []
    for i in range(len(inputData) -1):
        if len(visited) > 0:
            shortest = 0
            node = 0
            for j in range(len(inputData) - 1):
                if j not in visited:
                    tempResult = calcDist(inputData[visited[-1]], inputData[j])
                    if debug >= 1:
                        print visited[-1], "->", j, "=", round(tempResult, 2)
                    if (shortest == 0) or (shortest > tempResult):
                        shortest = tempResult
                        node = j
            result += shortest
        else:
            node = i
        visited.append(node)
    # calc return path
    tempResult = calcDist(inputData[visited[-1]], inputData[visited[0]])
    result += tempResult
    if debug >= 1:
        print visited[-1], "->", visited[0], "=", round(tempResult, 2)
    visited.append(visited[0])
    print "answer:", visited, "=", round(result, 2)
    end = time.time()
    print "time:", round((end - start), 5), "s"
```

<div class="page"/>

### ***A****
- Metoda A* - algorytm heurystyczny znajdowania najkrótszej ścieżki z dowolnego wierzchołka do wierzchołka spełniającego określony warunek zadania:  

    *Począwszy od punktu startu, jako następny punkt wybierz ten w którym jeszcze nie byłeś, a którego suma odległości do aktualnego punktu oraz punktu końcowego jest najkrótsza.*

```python
def aStar(inputData):
    start = time.time()
    result = 0
    print "================="
    print "aStar"

    visited = []
    for i in range(len(inputData) -1):
        if len(visited) > 0:
            shortest = 0
            node = 0
            for j in range(len(inputData) - 1):
                if j not in visited:
                    path = calcDist(inputData[visited[-1]], inputData[j])
                    heu = calcDist(inputData[j], inputData[visited[0]])
                    tempResult = path + heu
                    if debug >= 1:
                        print visited[-1], "->", j, "=", round(path, 2), "+", round(heu, 2), "=", round(tempResult, 2)
                    if (shortest == 0) or (shortest > tempResult):
                        shortest = tempResult
                        finalPath = path
                        node = j
            result += finalPath
        else:
            node = i
        visited.append(node)
    # calc return path
    path = calcDist(inputData[visited[-1]], inputData[visited[0]])
    result += path
    if debug >= 1:
        print visited[-1], "->", visited[0], "=", round(path, 2)
    visited.append(visited[0])
    print "answer:", visited, "=", round(result, 2)
    end = time.time()
    print "time:", round((end - start), 5), "s"
```

<div class="page"/>

## **3. Wnioski**

```
=================
num | posX | posY
[0, 32, 49]
[1, 28, 71]
[2, 66, 50]
[3, 7, 21]
[4, 21, 9]
[5, 58, 63]
[6, 16, 40]
[7, 95, 51]
[8, 32, 82]
[9, 28, 2]
=================
bruteForce
answer: (0, 6, 3, 4, 9, 7, 2, 5, 8, 1, 0) = 261.28
time: 4.59848 s
=================
greedy
answer: [0, 6, 3, 4, 9, 2, 5, 1, 8, 7, 0] = 320.2
time: 0.00465 s
=================
aStar
answer: [0, 6, 1, 8, 5, 2, 7, 4, 3, 9, 0] = 318.8
time: 0.00171 s
```

- Metoda Brute Force zwróci najkrótszą drogę za każdym wywowałaniem algorytmu.

- Złożoność obliczeniowa w tym przypadku wynosi N! co pozostaje największą wadą algorytmu, o ile czas wykonania dla 10 miast wyniósł niecałe 5sec na przeciętnej jakości sprzęcie obliczeniowym to dla problemu N=20 uzyskanie odpowiedzi jest niemożliwe w rozsądnym czasie.

- Metoda Greedy jest stosunkowo prosta w implementacji z uwagi na fakt iż zawsze wyszukujemy jedynie w obrębie następnego kroku nie zważająć na pozostałą drogę do pokonania.

- Algorytm A* jest jednym z najpopularniejszych w radzeniu sobie z problemami podobnymi do TSP ponieważ pozwala wykorzystać heurystykę do otrzymania najbardziej opytmalnego rozwiązania w relatywnie krótkim czasie.

- A* łączy w sobie cechę metody Greedy (Najbliższy krok) oraz pozostałego dystansu do ostatecznego punktu podróży.
