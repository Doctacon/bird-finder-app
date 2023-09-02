import dlt
from dlt.sources.helpers import requests
import requests as req

@dlt.source
def ebirdapi_source(loc_code: str = 'US-WA', api_secret_key=dlt.secrets.value):
    return (
        recent_observations(loc_code, api_secret_key),
        taxonomy(api_secret_key),
        taxa_local_codes(api_secret_key),
        taxonomy_versions(api_secret_key)
    )

def _create_auth_headers(api_secret_key):
    """Constructs Bearer type authorization header which is the most common authorization method"""
    headers = {"X-eBirdApiToken": f"{api_secret_key}"}
    return headers

@dlt.resource(write_disposition="replace")
def recent_observations(loc_code: str, api_secret_key=dlt.secrets.value):
    headers = _create_auth_headers(api_secret_key)

    ebird_api_url = f'https://api.ebird.org/v2/data/obs/{loc_code}/recent/notable?detail=full'

    try:
        response = req.get(ebird_api_url, headers=headers) #, params=params
        response.raise_for_status()
        data = response.json()
        yield data

    except req.exceptions.RequestException as e:
        print("Error fetching data from eBird API:", e)
        yield []

@dlt.resource(write_disposition="replace")
def taxonomy(api_secret_key=dlt.secrets.value):
    headers = _create_auth_headers(api_secret_key)

    ebird_api_url = 'https://api.ebird.org/v2/ref/taxonomy/ebird'

    try:
        response = req.get(ebird_api_url, headers=headers) #, params=params
        response.raise_for_status()
        data = response.json()
        yield data

    except req.exceptions.RequestException as e:
        print("Error fetching data from eBird API:", e)
        yield []

@dlt.resource(write_disposition="replace")
def taxa_local_codes(api_secret_key=dlt.secrets.value):
    headers = _create_auth_headers(api_secret_key)

    ebird_api_url = 'https://api.ebird.org/v2/ref/taxa-locales/ebird'

    try:
        response = req.get(ebird_api_url, headers=headers) #, params=params
        response.raise_for_status()
        data = response.json()
        yield data

    except req.exceptions.RequestException as e:
        print("Error fetching data from eBird API:", e)
        yield []

@dlt.resource(write_disposition="replace")
def taxonomy_versions(api_secret_key=dlt.secrets.value):
    headers = _create_auth_headers(api_secret_key)

    ebird_api_url = 'https://api.ebird.org/v2/ref/taxonomy/versions'

    try:
        response = req.get(ebird_api_url, headers=headers) #, params=params
        response.raise_for_status()
        data = response.json()
        yield data

    except req.exceptions.RequestException as e:
        print("Error fetching data from eBird API:", e)
        yield []

if __name__ == "__main__":
    # Configure the pipeline with your destination details
    pipeline = dlt.pipeline(
        pipeline_name='ebirdapi',
        destination='duckdb',
        dataset_name='ebirdapi_data',
        import_schema_path="schemas/import",
        export_schema_path="schemas/export",
    )

    # Run the pipeline with your parameters
    load_info = pipeline.run(ebirdapi_source())

    # Pretty print the information on data that was loaded
    print(load_info)
