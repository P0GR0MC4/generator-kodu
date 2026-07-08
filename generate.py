import json
from jinja2 import Environment, FileSystemLoader

TYPE_MAPPING = {
    "int": "i",     # 4 bajty integer
    "float": "f",   # 4 bajty float
}

def load_interface(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def generate_code():
    data = load_interface('interface.json')

    struct_format = "".join([TYPE_MAPPING[field['type']] for field in data['fields']])
    data['struct_format'] = struct_format

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.py.jinja2')

    rendered_code = template.render(data)

    output_filename = "generated_codec.py"
    with open(output_filename, 'w') as f:
        f.write(rendered_code)

    print(f"Sukces! Wygenerowano plik: {output_filename}")

if __name__ == "__main__":
    generate_code()