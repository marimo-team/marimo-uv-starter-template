import marimo

__generated_with = "0.19.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A marimo notebook

    You can import your library code.
    """)
    print("hello script notebook")
    return


@app.cell
def _():
    from marimo_template.utils import add

    return (add,)


@app.cell
def _(add):
    add(1, 2)
    return


if __name__ == "__main__":
    app.run()
