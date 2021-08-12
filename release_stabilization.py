import logging

log = logging.getLogger(__name__)


class Callbacks:
    def __init__(self, working_dir, leaf, dry_run):
        self.working_dir = working_dir
        self.leaf = leaf
        self.dry_run = dry_run

    def version_as_leaf(self):
        log.info(f"called version_as_leaf, {self}")
        return self.leaf == 'ksql'

    def __str__(self):
        return f"Callbacks({self.working_dir!r}, {self.leaf!r}, {self.dry_run!r})"
