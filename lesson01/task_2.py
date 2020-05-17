A = 5
B = 6

print(f'5 AND 6: {A & B} ({bin(A & B)})')
print(f'5 OR 6: {A | B} ({bin(A | B)})')
print(f'5 XOR 6: {A ^ B} ({bin(A ^ B)})')
print(f'NOT 5: {~A} ({bin(~A)})')
print(f'NOT 6: {~B} ({bin(~A)})')
print(f'5 shifted left by 2 digits: {5 << 2} ({bin(5 << 2)})')
print(f'5 shifted right by 2 digits: {5 >> 2} ({bin(5 >> 2)})')
