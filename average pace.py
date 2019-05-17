K = int(input('Enter no.of kilometers = '))
S1 = int(input('Enter Time in minutes ='))
S2 = int(input('Enter Time in seconds ='))
S3 = S1*60
T = S3 + S2
A = (T/K) #average pace 
print(A)
print(T)
