# Privacy policies and terms of use of Petro-Rulers, MarineGram and Quran Guardians
# (27 November 2026), in the site's three languages: /<app>/privacy/ and
# /<app>/terms/. Written for these apps as they are (they are not copies of
# PetroGram's texts):
#   - Petro-Rulers, the tool app: no account; ads, the "Remove ads" purchase,
#     crash reports, statistics, the update check and messages as in
#     PetroGram; photos stay on the phone. Its terms are the app's own words
#     (lib/strings_services.dart of the Petro-Rulers repository): change
#     them together.
#   - MarineGram: no internet use and no data at all (so far); the AR button
#     of the 3D view opens the phone's own AR viewer, which uses the camera.
#   - Quran Guardians (first called Hafiz; key and folder "quran-guardians"
#     since 28 November 2026): no ads, no account, no data. Recitations are downloaded (AlQuran
#     Cloud); the city name for prayer times comes from the phone's own map
#     service; optional gifts go through the stores; the microphone is used
#     for the person's own recordings, kept on the phone. Its policy must
#     agree with the app's own "privacy" and "privacyLocation" texts
#     (lib/strings.dart of the quran-guardians repository).
# When an app changes what it stores or sends, change its text here, change
# the date, and rebuild. The other languages of the apps (Arabic, Spanish,
# French, Chinese for Petro-Rulers; Turkish, Persian, Arabic, Urdu,
# Indonesian for Quran Guardians) are not written yet.
#
# A text is plain lines: "# " the title, "@ " a small grey line, "## " a
# heading, "- " a list item, anything else a paragraph. {MAIL} is the
# support address. build.py (solo_doc) turns them into pages.
SOLO_DOCS = {
'petro-rulers': {
  'privacy': {
    'en': r'''# Petro-Rulers Privacy Policy
@ Effective date: 27 November 2026
@ Developer: Vatani Tech (Fardin Vatani), Baku, Azerbaijan
## 1. Summary
Petro-Rulers is a tool app for oil and gas sites, for Android and iPhone: a ruler, a protractor and a camera scanner that suggests the name of a valve or a piece of equipment. It has no account. The photos you take or choose are examined on your phone and are not sent anywhere (section 3). Anonymous crash reports (Sentry) and usage statistics (PostHog) help us fix and improve the app; they contain no name, email, photo or anything you type, and you can turn them off in Settings → Privacy (sections 6 and 7). Google AdMob shows banner ads to users who have not bought "Remove ads"; AdMob may collect device data for those ads, with your consent where the law requires it, and on iPhone Apple's advertising identifier is used only if you allow tracking (section 4). Google Play (Android) and the App Store (iPhone) handle the optional one-time "Remove ads" purchase (section 5). When it starts, the app asks Google Firebase whether an update is required (section 8).
## 2. Information stored on your device
The app saves the following in your phone's local storage:
- your settings: language, light or dark theme and your privacy choices;
- whether you bought "Remove ads", so the app stays ad-free offline;
- your ad consent choice, stored by Google's consent tool (section 4).
This information stays on your device. It is removed when you clear the app's data or uninstall the app. If backup is turned on for your phone, Android or iOS may include the app's saved data in your own Google or iCloud backup; we cannot see or access that backup.
## 3. Camera and photos
The app uses the camera only when you take a photo to identify a valve or a piece of equipment, and opens a photo from your gallery only when you choose one. The photo is examined by a model inside the app, on your phone. It is not sent to us or to anyone else. The ruler and the protractor work on the phone itself and send nothing.
## 4. Advertising (Google AdMob)
Users who have not bought "Remove ads" see banner ads provided by Google AdMob (Google LLC, or Google Ireland Limited in the EEA, the UK and Switzerland). To show, measure and protect ads against fraud, the AdMob software in the app may collect and send to Google:
- device identifiers, such as the Android advertising ID or, on iPhone, Apple's advertising identifier (IDFA) if you allow tracking;
- the IP address and the approximate location derived from it;
- device and app information, such as the model, operating system, language and app version;
- ad interactions, such as ads viewed and tapped, and diagnostic data.
In the European Economic Area, the United Kingdom and Switzerland, the app shows Google's consent form before any ad is loaded. You can choose whether Google may use your data for personalised ads, and you can change your choice at any time in the app's Settings. Where consent is not given, Google may still show non-personalised or limited ads. On iPhone, the app also shows Apple's "Allow tracking?" message; if you choose "Ask App Not to Track", Apple's advertising identifier is not shared with Google.
Google processes this data under its own policies (policies.google.com/privacy). We do not receive this data about you; AdMob gives us only totals, such as the number of ads shown and earnings. Your photos are never shared with AdMob.
## 5. The "Remove ads" purchase (Google Play and App Store)
"Remove ads" is an optional one-time purchase. On Android it is made through Google Play billing, on iPhone through Apple's App Store. Google or Apple processes the payment under its own terms and privacy policy. We never receive your card or payment details: Google gives us a record of each order (such as the order number, date, product, price and country), and Apple gives us only sales reports. The app stores on your phone only whether ads are removed, and checks with Google Play or the App Store whether the purchase is still valid.
## 6. Crash reports
If the app crashes or meets a serious error, a technical report is sent to Sentry (Functional Software, Inc., EU data region): what went wrong and where in the app's code, the app version, the phone model and system version, with a random number for this installation. It contains no name, email, photo, IP address or location. Reports are kept for 90 days and used only to fix problems. You can turn them off in Settings → Privacy.
## 7. Anonymous usage statistics
The app counts which pages are opened and the language the app is set to, and sends these counts to PostHog (PostHog Inc., EU Cloud) under a random number for this installation. It never sends names, emails, photos or anything you type. From the internet address (IP address) of the connection PostHog works out an approximate region (country and city, not your exact position); the address itself is not stored. We use the counts only to improve the app. Statistics are off until you allow them: the app asks once, and you can change your choice at any time in Settings → Privacy.
## 8. Update check
When the app starts, it asks Google Firebase (Remote Config) which is the oldest version of the app that may still be used, so that it can tell you when an update is necessary. The request carries a random number that Firebase creates for this installation, the app version, the system version, and the language, country and time zone set on your phone; it contains no name, no email and nothing you have typed. As with any internet connection, Google's servers receive your device's IP address. This check cannot be turned off.
## 9. Messages you send from the app
In "Report a problem" and "Contact" you can write a message to us inside the app. When you press Send, your text, your email address if you choose to add one, the app version, the phone model and system version, the app's language and the name of the screen you were on are sent to Sentry (Functional Software, Inc., EU data region), where we read them. No photo, screenshot, location or IP address is stored. We use the message only to answer you and to fix or improve the app, and it is kept for up to 90 days. Nothing is sent unless you press Send.
## 10. Third-party services
The app uses these services, each under its own privacy policy: Google AdMob (ads), Google Play and the App Store (the purchase), Sentry (crash reports and your messages), PostHog (statistics, only if you allow them) and Google Firebase Remote Config (the update check). We do not sell your data.
## 11. Children
The app is made for professionals and students and is not directed at children under 13. We do not knowingly collect personal data from children.
## 12. Your rights
The app has no account, so we hold no profile of you. You can turn off crash reports and statistics in Settings → Privacy and change your ad choices in the app's Settings. Depending on where you live (for example under the GDPR), you may have the right to access, correct or delete personal data about you, to object to its use, and to complain to your data protection authority. To use these rights, write to us.
## 13. Changes
We may update this policy when the app changes. The date at the top shows the latest version.
## 14. Contact
Vatani Tech (Fardin Vatani), Baku, Azerbaijan. Email: {MAIL}''',
    'az': r'''# Petro-Rulers Məxfilik Siyasəti
@ Qüvvəyə minmə tarixi: 27 noyabr 2026
@ Tərtibatçı: Vatani Tech (Fardin Vatani), Bakı, Azərbaycan
## 1. Xülasə
Petro-Rulers neft-qaz sahələri üçün Android və iPhone alət tətbiqidir: xətkeş, bucaqölçən və siyirtmənin və ya avadanlığın adını təklif edən kamera skaneri. Tətbiqdə hesab yoxdur. Çəkdiyiniz və ya seçdiyiniz şəkillər telefonunuzda təhlil olunur və heç yerə göndərilmir (bölmə 3). Anonim xəta hesabatları (Sentry) və istifadə statistikası (PostHog) tətbiqi düzəltməyə və yaxşılaşdırmağa kömək edir; onlarda ad, e-poçt, şəkil və ya yazdığınız heç nə olmur və onları Ayarlar → Məxfilik bölməsində söndürə bilərsiniz (bölmə 6 və 7). “Reklamı sil” almayan istifadəçilərə Google AdMob banner reklamları göstərir; AdMob bu reklamlar üçün cihaz məlumatlarını toplaya bilər (qanun tələb etdiyi yerdə razılığınızla), iPhone-da isə Apple-ın reklam identifikatoru yalnız izləməyə icazə verdiyiniz halda istifadə olunur (bölmə 4). İstəyə bağlı birdəfəlik “Reklamı sil” alışını Google Play (Android) və App Store (iPhone) həyata keçirir (bölmə 5). Tətbiq açılanda Google Firebase-dən yeniləmənin vacib olub-olmadığını soruşur (bölmə 8).
## 2. Cihazınızda saxlanılan məlumat
Tətbiq telefonunuzun yerli yaddaşında bunları saxlayır:
- ayarlarınız: dil, açıq və ya tünd rejim və məxfilik seçimləriniz;
- “Reklamı sil” alıb-almadığınız (tətbiq oflayn da reklamsız qalsın deyə);
- reklam razılığı seçiminiz: onu Google-un razılıq aləti saxlayır (bölmə 4).
Bu məlumat cihazınızda qalır. Tətbiqin məlumatlarını təmizlədikdə və ya tətbiqi sildikdə o da silinir. Telefonunuzda ehtiyat nüsxə yandırılıbsa, Android və ya iOS tətbiqin saxladığı məlumatı sizin öz Google və ya iCloud ehtiyat nüsxənizə daxil edə bilər; biz o nüsxəni görə və ona daxil ola bilmirik.
## 3. Kamera və şəkillər
Tətbiq kameradan yalnız siz siyirtməni və ya avadanlığı tanımaq üçün şəkil çəkəndə istifadə edir, qalereyadan isə yalnız özünüz seçdiyiniz şəkli açır. Şəkli tətbiqin içindəki model telefonunuzda təhlil edir. O, nə bizə, nə də başqa birinə göndərilir. Xətkeş və bucaqölçən telefonun özündə işləyir və heç nə göndərmir.
## 4. Reklam (Google AdMob)
“Reklamı sil” almayan istifadəçilər Google AdMob-un (Google LLC, AİZ, Böyük Britaniya və İsveçrədə isə Google Ireland Limited) təqdim etdiyi banner reklamlarını görürlər. Reklamları göstərmək, ölçmək və saxtakarlıqdan qorumaq üçün tətbiqdəki AdMob proqramı aşağıdakıları toplaya və Google-a göndərə bilər:
- cihaz identifikatorları, məsələn, Android reklam identifikatoru və ya iPhone-da, izləməyə icazə versəniz, Apple-ın reklam identifikatoru (IDFA);
- IP ünvanı və ondan müəyyən edilən təxmini yer;
- cihaz və tətbiq haqqında məlumat, məsələn, model, əməliyyat sistemi, dil və tətbiqin versiyası;
- reklamlarla qarşılıqlı əlaqə (baxılan və toxunulan reklamlar) və diaqnostika məlumatı.
Avropa İqtisadi Zonasında, Böyük Britaniyada və İsveçrədə tətbiq hər hansı reklam yüklənməzdən əvvəl Google-un razılıq formasını göstərir. Google-un məlumatlarınızdan fərdiləşdirilmiş reklam üçün istifadə edib-etməyəcəyini özünüz seçirsiniz və seçiminizi istənilən vaxt tətbiqin Ayarlar bölməsində dəyişə bilərsiniz. Razılıq verilmədikdə Google yenə də fərdiləşdirilməmiş və ya məhdud reklamlar göstərə bilər. iPhone-da tətbiq həmçinin Apple-ın “İzləməyə icazə verilsin?” mesajını göstərir; “Tətbiqdən izləməməyi xahiş et” seçsəniz, Apple-ın reklam identifikatoru Google ilə paylaşılmır.
Google bu məlumatı öz siyasətlərinə uyğun emal edir (policies.google.com/privacy). Sizin haqqınızda bu məlumatı biz almırıq; AdMob bizə yalnız ümumi rəqəmləri verir, məsələn, göstərilən reklamların sayı və gəlir. Şəkilləriniz heç vaxt AdMob ilə paylaşılmır.
## 5. “Reklamı sil” alışı (Google Play və App Store)
“Reklamı sil” istəyə bağlı birdəfəlik alışdır. Android-də o, Google Play ödəniş sistemi, iPhone-da isə Apple-ın App Store-u vasitəsilə edilir. Ödənişi Google və ya Apple öz şərtlərinə və məxfilik siyasətinə uyğun emal edir. Kart və ya ödəniş məlumatlarınızı biz heç vaxt almırıq: Google bizə hər sifarişin qeydini verir (məsələn, sifarişin nömrəsi, tarix, məhsul, qiymət və ölkə), Apple isə yalnız satış hesabatlarını. Tətbiq telefonunuzda yalnız reklamların silinib-silinmədiyini saxlayır və alışın hələ də etibarlı olduğunu Google Play və ya App Store-dan yoxlayır.
## 6. Xəta hesabatları
Tətbiq dayandıqda və ya ciddi xəta baş verdikdə Sentry-yə (Functional Software, Inc., AB məlumat regionu) texniki hesabat göndərilir: nəyin səhv getdiyi və tətbiq kodunun harasında, tətbiqin versiyası, telefonun modeli və sistemin versiyası, eləcə də bu quraşdırma üçün təsadüfi nömrə. Hesabatda ad, e-poçt, şəkil, IP ünvanı və ya məkan olmur. Hesabatlar 90 gün saxlanılır və yalnız problemləri düzəltmək üçün istifadə olunur. Onları Ayarlar → Məxfilik bölməsində söndürə bilərsiniz.
## 7. Anonim istifadə statistikası
Tətbiq hansı səhifələrin açıldığını və tətbiqin dilini sayır və bu sayları bu quraşdırma üçün təsadüfi nömrə ilə PostHog-a (PostHog Inc., EU Cloud) göndərir. Adlar, e-poçtlar, şəkillər və ya yazdıqlarınız heç vaxt göndərilmir. PostHog bağlantının internet ünvanından (IP ünvanı) təxmini regionu (ölkə və şəhər, dəqiq yeriniz yox) müəyyən edir; ünvanın özü saxlanılmır. Bu saylardan yalnız tətbiqi yaxşılaşdırmaq üçün istifadə edirik. Statistika siz icazə verənə qədər söndürülmüş olur: tətbiq bir dəfə soruşur, seçiminizi istənilən vaxt Ayarlar → Məxfilik bölməsində dəyişə bilərsiniz.
## 8. Yeniləmə yoxlaması
Tətbiq açılanda Google Firebase-dən (Remote Config) tətbiqin hələ istifadə oluna bilən ən köhnə versiyasını soruşur ki, yeniləmə vacib olanda sizə bildirsin. Sorğuda Firebase-in bu quraşdırma üçün yaratdığı təsadüfi nömrə, tətbiqin versiyası, sistemin versiyası və telefonunuzda qurulmuş dil, ölkə və saat qurşağı olur; ad, e-poçt və yazdığınız heç nə olmur. Hər internet bağlantısında olduğu kimi, Google-un serverləri cihazınızın IP ünvanını alır. Bu yoxlamanı söndürmək olmur.
## 9. Tətbiqdən göndərdiyiniz mesajlar
“Problemi bildir” və “Əlaqə” bölmələrində bizə tətbiqin daxilində mesaj yaza bilərsiniz. “Göndər” düyməsinə basdıqda mətniniz, istəsəniz əlavə etdiyiniz e-poçt ünvanınız, tətbiqin versiyası, telefonun modeli və sistemin versiyası, tətbiqin dili və olduğunuz ekranın adı Sentry-yə (Functional Software, Inc., AB məlumat regionu) göndərilir və biz onları orada oxuyuruq. Şəkil, ekran görüntüsü, məkan və ya IP ünvanı saxlanılmır. Mesajdan yalnız sizə cavab vermək və tətbiqi düzəltmək və ya yaxşılaşdırmaq üçün istifadə edirik; o, ən çoxu 90 gün saxlanılır. “Göndər” düyməsinə basmasanız, heç nə göndərilmir.
## 10. Üçüncü tərəf xidmətləri
Tətbiq bu xidmətlərdən istifadə edir, hər birinin öz məxfilik siyasəti var: Google AdMob (reklam), Google Play və App Store (alış), Sentry (xəta hesabatları və mesajlarınız), PostHog (statistika, yalnız icazə versəniz) və Google Firebase Remote Config (yeniləmə yoxlaması). Məlumatlarınızı satmırıq.
## 11. Uşaqlar
Tətbiq mütəxəssislər və tələbələr üçün hazırlanıb və 13 yaşdan kiçik uşaqlar üçün nəzərdə tutulmayıb. Uşaqlardan bilərəkdən şəxsi məlumat toplamırıq.
## 12. Hüquqlarınız
Tətbiqdə hesab yoxdur, buna görə sizin haqqınızda profil saxlamırıq. Xəta hesabatlarını və statistikanı Ayarlar → Məxfilik bölməsində söndürə, reklam seçimlərinizi isə tətbiqin Ayarlar bölməsində dəyişə bilərsiniz. Yaşadığınız yerdən asılı olaraq (məsələn, GDPR-ə əsasən) haqqınızdakı şəxsi məlumata baxmaq, onu düzəltmək və ya sildirmək, istifadəsinə etiraz etmək və məlumatların qorunması üzrə orqana şikayət etmək hüququnuz ola bilər. Bu hüquqlardan istifadə etmək üçün bizə yazın.
## 13. Dəyişikliklər
Tətbiq dəyişdikdə bu siyasəti yeniləyə bilərik. Yuxarıdakı tarix son versiyanı göstərir.
## 14. Əlaqə
Vatani Tech (Fardin Vatani), Bakı, Azərbaycan. E-poçt: {MAIL}''',
    'ru': r'''# Политика конфиденциальности Petro-Rulers
@ Дата вступления в силу: 27 ноября 2026 г.
@ Разработчик: Vatani Tech (Fardin Vatani), Баку, Азербайджан
## 1. Кратко
Petro-Rulers — приложение-инструмент для нефтегазовых объектов, для Android и iPhone: линейка, транспортир и сканер с камерой, который подсказывает название арматуры или оборудования. В приложении нет аккаунта. Фотографии, которые вы делаете или выбираете, анализируются на вашем телефоне и никуда не отправляются (раздел 3). Анонимные отчёты о сбоях (Sentry) и статистика использования (PostHog) помогают нам исправлять и улучшать приложение; в них нет имени, электронной почты, фотографий и того, что вы вводите, и их можно отключить в разделе Настройки → Конфиденциальность (разделы 6 и 7). Тем, кто не купил «Убрать рекламу», Google AdMob показывает баннерную рекламу; для этой рекламы AdMob может собирать данные об устройстве (с вашего согласия там, где этого требует закон), а на iPhone рекламный идентификатор Apple используется, только если вы разрешили отслеживание (раздел 4). Необязательную разовую покупку «Убрать рекламу» проводят Google Play (Android) и App Store (iPhone) (раздел 5). При запуске приложение спрашивает у Google Firebase, требуется ли обновление (раздел 8).
## 2. Данные, которые хранятся на вашем устройстве
Приложение сохраняет в локальной памяти телефона:
- ваши настройки: язык, светлую или тёмную тему и выбор параметров конфиденциальности;
- купили ли вы «Убрать рекламу», чтобы приложение оставалось без рекламы и офлайн;
- ваш выбор согласия на рекламу: его хранит инструмент согласия Google (раздел 4).
Эти данные остаются на вашем устройстве. Они удаляются, когда вы очищаете данные приложения или удаляете приложение. Если на телефоне включено резервное копирование, Android или iOS могут включить сохранённые данные приложения в вашу собственную резервную копию Google или iCloud; у нас нет доступа к этой копии.
## 3. Камера и фотографии
Приложение использует камеру, только когда вы делаете снимок, чтобы определить арматуру или оборудование, и открывает фотографию из галереи, только когда вы сами её выбираете. Фотографию анализирует модель внутри приложения, на вашем телефоне. Она не отправляется ни нам, ни кому-либо ещё. Линейка и транспортир работают на самом телефоне и ничего не отправляют.
## 4. Реклама (Google AdMob)
Те, кто не купил «Убрать рекламу», видят баннерную рекламу, которую предоставляет Google AdMob (Google LLC, а в ЕЭЗ, Великобритании и Швейцарии — Google Ireland Limited). Чтобы показывать рекламу, измерять её и защищать от мошенничества, программа AdMob в приложении может собирать и отправлять в Google:
- идентификаторы устройства, например рекламный идентификатор Android или, на iPhone, рекламный идентификатор Apple (IDFA), если вы разрешили отслеживание;
- IP-адрес и определяемое по нему примерное местоположение;
- сведения об устройстве и приложении, например модель, операционную систему, язык и версию приложения;
- действия с рекламой (просмотры и нажатия) и диагностические данные.
В Европейской экономической зоне, Великобритании и Швейцарии приложение показывает форму согласия Google до загрузки любой рекламы. Вы решаете, может ли Google использовать ваши данные для персонализированной рекламы, и можете изменить выбор в любое время в настройках приложения. Без согласия Google всё равно может показывать неперсонализированную или ограниченную рекламу. На iPhone приложение также показывает сообщение Apple «Разрешить отслеживание?»; если вы выберете «Попросить не отслеживать», рекламный идентификатор Apple не передаётся Google.
Google обрабатывает эти данные по собственным правилам (policies.google.com/privacy). Мы не получаем эти данные о вас; AdMob сообщает нам только итоговые цифры, например число показов и доход. Ваши фотографии никогда не передаются AdMob.
## 5. Покупка «Убрать рекламу» (Google Play и App Store)
«Убрать рекламу» — необязательная разовая покупка. На Android она совершается через платёжную систему Google Play, на iPhone — через App Store компании Apple. Платёж обрабатывает Google или Apple на своих условиях и по своей политике конфиденциальности. Мы никогда не получаем данные вашей карты или платежа: Google передаёт нам запись о каждом заказе (например, номер заказа, дату, товар, цену и страну), а Apple — только отчёты о продажах. Приложение хранит на телефоне только отметку о том, убрана ли реклама, и проверяет в Google Play или App Store, действительна ли покупка.
## 6. Отчёты о сбоях
Если приложение аварийно закрывается или встречает серьёзную ошибку, технический отчёт отправляется в Sentry (Functional Software, Inc., регион хранения данных ЕС): что произошло и в каком месте кода, версия приложения, модель телефона и версия системы, а также случайный номер этой установки. В нём нет имени, электронной почты, фотографий, IP-адреса или местоположения. Отчёты хранятся 90 дней и используются только для исправления ошибок. Их можно отключить в разделе Настройки → Конфиденциальность.
## 7. Анонимная статистика использования
Приложение считает, какие страницы открываются, и язык приложения и отправляет эти данные в PostHog (PostHog Inc., EU Cloud) под случайным номером этой установки. Оно никогда не отправляет имена, адреса почты, фотографии или то, что вы вводите. По интернет-адресу (IP-адресу) соединения PostHog определяет примерный регион (страну и город, не точное местоположение); сам адрес не сохраняется. Мы используем эти данные только для улучшения приложения. Статистика выключена, пока вы её не разрешите: приложение спрашивает один раз, а изменить выбор можно в любое время в разделе Настройки → Конфиденциальность.
## 8. Проверка обновлений
При запуске приложение спрашивает у Google Firebase (Remote Config), какая самая старая версия приложения ещё может использоваться, чтобы сообщить вам, когда обновление необходимо. В запросе передаются случайный номер, который Firebase создаёт для этой установки, версия приложения, версия системы, а также язык, страна и часовой пояс, заданные на телефоне; в нём нет имени, электронной почты и того, что вы вводили. Как и при любом интернет-соединении, серверы Google получают IP-адрес вашего устройства. Эту проверку нельзя отключить.
## 9. Сообщения, которые вы отправляете из приложения
В разделах «Сообщить о проблеме» и «Связаться» можно написать нам прямо в приложении. Когда вы нажимаете «Отправить», ваш текст, адрес электронной почты (если вы решили его указать), версия приложения, модель телефона и версия системы, язык приложения и название экрана, на котором вы были, отправляются в Sentry (Functional Software, Inc., регион хранения данных ЕС), где мы их читаем. Фотографии, снимки экрана, местоположение и IP-адрес не сохраняются. Мы используем сообщение только для того, чтобы ответить вам и исправить или улучшить приложение; оно хранится не дольше 90 дней. Ничего не отправляется, пока вы не нажмёте «Отправить».
## 10. Сторонние сервисы
Приложение использует следующие сервисы, у каждого своя политика конфиденциальности: Google AdMob (реклама), Google Play и App Store (покупка), Sentry (отчёты о сбоях и ваши сообщения), PostHog (статистика, только с вашего разрешения) и Google Firebase Remote Config (проверка обновлений). Мы не продаём ваши данные.
## 11. Дети
Приложение создано для специалистов и студентов и не предназначено для детей младше 13 лет. Мы сознательно не собираем персональные данные детей.
## 12. Ваши права
В приложении нет аккаунта, поэтому мы не храним ваш профиль. Отчёты о сбоях и статистику можно отключить в разделе Настройки → Конфиденциальность, а выбор в отношении рекламы изменить в настройках приложения. В зависимости от того, где вы живёте (например, по GDPR), у вас может быть право получить доступ к персональным данным о вас, исправить или удалить их, возразить против их использования и подать жалобу в орган по защите данных. Чтобы воспользоваться этими правами, напишите нам.
## 13. Изменения
Мы можем обновлять эту политику, когда меняется приложение. Дата вверху показывает последнюю версию.
## 14. Контакты
Vatani Tech (Fardin Vatani), Баку, Азербайджан. Электронная почта: {MAIL}''',
  },
  'terms': {
    'en': r'''# Petro-Rulers – Terms of use
By using Petro-Rulers you agree to these terms. They are short and written in plain language.
## 1. Approximate results
Petro-Rulers measures with your phone’s screen and sensors and suggests names from photos. Results are approximate and the camera can be wrong. Never use them instead of proper instruments, a qualified engineer, official standards or your company’s procedures. You use the results at your own risk.
## 2. No warranty
The app is provided “as is”, without any warranty. To the extent the law allows, the developer is not liable for any loss or damage resulting from its use.
## 3. Purchases and ads
The app is free and shows ads. “Remove ads” is a one-time purchase handled by Google Play or the App Store under their terms; restore it with “Restore purchases”.
## 4. Content
Texts, drawings and data in the app belong to the developer or their owners. You may share screenshots and results for personal, non-commercial use.
## 5. Changes and contact
These terms may change with new versions of the app. Questions: use “Contact” in the app. Privacy: see the privacy policy.
@ Last updated: 20 November 2026''',
    'az': r'''# Petro-Rulers – İstifadə şərtləri
Petro-Rulers-dan istifadə etməklə bu şərtlərlə razılaşırsınız. Onlar qısadır və sadə dillə yazılıb.
## 1. Təxmini nəticələr
Petro-Rulers telefonunuzun ekranı və sensorları ilə ölçür və şəkillərə görə adlar təklif edir. Nəticələr təxminidir və kamera səhv edə bilər. Onları heç vaxt düzgün cihazların, ixtisaslı mühəndisin, rəsmi standartların və ya şirkətinizin qaydalarının əvəzinə istifadə etməyin. Nəticələrdən öz riskinizlə istifadə edirsiniz.
## 2. Zəmanət yoxdur
Tətbiq heç bir zəmanət olmadan “olduğu kimi” təqdim olunur. Qanunun icazə verdiyi həddə tərtibatçı onun istifadəsindən yaranan heç bir itki və ya ziyana görə məsuliyyət daşımır.
## 3. Alışlar və reklam
Tətbiq pulsuzdur və reklam göstərir. “Reklamı sil” Google Play və ya App Store tərəfindən onların şərtlərinə əsasən həyata keçirilən birdəfəlik alışdır; onu “Alışı bərpa et” ilə bərpa edin.
## 4. Məzmun
Tətbiqdəki mətnlər, rəsmlər və məlumatlar tərtibatçıya və ya onların sahiblərinə məxsusdur. Ekran görüntülərini və nəticələri şəxsi, qeyri-kommersiya məqsədilə paylaşa bilərsiniz.
## 5. Dəyişikliklər və əlaqə
Bu şərtlər tətbiqin yeni versiyaları ilə dəyişə bilər. Suallar üçün: tətbiqdə “Əlaqə” bölməsindən istifadə edin. Məxfilik: “Məxfilik siyasəti”nə baxın.
@ Son yenilənmə: 20 noyabr 2026''',
    'ru': r'''# Petro-Rulers – Условия использования
Пользуясь Petro-Rulers, вы соглашаетесь с этими условиями. Они короткие и написаны простым языком.
## 1. Приблизительные результаты
Petro-Rulers измеряет с помощью экрана и датчиков телефона и предлагает названия по фотографиям. Результаты приблизительны, и камера может ошибаться. Никогда не используйте их вместо настоящих приборов, квалифицированного инженера, официальных стандартов или процедур вашей компании. Вы используете результаты на свой риск.
## 2. Без гарантий
Приложение предоставляется «как есть», без каких-либо гарантий. В пределах, допускаемых законом, разработчик не несёт ответственности за любые убытки или ущерб от его использования.
## 3. Покупки и реклама
Приложение бесплатное и показывает рекламу. «Убрать рекламу» — разовая покупка через Google Play или App Store на их условиях; восстановить её можно кнопкой «Восстановить покупку».
## 4. Содержимое
Тексты, рисунки и данные в приложении принадлежат разработчику или их владельцам. Вы можете делиться скриншотами и результатами для личного некоммерческого использования.
## 5. Изменения и связь
Эти условия могут меняться с новыми версиями приложения. Вопросы: используйте «Связаться» в приложении. Конфиденциальность: см. «Политику конфиденциальности».
@ Последнее обновление: 20 ноября 2026 г.''',
  },
},
'marinegram': {
  'privacy': {
    'en': r'''# MarineGram Privacy Policy
@ Effective date: 28 November 2026
@ Developer: Vatani Tech (Fardin Vatani), Baku, Azerbaijan
## 1. Summary
MarineGram is an offline pocket reference for marine work, for Android and iPhone. It is still being made. The app collects no personal data: it has no account, no ads, no usage statistics and no crash reports, and it does not use the internet.
## 2. Information stored on your device
The app saves only its own settings in your phone's local storage. They stay on your device and are removed when you clear the app's data or uninstall the app. If backup is turned on for your phone, Android or iOS may include the app's settings in your own Google or iCloud backup; we cannot see or access that backup.
## 3. Internet use
The app works fully offline and sends nothing. Its map, texts, drawings and 3D models are stored inside the app. The AR button of the 3D view, on phones that support it, opens the phone's own AR viewer (Apple's or Google's), which uses the camera to show the ship in your room; the app itself does not save or send any picture. If you open a link from the app, such as this policy, your phone's browser or email app opens; those apps have their own privacy practices.
## 4. Third-party services
No third party receives data from the app.
## 5. Children
The app does not collect personal data from anyone, including children.
## 6. Changes
The app is in development. If a later version adds features that use the internet, such as ads, purchases, crash reports or statistics, this policy will be updated before that version is published. The date at the top shows the latest version.
## 7. Contact
Vatani Tech (Fardin Vatani), Baku, Azerbaijan. Email: {MAIL}''',
    'az': r'''# MarineGram Məxfilik Siyasəti
@ Qüvvəyə minmə tarixi: 28 noyabr 2026
@ Tərtibatçı: Vatani Tech (Fardin Vatani), Bakı, Azərbaycan
## 1. Xülasə
MarineGram dənizçilik işi üçün Android və iPhone-da işləyən oflayn cib bələdçisidir. Tətbiq hələ hazırlanır. Tətbiq heç bir şəxsi məlumat toplamır: onda hesab, reklam, istifadə statistikası və xəta hesabatları yoxdur və o, internetdən istifadə etmir.
## 2. Cihazınızda saxlanılan məlumat
Tətbiq telefonunuzun yerli yaddaşında yalnız öz ayarlarını saxlayır. Onlar cihazınızda qalır və tətbiqin məlumatlarını təmizlədikdə və ya tətbiqi sildikdə silinir. Telefonunuzda ehtiyat nüsxə yandırılıbsa, Android və ya iOS tətbiqin ayarlarını sizin öz Google və ya iCloud ehtiyat nüsxənizə daxil edə bilər; biz o nüsxəni görə və ona daxil ola bilmirik.
## 3. İnternetdən istifadə
Tətbiq tam oflayn işləyir və heç nə göndərmir. Xəritəsi, mətnləri, rəsmləri və 3D modelləri tətbiqin içində saxlanılır. 3D görünüşün AR düyməsi (onu dəstəkləyən telefonlarda) telefonun öz AR baxış proqramını (Apple və ya Google) açır; o, gəmini otağınızda göstərmək üçün kameradan istifadə edir. Tətbiqin özü heç bir şəkli saxlamır və göndərmir. Tətbiqdən bir keçid açsanız (məsələn, bu siyasəti), telefonunuzun brauzeri və ya e-poçt tətbiqi açılır; onların öz məxfilik qaydaları var.
## 4. Üçüncü tərəf xidmətləri
Heç bir üçüncü tərəf tətbiqdən məlumat almır.
## 5. Uşaqlar
Tətbiq heç kimdən, o cümlədən uşaqlardan şəxsi məlumat toplamır.
## 6. Dəyişikliklər
Tətbiq hazırlanma mərhələsindədir. Sonrakı versiyaya internetdən istifadə edən funksiyalar (məsələn, reklam, alışlar, xəta hesabatları və ya statistika) əlavə olunarsa, bu siyasət həmin versiya dərc edilməzdən əvvəl yenilənəcək. Yuxarıdakı tarix son versiyanı göstərir.
## 7. Əlaqə
Vatani Tech (Fardin Vatani), Bakı, Azərbaycan. E-poçt: {MAIL}''',
    'ru': r'''# Политика конфиденциальности MarineGram
@ Дата вступления в силу: 28 ноября 2026 г.
@ Разработчик: Vatani Tech (Fardin Vatani), Баку, Азербайджан
## 1. Кратко
MarineGram — карманный офлайн-справочник по морскому делу для Android и iPhone. Приложение ещё создаётся. Оно не собирает персональные данные: в нём нет аккаунта, рекламы, статистики использования и отчётов о сбоях, и оно не использует интернет.
## 2. Данные, которые хранятся на вашем устройстве
Приложение сохраняет в локальной памяти телефона только собственные настройки. Они остаются на вашем устройстве и удаляются, когда вы очищаете данные приложения или удаляете приложение. Если на телефоне включено резервное копирование, Android или iOS могут включить настройки приложения в вашу собственную резервную копию Google или iCloud; у нас нет доступа к этой копии.
## 3. Использование интернета
Приложение полностью работает офлайн и ничего не отправляет. Карта, тексты, рисунки и 3D-модели хранятся внутри приложения. Кнопка AR в 3D-просмотре (на телефонах, которые это поддерживают) открывает собственное средство просмотра AR телефона (Apple или Google), которое использует камеру, чтобы показать судно в вашей комнате; само приложение не сохраняет и не отправляет никаких изображений. Если вы открываете из приложения ссылку, например эту политику, открывается браузер или почтовое приложение телефона; у них свои правила конфиденциальности.
## 4. Сторонние сервисы
Ни одна третья сторона не получает данные из приложения.
## 5. Дети
Приложение не собирает персональные данные ни у кого, включая детей.
## 6. Изменения
Приложение находится в разработке. Если в следующей версии появятся функции, использующие интернет (например, реклама, покупки, отчёты о сбоях или статистика), эта политика будет обновлена до публикации такой версии. Дата вверху показывает последнюю версию.
## 7. Контакты
Vatani Tech (Fardin Vatani), Баку, Азербайджан. Электронная почта: {MAIL}''',
  },
  'terms': {
    'en': r'''# MarineGram – Terms of use
By using MarineGram you agree to these terms. They are short and written in plain language.
## 1. For learning only
MarineGram is a reference and learning tool. Its map, glossary, descriptions of ships and ship systems, figures and 3D models are given in good faith but may contain mistakes. Never use them for navigation, and never instead of official charts and publications, international rules (SOLAS, COLREG, MARPOL, STCW), the maker's manuals, your ship's safety management system, your company's procedures or the orders of the master and officers. You use the information at your own risk.
## 2. No warranty
The app is provided “as is”, without any warranty. To the extent the law allows, the developer is not liable for any loss or damage resulting from its use.
## 3. Content
Texts, drawings and data in the app belong to the developer or their owners. The map is made with Natural Earth data, which is in the public domain. Some 3D models were made by other authors and are used under the Creative Commons Attribution 4.0 licence; each is credited in the app, under the model. You may share screenshots for personal, non-commercial use.
## 4. Changes and contact
These terms may change with new versions of the app. Questions: write to {MAIL}. Privacy: see the privacy policy.
@ Last updated: 28 November 2026''',
    'az': r'''# MarineGram – İstifadə şərtləri
MarineGram-dan istifadə etməklə bu şərtlərlə razılaşırsınız. Onlar qısadır və sadə dillə yazılıb.
## 1. Yalnız öyrənmək üçün
MarineGram məlumat və öyrənmə vasitəsidir. Xəritəsi, lüğəti, gəmilərin və gəmi sistemlərinin təsvirləri, rəqəmləri və 3D modelləri vicdanla hazırlanıb, lakin səhvlər ola bilər. Onlardan heç vaxt naviqasiya üçün, eləcə də rəsmi xəritələrin və nəşrlərin, beynəlxalq qaydaların (SOLAS, COLREG, MARPOL, STCW), istehsalçının təlimatlarının, gəminizin təhlükəsizliyin idarə edilməsi sisteminin, şirkətinizin qaydalarının və ya kapitanın və zabitlərin əmrlərinin əvəzinə istifadə etməyin. Məlumatdan öz riskinizlə istifadə edirsiniz.
## 2. Zəmanət yoxdur
Tətbiq heç bir zəmanət olmadan “olduğu kimi” təqdim olunur. Qanunun icazə verdiyi həddə tərtibatçı onun istifadəsindən yaranan heç bir itki və ya ziyana görə məsuliyyət daşımır.
## 3. Məzmun
Tətbiqdəki mətnlər, rəsmlər və məlumatlar tərtibatçıya və ya onların sahiblərinə məxsusdur. Xəritə ictimai mülkiyyətdə olan Natural Earth məlumatları ilə hazırlanıb. Bəzi 3D modelləri başqa müəlliflər hazırlayıb və onlar Creative Commons Attribution 4.0 lisenziyası ilə istifadə olunur; hər birinin müəllifi tətbiqdə, modelin altında göstərilir. Ekran görüntülərini şəxsi, qeyri-kommersiya məqsədilə paylaşa bilərsiniz.
## 4. Dəyişikliklər və əlaqə
Bu şərtlər tətbiqin yeni versiyaları ilə dəyişə bilər. Suallar üçün {MAIL} ünvanına yazın. Məxfilik: “Məxfilik siyasəti”nə baxın.
@ Son yenilənmə: 28 noyabr 2026''',
    'ru': r'''# MarineGram – Условия использования
Используя MarineGram, вы соглашаетесь с этими условиями. Они короткие и написаны простым языком.
## 1. Только для обучения
MarineGram — справочный и учебный инструмент. Его карта, глоссарий, описания судов и судовых систем, цифры и 3D-модели подготовлены добросовестно, но могут содержать ошибки. Никогда не используйте их для навигации, а также вместо официальных карт и изданий, международных правил (SOLAS, COLREG, MARPOL, STCW), руководств изготовителя, системы управления безопасностью вашего судна, процедур вашей компании или распоряжений капитана и офицеров. Вы используете информацию на свой риск.
## 2. Без гарантий
Приложение предоставляется «как есть», без каких-либо гарантий. В пределах, допускаемых законом, разработчик не несёт ответственности за любые убытки или ущерб от его использования.
## 3. Содержимое
Тексты, рисунки и данные в приложении принадлежат разработчику или их владельцам. Карта создана на основе данных Natural Earth, находящихся в общественном достоянии. Некоторые 3D-модели созданы другими авторами и используются по лицензии Creative Commons Attribution 4.0; автор каждой указан в приложении под моделью. Вы можете делиться скриншотами для личного некоммерческого использования.
## 4. Изменения и связь
Эти условия могут меняться с новыми версиями приложения. Вопросы: пишите на {MAIL}. Конфиденциальность: см. «Политику конфиденциальности».
@ Последнее обновление: 28 ноября 2026 г.''',
  },
},
'quran-guardians': {
  'privacy': {
    'en': r'''# Quran Guardians Privacy Policy
@ Effective date: 28 November 2026
@ Developer: Vatani Tech (Fardin Vatani), Baku, Azerbaijan
## 1. Summary
Quran Guardians (first called Hafiz) is a free app for reading and memorising the Quran, with recitations, a short tafsir, hadiths and prayer times, for Android and iPhone. What you do in the app stays on your phone. The app has no ads and no account, and it collects no data: no usage statistics and no crash reports. The internet is used for three things only: to download recitations when you choose to listen (section 3), to ask your phone's own map service for the name of your city if you use your location for prayer times (section 4), and for an optional gift through the App Store or Google Play (section 6).
## 2. Information stored on your device
The app saves the following in your phone's local storage:
- your settings: app language, translation, tafsir, reciter, text sizes and colours;
- where you stopped reading, your bookmarks, notes and highlighted verses;
- your memorising progress, the dates of your next reviews, your reading plan and your statistics (time spent reading and memorising, days in a row);
- what you enter on the Prayer tab: the prayers and fasts you tick, your tasbih counts and the figures you type into the zakat calculator;
- your place for prayer times, if you use your location (section 4);
- the recitations you have played or downloaded, and your own recordings (section 5).
This information stays on your device; we cannot see it. In Settings you can delete your progress with “Reset memorization progress”, the saved recitations with “Delete saved audio” and your recordings with “Delete recordings”. Everything is removed when you clear the app's data or uninstall the app. “Save backup file” writes your progress, bookmarks, plan and settings into a file, and sharing a verse makes a picture; your phone's share sheet then opens and you choose where the file or the picture goes. The app itself sends them nowhere. If backup is turned on for your phone, Android or iOS may include the app's saved data in your own Google or iCloud backup; we cannot see or access that backup.
## 3. Recitations (internet)
When you play or download a recitation, the app downloads the audio from AlQuran Cloud (the Islamic Network, at cdn.islamic.network). The request says only which verse and which reciter. It contains no personal data. As with any internet connection, that server receives your device's IP address and handles it under its own rules (alquran.cloud). A recitation is downloaded once, saved on your phone and then played from there.
Everything else (the text, the translations, the tafsir, the hadiths and the calculation of prayer times) works without an internet connection. If you open a link from the app, such as this policy or a source's website, your phone's browser or email app opens; those apps have their own privacy practices.
## 4. Location (prayer times and Qibla)
Prayer times and the direction of the Qibla are calculated on your phone. If you tap “Use my location”, the app asks for your permission and reads your approximate location once. It is kept on your phone only and is never sent to us. To show the name of your city, the app asks your phone's own map service (Apple's on iPhone, Google's on Android) once; that service receives the position and handles it under its own privacy policy. The Qibla compass uses your phone's compass sensor.
## 5. Microphone, notifications and widgets
The microphone is used only when you tap “Record” to record your own recitation. Recordings are saved in the app's own folder on your phone; they are never uploaded and are not part of the backup file. The daily reminder and the prayer notifications are planned by the app on your phone; no server sends them. The home-screen widgets (verse of the day, prayer times) show what the app has saved on your phone.
## 6. Gifts (App Store and Google Play)
The app is free and nothing in it has to be bought. If you wish, you can give a one-time gift to the makers of the app on its support page. On Android it is made through Google Play billing, on iPhone through Apple's App Store. Google or Apple processes the payment under its own terms and privacy policy. We never receive your card or payment details: Google gives us a record of each order (such as the order number, date, product, price and country), and Apple gives us only sales reports. A gift unlocks nothing in the app.
## 7. Third-party services
AlQuran Cloud provides the recitation audio (section 3). Your phone's map service, from Apple or Google, gives the name of your city (section 4). The App Store and Google Play handle gifts (section 6). The app uses no advertising, statistics or crash-report service, and we do not sell or share any data.
## 8. Children
The app does not collect personal data from anyone, including children.
## 9. Your rights
We hold no data about you: what the app saves is only on your phone, under your control. If you have a question, write to us.
## 10. Changes
We may update this policy when the app changes. The date at the top shows the latest version.
## 11. Contact
Vatani Tech (Fardin Vatani), Baku, Azerbaijan. Email: {MAIL}''',
    'az': r'''# Quran Guardians Məxfilik Siyasəti
@ Qüvvəyə minmə tarixi: 28 noyabr 2026
@ Tərtibatçı: Vatani Tech (Fardin Vatani), Bakı, Azərbaycan
## 1. Xülasə
Quran Guardians (Azərbaycan dilində “Quran Keşikçiləri”; əvvəlki adı Hafiz) Quranı oxumaq və əzbərləmək üçün Android və iPhone-da işləyən pulsuz tətbiqdir: tilavətlər, qısa təfsir, hədislər və namaz vaxtları ilə. Tətbiqdə etdikləriniz telefonunuzda qalır. Tətbiqdə reklam və hesab yoxdur, heç bir məlumat toplanmır: nə istifadə statistikası, nə də xəta hesabatları. İnternetdən yalnız üç halda istifadə olunur: dinləmək istədiyiniz tilavətləri yükləmək üçün (bölmə 3), namaz vaxtları üçün məkanınızı istifadə etdikdə şəhərinizin adını telefonun öz xəritə xidmətindən soruşmaq üçün (bölmə 4) və App Store və ya Google Play vasitəsilə istəyə bağlı hədiyyə üçün (bölmə 6).
## 2. Cihazınızda saxlanılan məlumat
Tətbiq telefonunuzun yerli yaddaşında bunları saxlayır:
- ayarlarınız: tətbiqin dili, tərcümə, təfsir, qari, mətn ölçüləri və rənglər;
- oxumağı harada dayandırdığınız, əlfəcinləriniz, qeydləriniz və rənglə işarələdiyiniz ayələr;
- əzbərləmə irəliləyişiniz, növbəti təkrarların tarixləri, oxu planınız və statistikanız (oxumağa və əzbərləməyə sərf etdiyiniz vaxt, ardıcıl günlər);
- “Namaz” bölməsində daxil etdikləriniz: qeyd etdiyiniz namazlar və oruclar, təsbeh saylarınız və zəkat kalkulyatoruna yazdığınız rəqəmlər;
- namaz vaxtları üçün yeriniz, əgər məkanınızı istifadə etsəniz (bölmə 4);
- dinlədiyiniz və ya yüklədiyiniz tilavətlər və öz səs yazılarınız (bölmə 5).
Bu məlumat cihazınızda qalır; biz onu görə bilmirik. Ayarlarda irəliləyişinizi “Əzbər irəliləyişini sıfırla”, saxlanmış tilavətləri “Saxlanmış səsləri sil”, səs yazılarınızı isə “Yazıları sil” ilə silə bilərsiniz. Tətbiqin məlumatlarını təmizlədikdə və ya tətbiqi sildikdə hər şey silinir. “Ehtiyat faylını saxla” irəliləyişinizi, əlfəcinlərinizi, planınızı və ayarlarınızı bir fayla yazır, ayəni paylaşdıqda isə şəkil hazırlanır; sonra telefonunuzun paylaşma pəncərəsi açılır və faylın və ya şəklin hara gedəcəyini özünüz seçirsiniz. Tətbiqin özü onları heç yerə göndərmir. Telefonunuzda ehtiyat nüsxə yandırılıbsa, Android və ya iOS tətbiqin saxladığı məlumatı sizin öz Google və ya iCloud ehtiyat nüsxənizə daxil edə bilər; biz o nüsxəni görə və ona daxil ola bilmirik.
## 3. Tilavətlər (internet)
Tilavəti dinlədikdə və ya yüklədikdə tətbiq səsi AlQuran Cloud-dan (Islamic Network, cdn.islamic.network) yükləyir. Sorğuda yalnız hansı ayə və hansı qari olduğu göstərilir. Onda şəxsi məlumat olmur. Hər internet bağlantısında olduğu kimi, həmin server cihazınızın IP ünvanını alır və onu öz qaydalarına uyğun emal edir (alquran.cloud). Tilavət bir dəfə yüklənir, telefonunuzda saxlanılır və sonra oradan səsləndirilir.
Qalan hər şey (mətn, tərcümələr, təfsir, hədislər və namaz vaxtlarının hesablanması) internetsiz işləyir. Tətbiqdən bir keçid açsanız (məsələn, bu siyasəti və ya mənbənin saytını), telefonunuzun brauzeri və ya e-poçt tətbiqi açılır; onların öz məxfilik qaydaları var.
## 4. Məkan (namaz vaxtları və Qiblə)
Namaz vaxtları və Qiblə istiqaməti telefonunuzda hesablanır. “Məkanımı istifadə et” düyməsinə toxunsanız, tətbiq icazənizi soruşur və təxmini məkanınızı bir dəfə oxuyur. O, yalnız telefonunuzda saxlanılır və bizə heç vaxt göndərilmir. Şəhərinizin adını göstərmək üçün tətbiq telefonun öz xəritə xidmətinə (iPhone-da Apple, Android-də Google) bir dəfə sorğu göndərir; həmin xidmət mövqeyi alır və onu öz məxfilik siyasətinə uyğun emal edir. Qiblə kompası telefonunuzun kompas sensorundan istifadə edir.
## 5. Mikrofon, bildirişlər və vidcetlər
Mikrofondan yalnız öz tilavətinizi yazmaq üçün “Yaz” düyməsinə toxunduqda istifadə olunur. Səs yazıları telefonunuzda, tətbiqin öz qovluğunda saxlanılır; onlar heç yerə yüklənmir və ehtiyat faylına daxil edilmir. Gündəlik xatırlatmanı və namaz bildirişlərini tətbiq telefonunuzda özü planlaşdırır; onları heç bir server göndərmir. Əsas ekran vidcetləri (günün ayəsi, namaz vaxtları) tətbiqin telefonunuzda saxladıqlarını göstərir.
## 6. Hədiyyələr (App Store və Google Play)
Tətbiq pulsuzdur və onda heç nə almaq lazım deyil. İstəsəniz, dəstək səhifəsində tətbiqi hazırlayanlara birdəfəlik hədiyyə edə bilərsiniz. Android-də o, Google Play ödəniş sistemi, iPhone-da isə Apple-ın App Store-u vasitəsilə edilir. Ödənişi Google və ya Apple öz şərtlərinə və məxfilik siyasətinə uyğun emal edir. Kart və ya ödəniş məlumatlarınızı biz heç vaxt almırıq: Google bizə hər sifarişin qeydini verir (məsələn, sifarişin nömrəsi, tarix, məhsul, qiymət və ölkə), Apple isə yalnız satış hesabatlarını. Hədiyyə tətbiqdə heç nəyi açmır.
## 7. Üçüncü tərəf xidmətləri
Tilavətlərin səsini AlQuran Cloud təqdim edir (bölmə 3). Şəhərinizin adını telefonunuzun xəritə xidməti (Apple və ya Google) verir (bölmə 4). Hədiyyələri App Store və Google Play həyata keçirir (bölmə 6). Tətbiq heç bir reklam, statistika və ya xəta hesabatı xidmətindən istifadə etmir; heç bir məlumatı satmırıq və paylaşmırıq.
## 8. Uşaqlar
Tətbiq heç kimdən, o cümlədən uşaqlardan şəxsi məlumat toplamır.
## 9. Hüquqlarınız
Sizin haqqınızda heç bir məlumat saxlamırıq: tətbiqin saxladıqları yalnız telefonunuzdadır və sizin nəzarətinizdədir. Sualınız olsa, bizə yazın.
## 10. Dəyişikliklər
Tətbiq dəyişdikdə bu siyasəti yeniləyə bilərik. Yuxarıdakı tarix son versiyanı göstərir.
## 11. Əlaqə
Vatani Tech (Fardin Vatani), Bakı, Azərbaycan. E-poçt: {MAIL}''',
    'ru': r'''# Политика конфиденциальности Quran Guardians
@ Дата вступления в силу: 28 ноября 2026 г.
@ Разработчик: Vatani Tech (Fardin Vatani), Баку, Азербайджан
## 1. Кратко
Quran Guardians (по-русски «Хранители Корана»; прежнее название — Hafiz) — бесплатное приложение для чтения и заучивания Корана, с чтениями, кратким тафсиром, хадисами и временем намаза, для Android и iPhone. Всё, что вы делаете в приложении, остаётся на вашем телефоне. В приложении нет рекламы и аккаунта, оно не собирает данные: нет ни статистики использования, ни отчётов о сбоях. Интернет используется только в трёх случаях: чтобы скачать чтения, когда вы решаете их слушать (раздел 3); чтобы узнать название вашего города у картографической службы самого телефона, если вы используете местоположение для времени намаза (раздел 4); и для необязательного подарка через App Store или Google Play (раздел 6).
## 2. Данные, которые хранятся на вашем устройстве
Приложение сохраняет в локальной памяти телефона:
- ваши настройки: язык приложения, перевод, тафсир, чтеца, размеры текста и цвета;
- место, где вы остановились при чтении, ваши закладки, заметки и выделенные цветом аяты;
- ваш прогресс заучивания, даты следующих повторений, план чтения и статистику (время чтения и заучивания, дни подряд);
- то, что вы вводите на вкладке «Намаз»: отмеченные намазы и посты, счёт тасбиха и цифры, введённые в калькулятор закята;
- ваше место для расчёта времени намаза, если вы используете местоположение (раздел 4);
- чтения, которые вы прослушали или скачали, и ваши собственные записи (раздел 5).
Эти данные остаются на вашем устройстве; мы их не видим. В настройках прогресс можно удалить кнопкой «Сбросить прогресс заучивания», сохранённые чтения — кнопкой «Удалить сохранённое аудио», а ваши записи — кнопкой «Удалить записи». Всё удаляется, когда вы очищаете данные приложения или удаляете приложение. Кнопка «Сохранить файл копии» записывает ваш прогресс, закладки, план и настройки в файл, а когда вы делитесь аятом, создаётся картинка; затем открывается системное меню «Поделиться», и вы сами выбираете, куда отправить файл или картинку. Само приложение никуда их не отправляет. Если на телефоне включено резервное копирование, Android или iOS могут включить сохранённые данные приложения в вашу собственную резервную копию Google или iCloud; у нас нет доступа к этой копии.
## 3. Чтения (интернет)
Когда вы слушаете или скачиваете чтение, приложение загружает аудио с AlQuran Cloud (Islamic Network, cdn.islamic.network). В запросе указано только, какой аят и какой чтец. В нём нет персональных данных. Как и при любом интернет-соединении, этот сервер получает IP-адрес вашего устройства и обрабатывает его по собственным правилам (alquran.cloud). Чтение скачивается один раз, сохраняется на телефоне и затем воспроизводится оттуда.
Всё остальное (текст, переводы, тафсир, хадисы и расчёт времени намаза) работает без интернета. Если вы открываете из приложения ссылку, например эту политику или сайт источника, открывается браузер или почтовое приложение телефона; у них свои правила конфиденциальности.
## 4. Местоположение (время намаза и кибла)
Время намаза и направление киблы рассчитываются на вашем телефоне. Если вы нажимаете «Моё местоположение», приложение спрашивает разрешение и один раз определяет ваше примерное местоположение. Оно хранится только на телефоне и никогда не отправляется нам. Чтобы показать название города, приложение один раз обращается к картографической службе самого телефона (Apple на iPhone, Google на Android); эта служба получает координаты и обрабатывает их по своей политике конфиденциальности. Компас киблы использует датчик компаса телефона.
## 5. Микрофон, уведомления и виджеты
Микрофон используется, только когда вы нажимаете «Записать», чтобы записать собственное чтение. Записи хранятся в папке приложения на телефоне; они никуда не загружаются и не входят в файл копии. Ежедневное напоминание и уведомления о намазе приложение планирует само на вашем телефоне; их не отправляет никакой сервер. Виджеты на главном экране (аят дня, время намаза) показывают то, что приложение сохранило на телефоне.
## 6. Подарки (App Store и Google Play)
Приложение бесплатное, и в нём ничего не нужно покупать. При желании на странице поддержки можно сделать разовый подарок создателям приложения. На Android он совершается через платёжную систему Google Play, на iPhone — через App Store компании Apple. Платёж обрабатывает Google или Apple на своих условиях и по своей политике конфиденциальности. Мы никогда не получаем данные вашей карты или платежа: Google передаёт нам запись о каждом заказе (например, номер заказа, дату, товар, цену и страну), а Apple — только отчёты о продажах. Подарок ничего не открывает в приложении.
## 7. Сторонние сервисы
Аудио чтений предоставляет AlQuran Cloud (раздел 3). Название города сообщает картографическая служба телефона, Apple или Google (раздел 4). Подарки проводят App Store и Google Play (раздел 6). Приложение не использует сервисы рекламы, статистики или отчётов о сбоях; мы не продаём и не передаём никакие данные.
## 8. Дети
Приложение не собирает персональные данные ни у кого, включая детей.
## 9. Ваши права
Мы не храним никаких данных о вас: всё, что сохраняет приложение, находится только на вашем телефоне и под вашим контролем. Если у вас есть вопрос, напишите нам.
## 10. Изменения
Мы можем обновлять эту политику, когда меняется приложение. Дата вверху показывает последнюю версию.
## 11. Контакты
Vatani Tech (Fardin Vatani), Баку, Азербайджан. Электронная почта: {MAIL}''',
  },
  'terms': {
    'en': r'''# Quran Guardians – Terms of use
By using Quran Guardians you agree to these terms. They are short and written in plain language.
## 1. The text, the translations and the other sources
The Arabic text is the Uthmani text of the Tanzil Project (tanzil.net), unchanged. The translations of the meaning and the short tafsir (Al-Mukhtasar, by the Tafsir Center for Quranic Studies) come from QuranEnc.com, unchanged. The hadiths and their explanations come from HadeethEnc.com. The recitations come from AlQuran Cloud. The tajweed colours are based on the quran-tajweed data (Creative Commons Attribution 4.0). They belong to their owners and are used under their terms; the full list of sources is in the app's Settings. A translation gives the meaning of the Quran in another language; it is not the Quran itself. We handle these texts with care; if you notice a mistake, please write to us.
## 2. A help for learning and worship
The memorising tools and the review schedule help you learn and revise. They do not replace a teacher. Prayer times, the direction of the Qibla and the Islamic calendar are calculated on your phone and may differ a little from those of your mosque or of the authority in your country: when in doubt, follow them. The zakat calculator gives an estimate only; ask a scholar about your own case.
## 3. Free, with no ads
The app is free and has no ads. Every feature is free and nothing has to be bought. If you wish, you can support the app with a one-time gift, handled by the App Store or Google Play under their terms. A gift unlocks nothing; it is a gift to the makers of the app, not zakat or charity.
## 4. No warranty
The app is provided “as is”, without any warranty. To the extent the law allows, the developer is not liable for any loss or damage resulting from its use.
## 5. Changes and contact
These terms may change with new versions of the app. Questions: write to {MAIL}. Privacy: see the privacy policy.
@ Last updated: 28 November 2026''',
    'az': r'''# Quran Guardians – İstifadə şərtləri
Quran Guardians tətbiqindən istifadə etməklə bu şərtlərlə razılaşırsınız. Onlar qısadır və sadə dillə yazılıb.
## 1. Mətn, tərcümələr və digər mənbələr
Ərəbcə mətn Tanzil layihəsinin (tanzil.net) Osmani mətnidir, dəyişdirilməyib. Mənaların tərcümələri və qısa təfsir (Al-Mukhtasar, Tafsir Center for Quranic Studies) QuranEnc.com saytından götürülüb, dəyişdirilməyib. Hədislər və onların izahları HadeethEnc.com saytından götürülüb. Tilavətlər AlQuran Cloud-dan gəlir. Təcvid rəngləri quran-tajweed məlumatlarına əsaslanır (Creative Commons Attribution 4.0). Onlar öz sahiblərinə məxsusdur və onların şərtlərinə uyğun istifadə olunur; mənbələrin tam siyahısı tətbiqin Ayarlar bölməsindədir. Tərcümə Quranın mənasını başqa dildə çatdırır; o, Quranın özü deyil. Bu mətnlərə diqqətlə yanaşırıq; səhv görsəniz, xahiş edirik, bizə yazın.
## 2. Öyrənməyə və ibadətə kömək
Əzbərləmə alətləri və təkrar cədvəli öyrənməyə və təkrarlamağa kömək edir. Onlar müəllimi əvəz etmir. Namaz vaxtları, Qiblə istiqaməti və İslam təqvimi telefonunuzda hesablanır və məscidinizin və ya ölkənizdəki rəsmi qurumun göstəricilərindən bir qədər fərqlənə bilər: şübhə olduqda onlara əsaslanın. Zəkat kalkulyatoru yalnız təxmini hesab verir; öz vəziyyətiniz barədə alimdən soruşun.
## 3. Pulsuz və reklamsız
Tətbiq pulsuzdur və onda reklam yoxdur. Bütün imkanlar pulsuzdur, heç nə almaq lazım deyil. İstəsəniz, tətbiqə birdəfəlik hədiyyə ilə dəstək ola bilərsiniz; onu App Store və ya Google Play öz şərtlərinə əsasən həyata keçirir. Hədiyyə heç nəyi açmır; bu, tətbiqi hazırlayanlara hədiyyədir, zəkat və ya sədəqə deyil.
## 4. Zəmanət yoxdur
Tətbiq heç bir zəmanət olmadan “olduğu kimi” təqdim olunur. Qanunun icazə verdiyi həddə tərtibatçı onun istifadəsindən yaranan heç bir itki və ya ziyana görə məsuliyyət daşımır.
## 5. Dəyişikliklər və əlaqə
Bu şərtlər tətbiqin yeni versiyaları ilə dəyişə bilər. Suallar üçün {MAIL} ünvanına yazın. Məxfilik: “Məxfilik siyasəti”nə baxın.
@ Son yenilənmə: 28 noyabr 2026''',
    'ru': r'''# Quran Guardians – Условия использования
Используя Quran Guardians, вы соглашаетесь с этими условиями. Они короткие и написаны простым языком.
## 1. Текст, переводы и другие источники
Арабский текст — османский текст проекта Tanzil (tanzil.net), без изменений. Переводы смыслов и краткий тафсир (Al-Mukhtasar, Tafsir Center for Quranic Studies) взяты с сайта QuranEnc.com, без изменений. Хадисы и их разъяснения взяты с сайта HadeethEnc.com. Чтения предоставляет AlQuran Cloud. Цвета таджвида основаны на данных quran-tajweed (Creative Commons Attribution 4.0). Они принадлежат своим владельцам и используются на их условиях; полный список источников есть в настройках приложения. Перевод передаёт смысл Корана на другом языке; это не сам Коран. Мы бережно относимся к этим текстам; если вы заметите ошибку, пожалуйста, напишите нам.
## 2. Помощь в обучении и поклонении
Инструменты заучивания и расписание повторений помогают учить и повторять. Они не заменяют учителя. Время намаза, направление киблы и исламский календарь рассчитываются на вашем телефоне и могут немного отличаться от данных вашей мечети или официального органа вашей страны: в случае сомнений следуйте им. Калькулятор закята даёт только приблизительный расчёт; о своём случае спросите учёного.
## 3. Бесплатно и без рекламы
Приложение бесплатное, и в нём нет рекламы. Все возможности бесплатны, ничего покупать не нужно. При желании вы можете поддержать приложение разовым подарком; его проводит App Store или Google Play на своих условиях. Подарок ничего не открывает; это подарок создателям приложения, а не закят и не милостыня.
## 4. Без гарантий
Приложение предоставляется «как есть», без каких-либо гарантий. В пределах, допускаемых законом, разработчик не несёт ответственности за любые убытки или ущерб от его использования.
## 5. Изменения и связь
Эти условия могут меняться с новыми версиями приложения. Вопросы: пишите на {MAIL}. Конфиденциальность: см. «Политику конфиденциальности».
@ Последнее обновление: 28 ноября 2026 г.''',
  },
},
}
