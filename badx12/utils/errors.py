# -*- coding: utf-8 -*-
import json


class FieldValidationError(Exception):
    """Exception raised for errors in the input.
    Attributes:
        segment -- segment in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, segment, msg):
        self.segment = segment
        self.msg = msg

    def __str__(self) -> str:
        return "segment:'{}', message:'{}'".format(self.segment, self.msg)

    def __repr__(self) -> str:
        return self.__str__()


class IDMismatchError(Exception):
    """Exception raised for errors in the input.
        Attributes:
            segment -- segment in which the error occurred
            msg  -- explanation of the error
        """

    def __init__(self, segment, msg):
        self.segment = segment
        self.msg = msg


class SegmentCountError(Exception):
    """Exception raised for errors in the input.
        Attributes:
            segment -- segment in which the error occurred
            msg  -- explanation of the error
        """

    def __init__(self, segment, msg):
        self.segment = segment
        self.msg = msg


class InvalidFileTypeError(Exception):
    """Exception raised for errors in the input.
    Attributes:
        segment -- segment in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, segment, msg):
        self.expr = segment
        self.msg = msg


class SegmentTerminatorNotFoundError(Exception):
    """Exception raised for errors in the Interchange Header.
    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg
