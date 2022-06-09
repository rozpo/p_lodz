months = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]
data = ["","",0,0]
data[0] = input("pierwszy: ")
data[1] = input("drugi: ")

i = 0
while i < len(months):
    if months[i] == data[0]:
        data[2] = i
    if months[i] == data[1]:
        data[3] = i
    i += 1

result = data[3] - data[2]
if result > 0:
    print(result)
else:
    print(result + 12)