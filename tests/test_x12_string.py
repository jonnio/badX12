import json

import pytest

from badx12 import Parser
from badx12.utils import FieldValidationError
from tests.utils import TEST_FILE_DIR, TEST_271_STRING


@pytest.fixture
def test_files():
    return {
        "edi": list((TEST_FILE_DIR / "edi").glob("*.edi")),
        "errors": TEST_FILE_DIR / "errors",
    }


def test_edi(test_files):
    files = test_files["edi"]
    assert len(files) > 0

    for file in files:
        with open(file, 'r') as x12File:
            document = x12File.read().strip()

            parser = Parser(document)

            assert parser.document.text != ""
            assert parser.document.interchange is not None

            report = parser.document.validate()
            assert report.is_document_valid() is True
            assert len(report.error_list) == 0
            assert parser.document.format_as_edi() != ""


def test_edi_271():
    parser = Parser(TEST_271_STRING)
    assert parser.document.text != ""
    assert parser.document.interchange is not None

    report = parser.document.validate()
    if len(report.error_list) > 0:
        print(report.error_list)
    assert report.is_document_valid() is True
    assert len(report.error_list) == 0
    assert parser.document.format_as_edi() != ""
    # print(parser.document.format_as_edi())
    # print(json.dumps(parser.document.to_dict(), indent=2))
    print(json.dumps(parser.document.to_dict(minimal=True), indent=2))


def test_to_validation_error_string():
    errs = [FieldValidationError('segment-error', 'error-message'),
            FieldValidationError('2segment-2error', '2error-2message')]
    print(errs)
    s = str(errs)
    assert s != ''
    assert 'segment-error' in s
    assert '2segment-2error' in s
    assert 'error-message' in s
    assert '2error-2message' in s
