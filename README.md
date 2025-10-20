# Product Rating Report Generator

Программа для генерации отчётов о среднем рейтинге и цене брендов из CSV-файлов.

## Установка

```bash
git clone https://github.com/hyd3-me/py_jun_test_20.10.git source
python -m venv env
source env/bin/activate
cd source
pip install -r requirements.txt
```

## Запуск

```bash
python src/main.py --files file1.csv file2.csv --report average-rating
python src/main.py --files products1.csv products2.csv --report average-rating
```

## Структура проекта
```
source/
├── src/
│   ├── cli.py                 # Обработка аргументов
│   ├── main.py                # Точка входа
│   ├── parsers/
│   │   └── csv_parser.py      # Чтение CSV
│   └── reports/
│       ├── base.py            # Абстрактный класс отчёта
│       ├── manager.py         # Менеджер отчётов
│       ├── average_rating.py  # Отчёт по среднему рейтингу
│       └── average_price.py   # Отчёт по средней цене
├── tests/
│   ├── conftest.py            # Фикстуры для тестов
│   ├── test_cli.py
│   ├── test_csv_parser.py
│   ├── test_main.py
│   └── test_reports/
│       ├── test_average_rating.py
│       ├── test_average_price.py
│       └── test_manager.py
├── requirements.txt
└── README.md
```

## Как добавить новый отчет

```
- Создайте класс, наследующийся от BaseReport.
- Реализуйте метод generate.
- Зарегистрируйте отчёт в ReportManager.
```

### Пример:

```
from reports.base import BaseReport

class NewReport(BaseReport):
    def generate(self, data):
        return "..."
```

## Тесты

### Покрытие тестами
![alt text](/images/image.png)

```
python -m pytest tests/
```

## Примеры запуска скрипта:

### отчет для двух файлов по среднему рейтингу

![alt text](/images/image-1.png)

### новый отчет для двух файлов по средней цене

![alt text](/images/image-2.png)