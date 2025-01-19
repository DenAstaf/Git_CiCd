В данном проекте реализован FastApi.<br>
Используется pylint, pytest и pytest-cov.

1. pylint (для приведения проекта в стандарт):
<br>Запуск: `pylint $(git ls-files '*.py')`
2. pytest и pytest-cov (для тестирования функционала и проверки на сколько покрыт тестами функционал)
<br>Запуск: `pytest -s --cov --cov-report html --cov-fail-under=50`

В GitHub выполняются Actions Pylint и Pytest за счет настроенных .yml.