nums = list()

for pos in range (0,5):
    nums.append(int(input(f'Digite o valor para a posição {pos}: ')))
for v in range(0, len(nums)):

    if v == 0:
        menor = nums[v]
        maior  = nums[v]
    if menor > nums[v]:
        menor =  nums[v]
    if maior < nums[v]:
        maior = nums[v]

#for p in range(0, len(nums)):

 #   if nums[p] == maior:
 #       maiores.append(p)
 #   if nums[p] == menor:
 #       menores.append(p)


print(f'Você digitou os valores {nums}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, M in enumerate(nums):
    if M == maior:
        print(f'{p}...', end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for p, m in enumerate(nums):
    if m == menor:
        print(f'{p}...', end=' ')