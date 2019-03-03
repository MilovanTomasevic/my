class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_op(x):
    return x in ['+', '-', '*', '/']

def is_num(x):
    for i in range(len(x)):
            if not x[i] in ('0123456789-' if i == 0 else '0123456789'):
                return False
    return True

def is_neg_num(x):
    if x[0] == '-' and is_num(x):
        return True
    return False

def get_parse_three(s):
    A = s.split(" ")[::-1]
    (T, s) = get_parse_three_list(A)
    return T

def get_parse_three_list(A):
    if len(A) > 0:
        if not is_op(A[0]):
            n = Node(A[0])
            return (n, A[1:])
        else:
            n = Node(A[0])
            (n.right, A) = get_parse_three_list(A[1:])

            (n.left, A) = get_parse_three_list(A)

            return (n, A)
    else:
        return (None, '')

def eval_three(three, dictionary):
    if not is_op(three.val):
        if is_num(three.val):
            return eval(three.val)
        else:
            return dictionary[three.val]
    else:
        if three.val == '+':
            return (eval_three(three.left, dictionary) + eval_three(three.right, dictionary))
        elif three.val == '-':
            return (eval_three(three.left, dictionary) - eval_three(three.right, dictionary))
        elif three.val == '*':
            return (eval_three(three.left, dictionary) * eval_three(three.right, dictionary))
        elif three.val == '/':
            return (eval_three(three.left, dictionary) / eval_three(three.right,dictionary))
        else:
            print("SOMETHING WENT WRONG :(")
            return None

def make_infix(three):
    if not is_op(three.val):
        if (is_neg_num(three.val)):
            return "(" + three.val + ")"
        else:
            return three.val
    else:
        return "(" + make_infix(three.left) + " " + three.val + " " + make_infix(three.right) + ")"

if __name__ == "__main__":
    test_cases = [("23 45 67 + -", None), ("a 5 + b c 3 / - *", {'a': 34, 'b': 65, 'c': 3}), ("vel_0 time * g time * time 2 / * +", {'vel_0': -10, 'time': 20, 'g': 9.81}), ("-3 -5 - 1 +", None)]
    for test in test_cases:
        (s, d) = test

        T = get_parse_three(s)

        print("INPUT STRING: \"", s, "\"", sep = "")
        if d != None:
            print("VARIABLE DICTIONARY:" , d)
        print("EVAL_TREE RETURNS:", eval_three(T, d))
        print("MAKE_INFIX RETURNS:", make_infix(T))
        print()
