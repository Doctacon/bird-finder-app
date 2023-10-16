import yaml
import os

def generate_sql_staging_file(table_name, columns, reserved_words):
    def format_column_name(column_name):
        if column_name in reserved_words:
            return f'"{column_name}"'
        else:
            return column_name
    
    formatted_columns = ',\n'.join([f"        {format_column_name(col)} as '{col}'" for col in columns])
    sql_template = f"with final as (\n    select\n{formatted_columns}\n    from {{{{ source('ebirdapi', '{table_name}') }}}}\n)\nselect * from final"
    return sql_template

def main(yaml_file):
    with open(yaml_file, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            tables = data.get('tables', {})
            reserved_words = ["unique", "primary", "order", "name"]  # Add your list of reserved words here
            output_folder = "transformation/models/staging"
            os.makedirs(output_folder, exist_ok=True)
            
            for table_name, table_info in tables.items():
                columns = [col for col in table_info.get('columns', {}).keys()]
                sql_content = generate_sql_staging_file(table_name, columns, reserved_words)
                sql_file_name = os.path.join(output_folder, f"{table_name}.sql")
                with open(sql_file_name, 'w') as sql_file:
                    sql_file.write(sql_content)
                    print(f"Generated SQL staging file: {sql_file_name}")
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == "__main__":
    yaml_file = "/Users/crlough/Code/GitHub/bird-finder-app/ingestion/schemas/export/ebirdapi_source.schema.yaml"  # Replace with the path to your YAML file
    main(yaml_file)
