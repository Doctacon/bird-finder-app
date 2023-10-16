import yaml
import os

def generate_sql_staging_file(table_name, columns):
    sql_template = f"with final as (\n    select\n{columns}\n    from {{{{ source('ebirdapi', '{table_name}') }}}}\n)\nselect * from final"
    return sql_template

def main(yaml_file):
    with open(yaml_file, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            tables = data.get('tables', {})
            output_folder = "transformation/models/staging"
            os.makedirs(output_folder, exist_ok=True)
            
            for table_name, table_info in tables.items():
                columns = ',\n'.join([f"        {col} as '{col}'" for col in table_info.get('columns', {}).keys()])
                sql_content = generate_sql_staging_file(table_name, columns)
                sql_file_name = os.path.join(output_folder, f"{table_name}.sql")
                with open(sql_file_name, 'w') as sql_file:
                    sql_file.write(sql_content)
                    print(f"Generated SQL staging file: {sql_file_name}")
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == "__main__":
    yaml_file = "/Users/crlough/Code/GitHub/bird-finder-app/ingestion/schemas/export/ebirdapi_source.schema.yaml"  # Replace with the path to your YAML file
    main(yaml_file)
