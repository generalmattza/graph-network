#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# Created By  : Matthew Davidson
# Created Date: 2023-01-23
# version ='1.0'
# ---------------------------------------------------------------------------
"""A class to generate padded numerical ids of a specifed length"""
# ---------------------------------------------------------------------------


class IDGenerator:
    def __init__(self, nchars=4):
        self.last_id = -1
        self.nchars = nchars

    def get_new_id(self) -> str:
        self.last_id += 1
        return str(self.last_id).zfill(self.nchars)


def test_IDGenerator():
    _ids = IDGenerator()
    for _ in range(10):
        print(_ids.get_new_id())


if __name__ == "__main__":
    test_IDGenerator()
