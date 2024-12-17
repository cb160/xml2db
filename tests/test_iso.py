import os

import pytest
from lxml import etree

from xml2db import DataModel
from pathlib import Path

def test_create_iso_model():
    """A test for roundtrip insert to the database from and to XML"""
    
    xsd = Path("./tests/sample_models/iso/xsd/pain/pain.008.001.11.xsd")

    # Use sample_models/iso/xsd/pain.008.001.02.xsd
    model = DataModel(
         xsd_file=xsd,
         short_name="iso",
         connection_string="sqlite:///:memory:",
         db_schema="test_xml2db",
         model_config={},
    )
    assert model is not None
    
    print(model.get_entity_rel_diagram())

    
if __name__ == "__main__":
    test_create_iso_model()