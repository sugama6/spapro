from django.db import models
from django.db.models import CharField, Model, IntegerField
from django_mysql.models import ListCharField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Users(models.Model):
    login_id = models.CharField(max_length=8, unique=True, verbose_name='ログインID')
    last_name = models.CharField(max_length=100, verbose_name='性')
    first_name = models.CharField(max_length=100, verbose_name='名')
    mail_address = models.CharField(max_length=100, verbose_name='メールアドレス')
    password = models.CharField(max_length=100, verbose_name='パスワード')
    sex = models.CharField(max_length=10, verbose_name='性別')
    tel = models.CharField(max_length=12, verbose_name='電話番号')
    postal_code = models.CharField(max_length=7, verbose_name='郵便番号')
    prefectures = models.CharField(max_length=4, verbose_name='都道府県')
    municipalities = models.CharField(max_length=10, verbose_name='市区町村')
    address = models.CharField(max_length=50, verbose_name='番地・丁目')
    apartment_mansion = models.CharField(max_length=50, blank=True, verbose_name='アパート・マンション名')
    withdrawal = models.BooleanField(default=0, verbose_name='退会')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    join_time = models.DateTimeField(verbose_name='入会日')
    update_time = models.DateTimeField(verbose_name='更新日')


class Goal(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='会員ID')
    one_year_later = models.CharField(max_length=500, blank=True, verbose_name='1年後の目標')
    ten_years_later = models.CharField(max_length=500, blank=True, verbose_name='10年後目標')
    learning_programming_why = models.CharField(max_length=500, blank=True, verbose_name='なぜプログラミングを学習したいのか')
    selected_spapro_why = models.CharField(max_length=500, blank=True, verbose_name='なぜスパプロを選んだ')
    how_much_effort = models.CharField(max_length=500, blank=True, verbose_name='どのくらいの努力')
    what_i_can_do = models.CharField(max_length=500, blank=True, verbose_name='自分ができること')
    how_can_i_be = models.CharField(max_length=500, blank=True, verbose_name='どうしたらなれるのか')
    how_long_want_to_be = models.CharField(max_length=500, blank=True, verbose_name='いつまでに成功させたいのか')
    keep_a_promise = models.CharField(max_length=500, blank=True, verbose_name='約束を守れるか')
    key_man = models.CharField(max_length=500, blank=True, verbose_name='キーマンは誰か')
    orientation_expected_date = models.DateField(blank=True, verbose_name='オリエンテーション完了予定日')
    html_css_expected_date = models.DateField(blank=True, verbose_name='HTML/CSS完了予定日')
    javascript_expected_date = models.DateField(blank=True, verbose_name='JavaScript完了予定日')
    python1_expected_date = models.DateField(blank=True, verbose_name='Python基礎完了予定日')
    python2_expected_date = models.DateField(blank=True, verbose_name='Python応用完了予定日')
    sql_expected_date = models.DateField(blank=True, verbose_name='SQL基礎完了予定日')
    django_expected_date = models.DateField(blank=True, verbose_name='Django基礎完了予定日')
    portfolio_expected_date = models.DateField(blank=True, verbose_name='ポートフォリオ作成完了予定日')
    job_change_expected_date = models.DateField(blank=True, verbose_name='転職成功予定日')
    insert_time = models.DateTimeField(verbose_name='登録日')
    update_time = models.DateTimeField(verbose_name='更新日')


class LearningProgress(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='会員ID')


class TeachingMaterials(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.CharField(max_length=1000, verbose_name='内容')
    url = models.CharField(max_length=500, verbose_name='URL')
    image = models.CharField(max_length=100, verbose_name='画像')
    programming_language = models.CharField(max_length=100, verbose_name='言語')
    release_flg = models.BooleanField(default=0, verbose_name='公開フラグ')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日')
    update_time = models.DateTimeField(verbose_name='更新日')


class Inquiry(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='問い合わせ会員ID')
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.CharField(max_length=1000, verbose_name='内容')
    read_flg = models.BooleanField(default=0, verbose_name='既読フラグ')
    answer_flg = models.BooleanField(default=0, verbose_name='解決フラグ')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日')
    update_time = models.DateTimeField(verbose_name='更新日')


class Portfolio(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='会員ID')
    url = models.CharField(max_length=500, verbose_name='ポートフォリオURL')
    image = models.CharField(max_length=100, verbose_name='画像')
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.CharField(max_length=1000, verbose_name='内容')
    release_flg = models.BooleanField(default=0, verbose_name='公開フラグ')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日')
    update_time = models.DateTimeField(verbose_name='更新日')


class AdminUsers(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='性')
    first_name = models.CharField(max_length=100, verbose_name='名')
    mail_address = models.CharField(max_length=100, verbose_name='メールアドレス')
    password = models.CharField(max_length=100, verbose_name='パスワード')
    sex = models.CharField(max_length=10, verbose_name='性別')
    tel = models.CharField(max_length=12, verbose_name='電話番号')
    postal_code = models.IntegerField(verbose_name='郵便番号')
    prefectures = models.CharField(max_length=4, verbose_name='都道府県')
    municipalities = models.CharField(max_length=10, verbose_name='市区町村')
    address = models.CharField(max_length=50, verbose_name='番地・丁目')
    apartment_mansion = models.CharField(max_length=50, blank=True, verbose_name='アパート・マンション名')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    join_time = models.DateTimeField(verbose_name='入会日')
    update_time = models.DateTimeField(verbose_name='更新日')


class QandA(models.Model):
    update_admin_user_id = models.ForeignKey(AdminUsers, on_delete=models.CASCADE, verbose_name='更新管理者ID')
    question = models.CharField(max_length=500, verbose_name='質問')
    answer = models.CharField(max_length=500, verbose_name='回答')
    sort = models.IntegerField(verbose_name='表示順')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日')
    update_time = models.DateTimeField(verbose_name='更新日')


class News(models.Model):
    admin_user_id = models.ForeignKey(AdminUsers, on_delete=models.CASCADE, verbose_name='管理者ID')
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.CharField(max_length=1000, verbose_name='コンテンツ')
    image = models.CharField(max_length=100, verbose_name='画像')
    release_flg = models.BooleanField(default=0, verbose_name='公開フラグ')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日')
    update_time = models.DateTimeField(verbose_name='更新日')
