from seedwork.entity.nodes import Node

class JasminMapper():
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
        str: "Ljava/lang/String;"
    }
    
    store_types = {
        int: "istore",
        float: "fstore",
        str: "astore"
    }
    
    load_types = {
        int: "iload",
        float: "fload",
        str: "aload",
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
        "/":{
            int: "idiv",
            float: "fdiv",
        },
        "-":{
            int: "isub",
            float: "fsub",
        },
        ">":{
            int: "if_icmpgt",
            float: "if_fcmpg",
        },
        "<":{
            int: "if_icmplt",
            float: "if_fcmplt",
        },
        "==":{
            int: "if_icmpeq",
            float: "if_fcmpeq",
        },
        "!=":{
            int: "if_icmpne",
            float: "if_fcmpne",
        },
        ">=":{
            int: "if_icmpge",
            float: "if_fcmpge",
        },
        "<=":{
            int: "if_icmple",
            float: "if_fcmple",
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
    
    def generate_assign(self, type , nid, value):
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
    
    def generate_arith_operation(self, left, right, op: str, type: int | float, scope: str = None):
        code = self.load_numeric_terms([left, right], type, scope)
        code += f"{self.arith_op_mapping[op][type]}"
        
        return code
        
    
    def generate_function(self, id, type):
        code = f".method public static {id}(){self.types_flags[type]}\n"
        return code
    
    def generate_function_call(self, id, args, type, scope = None):
        code = self.load_numeric_terms(args, type, scope)
        code += f"invokestatic {id}(){self.types_flags[type]}"
        return code

        