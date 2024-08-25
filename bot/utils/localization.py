import os

import yaml


def load_language_data(lang_code):
    base_dir = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(base_dir, 'locales', f'{lang_code}.yml')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Warning: Language file not found: {file_path}")
        return {}


language_data = {
    'en': load_language_data('en'),
    'ru': load_language_data('ru')
}


def get_string(language):
    def inner(key):
        return language_data.get(language, language_data['en']).get(key, key)
    return inner


# Для отладки
print("Available languages:", list(language_data.keys()))
print("English data:", language_data['en'])
print("Russian data:", language_data['ru'])
