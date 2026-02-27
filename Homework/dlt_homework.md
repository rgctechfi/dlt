# Homework: Build Your Own dlt Pipeline

You've seen how to build a pipeline with a scaffolded source. Now it's your turn to do it from scratch with a **custom API**.

## Workshop Content

* [Workshop README](README.md)
* [dlt Pipeline Overview Notebook (Google Colab)](https://colab.research.google.com/github/anair123/data-engineering-zoomcamp/blob/workshop/dlt_2026/cohorts/2026/workshops/dlt/dlt_Pipeline_Overview.ipynb)
* [Workshop registration page](https://luma.com/hzis1yzp)

---

## Questions & Answers

Once your pipeline has run successfully, use the methods covered in the workshop to investigate the following questions.

### Question 1: What is the start date and end date of the dataset?

- 2009-01-01 to 2009-01-31
- 2009-06-01 to 2009-07-01
- 2024-01-01 to 2024-02-01
- 2024-06-01 to 2024-07-01

Selected answer:

```text
Justification: [Your answer and justification here]

dates = yellow_trips.aggregate([
    yellow_trips.pickup_datetime.min(),
    yellow_trips.pickup_datetime.max()
]).execute()
print('Q1 - Dates:', dates)
```

<p align="center">
  <img src="https://img.shields.io/badge/Answer-(2009-06-01 to 2009-07-01)-darkgreen" alt="Answer Q1">
</p>

---

### Question 2: What proportion of trips are paid with credit card?

- 16.66%
- 26.66%
- 36.66%
- 46.66%

Selected answer:

```text
Justification: [Your answer and justification here]
```

<p align="center">
  <img src="https://img.shields.io/badge/Answer-26.66%-darkgreen" alt="Answer Q2">
</p>

---

### Question 3: What is the total amount of money generated in tips?

- $4,063.41
- $6,063.41
- $8,063.41
- $10,063.41

Selected answer:

```text
Justification: [Your answer and justification here]
```

<p align="center">
  <img src="https://img.shields.io/badge/Answer-[SELECT YOUR ANSWER]-darkgreen" alt="Answer Q3">
</p>

---

## Investigation Methods

You can use any of these methods to answer the questions:

- **dlt Dashboard**: `dlt pipeline taxi_pipeline show`
- **dlt MCP Server**: Ask the agent questions about your pipeline
- **Marimo Notebook**: Build visualizations and run queries
- **DuckDB Direct**: Query the local database directly

We challenge you to try out the different methods explored in the workshop when answering these questions to see what works best for you. Feel free to share your thoughts on what worked (or didn't) in your submission!


### Resources

| Resource | Link |
|----------|------|
| dlt Dashboard Docs | [dlthub.com/docs/general-usage/dashboard](https://dlthub.com/docs/general-usage/dashboard) |
| marimo + dlt Guide | [dlthub.com/docs/general-usage/dataset-access/marimo](https://dlthub.com/docs/general-usage/dataset-access/marimo) |
| dlt Documentation | [dlthub.com/docs](https://dlthub.com/docs) |

---

## Submitting the Solutions

- Form for submitting: https://courses.datatalks.club/de-zoomcamp-2026/homework/dlt
- Deadline: See the website

---

## Tips

- The API returns paginated data. Make sure your pipeline handles pagination correctly.
- If the agent gets stuck, paste the error into the chat and let it debug.
- Use the dlt MCP server to ask questions about your pipeline metadata.

---

## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public".

Read more about the benefits [here](https://alexeyondata.substack.com/p/benefits-of-learning-in-public-and).

### Example post for LinkedIn

```
🚀 dlt Workshop of Data Engineering Zoomcamp by @DataTalksClub complete!

Just finished the Data Ingestion workshop with @dltHub. Learned how to:

✅ Build REST API data pipelines with dlt
✅ Use AI-assisted development with dlt MCP Server
✅ Load paginated API data into DuckDB
✅ Inspect pipeline data with dlt Dashboard and marimo notebooks

Built a full NYC taxi data pipeline from a custom API - AI-assisted data engineering is the future!

Here's my homework solution: <LINK>

Following along with this amazing free course - who else is learning data engineering?

You can sign up here: https://github.com/DataTalksClub/data-engineering-zoomcamp/
```

### Example post for Twitter/X

```
🔄 dlt Workshop of Data Engineering Zoomcamp done!

- REST API pipelines with @dltHub
- AI-assisted pipeline building
- DuckDB as local data warehouse
- dlt Dashboard & marimo notebooks

My solution: <LINK>

Free course by @DataTalksClub: https://github.com/DataTalksClub/data-engineering-zoomcamp/
```
