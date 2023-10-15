import yaml
import os

def generate_sql_staging_file(table_name, columns):
    sql_template = f"with final as (\n{columns}\n)\nselect * from final"
    return sql_template

def main(yaml_file):
    with open(yaml_file, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            tables = data.get('tables', {})
            for table_name, table_info in tables.items():
                columns = table_info.get('columns', {})
                columns_sql = ',\n'.join([f"  {col}: {col_info['data_type']}" for col, col_info in columns.items()])
                sql_content = generate_sql_staging_file(table_name, columns_sql)
                sql_file_name = f"{table_name}_staging.sql"
                with open(sql_file_name, 'w') as sql_file:
                    sql_file.write(sql_content)
                    print(f"Generated SQL staging file: {sql_file_name}")
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == "__main__":
    yaml_file = "/Users/crlough/Code/GitHub/bird-finder-app/ingestion/schemas/export/ebirdapi_source.schema.yaml"
    main(yaml_file)
