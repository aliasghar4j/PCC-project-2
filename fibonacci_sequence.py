def fib_func(s,e):
    fib_seq = [0, 1]
    def seq_gen(n):      
        if len(fib_seq) < n:
            next = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next)
            return seq_gen(n)
        else:    
            return fib_seq
    seq_gen(e)
    return fib_seq[s:e]
s = int(input('Enter the starting index: '))
e = int(input('Enter the ending index: ')) 
sequence = fib_func(s , e)
print('-------------------------------')
print('     Fibonacci Sequence')
print('-------------------------------')
print(f'''Here is the finobacci sequence 
{s}th index to {e}th index:''')
print(sequence)
print('-------------------------------')
input("Press Enter to exit...")
