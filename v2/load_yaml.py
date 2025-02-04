from typing import Any
import yaml

class LoadYaml:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._yaml_cache = None
        self.__load_yaml()
    
    def __load_yaml(self) -> dict[str, Any]:
        if self._yaml_cache is None:  # Load only once
            with open(f'testcases/{self.filename}.yaml') as f:
                self._yaml_cache = yaml.safe_load(f)
        return self._yaml_cache

    def get_test_cases(self) -> list[tuple[str, Any, Any]]:
        """Extracts test cases as a list of tuples (name, input, expected_output)."""
        return [(test["name"], test["input"], test["expected_output"]) for test in self._yaml_cache["tests"]]
    
    def get_timelimit(self) -> int:
        """Extracts timelimit as an int. if not found returns 10."""
        return self._yaml_cache.get("timeout", 10)
    
    def get_value(self, key: str) -> Any:
        """Retrieve a specific key from the loaded YAML data."""
        return self._yaml_cache.get(key, None)  # Return None if key is missing