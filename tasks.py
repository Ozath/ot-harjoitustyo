from invoke import task

@task
def start(ctx):
    with ctx.cd("./src"):
        ctx.run("python3 index.py")

@task
def build(ctx):
    ctx.run("python3 src/build.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
