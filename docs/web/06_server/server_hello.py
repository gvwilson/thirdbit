"""Hello server."""

from flask import Flask

HELLO = """\
<html>
<body>
<h1>Hello</h1>
</body>
</html>
"""


app = Flask("hello")


@app.route("/")
def root():
    return HELLO
