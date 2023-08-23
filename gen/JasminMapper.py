from seedwork.entity.nodes import Node


class JasminMapper:
    numeric_ids: dict = {}
    functions_labels = {}

    scan_types = {
        int: "nextInt()I",
        float: "nextFloat()F",
        bool: "nextBoolean()Z",
        str: "nextLine()Ljava/lang/String;",
    }

    types_flags = {
        int: "I",
        float: "F",
        bool: "Z",
        None: "V",
        str: "Ljava/lang/String;",
    }

    store_types = {int: "istore", float: "fstore", str: "astore"}

    load_types = {
        int: "iload",
        float: "fload",
        str: "aload",
    }

    return_types = {
        int: "ireturn",
        float: "freturn",
        str: "areturn",
        None: "return",
    }

    arith_op_mapping = {
        "+": {
            int: "iadd",
            float: "fadd",
        },
        "*": {
            int: "imul",
            float: "fmul",
        },
        "/": {
            int: "idiv",
            float: "fdiv",
        },
        "-": {
            int: "isub",
            float: "fsub",
        },
        ">": {
            int: "if_icmpgt",
            float: "fcmpg\nifgt",
        },
        "<": {
            int: "if_icmplt",
            float: "fcmpg\niflt",
        },
        "==": {
            int: "if_icmpeq",
            float: "fcmpg\nifeq",
        },
        "!=": {
            int: "if_icmpne",
            float: "fcmpg\nifne",
        },
        ">=": {
            int: "if_icmpge",
            float: "fcmpg\nifge",
        },
        "<=": {
            int: "if_icmple",
            float: "fcmlpg\nifle",
        },
    }

    _current_nids = {}
    _current_label = -1

    def increase_nid(self, scope):
        if scope not in self._current_nids:
            self._current_nids[scope] = -1

        self._current_nids[scope] += 1

        return self._current_nids[scope]

    def increase_label(self):
        self._current_label += 1
        return self._current_label

    def generate_assign(self, type, nid, value):
        store_type = JasminMapper.store_types[type]

        if value is not None:
            code = f"ldc {value}\n{store_type} {nid}\n"
        else:
            code = f"{store_type} {nid}\n"

        return code

    def find_nid_in_scope(self, id, scope):
        nid = self.numeric_ids[scope]["vars"].get(id)

        if nid is None:
            nid = self.numeric_ids[scope]["const"].get(id)

        return nid

    def load_numeric_terms(self, terms: list, type, scope: str = None):
        code = ""
        for term in terms:
            if term.value is not None:
                code += f"ldc {term}\n"
            else:
                nid = self.find_nid_in_scope(term.code, scope)
                if nid is not None:
                    code += f"{self.load_types[type]} {nid}\n"

        return code

    def generate_arith_operation(
        self, left, right, op: str, type: int | float, scope: str = None
    ):
        code = self.load_numeric_terms([left, right], type, scope)
        code += f"{self.arith_op_mapping[op][type]}"

        return code
    
    def generate_args(self, function_args):
        args_codes = "".join(
            [self.types_flags[t["type"]] for t in function_args.values()]
        )
        
        return args_codes

    def generate_function(self, id, type, function_args):
        args_codes = self.generate_args(function_args)
        code = f".method public static {id}({args_codes}){self.types_flags[type]}\n"
        return code

    def generate_function_call(self, id, type, function_args):
        args_codes = "".join(
            [self.types_flags[t["type"]] for t in function_args.values()]
        )
        code += f"invokestatic {id}({args_codes}){self.types_flags[type]}"
        return code
