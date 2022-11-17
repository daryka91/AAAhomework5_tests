## Запуск тестов для функции, возвращающей текущий год

В командной строке запустите команду:
```
python -m pytest -q test_mock.py --cov=what_is_year_now --cov . --cov-report html
```
флаги:

```--cov=what_is_year_now ```- для того, чтобы посмотреть покрытие тестами функции

```--cov . --cov-report html ```- отчет о покрытии в формате html

