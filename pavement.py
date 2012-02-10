from paver.easy import *
from paver.path import path
from paver.setuputils import setup
import simplejson as json

sublimation_dir = path(__file__).dirname().abspath()
metadata_file = path(sublimation_dir + "/package-metadata.json")
messages_file = path(sublimation_dir + "/messages.json")

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
def test():
    """run all unit tests"""
    pass


@task
@cmdopts([
    ('message=', 'm', 'Message for messages file')
    ])
def bump_rev(options):
    """--message=[msg] Bump the revision as a part of distribution"""
    if not hasattr(options, 'message'):
        raise Exception("requires --message")

    version = sh("git log --oneline --all | wc -l", capture=True,).strip()

    metadata = json.loads(metadata_file.text())
    metadata['version'] = version

    messages = json.loads(messages_file.text())
    messages[version] = messages['latest']
    del messages['latest']

    metadata_file.write_text(json.dumps(metadata, indent=4, sort_keys=True))
    messages_file.write_text(json.dumps(messages, indent=4, sort_keys=True))

    messages['latest'] = "Some sort of awesome change!"
    messages_file.write_text(json.dumps(messages, indent=4, sort_keys=True))


@task
def tag():
    metadata = json.loads(metadata_file.text())
    _git_tag(metadata['version'])


@task
@cmdopts([
    ('node-version=', 'v', 'Version to install (defaults to 0.6.6)')
])
def foo(options):
    print dir(options)
    print options.foo.keys()
    print options.foo.node_version if hasattr(options.foo, 'node_version') else "v"
