from django.utils.text import slugify
from django.template.defaultfilters import slugify as slugify_ru


def slugify(s: str) -> slugify_ru:
    """
    Overriding the standard slugify () function, which also allows
    the use of Russian words in slug.
    Переопределение стандартной функции slugify(), позволяющей также
    использовать русские слова в slug.
    """
    ABC_RU = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
              'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k',
              'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
              'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
              'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
              'я': 'ya'}

    return slugify_ru(''.join(ABC_RU.get(w, w) for w in s.lower()))
