from bs4 import NavigableString
from env import Env
from visitor import Visitor

# [import]
import z_if
import z_loop
import z_num
import z_var

HANDLERS = {
    "z-if": z_if,
    "z-loop": z_loop,
    "z-num": z_num,
    "z-var": z_var
}
# [/import]


# [construct]
class Expander(Visitor):
    def __init__(self, root, variables):
        super().__init__(root)
        self.env = Env(variables)
        self.handlers = HANDLERS
        self.result = []
# [/construct]

    # [open]
    def open(self, node):
        if isinstance(node, NavigableString):
            self.output(node.string)
            return False
        elif self.hasHandler(node):
            return self.getHandler(node).open(self, node)
        else:
            self.showTag(node, False)
            return True
    # [/open]

    # [close]
    def close(self, node):
        if isinstance(node, NavigableString):
            return
        elif self.hasHandler(node):
            self.getHandler(node).close(self, node)
        else:
            self.showTag(node, True)
    # [/close]

    # [handlers]
    def hasHandler(self, node):
        return any(
            name in self.handlers
            for name in node.attrs
        )

    def getHandler(self, node):
        possible = [
            name for name in node.attrs
            if name in self.handlers
        ]
        assert len(possible) == 1, "Should be exactly one handler"
        return self.handlers[possible[0]]
    # [/handlers]

    # [helpers]
    def showTag(self, node, closing):
        if closing:
            self.output(f"</{node.name}>")
            return
        self.output(f"<{node.name}")
        for name in node.attrs:
            if not name.startswith("z-"):
                self.output(f' {name}="{node.attrs[name]}"')
        self.output(">")

    def output(self, text):
        self.result.append("UNDEF" if text is None else text)

    def getResult(self):
        return "".join(self.result)
    # [/helpers]
