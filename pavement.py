import os
from paver.easy import *
from paver.path import path
from paver.setuputils import setup
import simplejson as json

sublimation_dir = path(__file__).dirname().abspath()

setup(
    name="Sublimation",
    packages=['sublimation'],
    version="Today",
    url="https://NorthIsUp@github.com/NorthIsUp/Sublimation.git",
    author="Adam Hitchcock",
    author_email="adam@northisup.com"
)


def _git_tag(tag):
    sh("git tag '%s'" % tag)


def _git_amend():
    sh("git commit --amend -aC HEAD")


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
    revision_count = sh("git log --oneline --all | wc -l", capture=True,).strip()
    project_version = sh("git describe --tags --long", capture=True).strip()

    version = "-".join((project_version, revision_count))

    metadata_file = path(sublimation_dir + "/package-metadata.json")
    messages_file = path(sublimation_dir + "/messages.json")

    metadata = json.loads(metadata_file.text())
    metadata['version'] = version

    messages = json.loads(messages_file.text())
    messages[version] = messages['latest']
    del messages['latest']

    metadata_file.write_text(json.dumps(metadata, indent=4, sort_keys=True))
    messages_file.write_text(json.dumps(messages, indent=4, sort_keys=True))

    messages['latest'] = "Some sort of awesome change!"
    messages_file.write_text(json.dumps(messages, indent=4, sort_keys=True))

    print version
    # _git_amend()  # save the new version number
    # _git_tag(metadata['version'])


@task
def test():
    """run all unit tests"""
    pass


@task
@cmdopts([
    ('node-version=', 'v', 'Version to install (defaults to 0.6.6)')
])
def foo(options):
    print dir(options)
    print options.foo.keys()
    print options.foo.node_version if hasattr(options.foo, 'node_version') else "v"
