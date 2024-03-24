from nox_poetry import session


@session(python="3.11")
def type_check(session):
    session.install("pydantic")
    session.install("mypy")
    session.run("mypy", ".")


@session(python="3.11")
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", ".")


@session(python="3.11")
def format(session):
    session.install("ruff")
    session.run("ruff", "format", ".")

@session(python="3.11")
def sort(session):
    session.install("isort")
    session.run("isort", ".")
