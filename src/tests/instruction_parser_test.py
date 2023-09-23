from ..utilities import instruction_parser as parser

ins_lst = [
    "/main -a 284 -b 284"
]

def main():
    for i in ins_lst:
        print(parser.parse(i))