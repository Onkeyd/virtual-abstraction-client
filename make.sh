#!/bin/bash

function print_help {
    echo "Builds the Virtual Abstraction Client"
    echo "-c  | --clean     : Clean build environment hard, including deleting the 'build' and 'install' folders."
}

VAC_DIR=$(dirname "$(readlink -f "$0")")

cd `dirname $0`
mkdir -p build
cd build

TOP_TARGET="install"

# Evaluate input args
while [ $# -gt 0 ] ; do
    if [ "$1" = "--help" -o "$1" = "-h" ]; then
        print_help
        exit 0
    elif [ "$1" = "--clean" -o "$1" = "-c" ] ; then
        TOP_TARGET="clean"
        shift
    else
        print_help
        exit 0
    fi
done

if [ "$TOP_TARGET" = "install" ]; then
    if [ ! -z "$1" ]; then
        cmake --target "$1" ../
    else
        cmake ../
    fi
    make -j `nproc` $*
elif [ "$TOP_TARGET" = "clean" ]; then
    cd $VAC_DIR
    echo -e "rm -rf build"
    rm -rf build
    echo -e "rm -rf bin"
    rm -rf bin
fi
