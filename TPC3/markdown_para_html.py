import re

def markdown_para_html(markdown_text):
    markdown_text = re.sub(r"^# (.*)", r"<h1>\1</h1>", markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r"^## (.*)", r"<h2>\1</h2>", markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r"^### (.*)", r"<h3>\1</h3>", markdown_text, flags=re.MULTILINE)
    
    markdown_text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", markdown_text)
    
    markdown_text = re.sub(r"\*(.*?)\*", r"<i>\1</i>", markdown_text)
    
    markdown_text = re.sub(r'(?<=\n)(\d+\.) (.+?)(?=\n\n|\n\s*\d+\.)', r'<li>\2</li>', markdown_text)
    markdown_text = re.sub(r'(\n<li>.+?</li>)+', r'\n<ol>\g<0>\n</ol>', markdown_text)

    markdown_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown_text)

    markdown_text = re.sub(r"\[([^\]]+)\]\((.*?)\)", r'<a href="\2">\1</a>', markdown_text)
    
    return markdown_text

def converter_markdown_para_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    html_text = markdown_para_html(markdown_text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_text)

    print(f"Arquivo HTML gerado em: {output_file}")

input_file = 'teste.md'
output_file = 'saida_do_teste.html'

converter_markdown_para_html(input_file, output_file)
