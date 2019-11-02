#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释
import random


user_agent_list = [
    # Chrome Win10:
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    # Firefox Win7:
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    # Safari Win7:
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    # Opera Win7:
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    # IE Win7+ie9：
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)",
    # Win7+ie8：
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)",
    # WinXP+ie8：
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)",
    # WinXP+ie7：
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    # WinXP+ie6：
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    # 傲游3.1.7在Win7+ie9,高速模式:
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
    # 傲游3.1.7在Win7+ie9,IE内核兼容模式:
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)",
    # 搜狗3.0在Win7+ie9,IE内核兼容模式:
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    # 搜狗3.0在Win7+ie9,高速模式:
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0",
    # 360浏览器3.0在Win7+ie9:
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)",
    # QQ浏览器6.9(11079)在Win7+ie9,极速模式:
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201",
    # QQ浏览器6.9(11079)在Win7+ie9,IE内核兼容模式:
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201",
    # 阿云浏览器1.3.0.1724 Beta(编译日期2011-12-05)在Win7+ie9:
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"
]


def gen_header():
    header = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Referer": "https://www.zhihu.com",
        "Host": "www.zhihu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(user_agent_list),
        "x-requested-with": "fetch",
        "x-ab-param": "se_cardrank_3=0;se_time_threshold=0;pf_creator_card=1;zr_rel_search=base;se_ctr_pyc=1;se_zu_recommend=0;se_famous=1;tsp_billboardhead=3;ug_follow_topic_1=2;se_backsearch=0;se_agency= 0;tsp_childbillboard=2;se_ltr_cp_new=0;se_auto_syn=0;tp_qa_metacard=1;ug_follow_answerer=0;li_pay_banner_type=4;zr_km_item_cf=open;ug_goodcomment_0=1;qap_payc_invite=0;zr_km_slot_style=event_card;se_webrs=1;pf_fuceng=1;zr_item_nn_recall=close;se_payconsult=5;ug_zero_follow_0=0;tsp_vote=2;se_mclick1=2;se_websearch=3;top_new_feed=5;li_tjys_ec_ab=0;se_pro=0;se_cardrank_1=0;tp_sft=a;ls_zvideo_license=1;ls_zvideo_trans=0;zw_payc_qaedit=0;se_college=default;tp_topic_head=0;ls_new_upload=0;top_quality=0;sem_up_growth=td;se_dnn_mt=0;se_ltr_dnn_cp=0;se_wannasearch=a;zr_km_recall=default;se_expired_ob=0;se_likebutton=0;se_whitelist=1;se_topiclabel=1;se_zu_onebox=0;se_ctr_user=1;se_preset_tech=0;li_salt_hot=2;li_se_heat=1;zr_km_answer=open_cvr;zr_km_special=close;se_site_onebox=0;tp_club_qa_pic=0;tp_qa_metacard_top=top;se_ad_index=10;li_se_xgb=0;li_video_section=0;zr_slot_cold_start=aver;zr_video_rank_nn=new_rank;se_featured=1;se_adxtest=1;top_native_answer=9;zr_cold_start=0;zr_video_rank=new_rank;zr_km_feed_prerank=new;se_time=0.5;tsp_hotctr=2;pf_newguide_vertical=0;ug_zero_follow=0;soc_special=0;ls_fmp4=0;zr_km_topic_zann=new;zr_rec_answer_cp=close;se_club_post=5;se_waterfall=0;tsp_newchild=1;li_qa_cover=old;zr_km_feed_nlp=old;tp_sft_v2=d;tsp_billboardsheep2=2;top_root=0;soc_zcfw_shipinshiti=0;ug_fw_answ_aut_1=0;ug_newtag=1;li_se_kv=0;qap_ques_invite=0;zw_sameq_sorce=999;se_subtext=1;zr_km_item_prerank=old;se_sug=0;se_cardrank_4=1;se_billboardsearch=0;tp_header_style=1;soc_yxzl_zcfw=0;li_album_liutongab=0;li_vip_no_ad_mon=0;zr_intervene=0;se_ab=0;se_mclick=0;se_go_ztext=0;se_colorfultab=1;top_test_4_liguangyi=1;li_hot_score_ab=0;li_book_button=0;zr_answer_rec_cp=open;se_entity_model=1;se_cardrank_2=0;li_search_answer=3;zr_km_style=mixed_10;se_webtimebox=1;se_search_feed=N;se_amovietab=1;se_college_cm=1;se_webmajorob=0;se_hotmore=0;se_movietab=1;soc_update=0;li_se_media_icon=0;zr_km_recall_num=close;se_spb309=0;soc_notification=1;top_universalebook=1;li_se_vertical=1;se_new_topic=0;se_ctr_topic=1;se_mobileweb=1;soc_zcfw_broadcast=1;pf_foltopic_usernum=50;zr_ans_rec=gbrank;se_topicfeed=0;se_ltr_user=1;top_v_album=1;zr_video_recall=current_recall;zr_km_category=close;se_ios_spb309=1;ug_follow_answerer_0=0;tp_club_qa=1;tp_meta_card=0;tp_qa_toast=1;li_se_album_card=0;li_se_paid_answer=0;zr_km_prerank=new;se_col_boost=0;soc_bignew=1;soc_bigone=1;soc_zuichangfangwen=1;zr_man_intervene=0;zr_test_aa1=1;se_aa_base=0;se_hotsearch=1;top_ebook=0;li_qa_new_cover=1;zr_infinity_member=close;se_lottery=0;se_use_zitem=0;se_p_slideshow=0;se_hot_timebox=1;top_hotcommerce=1;pf_noti_entry_num=0;top_ydyq=X;li_android_vip=0;zr_search_xgb=1;se_dnn_unbias=1;ls_videoad=2;zr_article_new=close;se_perf=0;tp_sticky_android=2;tp_m_intro_re_topic=1;li_purchase_test=0;li_se_section=1;zr_art_rec=base;top_vipconsume=1;soc_zcfw_badcase=0"
    }
    return header


if __name__ == '__main__':
    for i in range(100):
        print(gen_header())

