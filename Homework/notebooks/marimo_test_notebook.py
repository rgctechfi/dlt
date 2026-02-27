import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import duckdb

    DATABASE_URL = "taxi_pipeline.duckdb"
    engine = duckdb.connect(DATABASE_URL, read_only=False)
    return (engine,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Caracteristics
    """)
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT COUNT(*) AS row_number
        FROM "taxi_dataset"."taxi_trip";
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT
          column_name,
          data_type,
          is_nullable,
          column_default
        FROM information_schema.columns
        WHERE table_schema = 'taxi_dataset'
          AND table_name = 'taxi_trip'
        ORDER BY ordinal_position;
        """,
        engine=engine
    )
    return


@app.cell(hide_code=True)
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM "taxi_dataset"."taxi_trip" LIMIT 100
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT "tip_amt" FROM "taxi_dataset"."taxi_trip" LIMIT 100
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT SUM(total_amt) as total_tips
        FROM "taxi_dataset"."taxi_trip";
        """,
        engine=engine
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
