import xml.etree.ElementTree as ET

def analise_bky(data_bky):
    xml_data = data_bky

    root = ET.fromstring(xml_data)

    # Blocos de variáveis globais, funções e procedimentos
    block_types_global = {
        "component_event": "component_event",
        "global_declaration": "global_variables",
        "procedures_defnoreturn": "procedure",
        "procedures_defreturn": "function",
    }

    block_types_global_counts = {block_type: 0 for block_type in block_types_global.values()}

    for block in root.findall('.//{http://www.w3.org/1999/xhtml}block'):
        block_type = block.get('type')
        if block_type in block_types_global:
            block_types_global_counts[block_types_global[block_type]] += 1


    # Blocos dentro de eventos de componentes, funções ou procedimentos.
    block_types_component_event = {
        "local_declaration_statement": "local_variables",
        "local_declaration_expression": "local_variables",
        "controls_if": "if",
        "controls_choose": "if",
        "elseif": "elseif",
        "else": "else",
        "logic_operations": "logic_operations",
        "logic_boolean": "boolean",
        "logic_false": "boolean",
        "controls_forRange": "foreach",
        "controls_forEach": "foreach",
        "controls_while": "while",
        "math_number": "number",
        "math_number_radix": "number",
        "math_operations": "math_operations",
        "text": "string",
        "text_operations": "text_operations",
        "lists_create_with": "list",
        "lists_is_empty": "list",
        "list_operations": "list_operations",
        "component_method": "component_method",
        "component_set_get": "component_set_get",
        "helpers_assets": "helpers_assets",
        "lexical_variable_set": "lexical_variable_set",
        "lexical_variable_get": "lexical_variable_get"
    }

    block_type_counts = {block_type: 0 for block_type in block_types_component_event.values()}

    for event_block in root.findall('.//{http://www.w3.org/1999/xhtml}block'): 
        if event_block.get('type') == "component_event" or event_block.get('type') == "procedures_defreturn" or event_block.get('type') == "procedures_defnoreturn" or event_block.get('type') == "global_declaration":
            for block in event_block.findall('.//{http://www.w3.org/1999/xhtml}block'):
                block_type = block.get('type')
                if block_type in block_types_component_event:
                    block_type_counts[block_types_component_event[block_type]] += 1
                    # Verificar if, else e else if
                    if block_type == "controls_if":
                        mutation = block.find(".//{http://www.w3.org/1999/xhtml}mutation")
                        if mutation is not None:
                            else_attr = mutation.get('else')
                            elseif_attr = mutation.get('elseif')
                            if else_attr is not None:
                                block_type_counts["else"] += int(else_attr)
                            if elseif_attr is not None:
                                block_type_counts["elseif"] += int(elseif_attr)
                    elif block_type == "controls_choose":
                        block_type_counts["else"] += 1
                elif block_type.startswith("logic_"):
                    block_type_counts["logic_operations"] += 1
                elif block_type.startswith("math_"):
                    block_type_counts["math_operations"] += 1
                elif block_type.startswith("text_"):
                    block_type_counts["text_operations"] += 1
                elif block_type.startswith("lists_"):
                    block_type_counts["list_operations"] += 1

    data = []

    for block_type, count in block_types_global_counts.items():
        data.append([block_type, count])

    for block_type, count in block_type_counts.items():
        data.append([block_type, count])

    return data
