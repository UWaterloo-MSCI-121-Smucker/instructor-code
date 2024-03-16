from find_sequence import *
import timeit

# I was curious if the different versions showed much difference in performance.
# Turns out the version that slices is the fastest.  Not sure why this is the case,
# but I am guessing that the python interpreter recognizes this as a special case
# that it does quickly.

n=1000000

print("lists")

text = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10]
pattern = [1,2,3,4,5,6,7,8,9,10]

result = timeit.timeit(stmt='find_sequence_v1(text,pattern)', globals=globals(),number=n)
print(f'v1 time = {result}')

result = timeit.timeit(stmt='find_sequence_v2(text,pattern)', globals=globals(),number=n)
print(f'v2 time = {result}')

result = timeit.timeit(stmt='find_sequence_v3(text,pattern)', globals=globals(),number=n)
print(f'v3 time = {result}')

result = timeit.timeit(stmt='find_sequence(text,pattern)', globals=globals(),number=n)
print(f'find_sequence time = {result}')


print("strings")

text = "asdfasdfasdf1asdfasdfasdf2asdfasdfasdf3asdfasdfasdf4"
pattern = "asdfasdfasdf4"

result = timeit.timeit(stmt='find_sequence_v1(text,pattern)', globals=globals(),number=n)
print(f'v1 time = {result}')

result = timeit.timeit(stmt='find_sequence_v2(text,pattern)', globals=globals(),number=n)
print(f'v2 time = {result}')

result = timeit.timeit(stmt='find_sequence_v3(text,pattern)', globals=globals(),number=n)
print(f'v3 time = {result}')

result = timeit.timeit(stmt='find_sequence(text,pattern)', globals=globals(),number=n)
print(f'find_sequence time = {result}')





