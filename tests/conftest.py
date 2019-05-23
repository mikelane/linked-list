import logging
from pathlib import Path

import pytest

logger = logging.getLogger(__name__)


pytest_plugins = ['tests.fixtures']


class NoTestsFoundError(Exception):
    pass


@pytest.fixture(scope='session', autouse=True)
def root_dir():
    """The full path to the project root directory
    """
    return Path(__file__).resolve().parent.parent
