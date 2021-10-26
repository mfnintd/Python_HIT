s = input()
check = "TRẺTRÂU"
index = 0
for c in s:
    if index == 7:
        break
    if c == check[index]:
        index += 1

if index == 7:
    print("TRẺ TRÂU")
else:
    print("Không TRẺ TRÂU")
