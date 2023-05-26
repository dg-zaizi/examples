#!/usr/bin/env python3
import sys
import pom_xml_version

test_file = sys.argv[1] if len(sys.argv) > 1 else "pom.xml"
result = pom_xml_version.get_pom_version(test_file)
print(f"result={result}")
print(f"pom_xml_version.version_to_string(result)={pom_xml_version.version_to_string(result)}")

new_version = pom_xml_version.increment_version_patch(result)
print(f"new_version={new_version}")
pom_xml_version.set_pom_version(test_file, new_version)
result = pom_xml_version.get_pom_version(test_file)
print(f"result={result}")
print(f"pom_xml_version.version_to_string(result)={pom_xml_version.version_to_string(result)}")

new_version = pom_xml_version.increment_version_minor(result)
print(f"new_version={new_version}")
pom_xml_version.set_pom_version(test_file, new_version)
result = pom_xml_version.get_pom_version(test_file)
print(f"result={result}")
print(f"pom_xml_version.version_to_string(result)={pom_xml_version.version_to_string(result)}")

new_version = pom_xml_version.increment_version_major(result)
print(f"new_version={new_version}")
pom_xml_version.set_pom_version(test_file, new_version)
result = pom_xml_version.get_pom_version(test_file)
print(f"result={result}")
print(f"pom_xml_version.version_to_string(result)={pom_xml_version.version_to_string(result)}")

pom_xml_version.set_pom_version(test_file, new_version)
