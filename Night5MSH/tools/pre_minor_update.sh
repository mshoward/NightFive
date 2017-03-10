#!/bin/sh
echo `cat VERSION` && echo " --> " && echo `semver -i preminor --preid alpha \`cat VERSION\``
semver -i preminor --preid alpha `cat VERSION` > VERSION


