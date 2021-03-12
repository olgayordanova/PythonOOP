def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers ():
            yield i/2

    def take(n, seq):
        output_seq=[]
        for el in seq:
            if len(output_seq) == n:
                return output_seq
            output_seq.append(el)

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
