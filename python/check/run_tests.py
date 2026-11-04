import base64
import importlib.util
import sys
import traceback
import types
import unittest
import zlib
from pathlib import Path

ROOT = Path("/workspace")
FINAL_TASKS = {"08", "09", "10"}
LOAD_ERROR = 2
VISIBLE_FAILED = 3
HIDDEN_FAILED = 4


def load_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_hidden(task):
    packed = (ROOT / "check" / "hidden" / f"{task}.bin").read_bytes()
    source = zlib.decompress(base64.b64decode(packed)).decode("utf-8")
    module = types.ModuleType(f"hidden_{task}")
    exec(compile(source, "скрытые тесты", "exec"), module.__dict__)
    return module


def run_module(module):
    suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    result = unittest.TestResult()
    suite.run(result)
    return result


def test_title(test):
    return test._testMethodName.removeprefix("test_").replace("_", " ")


def failed_tests(result):
    return result.failures + result.errors


def passed_count(result):
    return result.testsRun - len(failed_tests(result))


def report_visible(result):
    print(f"Открытые тесты: пройдено {passed_count(result)} из {result.testsRun}")
    for test, details in failed_tests(result):
        print(f"\n  Не прошёл: {test_title(test)}\n")
        print(details)


def report_hidden(result, task):
    print(f"Скрытые тесты: пройдено {passed_count(result)} из {result.testsRun}")
    if task not in FINAL_TASKS:
        for test, _ in failed_tests(result):
            print(f"  Не прошёл: {test_title(test)}")


def main():
    task, path = sys.argv[1], sys.argv[2]
    try:
        load_file(f"task_{task}", path)
    except BaseException:
        print("Файл с решением не запускается:\n")
        traceback.print_exc(limit=-1, file=sys.stdout)
        return LOAD_ERROR

    visible = run_module(load_file(f"test_{task}", ROOT / "tests" / f"test_{task}.py"))
    report_visible(visible)
    hidden = run_module(load_hidden(task))
    report_hidden(hidden, task)

    if not visible.wasSuccessful():
        return VISIBLE_FAILED
    if not hidden.wasSuccessful():
        return HIDDEN_FAILED
    print("\nЗачёт!")
    return 0


sys.exit(main())
