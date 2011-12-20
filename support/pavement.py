from paver.easy import *
from paver.setuputils import setup
from datetime import datetime
from pprint import pprint
try:
    import simplejson as json
except Exception, e:
    import json

setup(
    name="Sublimation",
    packages=['sublimation'],
    version="Today",
    url="https://NorthIsUp@github.com/NorthIsUp/Sublimation.git",
    author="Adam Hitchcock",
    author_email="adam@northisup.com"
)


def _git_amend():
    sh("git commit --amend -C HEAD")


def _git_push():
    sh("git push")


@task
@needs(['bump_rev'])
def dist():
    """Generate docs and source distribution."""
    _git_push()


@task
@needs('paver.doctools.html')
def html():
    """Build Paver's documentation and install it into paver/docs"""
    builtdocs = path("docs") / options.sphinx.builddir / "html"
    destdir = path("paver") / "docs"
    destdir.rmtree()
    builtdocs.move(destdir)


@task
def bump_rev():
    """Bump the revision as a part of distribution"""
    metadata_file = path("../package-metadata.json")
    metadata = json.loads(metadata_file.text())
    metadata['version'] = sh("git reflog --all | wc -l", capture=True,).strip()
    metadata_file.write_text(json.dumps(metadata, indent=4, sort_keys=True))
    _git_amend()  # save the new version number
    sh("git tag %s" % metadata['version'])


@task
def test():
    """run all unit tests"""
    pass
