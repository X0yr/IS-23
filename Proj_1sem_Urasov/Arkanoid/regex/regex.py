1. [1-9]+;
2. [А-ЯЁA-Z]{2,};
3. [А-Яа-яёЁ]+[0-9]\w+;
4. [А-Яа-яёЁ][0-9]+;
5. \b[A-ZА-ЯёЁа-я];
6. \b[A-ZА-ЯЁ]\w+;
7. \b[аяуюоеёэиыАЯОЕЁУЭИЫЮ]\w+;
8.\B[1-9]\B;
9..*\*.*;
10. .*[(].*[)].*;
11. .*[<].*[;];
12. \w+[А-ЯA-Zа-я].*[<]
13. [^\S ]
14. .*[<].*[:];
