from lxml import etree


def build_minimal_ecf_xml(data: dict) -> bytes:
    """Build a minimal XML root for future DGII e-CF mapping."""
    root = etree.Element("ECF")
    for key, value in (data or {}).items():
        child = etree.SubElement(root, str(key))
        child.text = "" if value is None else str(value)
    return etree.tostring(root, encoding="UTF-8", xml_declaration=True, pretty_print=True)
