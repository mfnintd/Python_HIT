String = input()
m = int(input())

String = String[:m] + String[:m-1:-1]

print(String)
