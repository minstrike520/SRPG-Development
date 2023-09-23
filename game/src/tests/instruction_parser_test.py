from ..utilities.instruction_parser import parse

ins_lst = [
    "/main -a 284 -b 284",
    "/krkw 194 +&9"
]

def test():
    for i in ins_lst:
        print(parse(i))