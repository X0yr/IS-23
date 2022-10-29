def SortInc3(A, B, C):
    if C<B<A:
        A, B, C=C, B, A
        print(A, B, C)
    elif A<B<C:
        print(A, B, C)
    elif B<C<A:
        A, B, C=B, C, A
        print(A, B, C)
    elif B<A<C:
        A, B, C=B, A, C
        print(A, B, C)
    elif A<C<B:
        A, B, C=A, C, B
        print(A, B, C)
    else:
        A, B, C=C, A, B
        print(A, B, C)

A=int(input())
B=int(input())
C=int(input())
SortInc3(A, B, C)
