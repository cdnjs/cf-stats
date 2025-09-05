def get_template(template_file: str, variables: dict) -> str:
    # Load in template file
    with open("template/" + template_file) as f:
        template = f.read()

    # Substitute in variables
    for key, value in variables.items():
        template = template.replace("{{" + key + "}}", str(value))

    return template
