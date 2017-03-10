#!/bin/sh
echo `cat VERSION` && echo " --> " && echo `semver -i prerelease --preid alpha \`cat VERSION\``
semver -i prerelease --preid alpha `cat VERSION` > VERSION

