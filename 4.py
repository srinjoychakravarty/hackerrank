from collections import deque

def superStack(operations):

    def push(v):
        S.append(int(v))

    def pop():
        return S.pop()

    def inc(i,v):
        i, v = int(i), int(v)
        for pos in range(i):
            S[pos] += v

    S = deque()
    funcs = locals()

    for operation in operations:
        op, *args = operation.split(' ')
        funcs[op](*args)

        print(S[-1] if S else "EMPTY")

if __name__ == '__main__':
    operations = ['push 4', 'push 5', 'inc 2 1', 'pop', 'pop']
    superStack(operations)