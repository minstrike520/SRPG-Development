ins_lst = [
    "/main -a 284 -b 284"
]

def main():
    from utilities.src import instruction_parser as parser
    for i in ins_lst:
        print(parser.parse(i))