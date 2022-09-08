from random import randint


num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')

for i in num:
    print(f"{i}", end='')


print(f"O maior valor sorteado foi {max(num)}")
print(f"O menor valor sorteado foi {min(num)}")
