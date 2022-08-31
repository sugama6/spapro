from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import top, reset_pw, member_reg, teaching_materials, news,\
     inquiry, settings, change_mail, change_pw, withdrawal, portfolio, goal, \
    admin_top, admin_reg, admin_member, admin_send_mail, admin_forced_withdrawal,\
    admin_member_withdrawal, admin_list, admin_teaching_materials, admin_inquiry, admin_portfolio, admin_news, admin_q_and_a,\
    logout

urlpatterns = [
    # top
    path('', top.G010_top, name='G010_top'),
    path('G020_login/', top.G020_login, name='G020_login'),
    
    # reset_pw
    path('G030_reset_pw/', reset_pw.G030_reset_pw, name='G030_reset_pw'),
    path('G040_reset_pw_send_mail_comp/', reset_pw.G040_reset_pw_send_mail_comp, name='G040_reset_pw_send_mail_comp'),
    path('G050_resetting_pw/', reset_pw.G050_resetting_pw, name='G050_resetting_pw'),
    path('G060_resetting_pw_comp/', reset_pw.G060_resetting_pw_comp, name='G060_resetting_pw_comp'),
    
    # member_reg
    path('G070_reg/', member_reg.G070_reg, name='G070_reg'),
    path('G080_reg_conf/', member_reg.G080_reg_conf, name='G080_reg_conf'),
    path('G090_reg_comp/', member_reg.G090_reg_comp, name='G090_reg_comp'),
    path('G100_member_top/', member_reg.G100_member_top, name='G100_member_top'),
    path('G110_edit/', member_reg.G110_edit, name='G110_edit'),
    # path('G120_learning_progress/', .G120_learning_progress, name='G120_learning_progress'),

    # teaching_materials
    path('G130_teaching_materials/', teaching_materials.G130_teaching_materials, name='G130_teaching_materials'),
    path('G140_teaching_detail/<int:id>', teaching_materials.G140_teaching_detail, name='G140_teaching_detail'),

    # news
    path('G150_news/', news.G150_news, name='G150_news'),
    path('G160_news_detail/<int:id>', news.G160_news_detail, name='G160_news_detail'),

    # inquiry
    path('G170_inquiry/', inquiry.G170_inquiry, name='G170_inquiry'),
    path('G171_inquiry_conf/', inquiry.G171_inquiry_conf, name='G171_inquiry_conf'),
    path('G180_inquiry_comp/', inquiry.G180_inquiry_comp, name='G180_inquiry_comp'),
    path('G190_q_and_a/', inquiry.G190_q_and_a, name='G190_q_and_a'),

    # settings
    path('G200_settings/', settings.G200_settings, name='G200_settings'),

    # change_mail
    path('G210_change_mail/', change_mail.G210_change_mail, name='G210_change_mail'),
    path('G220_change_mail_c]onf/', change_mail.G220_change_mail_conf, name='G220_change_mail_conf'),
    path('G230_change_mail_comp/', change_mail.G230_change_mail_comp, name='G230_change_mail_comp'),

    # change_pw
    path('G240_change_pw/', change_pw.G240_change_pw, name='G240_change_pw'),
    path('G241_change_pw_conf/', change_pw.G241_change_pw_conf, name='G241_change_pw_conf'),
    path('G250_change_pw_comp/', change_pw.G250_change_pw_comp, name='G250_change_pw_comp'),

    # withdrawal
    path('G260_withdrawal/', withdrawal.G260_withdrawal, name='G260_withdrawal'),
    path('G270_withdrawal_conf/', withdrawal.G270_withdrawal_conf, name='G270_withdrawal_conf'),
    path('G280_withdrawal_comp/', withdrawal.G280_withdrawal_comp, name='G280_withdrawal_comp'),

    # portfolio
    path('G290_portfolio/<str:sort>', portfolio.G290_portfolio, name='G290_portfolio'),
    path('G300_portfolio_reg/', portfolio.G300_portfolio_reg, name='G300_portfolio_reg'),
    path('G310_portfolio_conf/', portfolio.G310_portfolio_conf, name='G310_portfolio_conf'),
    path('G320_portfolio_comp/', portfolio.G320_portfolio_comp, name='G320_portfolio_comp'),
    path('G321_my_portfolio_list/<str:sort>', portfolio.G321_my_portfolio_list, name='G321_my_portfolio_list'),
    path('G330_portfolio_edit/<int:id>', portfolio.G330_portfolio_edit, name='G330_portfolio_edit'),

    # goal
    path('G340_goal/', goal.G340_goal, name='G340_goal'),
    path('G350_goal_edit/', goal.G350_goal_edit, name='G350_goal_edit'),
    
    
    # admin_top
    path('G400_admin_login/', admin_top.G400_admin_login, name='G400_admin_login'),

    # admin_reg
    path('G410_admin_reg/', admin_reg.G410_admin_reg, name='G410_admin_reg'),
    path('G420_admin_reg_conf/', admin_reg.G420_admin_reg_conf, name='G420_admin_reg_conf'),
    path('G430_admin_reg_comp/', admin_reg.G430_admin_reg_comp, name='G430_admin_reg_comp'),

    #admin_member
    path('G440_admin_member_list/', admin_member.G440_admin_member_list, name='G440_admin_member_list'),
    path('G450_admin_member_detail/<int:id>', admin_member.G450_admin_member_detail, name='G450_admin_member_detail'),
    path('G460_admin_member_edit/<int:id>', admin_member.G460_admin_member_edit, name='G460_admin_member_edit'),

    # admin_send_mail
    path('G470_admin_send_mail/', admin_send_mail.G470_admin_send_mail, name='G470_admin_send_mail'),
    path('G480_admin_send_mail_conf/', admin_send_mail.G480_admin_send_mail_conf, name='G480_admin_send_mail_conf'),
    path('G490_admin_send_mail_comp/', admin_send_mail.G490_admin_send_mail_comp, name='G490_admin_send_mail_comp'),

    # admin_forced_withdrawal
    path('G500_admin_forced_withdrawal/', admin_forced_withdrawal.G500_admin_forced_withdrawal, name='G500_admin_forced_withdrawal'),
    path('G510_admin_forced_withdrawal_conf/<int:id>', admin_forced_withdrawal.G510_admin_forced_withdrawal_conf, name='G510_admin_forced_withdrawal_conf'),
    path('G520_admin_forced_withdrawal_comp/<int:id>', admin_forced_withdrawal.G520_admin_forced_withdrawal_comp, name='G520_admin_forced_withdrawal_comp'),
    path('G530_admin_member_withdrawal_list/', admin_member_withdrawal.G530_admin_member_withdrawal_list, name='G530_admin_member_withdrawal_list'),

    # admin_member_withdrawal
    path('G540_admin_member_withdrawal_detail/<int:id>', admin_member_withdrawal.G540_admin_member_withdrawal_detail, name='G540_admin_member_withdrawal_detail'),

    # admin_list
    path('G550_admin_list/', admin_list.G550_admin_list, name='G550_admin_list'),
    path('G560_admin_detail/<int:id>', admin_list.G560_admin_detail, name='G560_admin_detail'),
    path('G561_admin_edit/<int:id>', admin_list.G561_admin_edit, name='G561_admin_edit'),
    path('G570_admin_del_conf/<int:id>', admin_list.G570_admin_del_conf, name='G570_admin_del_conf'),
    path('G580_admin_del_comp/<int:id>', admin_list.G580_admin_del_comp, name='G580_admin_del_comp'),

    # admin_teaching_materials
    path('G590_admin_teaching_materials_list/', admin_teaching_materials.G590_admin_teaching_materials_list, name='G590_admin_teaching_materials_list'),
    path('G600_admin_teaching_materials_reg/', admin_teaching_materials.G600_admin_teaching_materials_reg, name='G600_admin_teaching_materials_reg'),
    path('G610_admin_teaching_materials_reg_conf/', admin_teaching_materials.G610_admin_teaching_materials_reg_conf, name='G610_admin_teaching_materials_reg_conf'),
    path('G620_admin_teaching_materials_reg_comp/', admin_teaching_materials.G620_admin_teaching_materials_reg_comp, name='G620_admin_teaching_materials_reg_comp'),
    path('G621_admin_teaching_materials_detail/<int:id>', admin_teaching_materials.G621_admin_teaching_materials_detail, name='G621_admin_teaching_materials_detail'),
    path('G622_admin_teaching_materials_edit/<int:id>', admin_teaching_materials.G622_admin_teaching_materials_edit, name='G622_admin_teaching_materials_edit'),
    path('G630_admin_teaching_materials_del_conf/', admin_teaching_materials.G630_admin_teaching_materials_del_conf, name='G630_admin_teaching_materials_del_conf'),
    path('G640_admin_teaching_materials_del_comp/', admin_teaching_materials.G640_admin_teaching_materials_del_comp, name='G640_admin_teaching_materials_del_comp'),

    # admin_inquiry
    path('G650_admin_inquiry_list/', admin_inquiry.G650_admin_inquiry_list, name='G650_admin_inquiry_list'),
    path('G660_admin_inquiry_detail/<int:id>', admin_inquiry.G660_admin_inquiry_detail, name='G660_admin_inquiry_detail'),
    path('G670_admin_inquiry_res/<int:id>', admin_inquiry.G670_admin_inquiry_res, name='G670_admin_inquiry_res'),
    path('G680_admin_inquiry_res_conf/<int:id>', admin_inquiry.G680_admin_inquiry_res_conf, name='G680_admin_inquiry_res_conf'),
    path('G690_admin_inquiry_res_comp/<int:id>', admin_inquiry.G690_admin_inquiry_res_comp, name='G690_admin_inquiry_res_comp'),

    # admin_portfolio
    path('G700_admin_portfolio_list/<str:sort>', admin_portfolio.G700_admin_portfolio_list, name='G700_admin_portfolio_list'),
    path('G701_admin_portfolio_detail/<int:id>', admin_portfolio.G701_admin_portfolio_detail, name='G701_admin_portfolio_detail'),
    path('G710_admin_portfolio_edit/<int:id>', admin_portfolio.G710_admin_portfolio_edit, name='G710_admin_portfolio_edit'),
    path('G711_admin_portfolio_delete_conf/<int:id>', admin_portfolio.G711_admin_portfolio_delete_conf, name='G711_admin_portfolio_delete_conf'),
    path('G712_admin_portfolio_delete_comp/<int:id>', admin_portfolio.G712_admin_portfolio_delete_comp, name='G712_admin_portfolio_delete_comp'),

    # admin_news
    path('G720_admin_news_list/', admin_news.G720_admin_news_list, name='G720_admin_news_list'),
    path('G730_admin_news_reg/', admin_news.G730_admin_news_reg, name='G730_admin_news_reg'),
    path('G740_admin_news_reg_conf/', admin_news.G740_admin_news_reg_conf, name='G740_admin_news_reg_conf'),
    path('G750_admin_news_reg_comp/', admin_news.G750_admin_news_reg_comp, name='G750_admin_news_reg_comp'),
    path('G760_admin_news_detail/<int:id>', admin_news.G760_admin_news_detail, name='G760_admin_news_detail'),
    path('G770_admin_news_edit/<int:id>', admin_news.G770_admin_news_edit, name='G770_admin_news_edit'),
    path('G780_admin_news_delete_conf/<int:id>', admin_news.G780_admin_news_delete_conf, name='G780_admin_news_delete_conf'),
    path('G790_admin_news_delete_comp/<int:id>', admin_news.G790_admin_news_delete_comp, name='G790_admin_news_delete_comp'),

    path('G800_admin_q_and_a_list/', admin_q_and_a.G800_admin_q_and_a_list, name='G800_admin_q_and_a_list'),
    path('G810_admin_q_and_a_reg/', admin_q_and_a.G810_admin_q_and_a_reg, name='G810_admin_q_and_a_reg'),
    path('G820_admin_q_and_a_reg_conf/', admin_q_and_a.G820_admin_q_and_a_reg_conf, name='G820_admin_q_and_a_reg_conf'),
    path('G830_admin_q_and_a_reg_comp/', admin_q_and_a.G830_admin_q_and_a_reg_comp, name='G830_admin_q_and_a_reg_comp'),
    path('G831_admin_q_and_a_detail/<int:id>', admin_q_and_a.G831_admin_q_and_a_detail, name='G831_admin_q_and_a_detail'),
    path('G840_admin_q_and_a_edit/<int:id>', admin_q_and_a.G840_admin_q_and_a_edit, name='G840_admin_q_and_a_edit'),
    path('G850_admin_q_and_a_del_conf/<int:id>', admin_q_and_a.G850_admin_q_and_a_del_conf, name='G850_admin_q_and_a_del_conf'),
    path('G860_admin_q_and_a_del_comp/<int:id>', admin_q_and_a.G860_admin_q_and_a_del_comp, name='G860_admin_q_and_a_del_comp'),

    path('logout/<str:login_id>', logout.logout, name='logout'),

]
# ] + static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
