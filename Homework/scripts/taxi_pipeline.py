import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig


# API doesn't require authentication
@dlt.source
def taxi_pipeline_rest_api_source():
    """Define dlt resources from REST API endpoints for NYC taxi data.
    
    This source loads data from a custom API with:
    - Paginated JSON responses (1,000 records per page)
    - Automatic pagination detection
    - Stops when an empty page is returned
    """
    config: RESTAPIConfig = {
        "client": {
            # Base URL for the REST API
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api",
        },
        "resources": [
            "taxi_trip"
        ],
    }

    yield from rest_api_resources(config)


pipeline = dlt.pipeline(
    pipeline_name='taxi_pipeline',
    destination='duckdb',
    dataset_name="taxi_dataset",
    pipelines_dir='/home/rgc/.dlt/pipelines',
    refresh="drop_sources",
    progress="log",
)


if __name__ == "__main__":
    
    # Extract info
    print("EXTRACT PHASE:")
    print("-" * 60)
    extract_info = pipeline.extract(taxi_pipeline_rest_api_source())

    load_id = extract_info.loads_ids[-1]
    m = extract_info.metrics[load_id][0]
    
    print(f"Resources extracted: {list(m['resource_metrics'].keys())}")
    print(f"Tables created: {list(m['table_metrics'].keys())}")
    print(f"Load ID: {load_id}\n")
    
    for resource, rm in m["resource_metrics"].items():
        print(f"  Resource: {resource}")
        print(f"    Rows extracted: {rm.items_count}")
    
    print()
    
    # Normalize info
    print("NORMALIZE PHASE:")
    print("-" * 60)
    normalize_info = pipeline.normalize()

    load_id = normalize_info.loads_ids[-1]
    m = normalize_info.metrics[load_id][0]
    
    print(f"Load ID: {load_id}\n")
    print("Tables created/updated:")
    for table_name, tm in m["table_metrics"].items():
        # skip dlt internal tables to keep it beginner-friendly
        if table_name.startswith("_dlt"):
            continue
        print(f"  - {table_name}: {tm.items_count} rows")
    
    print()
    
    # Schema info
    print("SCHEMA INFORMATION:")
    print("-" * 60)
    print(f"Default schema name: {pipeline.default_schema_name}")
    print(f"Available schemas: {list(pipeline.schemas.keys())}")
    print()
    
    # Load phase
    print("LOAD PHASE:")
    print("-" * 60)
    load_info = pipeline.load()
    print(f"Load completed successfully")
    print()
    
    # Inspect data
    print("DATA INSPECTION:")
    print("-" * 60)
    ds = pipeline.dataset()
    print(f"Available tables: {ds.tables}")

 # Run the complete ETL pipeline (extract -> normalize -> load)
    load_info = pipeline.run(taxi_pipeline_rest_api_source())
    
    print("=" * 60)
    print("PIPELINE EXECUTION SUMMARY")
    print("=" * 60)
    print(load_info)
    print()

# dlt dashboard to check the pipeline state