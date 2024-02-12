import xml.etree.ElementTree as ET

xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
<xml xmlns="http://www.w3.org/1999/xhtml">
   <block type="global_declaration" id="yMO;O7!`,93F,5dSd0;!" x="-454" y="-251">
      <field name="NAME">notdefinible</field>
   </block>
   <block type="text" id="1|[]1KhNlQN~|4*yMR[p" x="-442" y="-187">
      <field name="TEXT">testando variavel</field>
   </block>
   <yacodeblocks ya-version="223" language-version="36" />
</xml>'''  # Paste your XML string here

root = ET.fromstring(xml_data)

block_types = {
    "text": "string",
    "math_number": "number",
    "math_number_radix": "number",
    "logic_boolean": "boolean",
    "logic_false": "boolean"
}

block_type_counts = {block_type: 0 for block_type in block_types.values()}

for block in root.findall('.//{http://www.w3.org/1999/xhtml}block'):
    block_type = block.get('type')
    if block_type == "global_declaration":
        value_block = block.find('{http://www.w3.org/1999/xhtml}value/{http://www.w3.org/1999/xhtml}block')
        if value_block is not None:
            value_block_type = value_block.get('type')
            if value_block_type in block_types:
                block_type_counts[block_types[value_block_type]] += 1

for block_type, count in block_type_counts.items():
    print(f"{block_type}: {count}")