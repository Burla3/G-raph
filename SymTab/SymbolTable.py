
class SymbolTable():

    def __init__(self):
        self.symbols = {}

    def get(self, symkey):
        if symkey in self.symbols:
            if self.symbols[symkey]['type'] == 'ref':
                return self.symbols[symkey]['value']['table'].get(self.symbols[symkey]['value']['key'])
            else:
                return self.symbols[symkey]
        else:
            raise KeyError('Symbol key {0} not found in table'.format(symkey))

    def delete(self, symkey):
        del self.symbols[symkey]

    def _create_sym(self, symkey, symtype, value):
        self.symbols[symkey] = {'type': symtype, 'value': value}

    def _set_sym(self, symkey, symtype, value):
        self.symbols[symkey]['type'] = symtype
        self.symbols[symkey]['value'] = value

    def _set_sym_ref(self, symkey, symtype, value):
        self.symbols[symkey]['value']['reftab'].set(self.symbols[symkey]['value']['refkey'], symtype, value)

    def set(self, symkey, symtype, value, reftab=None, refkey=None):
        if symtype == 'ref':
            if not reftab or not refkey:
                raise ValueError(
                    'When creating a symbol reference type, you must supply a table(reftab) and key(refkey)'
                )
            value = {'table': reftab, 'key': refkey}

        if symkey in self.symbols:
            if self.symbols[symkey]['type'] == 'ref':
                self._set_sym_ref(symkey, symtype, value)
            else:
                self._set_sym(symkey, symtype, value)
        else:
            self._create_sym(symkey, symtype, value)
