from seedwork.entity.nodes import Node

class JasminMapper():
    numeric_ids: dict = {}
    functions_labels = {}
    
    types_flags = {
        int: "I",
        float: "F",
        bool: "Z",
        None: "V",
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
    
    _arith_op_mapping = {
        "+": {
            int: "iadd",
            float: "fadd",
        },
        "*": {
            int: "imul",
            float: "fmul",
        }
    }
    
    _current_nid = -1
    _current_label = -1
    
    def increase_nid(self):
        self._current_nid += 1
        return self._current_nid
    
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
    
    def load_terms(self, terms: list, type, scope: str = None):
        code = ""
        for term in terms:
            if term.isdigit():
                code += f"ldc {term}\n"
            else:
                nid = self.find_nid_in_scope(term, scope)
                if nid is not None:
                    code += f"{self.load_types[type]} {nid}\n"
                    
        return code
    
    def generate_arith_operation(self, left_ctx_text, right_ctx_text, op: str, type: int | float, scope: str = None):
        code = self.load_terms([left_ctx_text, right_ctx_text], type, scope)
        code += f"{self._arith_op_mapping[op][type]}"
        
        return code
    
    def generate_function(self, id, type):
        code = f".method public static {id}(){self.types_flags[type]}\n"
        return code
    
    def generate_function_call(self, id, args, type, scope = None):
        code = self.load_terms(args, type, scope)
        code += f"invokestatic {id}(){self.types_flags[type]}"
        return code