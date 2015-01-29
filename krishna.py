# krishna.py -- enumerate different ways to calculate 7+7/7+7*7-7

import sys,itertools

def rpn(code) :
    stack = []
    for i in code :
        if 0 :
            pass
        elif i in ('0','1','2','3','4','5','6','7','8','9') :
            stack.append(int(i))
        elif '-' == i :
            x = stack.pop()
            stack.append(stack.pop() - x)
        elif '+' == i :
            stack.append(stack.pop() + stack.pop())
        elif '/' == i :
            x = stack.pop()
            stack.append(stack.pop() / x)
        elif '*' == i :
            stack.append(stack.pop() * stack.pop())
        else :
            raise Exception('i don\'t know how to \'%s\'' % i)
    return stack

if __name__ == '__main__' :
    c = sys.argv[1]
    if 0 :
        pass
    elif 'rpn' == c :
        print rpn(sys.argv[2])
    elif 'count' == c :
        t = 0
        for i in itertools.permutations(sys.argv[2]) :
            t += 1
        print t
    elif 'krishna' == c :
        n = 0
        for i in itertools.permutations(sys.argv[2]) :
            n += 1
            code = ''.join(i)
            try :
                x = rpn(code)
                if 1 == len(x) :
                    s = 'OK'
                    y = x[0]
                else :
                    s = 'IND'
                    y = '?'
            except ZeroDivisionError :
                s = 'DBZ'
                y = '?'
            except :
                s = 'ERR'
                y = '?'
            print '%d\t%s\t%s\t%s\t%s' % (n,code,s,y,str(x))
    else :
        raise Exception('i don\'t know how to \'%s\'' % c)
