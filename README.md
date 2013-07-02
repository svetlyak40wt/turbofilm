Качатель фильмов с turbofilm.tv
===============================

Если ты являетешься счастливым обладателем аккаунта на [turbofilm.tv][tv], но по каким-то причинам
не можешь/хочешь смотреть сериалы online (я, например, предпочитаю делать это в общественном транспорте),
то эти скрипты для тебя.

Состав проекта
--------------

Тут всего три скрипта:

* `get-film` на JavaScript. Это основа основ. Он использует [Phantome.js][]
  для того, чтобы залогиниться на [турбофильм][tv] и достать оттуда ссылки
  на видео и субтитры, на выходе он генерит баш скрипт, качающий файлы
  через curl, и объединяющий видео и субтитры в один mp4 файл (годный
  для просмотра на ipad), с помощью [HandBrakeCLI][].
* `convert.py` конвертирует субтитры из кастомного xml формата
  турбофильма, в человеческий srt.
* `get-my-films` это скрипт на баше, который использует предыдущие два
  скрипта для того, чтобы скачать все указанные в командной строке
  сериалы.
  
Как их использовать
-------------------

* Для начала, создай в текущей директории файл `settings`, на основе
`settings.example`.
* Затем, установи [Phantom.js][] и [HandBrakeCLI][]. Первый я ставил
  используя homebrew, второй просто из пакета для OSX.
* Всё, после этого запусти в командной строке что-то вроде:

      ./get-my-films https://turbofilm.tv/Watch/Futurama/Season7/Episode15 https://turbofilm.tv/Watch/Futurama/Season7/Episode16

  Если всё пройдет хорошо, результаты окажутся в поддиректории `ipad`.
  
Бывает так, что одна из машинок cdn турбофильма по каким-то причинам
не содержит запрашиваемого видеофайла. Тогда скрипт вываливается с
ошибкой. Ничего страшного, пробуй запускать его снова и снова, и
однажды тебе повезет! :)


[HandBrakeCLI]: http://handbrake.fr/downloads2.php
[Phantom.js]: https://github.com/ariya/phantomjs
[tv]: http://turbofilm.tv/
