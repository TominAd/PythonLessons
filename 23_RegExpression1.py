
import re
mytext = "AWS Security Specialty, AWS Solutions Architect Associate, AWS Developer  Associate," \
         "MTA  Windows Server Administration, yandex, LPI  LInux Essentials, SumoLogic Admin," \
         " New Relic Performance.Pro, Google Cloud Platform  Associate Cloud Engineer," \
         " Google Cloud Platform  Professional Cloud Architect, Microsoft Azure: Azure Fundamentals," \
         " HashiCorp Certified Terraform Associate, yandex "

"""
\d = Any Digit 0-9 (Любая цифра)
\D = Any non DIGIT (любой символ но НЕ ЦИФРА) 
\w = Any Alphabet symbol [A-Z a-z] (любой алфаыитный символ)
\W = Any non Alphabet symbol (то угодно но не алфавитный символ)
\s = breakspace (поиск пробелов)
\S = non breakspace (кроме пробелов)

[0-9]{3} 
[A-Z]{5} только 5 символов
[A-Z][a-z]+ (для поиска с большое буквы дальше маленька и + дает возможность до конца слова)
\w+\.\w+ (для поиска . пример Performance.Pro

"""


textloolfor = r"\w+\.\w+"
allresults = re.findall(textloolfor, mytext)
print(allresults)