#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake

class ConantestConan(ConanFile):
    name = "conantest"
    version = "0.1"
    generators = "cmake"
    exports_sources = "*"
    no_copy_source = True
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        self.copy("*.hpp")
    
    def package_id(self):
        self.info.header_only()
