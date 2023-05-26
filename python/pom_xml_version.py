#!/usr/bin/env python3
import xml.etree.ElementTree
from xml.etree.ElementTree import parse

NAMESPACES = {
    "xmlns": "http://maven.apache.org/POM/4.0.0",
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xsi:schemaLocation": "http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"
}

VERSION_TAG = "xmlns:version"


def version_to_string(version: (int, int, int, str)) -> str:
    suffix = version[3]
    return f"{version[0]}.{version[1]}.{version[2]}" + f"-{suffix}" if suffix else ""


def get_pom_version(pom_file_path: str) -> (int, int, int, str):
    tree = parse(pom_file_path)
    root = tree.getroot()
    version_element = root.find(VERSION_TAG, NAMESPACES)
    if version_element is None:
        raise ValueError(f'Element "{VERSION_TAG}" not found in file "{pom_file_path}"')
    version_list = version_element.text.split("-")
    version_main_list = version_list[0].split(".")
    version_suffix = version_list[1] if len(version_list) > 1 else None
    return int(version_main_list[0]), int(version_main_list[1]), int(version_main_list[2]), version_suffix


def set_pom_version(pom_file_path: str, version: str):
    tree = parse(pom_file_path)
    root = tree.getroot()
    version_element = root.find(VERSION_TAG, NAMESPACES)
    if version_element is None:
        raise ValueError(f'Element "{VERSION_TAG}" not found in file "{pom_file_path}"')
    version_element.text = version_to_string(version)
    xml.etree.ElementTree.register_namespace("", NAMESPACES["xmlns"])  # prevent adding ns0 to all elements
    tree.write(pom_file_path)


def increment_version_major(version: (int, int, int, str)) -> (int, int, int, str):
    return version[0] + 1, 0, 0, version[3]


def increment_version_minor(version: (int, int, int, str)) -> (int, int, int, str):
    return version[0], version[1] + 1, 0, version[3]


def increment_version_patch(version: (int, int, int, str)) -> (int, int, int, str):
    return version[0], version[1], version[2] + 1, version[3]
