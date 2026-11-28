# The page "Delete your PetroGram account" (22 November 2026), in the seven
# languages of the app: /petrogram/delete-account/. Google Play asks for a
# public page where a person can ask to delete their account: it names the
# app and the developer, shows the steps and says what is deleted and kept.
#
# build.py runs this file after site_texts.py and privacy_texts.py. It gives:
#   - three rows of TX (the page's label, title and description; English,
#     Azerbaijani, Russian, like the rows of site_texts.py);
#   - DEL: the text of the page, one block per language;
#   - delete_secs(): the page's sections as HTML, for doc() in build.py.
#
# Names of buttons and pages are the app's own (lib/strings_*.dart, lib/zh/).
# Periods (30 days, 90 days) must stay the same as in the privacy policy and
# in what the owner really does. {MAIL} becomes the email link with the
# subject filled in, {PRIVACY} the address of the privacy policy.

DEL_SUBJECT = 'Delete my PetroGram account'     # the same in every language
DEL_MAIL = (f'<a href="mailto:support@vatanitech.com?subject={quote(DEL_SUBJECT)}">'
            'support@vatanitech.com</a>')
DEL_ASK = '<a href="mailto:support@vatanitech.com">support@vatanitech.com</a>'

TX.update({
'delete-account': ('Delete your account', 'Hesabın silinməsi', 'Удаление аккаунта'),
'delete_title': ('Delete your PetroGram account · Vatani Tech',
                 'PetroGram hesabının silinməsi · Vatani Tech',
                 'Удаление аккаунта PetroGram · Vatani Tech'),
'delete_desc': ('How to delete your account in the PetroGram app by Vatani Tech, and which data is deleted or kept. In seven languages.',
                'Vatani Tech-in PetroGram tətbiqində hesabı necə silmək olar, hansı məlumat silinir və hansı qalır.',
                'Как удалить аккаунт в приложении PetroGram от Vatani Tech, какие данные удаляются и какие остаются.'),
})
for _k in ('delete-account', 'delete_title', 'delete_desc'):
    assert len(TX[_k]) == len(LANGS) and all(TX[_k]), ('a text is missing in delete_texts.py', _k)

DEL = {
'en': dict(
  h1='Delete your PetroGram account',
  meta='App: PetroGram · Developer: Vatani Tech<br>\n  Last updated: 28 November 2026',
  intro='An account in the PetroGram app is optional. If you created one, you can delete it at any time: in the app, or by email if you no longer have the app. A deleted account cannot be brought back.',
  h_app='Way 1: in the app',
  app_steps=[
    'Open PetroGram and go to <strong>Settings → Account and check mark</strong>.',
    'Tap <strong>Delete my account</strong> and confirm.',
  ],
  app_note='The account and the data listed below are deleted at once. For safety, the app may first ask you to sign out and sign in again, or to confirm with Apple if you signed in with Apple.',
  h_mail='Way 2: by email, without the app',
  mail_steps=[
    'Write to {MAIL} from the email address of your account.',
    'Use the subject "Delete my PetroGram account".',
  ],
  mail_note='We delete the account within 30 days and send you a confirmation by email.',
  h_del='What is deleted',
  del_items=[
    '<strong>Your sign-in account:</strong> your email address and password. If you signed in with Google or Apple, also the link with Google or Apple, and the name and profile picture link that Google gives us at sign-in.',
    '<strong>Your lines on the online scoreboard:</strong> the name you chose and your results.',
    '<strong>The synced copy of your app data in the cloud:</strong> your notes, favourites, flashcard progress, interview marks, quiz results, mistakes to review, badges, your other learning progress and some app settings.',
  ],
  # Shown only for the apps that have the certificate (delete_secs).
  del_cert='<strong>Your public certificate page,</strong> if you put a certificate of completion online: the name on it, your result, the date and its number. A link to it, for example on LinkedIn, stops working; remove the entry from your LinkedIn profile yourself.',
  h_keep='What is not deleted',
  keep_items=[
    '<strong>Data on your phone.</strong> Your notes, progress and settings stay in the app on your phone until you remove the app or clear its data. If your phone\'s own backup is turned on, it may hold a copy too; we cannot see it.',
    '<strong>The "Remove ads" purchase.</strong> It belongs to your Google Play or App Store account, not to your PetroGram account. Deleting the account does not change it.',
    '<strong>Crash reports and anonymous usage statistics.</strong> They are not tied to your account and contain no name or email. Crash reports are kept for 90 days. You can turn both off in Settings → Privacy.',
    '<strong>Reports of a name.</strong> A report of a scoreboard name, sent by you or about your name, stays. It holds only random user numbers, no name and no email.',
    '<strong>Emails you sent us.</strong> They are not part of the account. If you want them deleted too, say so in your email.',
  ],
  h_part='Delete only your scoreboard data and keep the account',
  part='In the app, open the <strong>Scoreboard</strong>, open its menu and choose <strong>Leave the scoreboard</strong>. Your name and results are deleted from the scoreboard at once. Your account and your synced copy stay.',
  h_more='More information',
  more='The <a href="{PRIVACY}">PetroGram privacy policy</a> explains all the data the app uses. Questions: {ASK}.',
),
'az': dict(
  h1='PetroGram hesabınızın silinməsi',
  meta='Tətbiq: PetroGram · Tərtibatçı: Vatani Tech<br>\n  Son yenilənmə: 28 noyabr 2026',
  intro='PetroGram tətbiqində hesab könüllüdür. Hesab yaratmısınızsa, onu istənilən vaxt silə bilərsiniz: tətbiqdə və ya tətbiq artıq sizdə yoxdursa, e-poçtla. Silinmiş hesabı geri qaytarmaq olmur.',
  h_app='1-ci yol: tətbiqdə',
  app_steps=[
    'PetroGram-ı açın və <strong>Ayarlar → Hesab və təsdiq nişanı</strong> bölməsinə keçin.',
    '<strong>Hesabımı sil</strong> düyməsinə toxunun və təsdiqləyin.',
  ],
  app_note='Hesab və aşağıda sadalanan məlumat dərhal silinir. Təhlükəsizlik üçün tətbiq əvvəlcə çıxıb yenidən daxil olmağınızı, Apple ilə daxil olmusunuzsa, Apple ilə təsdiqləməyinizi xahiş edə bilər.',
  h_mail='2-ci yol: e-poçtla, tətbiq olmadan',
  mail_steps=[
    'Hesabınızın e-poçt ünvanından {MAIL} ünvanına yazın.',
    'Məktubun mövzusuna «Delete my PetroGram account» yazın.',
  ],
  mail_note='Hesabı 30 gün ərzində silirik və sizə e-poçtla təsdiq göndəririk.',
  h_del='Nə silinir',
  del_items=[
    '<strong>Daxil olma hesabınız:</strong> e-poçt ünvanınız və parolunuz. Google və ya Apple ilə daxil olmusunuzsa, Google və ya Apple ilə əlaqə, həmçinin Google-un daxil olarkən bizə verdiyi ad və profil şəklinin keçidi də silinir.',
    '<strong>Onlayn reytinq cədvəlindəki sətirləriniz:</strong> seçdiyiniz ad və nəticələriniz.',
    '<strong>Tətbiq məlumatınızın buluddakı sinxron nüsxəsi:</strong> qeydləriniz, seçilmişlər, kartoçka irəliləyişiniz, müsahibə qeydləri, test nəticələri, təkrar ediləcək səhvlər, nişanlar, digər öyrənmə irəliləyişiniz və bəzi tətbiq ayarları.',
  ],
  # Shown only for the apps that have the certificate (delete_secs).
  del_cert='<strong>Açıq sertifikat səhifəniz,</strong> əgər bitirmə sertifikatını onlayn yerləşdirmisinizsə: oradakı ad, nəticəniz, tarix və nömrə. Ona aparan keçid, məsələn LinkedIn-də, işləməyəcək; LinkedIn profilinizdəki qeydi özünüz silin.',
  h_keep='Nə silinmir',
  keep_items=[
    '<strong>Telefonunuzdakı məlumat.</strong> Qeydləriniz, irəliləyişiniz və ayarlarınız tətbiqi silənə və ya onun məlumatını təmizləyənə qədər telefonunuzdakı tətbiqdə qalır. Telefonun öz ehtiyat nüsxəsi aktivdirsə, orada da nüsxə ola bilər; biz onu görə bilmirik.',
    '<strong>«Reklamı sil» alışı.</strong> O, PetroGram hesabınıza yox, Google Play və ya App Store hesabınıza aiddir. Hesabın silinməsi onu dəyişmir.',
    '<strong>Xəta hesabatları və anonim istifadə statistikası.</strong> Onlar hesabınızla əlaqələndirilmir və onlarda ad və ya e-poçt olmur. Xəta hesabatları 90 gün saxlanılır. Hər ikisini Ayarlar → Məxfilik bölməsində söndürə bilərsiniz.',
    '<strong>Ad barədə şikayətlər.</strong> Reytinqdəki ad barədə sizin göndərdiyiniz və ya sizin adınız barədə göndərilən şikayət qalır. Onda yalnız təsadüfi istifadəçi nömrələri olur, ad və ya e-poçt olmur.',
    '<strong>Bizə göndərdiyiniz məktublar.</strong> Onlar hesabın bir hissəsi deyil. Onların da silinməsini istəyirsinizsə, bunu məktubunuzda yazın.',
  ],
  h_part='Yalnız reytinq məlumatını silmək və hesabı saxlamaq',
  part='Tətbiqdə <strong>Reytinq cədvəli</strong> səhifəsini açın, onun menyusunu açın və <strong>Reytinqdən çıx</strong> seçin. Adınız və nəticələriniz reytinqdən dərhal silinir. Hesabınız və sinxron nüsxəniz qalır.',
  h_more='Ətraflı məlumat',
  more='<a href="{PRIVACY}">PetroGram məxfilik siyasəti</a> tətbiqin istifadə etdiyi bütün məlumatı izah edir. Suallar üçün: {ASK}.',
),
'ru': dict(
  h1='Удаление аккаунта PetroGram',
  meta='Приложение: PetroGram · Разработчик: Vatani Tech<br>\n  Обновлено: 28 ноября 2026 г.',
  intro='Аккаунт в приложении PetroGram не обязателен. Если вы его создали, его можно удалить в любой момент: в приложении или по почте, если приложения у вас уже нет. Удалённый аккаунт нельзя восстановить.',
  h_app='Способ 1: в приложении',
  app_steps=[
    'Откройте PetroGram и перейдите в <strong>Настройки → Аккаунт и галочка</strong>.',
    'Нажмите <strong>Удалить аккаунт</strong> и подтвердите.',
  ],
  app_note='Аккаунт и перечисленные ниже данные удаляются сразу. Для безопасности приложение может сначала попросить выйти и войти снова, а если вы входили через Apple, подтвердить удаление через Apple.',
  h_mail='Способ 2: по почте, без приложения',
  mail_steps=[
    'Напишите на {MAIL} с адреса электронной почты вашего аккаунта.',
    'Укажите тему письма «Delete my PetroGram account».',
  ],
  mail_note='Мы удалим аккаунт в течение 30 дней и пришлём подтверждение по почте.',
  h_del='Что удаляется',
  del_items=[
    '<strong>Аккаунт для входа:</strong> ваш адрес электронной почты и пароль. Если вы входили через Google или Apple, удаляется и связь с Google или Apple, а также имя и ссылка на фото профиля, которые Google передаёт нам при входе.',
    '<strong>Ваши строки в онлайн-таблице лидеров:</strong> выбранное вами имя и ваши результаты.',
    '<strong>Синхронизированная копия данных приложения в облаке:</strong> заметки, избранное, прогресс по карточкам, отметки к собеседованию, результаты тестов, ошибки для повторения, значки, остальной учебный прогресс и некоторые настройки приложения.',
  ],
  # Shown only for the apps that have the certificate (delete_secs).
  del_cert='<strong>Ваша публичная страница сертификата,</strong> если вы разместили сертификат о прохождении онлайн: имя на нём, результат, дата и номер. Ссылка на неё, например в LinkedIn, перестанет работать; запись в профиле LinkedIn удалите сами.',
  h_keep='Что не удаляется',
  keep_items=[
    '<strong>Данные на телефоне.</strong> Заметки, прогресс и настройки остаются в приложении на телефоне, пока вы не удалите приложение или не очистите его данные. Если включено резервное копирование телефона, копия может быть и там; мы её не видим.',
    '<strong>Покупка «Убрать рекламу».</strong> Она относится к вашему аккаунту Google Play или App Store, а не к аккаунту PetroGram. Удаление аккаунта её не затрагивает.',
    '<strong>Отчёты о сбоях и анонимная статистика использования.</strong> Они не связаны с вашим аккаунтом, в них нет имени и почты. Отчёты о сбоях хранятся 90 дней. И то и другое можно отключить в разделе Настройки → Конфиденциальность.',
    '<strong>Жалобы на имя.</strong> Жалоба на имя в таблице лидеров, отправленная вами или на ваше имя, остаётся. В ней только случайные номера пользователей, без имени и почты.',
    '<strong>Письма, которые вы нам отправили.</strong> Они не входят в аккаунт. Если хотите, чтобы мы удалили и их, напишите об этом в письме.',
  ],
  h_part='Удалить только данные рейтинга и сохранить аккаунт',
  part='В приложении откройте страницу <strong>Таблица лидеров</strong>, затем её меню и выберите <strong>Выйти из рейтинга</strong>. Ваше имя и результаты сразу удаляются из рейтинга. Аккаунт и синхронизированная копия остаются.',
  h_more='Подробнее',
  more='<a href="{PRIVACY}">Политика конфиденциальности PetroGram</a> описывает все данные, которые использует приложение. Вопросы: {ASK}.',
),
'ar': dict(
  h1='حذف حسابك في PetroGram',
  meta='التطبيق: PetroGram · المطوّر: Vatani Tech<br>\n  آخر تحديث: 28 نوفمبر 2026',
  intro='الحساب في تطبيق PetroGram اختياري. إذا أنشأت حسابًا، يمكنك حذفه في أي وقت: من داخل التطبيق، أو بالبريد الإلكتروني إذا لم يعد التطبيق لديك. لا يمكن استرجاع الحساب بعد حذفه.',
  h_app='الطريقة 1: من داخل التطبيق',
  app_steps=[
    'افتح PetroGram وانتقل إلى <strong>الإعدادات ← الحساب وعلامة التوثيق</strong>.',
    'اضغط <strong>احذف حسابي</strong> ثم أكّد.',
  ],
  app_note='يُحذف الحساب والبيانات المذكورة أدناه فورًا. وللأمان قد يطلب منك التطبيق أولًا تسجيل الخروج ثم الدخول مجددًا، أو التأكيد عبر Apple إذا سجّلت الدخول باستخدام Apple.',
  h_mail='الطريقة 2: بالبريد الإلكتروني، بدون التطبيق',
  mail_steps=[
    'اكتب إلى {MAIL} من عنوان البريد الإلكتروني الخاص بحسابك.',
    'اكتب في موضوع الرسالة: «Delete my PetroGram account».',
  ],
  mail_note='نحذف الحساب خلال 30 يومًا ونرسل إليك تأكيدًا بالبريد الإلكتروني.',
  h_del='ما الذي يُحذف',
  del_items=[
    '<strong>حساب تسجيل الدخول:</strong> عنوان بريدك الإلكتروني وكلمة مرورك. وإذا سجّلت الدخول باستخدام Google أو Apple، يُحذف أيضًا الربط مع Google أو Apple، وكذلك الاسم ورابط صورة الملف الشخصي اللذان تعطيهما لنا Google عند تسجيل الدخول.',
    '<strong>أسطرك في لوحة المتصدرين على الإنترنت:</strong> الاسم الذي اخترته ونتائجك.',
    '<strong>النسخة المتزامنة من بيانات التطبيق في السحابة:</strong> ملاحظاتك والمفضلة وتقدّمك في البطاقات التعليمية وعلامات المقابلات ونتائج الاختبارات والأخطاء المطلوب مراجعتها والشارات وبقية تقدّمك في التعلّم وبعض إعدادات التطبيق.',
  ],
  # Shown only for the apps that have the certificate (delete_secs).
  del_cert='<strong>صفحة شهادتك العامة،</strong> إذا وضعت شهادة الإتمام على الإنترنت: الاسم المكتوب عليها ونتيجتك والتاريخ ورقمها. يتوقف الرابط إليها، مثلًا على LinkedIn، عن العمل؛ احذف الإدخال من ملفك على LinkedIn بنفسك.',
  h_keep='ما الذي لا يُحذف',
  keep_items=[
    '<strong>البيانات الموجودة على هاتفك.</strong> تبقى ملاحظاتك وتقدّمك وإعداداتك في التطبيق على هاتفك إلى أن تحذف التطبيق أو تمسح بياناته. وإذا كان النسخ الاحتياطي الخاص بهاتفك مفعّلًا، فقد توجد نسخة فيه أيضًا، ولا يمكننا رؤيتها.',
    '<strong>شراء «إزالة الإعلانات».</strong> يتبع حسابك في Google Play أو App Store، وليس حسابك في PetroGram. حذف الحساب لا يغيّره.',
    '<strong>تقارير الأعطال وإحصاءات الاستخدام المجهولة.</strong> ليست مرتبطة بحسابك ولا تحتوي على اسم أو بريد إلكتروني. تُحفظ تقارير الأعطال مدة 90 يومًا. يمكنك إيقافهما من الإعدادات ← الخصوصية.',
    '<strong>البلاغات عن الأسماء.</strong> يبقى أي بلاغ عن اسم في لوحة المتصدرين، سواء أرسلته أنت أو أُرسل عن اسمك. لا يحتوي إلا على أرقام مستخدمين عشوائية، بلا اسم ولا بريد إلكتروني.',
    '<strong>الرسائل التي أرسلتها إلينا.</strong> ليست جزءًا من الحساب. إذا أردت حذفها أيضًا، فاذكر ذلك في رسالتك.',
  ],
  h_part='حذف بيانات لوحة المتصدرين فقط مع إبقاء الحساب',
  part='في التطبيق، افتح <strong>لوحة المتصدرين</strong>، ثم افتح قائمتها واختر <strong>مغادرة لوحة المتصدرين</strong>. يُحذف اسمك ونتائجك من اللوحة فورًا. ويبقى حسابك ونسختك المتزامنة.',
  h_more='لمزيد من المعلومات',
  more='توضّح <a href="{PRIVACY}">سياسة خصوصية PetroGram</a> كل البيانات التي يستخدمها التطبيق. للأسئلة: {ASK}.',
),
'es': dict(
  h1='Eliminar tu cuenta de PetroGram',
  meta='Aplicación: PetroGram · Desarrollador: Vatani Tech<br>\n  Última actualización: 28 de noviembre de 2026',
  intro='La cuenta en la app PetroGram es opcional. Si creaste una, puedes eliminarla en cualquier momento: en la app, o por correo si ya no tienes la app. Una cuenta eliminada no se puede recuperar.',
  h_app='Opción 1: en la app',
  app_steps=[
    'Abre PetroGram y ve a <strong>Ajustes → Cuenta e insignia</strong>.',
    'Pulsa <strong>Eliminar mi cuenta</strong> y confirma.',
  ],
  app_note='La cuenta y los datos indicados más abajo se eliminan al instante. Por seguridad, la app puede pedirte antes que cierres sesión y vuelvas a entrar, o que confirmes con Apple si entraste con Apple.',
  h_mail='Opción 2: por correo, sin la app',
  mail_steps=[
    'Escribe a {MAIL} desde la dirección de correo de tu cuenta.',
    'Pon como asunto «Delete my PetroGram account».',
  ],
  mail_note='Eliminamos la cuenta en un plazo de 30 días y te enviamos una confirmación por correo.',
  h_del='Qué se elimina',
  del_items=[
    '<strong>Tu cuenta de inicio de sesión:</strong> tu dirección de correo y tu contraseña. Si entraste con Google o Apple, también el vínculo con Google o Apple, y el nombre y el enlace a la foto de perfil que Google nos da al iniciar sesión.',
    '<strong>Tus líneas en la clasificación en línea:</strong> el nombre que elegiste y tus resultados.',
    '<strong>La copia sincronizada de tus datos de la app en la nube:</strong> tus notas, tus favoritos, tu progreso en las tarjetas, tus marcas de entrevista, tus puntuaciones de tests, los errores por repasar, tus insignias, el resto de tu progreso de aprendizaje y algunos ajustes de la app.',
  ],
  # Shown only for the apps that have the certificate (delete_secs).
  del_cert='<strong>Tu página pública del certificado,</strong> si pusiste un certificado de finalización en línea: el nombre que figura en él, tu resultado, la fecha y su número. El enlace a ella, por ejemplo en LinkedIn, deja de funcionar; quita tú mismo la entrada de tu perfil de LinkedIn.',
  h_keep='Qué no se elimina',
  keep_items=[
    '<strong>Los datos de tu teléfono.</strong> Tus notas, tu progreso y tus ajustes se quedan en la app de tu teléfono hasta que desinstales la app o borres sus datos. Si la copia de seguridad del propio teléfono está activada, puede haber una copia también allí; no podemos verla.',
    '<strong>La compra «Quitar anuncios».</strong> Pertenece a tu cuenta de Google Play o del App Store, no a tu cuenta de PetroGram. Eliminar la cuenta no la cambia.',
    '<strong>Los informes de fallos y las estadísticas de uso anónimas.</strong> No están vinculados a tu cuenta y no contienen nombre ni correo. Los informes de fallos se conservan 90 días. Puedes desactivar ambos en Ajustes → Privacidad.',
    '<strong>Las denuncias de nombres.</strong> Una denuncia de un nombre de la clasificación, enviada por ti o sobre tu nombre, se mantiene. Solo contiene números de usuario aleatorios, sin nombre ni correo.',
    '<strong>Los correos que nos enviaste.</strong> No forman parte de la cuenta. Si quieres que también los borremos, dilo en tu correo.',
  ],
  h_part='Borrar solo tus datos de la clasificación y conservar la cuenta',
  part='En la app, abre la <strong>Clasificación</strong>, abre su menú y elige <strong>Salir de la clasificación</strong>. Tu nombre y tus resultados se borran de la clasificación al instante. Tu cuenta y tu copia sincronizada se mantienen.',
  h_more='Más información',
  more='La <a href="{PRIVACY}">política de privacidad de PetroGram</a> explica todos los datos que usa la app. Preguntas: {ASK}.',
),
'fr': dict(
  h1='Supprimer votre compte PetroGram',
  meta='Application : PetroGram · Développeur : Vatani Tech<br>\n  Dernière mise à jour : 28 novembre 2026',
  intro='Le compte dans l’app PetroGram est facultatif. Si vous en avez créé un, vous pouvez le supprimer à tout moment : dans l’app, ou par e-mail si vous n’avez plus l’app. Un compte supprimé ne peut pas être récupéré.',
  h_app='Méthode 1 : dans l’app',
  app_steps=[
    'Ouvrez PetroGram et allez dans <strong>Paramètres → Compte et badge</strong>.',
    'Appuyez sur <strong>Supprimer mon compte</strong> et confirmez.',
  ],
  app_note='Le compte et les données indiquées plus bas sont supprimés immédiatement. Par sécurité, l’app peut d’abord vous demander de vous déconnecter et de vous reconnecter, ou de confirmer avec Apple si vous vous êtes connecté avec Apple.',
  h_mail='Méthode 2 : par e-mail, sans l’app',
  mail_steps=[
    'Écrivez à {MAIL} depuis l’adresse e-mail de votre compte.',
    'Indiquez comme objet « Delete my PetroGram account ».',
  ],
  mail_note='Nous supprimons le compte dans un délai de 30 jours et vous envoyons une confirmation par e-mail.',
  h_del='Ce qui est supprimé',
  del_items=[
    '<strong>Votre compte de connexion :</strong> votre adresse e-mail et votre mot de passe. Si vous vous êtes connecté avec Google ou Apple, le lien avec Google ou Apple est supprimé aussi, ainsi que le nom et le lien vers la photo de profil que Google nous transmet à la connexion.',
    '<strong>Vos lignes au classement en ligne :</strong> le nom que vous avez choisi et vos résultats.',
    '<strong>La copie synchronisée des données de l’app dans le cloud :</strong> vos notes, vos favoris, votre progression dans les cartes mémoire, vos marques d’entretien, vos scores aux quiz, les erreurs à revoir, vos badges, le reste de votre progression et quelques réglages de l’app.',
  ],
  # Shown only for the apps that have the certificate (delete_secs).
  del_cert='<strong>Votre page publique de certificat,</strong> si vous avez mis un certificat de réussite en ligne : le nom qui y figure, votre résultat, la date et son numéro. Le lien vers cette page, par exemple sur LinkedIn, ne fonctionne plus ; retirez vous-même l’entrée de votre profil LinkedIn.',
  h_keep='Ce qui n’est pas supprimé',
  keep_items=[
    '<strong>Les données sur votre téléphone.</strong> Vos notes, votre progression et vos réglages restent dans l’app sur votre téléphone jusqu’à ce que vous désinstalliez l’app ou effaciez ses données. Si la sauvegarde de votre téléphone est activée, une copie peut s’y trouver aussi ; nous ne pouvons pas la voir.',
    '<strong>L’achat « Supprimer les pubs ».</strong> Il est lié à votre compte Google Play ou App Store, pas à votre compte PetroGram. Supprimer le compte ne le change pas.',
    '<strong>Les rapports de plantage et les statistiques d’utilisation anonymes.</strong> Ils ne sont pas liés à votre compte et ne contiennent ni nom ni e-mail. Les rapports de plantage sont conservés 90 jours. Vous pouvez désactiver les deux dans Paramètres → Confidentialité.',
    '<strong>Les signalements de noms.</strong> Un signalement d’un nom du classement, envoyé par vous ou à propos de votre nom, reste. Il ne contient que des numéros d’utilisateur aléatoires, sans nom ni e-mail.',
    '<strong>Les e-mails que vous nous avez envoyés.</strong> Ils ne font pas partie du compte. Si vous voulez qu’ils soient supprimés aussi, dites-le dans votre e-mail.',
  ],
  h_part='Supprimer seulement vos données du classement et garder le compte',
  part='Dans l’app, ouvrez le <strong>Classement</strong>, ouvrez son menu et choisissez <strong>Quitter le classement</strong>. Votre nom et vos résultats sont supprimés du classement immédiatement. Votre compte et votre copie synchronisée restent.',
  h_more='En savoir plus',
  more='La <a href="{PRIVACY}">politique de confidentialité de PetroGram</a> explique toutes les données utilisées par l’app. Questions : {ASK}.',
),
'zh': dict(
  h1='删除您的 PetroGram 账号',
  meta='应用：PetroGram · 开发者：Vatani Tech<br>\n  最后更新：2026 年 11 月 28 日',
  intro='PetroGram 应用中的账号是可选的。如果您创建了账号，可以随时删除：在应用内删除；如果您已经没有应用，也可以通过电子邮件申请。账号删除后无法恢复。',
  h_app='方法一：在应用内',
  app_steps=[
    '打开 PetroGram，进入<strong>设置 → 账号与认证标记</strong>。',
    '点击<strong>删除我的账号</strong>并确认。',
  ],
  app_note='账号和下面列出的数据会立即删除。为安全起见，应用可能会先要求您退出登录后重新登录；如果您通过 Apple 登录，则会要求您通过 Apple 再次确认。',
  h_mail='方法二：通过电子邮件，无需应用',
  mail_steps=[
    '用您账号的电子邮件地址写信至 {MAIL}。',
    '邮件主题请写“Delete my PetroGram account”。',
  ],
  mail_note='我们会在 30 天内删除账号，并通过电子邮件向您发送确认。',
  h_del='会删除的内容',
  del_items=[
    '<strong>您的登录账号：</strong>您的电子邮件地址和密码。如果您通过 Google 或 Apple 登录，还会删除与 Google 或 Apple 的关联，以及 Google 在登录时提供给我们的姓名和头像链接。',
    '<strong>您在在线排行榜上的记录：</strong>您选择的名字和您的成绩。',
    '<strong>应用数据在云端的同步副本：</strong>您的笔记、收藏、抽认卡进度、面试标记、测验成绩、待复习的错题、徽章、其他学习进度以及部分应用设置。',
  ],
  # Shown only for the apps that have the certificate (delete_secs).
  del_cert='<strong>您的公开证书页面，</strong>如果您曾将结业证书放到网上：上面的姓名、您的成绩、日期和编号。指向它的链接（例如 LinkedIn 上的链接）将失效；请自行从 LinkedIn 个人资料中删除该条目。',
  h_keep='不会删除的内容',
  keep_items=[
    '<strong>手机上的数据。</strong>您的笔记、学习进度和设置会保留在手机上的应用中，直到您卸载应用或清除其数据。如果您开启了手机自带的备份，备份中也可能有一份；我们无法查看。',
    '<strong>“去除广告”购买。</strong>它属于您的 Google Play 或 App Store 账户，而不属于您的 PetroGram 账号。删除账号不会影响它。',
    '<strong>崩溃报告和匿名使用统计。</strong>它们与您的账号没有关联，不含姓名或电子邮件。崩溃报告保存 90 天。您可以在“设置 → 隐私”中关闭这两项。',
    '<strong>对名字的举报。</strong>对排行榜上某个名字的举报（由您发送的，或针对您的名字的）会保留。其中只有随机用户编号，没有姓名或电子邮件。',
    '<strong>您发给我们的邮件。</strong>它们不属于账号的一部分。如果您希望一并删除，请在邮件中说明。',
  ],
  h_part='只删除排行榜数据，保留账号',
  part='在应用中打开<strong>排行榜</strong>，打开其菜单并选择<strong>退出排行榜</strong>。您的名字和成绩会立即从排行榜删除。您的账号和同步副本会保留。',
  h_more='更多信息',
  more='<a href="{PRIVACY}">PetroGram 隐私政策</a>说明了应用使用的全部数据。如有疑问，请联系 {ASK}。',
),
}
assert list(DEL) == list(DOC_LANGS), 'delete_texts.py: one block per language, in the order of DOC_LANGS'
for _l, _d in DEL.items():
    assert set(_d) == set(DEL['en']) and all(_d.values()), ('a text is missing in delete_texts.py', _l)
    assert all(len(_d[_k]) == len(DEL['en'][_k]) for _k in ('app_steps', 'mail_steps', 'del_items', 'keep_items')), _l


# The apps where a person can put a certificate of completion online.
CERT_APPS = ('petrogram', 'oregram')


def delete_secs(app='petrogram'):
    """The sections of the page (language -> HTML), for the site language
    being built. The link to the privacy policy leads to the same language:
    its own page in Azerbaijani and Russian, its part of the English page
    for the others. app: the app's folder on the site (build.py changes the
    name and the date for an app other than PetroGram)."""
    def items(rows):
        return '\n'.join(f'    <li>{r}</li>' for r in rows)

    out = {}
    for l, d in DEL.items():
        privacy = f'/{app}/privacy/#{l}' if L == 'en' else f'{PRE[L]}/{app}/privacy/'
        rtl = ' dir="rtl"' if l == 'ar' else ''
        hl = 'zh-Hans' if l == 'zh' else l
        sec = f'''<section id="{l}" lang="{hl}"{rtl}>
  <h1>{d['h1']}</h1>
  <p class="meta">{d['meta']}</p>
  <p>{d['intro']}</p>

  <h2>{d['h_app']}</h2>
  <ol>
{items(d['app_steps'])}
  </ol>
  <p>{d['app_note']}</p>

  <h2>{d['h_mail']}</h2>
  <ol>
{items(d['mail_steps'])}
  </ol>
  <p>{d['mail_note']}</p>

  <h2>{d['h_del']}</h2>
  <ul>
{items(d['del_items'] + ([d['del_cert']] if app in CERT_APPS else []))}
  </ul>

  <h2>{d['h_keep']}</h2>
  <ul>
{items(d['keep_items'])}
  </ul>

  <h2>{d['h_part']}</h2>
  <p>{d['part']}</p>

  <h2>{d['h_more']}</h2>
  <p>{d['more']}</p>
</section>'''
        out[l] = sec.replace('{MAIL}', DEL_MAIL).replace('{ASK}', DEL_ASK).replace('{PRIVACY}', privacy)
    return out
