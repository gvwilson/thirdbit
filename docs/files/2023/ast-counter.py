import ast
import sys

tree = ast.parse(sys.stdin.read())
names = {n.__class__.__name__ for n in ast.walk(tree)}
print(len(names))
