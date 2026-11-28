# Changes to the PetroGram privacy policy for the Vatani Tech website
# (21 November 2026): new studio contact, account / sync / sign-in, crash
# reports and statistics, in six languages, plus a full Chinese version.
# 22 November 2026: the phone's own backup (Google on Android) includes the
# app's data: section 2 and the summary, in all seven languages.
# 23 November 2026: section 6d (statistics) comes from the app's
# docs/PRIVACY_ADDITIONS.md: more counts and the approximate region.
# 24 November 2026: section 6g (a message written in the app goes to
# Sentry), also from docs/PRIVACY_ADDITIONS.md, in all seven languages.
# 28 November 2026: section 6h (the certificate of completion a person can
# put online, with their name, on /certificate/); the date of the policy.
# 25 November 2026: five things the app already did are now said (found
# while writing the Geo-Rulers policy). Here: the update check with Firebase
# Remote Config (sections 1, 3 and 8) and section 2 (the data on the phone
# is sent only through the optional scoreboard and sync). In the app's
# docs/PRIVACY_ADDITIONS.md: 6c (Sentry's random installation number), 6e
# (Google passes the name and picture link) and 6f (all that sync copies).

MAIL_OLD = '<a href="mailto:vatanifardin@gmail.com">vatanifardin@gmail.com</a>'
MAIL_NEW = '<a href="mailto:support@vatanitech.com">support@vatanitech.com</a>'
CONTACT = ('<p>Fardin Vatani<br>', '<p>Vatani Tech (Fardin Vatani)<br>')

PRIV = {
'en': dict(
  label6b='English', heading6c='English', semi=';',
  sum_start='We, the developer,', sum_end='(section 6). ',
  summary='Your notes and progress stay on your phone, and in your phone\'s own backup if you have it turned on (section 2). Some optional features send data only when you choose to use them: the quiz scoreboard, where the name you choose and your quiz results are stored with <strong>Google Firebase</strong> and shown to other users (section 6), and an account with sign-in by email, Google or Apple and sync between your phones (sections 6b, 6e, 6f). Anonymous crash reports (<strong>Sentry</strong>) and usage statistics (<strong>PostHog</strong>) help us fix and improve the app; they contain no name, email or anything you type, and you can turn them off in Settings → Privacy (sections 6c, 6d). ',
  replace=[
    ('19 November 2026', '28 November 2026'),
    # 25 November 2026: the update check (sections 1, 3, 8) and what leaves the phone (section 2)
    ('The Market page downloads public price data from the U.S. Energy Information Administration (EIA).', 'The Market page downloads public price data from the U.S. Energy Information Administration (EIA). When it starts, the app also asks Google Firebase whether an update is required (section 3).'),
    ('This information stays on your device and is never sent to us. We cannot see your notes or progress.', 'This information stays on your device. It is sent only if you use the optional features that need it: the scoreboard (section 6) and sync between your phones (section 6f). Otherwise we cannot see your notes or progress.'),
    ('<li><strong>Scoreboard.</strong>', '<li><strong>Update check.</strong> When the app starts, it asks Google Firebase (Remote Config) which is the oldest version of the app that may still be used, so that it can tell you when an update is necessary. The request carries a random number that Firebase creates for this installation, the app version, the system version, and the language, country and time zone set on your phone; it contains no name, no email and nothing you have typed. As with any internet connection, Google\'s servers receive your device\'s IP address. This check cannot be turned off.</li>\n    <li><strong>Scoreboard.</strong>'),
    ('<li>Google Firebase (Authentication and Cloud Firestore): the optional scoreboard (section 6);</li>', '<li>Google Firebase (Authentication and Cloud Firestore): the optional scoreboard (section 6);</li>\n    <li>Google Firebase Remote Config: the update check (section 3);</li>'),
    ("If Android backup is turned on for your phone, Android may include this data in your own Google account backup; we have no access to that backup.", "If Android backup is turned on for your phone, Android includes the app's saved data (your notes, progress and settings and, if you created an account, your sign-in) in your phone's backup in your own Google account. Google stores that backup; we cannot see or access it. The data is restored when you install the app on a new phone. You can turn the backup off in your phone's settings (Settings → Google → Backup; the wording varies by phone); Google then removes the copy under its own rules."),
    ('Developer: Fardin Vatani,', 'Developer: Vatani Tech (Fardin Vatani),'),
    CONTACT, (MAIL_OLD, MAIL_NEW),
    ('The app contains no analytics of its own.', 'Crash reports and statistics are used only to fix and improve the app, never for ads.'),
    ('it is not linked to your email, phone number, or Google or Apple account;', 'it is not linked to your email, phone number, or Google or Apple account unless you create an account (section 6b);'),
    ('<h2>11.', '<p>If you create an account, you can delete it at any time in Settings → Account and check mark → Delete my account; this deletes your email, your scoreboard lines and your synced copy in the cloud. You can turn crash reports and usage statistics off at any time in Settings → Privacy.</p>\n\n  <h2>11.'),
  ],
  sec3='<h2>3.', sec8='<h2>8.',
  bullet3='<li><strong>Account and sync.</strong> Only if you create an account, the app signs in with Google Firebase (by email, Google or Apple) and syncs your data between your phones (sections 6b, 6e, 6f).</li>\n    <li><strong>Crash reports and statistics.</strong> Crash reports go to Sentry unless you turn them off in Settings → Privacy; anonymous usage counts go to PostHog only if you allow it (sections 6c, 6d).</li>\n    <li><strong>Messages to us.</strong> Only if you write a message in the app and press Send, it is sent to Sentry, where we read it (section 6g).</li>',
  bullets8='<li>Google Firebase Authentication and Cloud Firestore: the optional account and sync between phones (sections 6b, 6f);</li>\n    <li>Google Sign-In and Sign in with Apple: optional sign-in (section 6e);</li>\n    <li>Sentry (Functional Software, Inc., EU data region): crash reports, and messages you send us from the app (sections 6c, 6g);</li>\n    <li>PostHog (PostHog Inc., EU Cloud): anonymous usage statistics (section 6d).</li>',
),
'az': dict(
  label6b='Azərbaycanca', heading6c='Azərbaycanca', semi=';',
  sum_start='Biz, tərtibatçı,', sum_end='(6-cı bənd). ',
  summary='Qeydləriniz və irəliləyişiniz telefonunuzda qalır; telefonun öz ehtiyat nüsxəsi aktivdirsə, orada da saxlanılır (2-ci bənd). Bəzi könüllü funksiyalar məlumatı yalnız onlardan istifadə etməyi seçdikdə göndərir: test reytinqi, burada seçdiyiniz ad və test nəticələriniz <strong>Google Firebase</strong>-də saxlanılır və digər istifadəçilərə göstərilir (6-cı bənd), həmçinin e-poçt, Google və ya Apple ilə daxil olunan və telefonlarınız arasında sinxronizasiya edən hesab (6b, 6e, 6f bəndləri). Anonim xəta hesabatları (<strong>Sentry</strong>) və istifadə statistikası (<strong>PostHog</strong>) tətbiqi düzəltməyə və yaxşılaşdırmağa kömək edir; onlarda ad, e-poçt və ya yazdıqlarınız olmur və onları Ayarlar → Məxfilik bölməsində söndürə bilərsiniz (6c, 6d bəndləri). ',
  replace=[
    ('19 noyabr 2026', '28 noyabr 2026'),
    # 25 November 2026: the update check (sections 1, 3, 8) and what leaves the phone (section 2)
    ('«Bazar» səhifəsi ABŞ Energetika İnformasiya İdarəsindən (EIA) açıq qiymət məlumatlarını yükləyir.', '«Bazar» səhifəsi ABŞ Energetika İnformasiya İdarəsindən (EIA) açıq qiymət məlumatlarını yükləyir. Tətbiq açılanda həmçinin Google Firebase-dən yeniləmənin vacib olub-olmadığını soruşur (3-cü bənd).'),
    ('Bu məlumat cihazınızda qalır və bizə heç vaxt göndərilmir. Biz qeydlərinizi və irəliləyişinizi görə bilmirik.', 'Bu məlumat cihazınızda qalır. O, yalnız bunu tələb edən könüllü funksiyalardan istifadə etdikdə göndərilir: reytinq (6-cı bənd) və telefonlarınız arasında sinxronizasiya (6f bəndi). Əks halda biz qeydlərinizi və irəliləyişinizi görə bilmirik.'),
    ('<li><strong>Reytinq.</strong>', '<li><strong>Yenilənmənin yoxlanması.</strong> Tətbiq açılanda Google Firebase-dən (Remote Config) tətbiqin hələ istifadə oluna bilən ən köhnə versiyasını soruşur ki, yeniləmə vacib olduqda sizə bildirə bilsin. Sorğuda Firebase-in bu quraşdırma üçün yaratdığı təsadüfi nömrə, tətbiqin versiyası, sistemin versiyası, həmçinin telefonunuzda seçilmiş dil, ölkə və saat qurşağı olur; ad, e-poçt və yazdığınız heç nə olmur. Hər internet bağlantısında olduğu kimi, Google serverləri cihazınızın IP ünvanını görür. Bu yoxlamanı söndürmək olmur.</li>\n    <li><strong>Reytinq.</strong>'),
    ('<li>Google Firebase (Authentication və Cloud Firestore): könüllü reytinq (6-cı bənd);</li>', '<li>Google Firebase (Authentication və Cloud Firestore): könüllü reytinq (6-cı bənd);</li>\n    <li>Google Firebase Remote Config: yenilənmənin yoxlanması (3-cü bənd);</li>'),
    ("Telefonunuzda Android ehtiyat nüsxəsi aktivdirsə, Android bu məlumatı sizin öz Google hesabınızın ehtiyat nüsxəsinə daxil edə bilər; həmin nüsxəyə bizim çıxışımız yoxdur.", "Telefonunuzda Android ehtiyat nüsxəsi aktivdirsə, Android tətbiqin saxladığı məlumatı (qeydləriniz, irəliləyişiniz və ayarlarınız, hesab yaratmısınızsa, həm də hesaba daxil olma məlumatınız) telefonun sizin öz Google hesabınızdakı ehtiyat nüsxəsinə daxil edir. Həmin nüsxəni Google saxlayır; biz onu görə bilmirik və ona çıxışımız yoxdur. Tətbiqi yeni telefona quraşdırdıqda bu məlumat bərpa olunur. Ehtiyat nüsxəsini telefonun ayarlarında söndürə bilərsiniz (Ayarlar → Google → Ehtiyat nüsxəsi; adlar telefondan asılı olaraq fərqlənə bilər); bundan sonra Google nüsxəni öz qaydalarına uyğun olaraq silir."),
    ('Tərtibatçı: Fardin Vatani,', 'Tərtibatçı: Vatani Tech (Fardin Vatani),'),
    CONTACT, (MAIL_OLD, MAIL_NEW),
    ('Tətbiqin öz analitikası yoxdur.', 'Xəta hesabatları və statistika yalnız tətbiqi düzəltmək və yaxşılaşdırmaq üçün istifadə olunur, heç vaxt reklam üçün yox.'),
    ('Google və Apple hesabınızla əlaqələndirilmir;', 'Google və Apple hesabınızla əlaqələndirilmir, hesab yaratmasanız (6b bəndi);'),
    ('<h2>11.', '<p>Hesab yaratsanız, onu istənilən vaxt Ayarlar → Hesab və təsdiq nişanı → Hesabımı sil bölməsində silə bilərsiniz; bu, e-poçtunuzu, reytinq sətirlərinizi və buluddakı sinxron nüsxəni silir. Xəta hesabatlarını və istifadə statistikasını istənilən vaxt Ayarlar → Məxfilik bölməsində söndürə bilərsiniz.</p>\n\n  <h2>11.'),
  ],
  sec3='<h2>3.', sec8='<h2>8.',
  bullet3='<li><strong>Hesab və sinxronizasiya.</strong> Yalnız hesab yaratsanız, tətbiq Google Firebase ilə (e-poçt, Google və ya Apple ilə) daxil olur və məlumatlarınızı telefonlarınız arasında sinxronlaşdırır (6b, 6e, 6f bəndləri).</li>\n    <li><strong>Xəta hesabatları və statistika.</strong> Ayarlar → Məxfilik bölməsində söndürməsəniz, xəta hesabatları Sentry-yə göndərilir; anonim istifadə sayları isə yalnız icazə versəniz PostHog-a göndərilir (6c, 6d bəndləri).</li>\n    <li><strong>Bizə mesajlar.</strong> Yalnız tətbiqdə mesaj yazıb "Göndər" düyməsinə basdıqda o, Sentry-yə göndərilir və biz onu orada oxuyuruq (6g bəndi).</li>',
  bullets8='<li>Google Firebase Authentication və Cloud Firestore: könüllü hesab və telefonlar arasında sinxronizasiya (6b, 6f bəndləri);</li>\n    <li>Google Sign-In və Sign in with Apple: könüllü daxil olma (6e bəndi);</li>\n    <li>Sentry (Functional Software, Inc., AB məlumat regionu): xəta hesabatları və tətbiqdən bizə göndərdiyiniz mesajlar (6c, 6g bəndləri);</li>\n    <li>PostHog (PostHog Inc., EU Cloud): anonim istifadə statistikası (6d bəndi).</li>',
),
'ru': dict(
  label6b='Русский', heading6c='Русский', semi=';',
  sum_start='Мы, разработчик,', sum_end='(раздел 6). ',
  summary='Ваши заметки и прогресс остаются на телефоне, а если включено резервное копирование телефона, то и в его резервной копии (раздел 2). Некоторые необязательные функции отправляют данные, только если вы решите ими пользоваться: рейтинг тестов, где выбранное вами имя и результаты хранятся в <strong>Google Firebase</strong> и видны другим пользователям (раздел 6), а также аккаунт со входом по почте, через Google или Apple и синхронизацией между вашими телефонами (разделы 6b, 6e, 6f). Анонимные отчёты о сбоях (<strong>Sentry</strong>) и статистика использования (<strong>PostHog</strong>) помогают нам исправлять и улучшать приложение; в них нет имени, почты или того, что вы вводите, и их можно отключить в разделе Настройки → Конфиденциальность (разделы 6c, 6d). ',
  replace=[
    ('19 ноября 2026 г.', '28 ноября 2026 г.'),
    # 25 November 2026: the update check (sections 1, 3, 8) and what leaves the phone (section 2)
    ('Страница «Рынок» загружает общедоступные данные о ценах Управления энергетической информации США (EIA).', 'Страница «Рынок» загружает общедоступные данные о ценах Управления энергетической информации США (EIA). При запуске приложение также спрашивает у Google Firebase, не требуется ли обновление (раздел 3).'),
    ('Эти данные остаются на устройстве и никогда не передаются нам. Мы не видим ваших заметок и прогресса.', 'Эти данные остаются на устройстве. Они отправляются, только если вы пользуетесь необязательными функциями, которым они нужны: рейтингом (раздел 6) и синхронизацией между вашими телефонами (раздел 6f). В остальных случаях мы не видим ваших заметок и прогресса.'),
    ('<li><strong>Рейтинг.</strong>', '<li><strong>Проверка обновления.</strong> При запуске приложение спрашивает у Google Firebase (Remote Config), какая самая старая версия приложения ещё может использоваться, чтобы сообщить вам, когда обновление необходимо. Запрос содержит случайный номер, который Firebase создаёт для этой установки, версию приложения, версию системы, а также язык, страну и часовой пояс, заданные на телефоне; в нём нет имени, почты и ничего из того, что вы ввели. Как и при любом подключении к интернету, серверы Google получают IP-адрес вашего устройства. Отключить эту проверку нельзя.</li>\n    <li><strong>Рейтинг.</strong>'),
    ('<li>Google Firebase (Authentication и Cloud Firestore): необязательный рейтинг (раздел 6);</li>', '<li>Google Firebase (Authentication и Cloud Firestore): необязательный рейтинг (раздел 6);</li>\n    <li>Google Firebase Remote Config: проверка обновления (раздел 3);</li>'),
    ("Если на телефоне включено резервное копирование Android, система может включить эти данные в резервную копию вашего собственного аккаунта Google; у нас нет доступа к этой копии.", "Если на телефоне включено резервное копирование Android, система включает сохранённые данные приложения (заметки, прогресс и настройки, а если вы создали аккаунт, то и вход в него) в резервную копию телефона в вашем собственном аккаунте Google. Эту копию хранит Google; мы не видим её и не имеем к ней доступа. Данные восстанавливаются, когда вы устанавливаете приложение на новый телефон. Резервное копирование можно отключить в настройках телефона (Настройки → Google → Резервное копирование; названия зависят от телефона); после этого Google удаляет копию по своим правилам."),
    ('Разработчик: Fardin Vatani,', 'Разработчик: Vatani Tech (Fardin Vatani),'),
    CONTACT, (MAIL_OLD, MAIL_NEW),
    ('Собственной аналитики в приложении нет.', 'Отчёты о сбоях и статистика используются только для исправления и улучшения приложения, но не для рекламы.'),
    ('или аккаунтом Google или Apple;', 'или аккаунтом Google или Apple, если вы не создадите аккаунт (раздел 6b);'),
    ('<h2>11.', '<p>Если вы создали аккаунт, его можно удалить в любой момент: Настройки → Аккаунт и галочка → Удалить аккаунт; при этом удаляются ваша почта, строки в рейтинге и синхронизированная копия в облаке. Отчёты о сбоях и статистику использования можно в любой момент отключить в разделе Настройки → Конфиденциальность.</p>\n\n  <h2>11.'),
  ],
  sec3='<h2>3.', sec8='<h2>8.',
  bullet3='<li><strong>Аккаунт и синхронизация.</strong> Только если вы создадите аккаунт, приложение выполняет вход через Google Firebase (по почте, через Google или Apple) и синхронизирует ваши данные между телефонами (разделы 6b, 6e, 6f).</li>\n    <li><strong>Отчёты о сбоях и статистика.</strong> Отчёты о сбоях отправляются в Sentry, если вы не отключите их в разделе Настройки → Конфиденциальность; анонимные счётчики использования отправляются в PostHog, только если вы это разрешите (разделы 6c, 6d).</li>\n    <li><strong>Сообщения нам.</strong> Только если вы напишете сообщение в приложении и нажмёте «Отправить», оно отправляется в Sentry, где мы его читаем (раздел 6g).</li>',
  bullets8='<li>Google Firebase Authentication и Cloud Firestore: необязательный аккаунт и синхронизация между телефонами (разделы 6b, 6f);</li>\n    <li>Google Sign-In и Sign in with Apple: необязательный вход (раздел 6e);</li>\n    <li>Sentry (Functional Software, Inc., регион данных ЕС): отчёты о сбоях и сообщения, которые вы отправляете нам из приложения (разделы 6c, 6g);</li>\n    <li>PostHog (PostHog Inc., EU Cloud): анонимная статистика использования (раздел 6d).</li>',
),
'ar': dict(
  label6b='العربية', heading6c='العربية', semi='؛',
  sum_start='نحن، المطوّر،', sum_end='(البند 6). ',
  summary='تبقى ملاحظاتك وتقدّمك على هاتفك، وكذلك في النسخة الاحتياطية الخاصة بهاتفك إذا كان النسخ الاحتياطي مفعّلًا (البند 2). بعض الميزات الاختيارية لا ترسل بيانات إلا إذا اخترت استخدامها: لوحة متصدري الاختبارات، حيث يُخزَّن الاسم الذي تختاره ونتائج اختباراتك لدى <strong>Google Firebase</strong> ويظهران للمستخدمين الآخرين (البند 6)، والحساب مع تسجيل الدخول بالبريد الإلكتروني أو Google أو Apple والمزامنة بين هواتفك (البنود 6ب و6هـ و6و). وتساعدنا تقارير الأعطال المجهولة (<strong>Sentry</strong>) وإحصاءات الاستخدام (<strong>PostHog</strong>) على إصلاح التطبيق وتحسينه؛ فهي لا تحتوي على اسم أو بريد إلكتروني أو أي شيء تكتبه، ويمكنك إيقافها من الإعدادات ← الخصوصية (البندان 6ج و6د). ',
  replace=[
    ('19 نوفمبر 2026', '28 نوفمبر 2026'),
    # 25 November 2026: the update check (sections 1, 3, 8) and what leaves the phone (section 2)
    ('وتنزّل صفحة السوق بيانات أسعار عامة من إدارة معلومات الطاقة الأمريكية (EIA).', 'وتنزّل صفحة السوق بيانات أسعار عامة من إدارة معلومات الطاقة الأمريكية (EIA). وعند التشغيل يسأل التطبيق أيضًا Google Firebase عمّا إذا كان التحديث مطلوبًا (البند 3).'),
    ('تبقى هذه المعلومات على جهازك ولا تُرسل إلينا أبدًا، ولا يمكننا رؤية ملاحظاتك أو تقدّمك.', 'تبقى هذه المعلومات على جهازك. ولا تُرسَل إلا إذا استخدمت الميزات الاختيارية التي تحتاج إليها: لوحة المتصدرين (البند 6) والمزامنة بين هواتفك (البند 6و). وفيما عدا ذلك لا يمكننا رؤية ملاحظاتك أو تقدّمك.'),
    ('<li><strong>لوحة المتصدرين.</strong>', '<li><strong>التحقق من التحديث.</strong> عند تشغيل التطبيق يسأل Google Firebase (Remote Config) عن أقدم إصدار من التطبيق ما زال استخدامه ممكنًا، حتى يخبرك عندما يصبح التحديث ضروريًا. يحمل الطلب رقمًا عشوائيًا تنشئه Firebase لهذا التثبيت، وإصدار التطبيق، وإصدار النظام، واللغة والبلد والمنطقة الزمنية المضبوطة على هاتفك؛ ولا يحتوي على اسم أو بريد إلكتروني أو أي شيء كتبته. وكما في أي اتصال بالإنترنت، تتلقى خوادم Google عنوان IP لجهازك. لا يمكن إيقاف هذا التحقق.</li>\n    <li><strong>لوحة المتصدرين.</strong>'),
    ('<li>Google Firebase (Authentication وCloud Firestore): لوحة المتصدرين الاختيارية (البند 6)؛</li>', '<li>Google Firebase (Authentication وCloud Firestore): لوحة المتصدرين الاختيارية (البند 6)؛</li>\n    <li>Google Firebase Remote Config: التحقق من التحديث (البند 3)؛</li>'),
    ("إذا كان النسخ الاحتياطي في Android مفعّلًا على هاتفك، فقد يضمّن Android هذه البيانات في النسخة الاحتياطية لحسابك الخاص على Google، ولا يمكننا الوصول إلى تلك النسخة.", "إذا كان النسخ الاحتياطي في Android مفعّلًا على هاتفك، فإن Android يضمّن بيانات التطبيق المحفوظة (ملاحظاتك وتقدّمك وإعداداتك، وكذلك تسجيل دخولك إذا أنشأت حسابًا) في النسخة الاحتياطية لهاتفك في حسابك الخاص على Google. تحتفظ Google بهذه النسخة، ولا يمكننا رؤيتها أو الوصول إليها. وتُستعاد البيانات عند تثبيت التطبيق على هاتف جديد. يمكنك إيقاف النسخ الاحتياطي من إعدادات هاتفك (الإعدادات ← Google ← النسخ الاحتياطي؛ وقد تختلف التسميات من هاتف إلى آخر)، وبعد ذلك تحذف Google النسخة وفق قواعدها."),
    ('المطوّر: Fardin Vatani،', 'المطوّر: Vatani Tech (Fardin Vatani)،'),
    CONTACT, (MAIL_OLD, MAIL_NEW),
    ('ولا يحتوي التطبيق على أدوات تحليل خاصة به.', 'وتُستخدم تقارير الأعطال والإحصاءات فقط لإصلاح التطبيق وتحسينه، وليس للإعلانات أبدًا.'),
    ('أو حسابك في Google أو Apple؛', 'أو حسابك في Google أو Apple، ما لم تنشئ حسابًا (البند 6ب)؛'),
    ('<h2>11.', '<p>إذا أنشأت حسابًا، يمكنك حذفه في أي وقت من الإعدادات ← الحساب وعلامة التوثيق ← احذف حسابي؛ ويؤدي ذلك إلى حذف بريدك وأسطرك في لوحة المتصدرين ونسختك المتزامنة في السحابة. ويمكنك إيقاف تقارير الأعطال وإحصاءات الاستخدام في أي وقت من الإعدادات ← الخصوصية.</p>\n\n  <h2>11.'),
  ],
  sec3='<h2>3.', sec8='<h2>8.',
  bullet3='<li><strong>الحساب والمزامنة.</strong> فقط إذا أنشأت حسابًا، يسجّل التطبيق الدخول عبر Google Firebase (بالبريد الإلكتروني أو Google أو Apple) ويزامن بياناتك بين هواتفك (البنود 6ب و6هـ و6و).</li>\n    <li><strong>تقارير الأعطال والإحصاءات.</strong> تُرسَل تقارير الأعطال إلى Sentry ما لم توقفها من الإعدادات ← الخصوصية؛ أما أعداد الاستخدام المجهولة فلا تُرسَل إلى PostHog إلا إذا سمحت بذلك (البندان 6ج و6د).</li>\n    <li><strong>رسائلك إلينا.</strong> فقط إذا كتبت رسالة في التطبيق وضغطت على "إرسال"، تُرسَل إلى Sentry حيث نقرؤها (البند 6ز).</li>',
  bullets8='<li>Google Firebase Authentication وCloud Firestore: الحساب الاختياري والمزامنة بين الهواتف (البندان 6ب و6و)؛</li>\n    <li>Google Sign-In وSign in with Apple: تسجيل الدخول الاختياري (البند 6هـ)؛</li>\n    <li>Sentry (من Functional Software, Inc.، منطقة بيانات الاتحاد الأوروبي): تقارير الأعطال والرسائل التي ترسلها إلينا من التطبيق (البندان 6ج و6ز)؛</li>\n    <li>PostHog (من PostHog Inc.، EU Cloud): إحصاءات استخدام مجهولة الهوية (البند 6د).</li>',
),
'es': dict(
  label6b='Español', heading6c='Español', semi=';',
  sum_start='Nosotros, el desarrollador,', sum_end='(sección 6). ',
  summary='Tus notas y tu progreso se quedan en tu teléfono y, si la tienes activada, en la copia de seguridad del propio teléfono (sección 2). Algunas funciones opcionales envían datos solo si decides usarlas: la clasificación de tests, donde el nombre que elijas y tus resultados se guardan en <strong>Google Firebase</strong> y se muestran a otros usuarios (sección 6), y una cuenta con inicio de sesión por correo, Google o Apple y sincronización entre tus teléfonos (secciones 6b, 6e, 6f). Los informes de fallos anónimos (<strong>Sentry</strong>) y las estadísticas de uso (<strong>PostHog</strong>) nos ayudan a corregir y mejorar la app; no contienen nombre, correo ni nada de lo que escribes, y puedes desactivarlos en Ajustes → Privacidad (secciones 6c, 6d). ',
  replace=[
    ('19 de noviembre de 2026', '28 de noviembre de 2026'),
    # 25 November 2026: the update check (sections 1, 3, 8) and what leaves the phone (section 2)
    ('La página Mercado descarga datos públicos de precios de la Administración de Información Energética de EE. UU. (EIA).', 'La página Mercado descarga datos públicos de precios de la Administración de Información Energética de EE. UU. (EIA). Al iniciarse, la aplicación también pregunta a Google Firebase si hace falta una actualización (sección 3).'),
    ('Esta información permanece en tu dispositivo y nunca se nos envía. No podemos ver tus notas ni tu progreso.', 'Esta información permanece en tu dispositivo. Solo se envía si usas las funciones opcionales que la necesitan: la clasificación (sección 6) y la sincronización entre tus teléfonos (sección 6f). En los demás casos no podemos ver tus notas ni tu progreso.'),
    ('<li><strong>Clasificación.</strong>', '<li><strong>Comprobación de actualización.</strong> Al iniciarse, la aplicación pregunta a Google Firebase (Remote Config) cuál es la versión más antigua de la aplicación que todavía se puede usar, para poder avisarte cuando una actualización sea necesaria. La solicitud lleva un número aleatorio que Firebase crea para esta instalación, la versión de la aplicación, la versión del sistema y el idioma, el país y la zona horaria configurados en tu teléfono; no contiene nombre, correo ni nada de lo que hayas escrito. Como en cualquier conexión a internet, los servidores de Google reciben la dirección IP de tu dispositivo. Esta comprobación no se puede desactivar.</li>\n    <li><strong>Clasificación.</strong>'),
    ('<li>Google Firebase (Authentication y Cloud Firestore): la clasificación opcional (sección 6);</li>', '<li>Google Firebase (Authentication y Cloud Firestore): la clasificación opcional (sección 6);</li>\n    <li>Google Firebase Remote Config: la comprobación de actualización (sección 3);</li>'),
    ("Si la copia de seguridad de Android está activada en tu teléfono, Android puede incluir estos datos en la copia de seguridad de tu propia cuenta de Google; no tenemos acceso a esa copia.", "Si la copia de seguridad de Android está activada en tu teléfono, Android incluye los datos guardados de la aplicación (tus notas, tu progreso y tus ajustes y, si has creado una cuenta, tu inicio de sesión) en la copia de seguridad del teléfono, en tu propia cuenta de Google. Google guarda esa copia; no podemos verla ni acceder a ella. Los datos se restauran cuando instalas la aplicación en un teléfono nuevo. Puedes desactivar la copia de seguridad en los ajustes del teléfono (Ajustes → Google → Copia de seguridad; los nombres varían según el teléfono); después, Google elimina la copia según sus propias normas."),
    ('Desarrollador: Fardin Vatani,', 'Desarrollador: Vatani Tech (Fardin Vatani),'),
    CONTACT, (MAIL_OLD, MAIL_NEW),
    ('La aplicación no tiene analíticas propias.', 'Los informes de fallos y las estadísticas solo se usan para corregir y mejorar la app, nunca para publicidad.'),
    ('ni tu cuenta de Google o Apple;', 'ni tu cuenta de Google o Apple, salvo que crees una cuenta (sección 6b);'),
    ('<h2>11.', '<p>Si creas una cuenta, puedes eliminarla en cualquier momento en Ajustes → Cuenta e insignia → Eliminar mi cuenta; así se borran tu correo, tus líneas en la clasificación y tu copia sincronizada en la nube. Puedes desactivar los informes de fallos y las estadísticas de uso en cualquier momento en Ajustes → Privacidad.</p>\n\n  <h2>11.'),
  ],
  sec3='<h2>3.', sec8='<h2>8.',
  bullet3='<li><strong>Cuenta y sincronización.</strong> Solo si creas una cuenta, la app inicia sesión con Google Firebase (por correo, Google o Apple) y sincroniza tus datos entre tus teléfonos (secciones 6b, 6e, 6f).</li>\n    <li><strong>Informes de fallos y estadísticas.</strong> Los informes de fallos se envían a Sentry salvo que los desactives en Ajustes → Privacidad; los recuentos de uso anónimos se envían a PostHog solo si lo permites (secciones 6c, 6d).</li>\n    <li><strong>Mensajes para nosotros.</strong> Solo si escribes un mensaje en la app y pulsas Enviar, se envía a Sentry, donde lo leemos (sección 6g).</li>',
  bullets8='<li>Google Firebase Authentication y Cloud Firestore: la cuenta opcional y la sincronización entre teléfonos (secciones 6b, 6f);</li>\n    <li>Google Sign-In e Iniciar sesión con Apple: el inicio de sesión opcional (sección 6e);</li>\n    <li>Sentry (Functional Software, Inc., región de datos de la UE): informes de fallos y los mensajes que nos envías desde la app (secciones 6c, 6g);</li>\n    <li>PostHog (PostHog Inc., EU Cloud): estadísticas de uso anónimas (sección 6d).</li>',
),
'fr': dict(
  label6b='Français', heading6c='Français', semi=' ;',
  sum_start='Nous, le développeur,', sum_end='(section 6). ',
  summary='Vos notes et vos progrès restent sur votre téléphone, ainsi que dans la sauvegarde de votre téléphone si elle est activée (section 2). Certaines fonctions facultatives n’envoient des données que si vous choisissez de les utiliser : le classement des quiz, où le nom que vous choisissez et vos résultats sont enregistrés chez <strong>Google Firebase</strong> et affichés aux autres utilisateurs (section 6), et un compte avec connexion par e-mail, Google ou Apple et synchronisation entre vos téléphones (sections 6b, 6e, 6f). Les rapports de plantage anonymes (<strong>Sentry</strong>) et les statistiques d’utilisation (<strong>PostHog</strong>) nous aident à corriger et à améliorer l’app ; ils ne contiennent ni nom, ni e-mail, ni rien de ce que vous saisissez, et vous pouvez les désactiver dans Paramètres → Confidentialité (sections 6c, 6d). ',
  replace=[
    ('19 novembre 2026', '28 novembre 2026'),
    # 25 November 2026: the update check (sections 1, 3, 8) and what leaves the phone (section 2)
    ('La page Marché télécharge des données de prix publiques de l’Energy Information Administration des États-Unis (EIA).', 'La page Marché télécharge des données de prix publiques de l’Energy Information Administration des États-Unis (EIA). Au démarrage, l’application demande aussi à Google Firebase si une mise à jour est nécessaire (section 3).'),
    ('Ces informations restent sur votre appareil et ne nous sont jamais envoyées. Nous ne pouvons voir ni vos notes ni votre progression.', 'Ces informations restent sur votre appareil. Elles ne sont envoyées que si vous utilisez les fonctions facultatives qui en ont besoin : le classement (section 6) et la synchronisation entre vos téléphones (section 6f). Dans les autres cas, nous ne pouvons voir ni vos notes ni votre progression.'),
    ('<li><strong>Classement.</strong>', '<li><strong>Vérification de mise à jour.</strong> Au démarrage, l’application demande à Google Firebase (Remote Config) quelle est la plus ancienne version de l’application encore utilisable, afin de vous prévenir lorsqu’une mise à jour est nécessaire. La requête contient un numéro aléatoire que Firebase crée pour cette installation, la version de l’application, la version du système, ainsi que la langue, le pays et le fuseau horaire réglés sur votre téléphone ; elle ne contient ni nom, ni e-mail, ni rien de ce que vous avez saisi. Comme pour toute connexion internet, les serveurs de Google reçoivent l’adresse IP de votre appareil. Cette vérification ne peut pas être désactivée.</li>\n    <li><strong>Classement.</strong>'),
    ('<li>Google Firebase (Authentication et Cloud Firestore) : le classement facultatif (section 6) ;</li>', '<li>Google Firebase (Authentication et Cloud Firestore) : le classement facultatif (section 6) ;</li>\n    <li>Google Firebase Remote Config : la vérification de mise à jour (section 3) ;</li>'),
    ("Si la sauvegarde Android est activée sur votre téléphone, Android peut inclure ces données dans la sauvegarde de votre propre compte Google ; nous n’avons pas accès à cette sauvegarde.", "Si la sauvegarde Android est activée sur votre téléphone, Android inclut les données enregistrées par l’application (vos notes, votre progression et vos réglages et, si vous avez créé un compte, votre connexion à ce compte) dans la sauvegarde du téléphone, sur votre propre compte Google. Google conserve cette sauvegarde ; nous ne pouvons ni la voir ni y accéder. Les données sont restaurées lorsque vous installez l’application sur un nouveau téléphone. Vous pouvez désactiver la sauvegarde dans les paramètres du téléphone (Paramètres → Google → Sauvegarde ; les intitulés varient selon le téléphone) ; Google supprime ensuite la copie selon ses propres règles."),
    ('Développeur : Fardin Vatani,', 'Développeur : Vatani Tech (Fardin Vatani),'),
    CONTACT, (MAIL_OLD, MAIL_NEW),
    ('L’application ne contient aucun outil d’analyse propre.', 'Les rapports de plantage et les statistiques servent uniquement à corriger et à améliorer l’app, jamais à la publicité.'),
    ('ni à votre compte Google ou Apple ;', 'ni à votre compte Google ou Apple, sauf si vous créez un compte (section 6b) ;'),
    ('<h2>11.', '<p>Si vous créez un compte, vous pouvez le supprimer à tout moment dans Paramètres → Compte et badge → Supprimer mon compte ; cela efface votre e-mail, vos lignes au classement et votre copie synchronisée dans le cloud. Vous pouvez désactiver les rapports de plantage et les statistiques d’utilisation à tout moment dans Paramètres → Confidentialité.</p>\n\n  <h2>11.'),
  ],
  sec3='<h2>3.', sec8='<h2>8.',
  bullet3='<li><strong>Compte et synchronisation.</strong> Seulement si vous créez un compte, l’app se connecte via Google Firebase (par e-mail, Google ou Apple) et synchronise vos données entre vos téléphones (sections 6b, 6e, 6f).</li>\n    <li><strong>Rapports de plantage et statistiques.</strong> Les rapports de plantage sont envoyés à Sentry sauf si vous les désactivez dans Paramètres → Confidentialité ; les comptages d’utilisation anonymes ne sont envoyés à PostHog que si vous l’autorisez (sections 6c, 6d).</li>\n    <li><strong>Messages pour nous.</strong> Seulement si vous écrivez un message dans l’app et appuyez sur Envoyer, il est envoyé à Sentry, où nous le lisons (section 6g).</li>',
  bullets8='<li>Google Firebase Authentication et Cloud Firestore : le compte facultatif et la synchronisation entre téléphones (sections 6b, 6f) ;</li>\n    <li>Google Sign-In et Se connecter avec Apple : la connexion facultative (section 6e) ;</li>\n    <li>Sentry (Functional Software, Inc., région de données UE) : rapports de plantage et messages que vous nous envoyez depuis l’app (sections 6c, 6g) ;</li>\n    <li>PostHog (PostHog Inc., EU Cloud) : statistiques d’utilisation anonymes (section 6d).</li>',
),
}

ZH_SECTION = '''<section id="zh" lang="zh-Hans">
  <h1>PetroGram 隐私政策</h1>
  <p class="meta">生效日期：2026 年 11 月 28 日<br>
  开发者：Vatani Tech（Fardin Vatani），阿塞拜疆巴库</p>

  <h2>1. 概要</h2>
  <p>PetroGram 是一款面向石油天然气行业的参考与学习应用，支持 Android 和 iPhone。您的笔记和学习进度保存在您的手机上；如果您开启了手机自带的备份，备份中也会有一份（见第 2 节）。部分可选功能只有在您选择使用时才会发送数据：测验排行榜（您选择的名称和测验成绩保存在 <strong>Google Firebase</strong> 中，并向其他用户显示，见第 6 节），以及可通过电子邮件、Google 或 Apple 登录并在您的手机之间同步的账号（见第 6b、6e、6f 节）。匿名崩溃报告（<strong>Sentry</strong>）和使用统计（<strong>PostHog</strong>）帮助我们修复和改进应用；其中不含姓名、电子邮件或您输入的任何内容，您可以在“设置 → 隐私”中关闭它们（见第 6c、6d 节）。<strong>Google AdMob</strong> 向未购买“去除广告”的用户显示横幅广告；AdMob 可能为这些广告收集设备数据，在法律要求时会先征得您的同意；在 iPhone 上，只有在您允许跟踪时才会使用 Apple 的广告标识符。<strong>Google Play</strong>（Android）和 <strong>App Store</strong>（iPhone）处理可选的一次性“去除广告”购买。“市场”页面会从美国能源信息署（EIA）下载公开的价格数据。应用启动时还会向 Google Firebase 查询是否必须更新（见第 3 节）。</p>

  <h2>2. 保存在您设备上的信息</h2>
  <p>应用会在手机的本地存储中保存以下内容：</p>
  <ul>
    <li>您的设置：语言、浅色或深色主题、提醒时间、振动、学习目标和领域，以及信息栏选项；</li>
    <li>您收藏的术语、最近的搜索，以及您在“我的笔记”中写下的笔记；</li>
    <li>您的学习进度：闪卡、测验成绩、待复习的错题、徽章和最近的活动；</li>
    <li>“市场”页面最近下载的价格，以便在没有网络时显示；</li>
    <li>您是否已购买“去除广告”，以便离线时也不显示广告；</li>
    <li>您的广告同意选择，由 Google 的同意工具保存（见第 4 节）；</li>
    <li>如果您加入了排行榜：您的随机用户 ID、您选择的名称、尚未发送的成绩以及您选择隐藏的人（见第 6 节）。</li>
  </ul>
  <p>这些信息保存在您的设备上。只有在您使用需要这些信息的可选功能时才会发送：排行榜（见第 6 节）和手机之间的同步（见第 6f 节）。除此之外，我们看不到您的笔记或进度。当您在应用中删除这些信息、清除应用数据或卸载应用时，它们会被删除。您导出的备份文件只会保存或分享到您选择的位置。如果您的手机开启了 Android 备份，Android 会将应用保存的数据（您的笔记、学习进度和设置；如果您创建了账号，还包括登录状态）包含在手机备份中，保存在您自己的 Google 账号里。该备份由 Google 保存，我们无法查看或访问。当您在新手机上安装应用时，这些数据会被恢复。您可以在手机设置中关闭备份（设置 → Google → 备份；不同手机上的名称可能不同）；关闭后，Google 会按其自身规则删除该备份。在 iPhone 上，iOS 可能会将这些数据包含在您自己的 iCloud 或电脑备份中；我们同样无法访问。</p>

  <h2>3. 网络使用</h2>
  <ul>
    <li><strong>市场价格。</strong>当您打开“市场”页面时，应用会从 api.eia.gov 下载 EIA 的公开价格数据。请求中只包含所需的价格列表和应用的访问密钥，不含任何个人数据或您输入的内容。与任何网络连接一样，EIA 的服务器会收到您设备的 IP 地址；EIA 依据其在 eia.gov 上公布的隐私政策处理该地址。</li>
    <li><strong>广告。</strong>如果您没有购买“去除广告”，应用会连接 Google 以显示广告（见第 4 节）。</li>
    <li><strong>Google Play 和 App Store。</strong>应用会向 Google Play（Android）或 App Store（iPhone）查询“去除广告”的价格以及您是否已拥有它（见第 5 节）。</li>
    <li><strong>更新检查。</strong>应用启动时会向 Google Firebase（Remote Config）查询仍可使用的最低应用版本，以便在必须更新时提醒您。请求中包含 Firebase 为本次安装创建的一个随机编号、应用版本、系统版本，以及您手机上设置的语言、国家/地区和时区；不含姓名、电子邮件或您输入的任何内容。与任何网络连接一样，Google 的服务器会收到您设备的 IP 地址。此项检查无法关闭。</li>
    <li><strong>排行榜。</strong>只有在您加入可选的排行榜时，应用才会将您选择的名称和测验成绩发送到 Google Firebase，并加载排行榜（见第 6 节）。</li>
    <li><strong>账号和同步。</strong>只有在您创建账号时，应用才会通过 Google Firebase 登录（使用电子邮件、Google 或 Apple），并在您的手机之间同步数据（见第 6b、6e、6f 节）。</li>
    <li><strong>崩溃报告和统计。</strong>崩溃报告会发送到 Sentry，除非您在“设置 → 隐私”中关闭；匿名使用计数只有在您允许后才会发送到 PostHog（见第 6c、6d 节）。</li>
    <li><strong>给我们的留言。</strong>只有当您在应用内写下留言并点按“发送”时，留言才会发送到 Sentry，我们在那里阅读（见第 6g 节）。</li>
  </ul>
  <p>其他所有功能无需联网即可使用；离线时不会显示广告。如果您点击“联系”“报告问题”“拨打电话”或“隐私政策”，应用会转到您手机上的其他应用（邮件、电话或浏览器）。这些应用有各自的隐私做法。</p>

  <h2>4. 广告（Google AdMob）</h2>
  <p>未购买“去除广告”的用户会在顶部栏下方看到由 Google AdMob（Google LLC；在欧洲经济区、英国和瑞士为 Google Ireland Limited）提供的横幅广告。为了展示、衡量广告并防止欺诈，应用中的 AdMob 软件可能会收集以下数据并发送给 Google：</p>
  <ul>
    <li>设备标识符，例如 Android 广告 ID；在 iPhone 上，如果您允许跟踪，则为 Apple 的广告标识符（IDFA）；</li>
    <li>IP 地址及据此推断的大致位置；</li>
    <li>设备和应用信息，例如型号、操作系统、语言和应用版本；</li>
    <li>广告互动，例如浏览和点击的广告，以及诊断数据。</li>
  </ul>
  <p>在欧洲经济区、英国和瑞士，应用会在加载任何广告之前显示 Google 的同意表单。您可以选择 Google 是否可以使用您的数据投放个性化广告，并可随时在<strong>设置 → 广告 → 隐私和广告设置</strong>中更改选择。在未获同意的情况下，Google 仍可能显示非个性化或有限广告，这类广告会为频次控制、效果衡量和防止欺诈等目的使用数据。您也可以在手机的 Android 设置（Google → 广告）中重置或删除广告 ID。</p>
  <p>在 iPhone 上，应用随后会显示 Apple 的“允许跟踪？”提示。如果您选择“要求 App 不跟踪”，Apple 的广告标识符不会与 Google 共享。您可以随时在 iPhone 的<strong>设置 → 隐私与安全性 → 跟踪</strong>中更改。</p>
  <p>Google 依据其自身政策处理这些数据：<a href="https://policies.google.com/privacy">policies.google.com/privacy</a> 和 <a href="https://policies.google.com/technologies/partner-sites">policies.google.com/technologies/partner-sites</a>。我们不会收到关于您的这些数据；AdMob 只向我们提供汇总数据，例如广告展示次数和收入。</p>
  <p>您写的笔记、学习进度以及您在应用中输入的任何内容都不会与 AdMob 共享。</p>

  <h2>5. “去除广告”购买（Google Play 和 App Store）</h2>
  <p>“去除广告”是一项可选的一次性购买。在 Android 上通过 Google Play 结算完成：Google 依据 Google Play 条款和 Google 隐私政策处理付款，并向我们提供每笔订单的记录，例如订单号、日期、产品、价格和国家/地区，我们仅用其管理购买，例如处理退款。在 iPhone 上通过 Apple 的 App Store 完成：Apple 依据其自身条款和隐私政策处理付款，只向我们提供销售报告，不提供您的姓名或联系方式。我们绝不会收到您的银行卡或付款信息。应用只在您的手机上保存是否已去除广告，并向 Google Play 或 App Store 核实购买是否仍然有效。</p>

  <h2>6. 测验排行榜（可选）</h2>
  <p>“测验”标签页中有一个可选的全球排行榜。除非您点击“加入排行榜”，否则不会发送任何内容，且无需电子邮件地址、电话号码或密码。加入后，应用会使用 Google Firebase（Firebase Authentication 和 Cloud Firestore，由 Google LLC 提供）保存：</p>
  <ul>
    <li>Firebase 为您安装的应用创建的随机用户 ID（匿名登录）；除非您创建账号（见第 6b 节），它不会与您的电子邮件、电话号码或 Google、Apple 账号关联；</li>
    <li>您选择显示的名称：您的名字和姓氏，或仅首字母，由您决定。<strong>所有使用 PetroGram 的人都能看到这个名称；</strong></li>
    <li>您加入后的测验成绩：今天、本周和全部时间的积分与用时、答对的题数，以及最后更新时间；</li>
    <li>如果您举报某个名称：您举报的名称和您的随机用户 ID，以便我们审核。</li>
  </ul>
  <p>您的成绩会先保存在手机上，联网时再发送。与任何网络连接一样，Google 的服务器会收到您设备的 IP 地址。您的笔记、闪卡和其他输入内容永远不会被发送，您隐藏的人只记录在您的手机上。我们仅将这些数据用于运行排行榜和删除违反规则的名称。它们不会用于广告，AdMob 也不会收到。</p>
  <p>您可以随时更改名称，也可以通过排行榜菜单中的<strong>退出排行榜</strong>离开：您的名称和成绩会立即从排行榜服务器中删除。如果您未退出就卸载了应用，您的条目会一直保留，直到您要求我们删除（见第 12 节）。我们处理这些数据是因为您选择加入（您的同意）；您可以随时通过退出来撤回同意。Google 作为我们的服务提供商代表我们处理这些数据，其服务器可能位于您所在国家/地区以外，包括美国。详见 <a href="https://firebase.google.com/support/privacy">firebase.google.com/support/privacy</a>。</p>

  <h2>6b. 可选账号</h2>
  <p>如果您创建账号，我们会保存您的电子邮件地址和密码（由 Google Firebase Authentication 以我们无法读取的形式保存）。它们仅用于让您登录、确认该地址属于您，以及在该地址属于公司时，在您的排行榜名称旁显示蓝色认证标记。您的电子邮件绝不会显示给其他用户。您可以随时在“设置 → 账号与认证标记 → 删除我的账号”中删除账号；这会删除电子邮件、密码以及您在排行榜中的记录。</p>

  {BLOCKS6CF}

  <h2>7. 您发给我们的邮件</h2>
  <p>如果您向我们发送报告或消息，我们会收到您发送的内容：您的电子邮件地址、消息、您附上的截图，以及邮件模板中包含的应用版本、语言和页面名称。我们仅将其用于回复您和修复问题。我们不会出售或与第三方共享这些内容，并会在不再需要时删除。</p>

  <h2>8. 第三方服务</h2>
  <ul>
    <li>美国能源信息署（EIA）：公开价格数据（见第 3 节）；</li>
    <li>Google AdMob，包括 Google 的同意工具（User Messaging Platform）：广告（见第 4 节）；</li>
    <li>Google Firebase（Authentication 和 Cloud Firestore）：可选的排行榜、账号以及手机之间的同步（见第 6、6b、6f 节）；</li>
    <li>Google Firebase Remote Config：更新检查（见第 3 节）；</li>
    <li>Google Play 结算（Android）和 Apple 的 App Store（iPhone）：“去除广告”购买（见第 5 节）；</li>
    <li>Google Sign-In 和“通过 Apple 登录”：可选登录（见第 6e 节）；</li>
    <li>Sentry（Functional Software, Inc.，欧盟数据区域）：崩溃报告，以及您在应用内发给我们的留言（见第 6c、6g 节）；</li>
    <li>PostHog（PostHog Inc.，EU Cloud）：匿名使用统计（见第 6d 节）。</li>
  </ul>
  <p>我们不出售个人数据。崩溃报告和统计仅用于修复和改进应用，绝不用于广告。</p>

  <h2>9. 儿童</h2>
  <p>本应用面向石油天然气行业的从业人员和学生，不针对 13 岁以下的儿童。我们不会在知情的情况下收集儿童的个人数据。</p>

  <h2>10. 您的权利</h2>
  <p>通过应用，我们只在您加入排行榜或创建账号时持有您的个人数据：您选择的名称、成绩和随机用户 ID（见第 6 节），以及账号的电子邮件和同步副本（见第 6b、6f 节）。您可以在应用中查看并更改名称，通过“退出排行榜”立即删除排行榜数据，也可以写信给我们要求访问或删除。如果您创建了账号，可以随时在“设置 → 账号与认证标记 → 删除我的账号”中删除；这会删除您的电子邮件、排行榜记录以及云端的同步副本。您可以随时在“设置 → 隐私”中关闭崩溃报告和使用统计。设备上的数据由您掌控，可随时删除。您可以在“设置 → 广告 → 隐私和广告设置”中更改广告同意，在 Android 设置中重置广告 ID，在 iPhone 的“设置 → 隐私与安全性 → 跟踪”中更改跟踪权限，或通过购买“去除广告”停止所有广告。对于 Google 或 Apple 处理的数据，请参阅它们的隐私政策，其中说明了如何向它们行使您的权利。您也可以联系我们，要求删除您发给我们的任何邮件。如果您居住在欧洲经济区或英国，还可以向您所在地的数据保护机构投诉。</p>

  <h2>11. 变更</h2>
  <p>我们可能会更新本政策。顶部的生效日期表示最后一次更改的时间。</p>

  <h2>12. 联系方式</h2>
  <p>Vatani Tech（Fardin Vatani）<br>
  电子邮件：<a href="mailto:support@vatanitech.com">support@vatanitech.com</a><br>
  电话：+994 70 294 19 98</p>
</section>'''
