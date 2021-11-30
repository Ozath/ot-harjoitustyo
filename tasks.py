from invoke import task

@task
def start(ctx):
    with ctx.cd("./src"):
        ctx.run("python3 index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task()
def coverage_report(ctx):
    ctx.run("coverage html")
