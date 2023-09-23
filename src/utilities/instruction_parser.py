from .tools import spaces, combine

COMMAND_INDICATOR = "/"

PARAMETER_INDICATOR = "-"

class IllegalInstruction(Exception):
    def __init__(self, err_msg, inp, position):
        super().__init__(
            f"{err_msg}\n....{inp}\n....{spaces(position)}^"
        )
    pass


def parse(s):
    from string import ascii_lowercase, ascii_uppercase
    LEGAL_CHARACTER = list(ascii_lowercase) + list(ascii_uppercase) + [str(i) for i in range(0,10)]
    li = s.split(" ")
    if li[0][0] != COMMAND_INDICATOR:
        raise IllegalInstruction(f"command starts without `{COMMAND_INDICATOR}`", s, 0)
    cmd_dict = {"command": li[0][1:],}
    i = 1
    while i < len(li):
        if li[i][0] == PARAMETER_INDICATOR:
            val = None
            try:
                if li[i+1][0] != PARAMETER_INDICATOR:
                    val = li[i+1]
                    
            except IndexError:
                pass
            cmd_dict[li[i][1:]] = val
        elif li[i][0] not in LEGAL_CHARACTER:
            raise IllegalInstruction(
                f"invalid parameter value: first character must start with alphabet or number `{PARAMETER_INDICATOR}`",
                s,
                len(combine(li[:i]))
            )
        i += 1
    return cmd_dict