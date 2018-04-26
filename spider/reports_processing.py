#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ziyi'

import os
import pandas as pd

def get_scale_list(file_name,path):
    scale_list = []
    # customer_list = []
    # supplier_list = []
    relevance_list = []
    five_customer_name = []
    five_supplier_name = []
    five_company_name = []
    # other_formulation = ['第一名','第二名','第三名','第四名','第五名','第1名','第2名','第3名','第4名','第5名','客户一','客户二','客户三','客户四','客户五','客户1','客户2','客户3','客户4','客户5','客户6','供应商一','供应商二','供应商三','供应商','']

    print(file_name)
    with open (path) as f:
        for i, company_line in enumerate (f):
            if '0%' in company_line or '0.00%' in company_line or '0.0%' in company_line:
                scale_list.append(i)
            # if '前5客户' in company_line or '前五客户' in company_line or '前5大客户' in company_line  or '前5名客户' in company_line or '前五大客户' in company_line or '前五名客户' in company_line:
            #     customer_list.append(i)
            # if '前5供应商' in company_line or '前五供应商' in company_line or '前5大供应商' in company_line  or '前5名供应商' in company_line or '前五大供应商' in company_line or '前五名供应商' in company_line:
            #     supplier_list.append(i)
            if '关联关系' in company_line or '关联方' in company_line or '与本公司关系' in company_line:
                relevance_list.append(i)
            if '有限公司' in company_line or '股份公司' in company_line or '有限责任公司' in company_line:
                five_company_name.append(i)
            if '客户1' in company_line or '客户一' in company_line or '第一名' in company_line or '第1名' in company_line:
                five_customer_name.append(i)
            if '供应商1' in company_line or '供应商一' in company_line or '第一名' in company_line or '第1名' in company_line:
                five_supplier_name.append(i)
    print(scale_list,relevance_list,five_company_name, five_customer_name,five_supplier_name)
    return scale_list, relevance_list,five_company_name, five_customer_name,five_supplier_name

def create_reports_table(file_name,path,scale_list, relevance_list,five_company_name, five_customer_name,five_supplier_name):

    df = pd.DataFrame ({})
    analysis_data = {}
    failed_company = []
    # 所有内容初始化
    analysis_data['total_information'] = 0
    analysis_data['five_customers_sale_all'] = 0
    analysis_data['five_relevance_customers_sale'] = 0
    analysis_data['five_relevance_customers_check'] = 0
    analysis_data['five_customers_name'] = 0
    analysis_data['five_customers_sale'] = 0

    analysis_data['five_supplier_buy_all'] = 0
    analysis_data['five_relevance_supplier_buy'] = 0
    analysis_data['five_relevance_supplier_check'] = 0
    analysis_data['five_supplier_name'] = 0
    analysis_data['five_supplier_buy'] = 0

    with open(path) as all:
        company_name = {}
        company_index = []
        all_txt = all.read()
        # 判断披露金额占比是否有0%的情况存在
        if '0%' not in all_txt or '0.00%' not in all_txt or '0.0%' not in all_txt:
            show_check = 1
        else:
            show_check = 0

        # 财报中未披露前五客户或前五供应商信息的公司情况
        if "未披露" in all_txt:
            print('未披露')

        # 财报中未披露前五客户或前五供应商信息的公司情况
        elif "pdf解码错误" in all_txt:
            print('pdf解码错误')
            failed_company.append(file_name)
        else:
            customer = 0
            supplier = 0
            total_scale = 0
            supplier_total_scale = 0
            relevance_check = 0
            check_customer = 0
            # print(''.join(content for content in all_txt.strip().split()))
            with open (path) as f:
                for i,company_line in enumerate(f):
                    # print(company_line)
                    # 有披露内容的指标的判断
                    # 1前五名客户合计销售金额占年度销售总额的比例
                    if '前五' in company_line or '前5' in company_line:
                        if '客户' in company_line:
                            if '销售' in company_line or '营业' in company_line or '采购' in company_line:
                                customer = 2
                                total_scale = i
                                if '总额' in company_line or '合计' in company_line or '全部' in company_line:
                                    customer = 1
                                    total_scale = i
                                    if '占' in company_line or '比' in company_line or '占比' in company_line:
                                        analysis_data['five_customers_sale_all'] = 1

                    # 纯文字表述情况统计
                    # print(customer)
                    if customer == 1 and abs(i - total_scale) < 8 :
                        if '占比' in company_line or '比' in company_line or '占' in company_line:
                            analysis_data['five_customers_sale_all'] = 1
                    elif customer == 2 and abs(i - total_scale) < 8 :
                        if '总额' in company_line or '全部' in company_line or '合计' in company_line:
                            if '占比' in company_line or '比' in company_line or '占' in company_line:
                                analysis_data['five_customers_sale_all'] = 1
                    #                 analysis_data['five_customers_sale_all'] = 1:
                    # elif customer == 3 and abs(i - total_scale) < 5 :
                    #     if '销售' in company_line or '营业' in company_line or '采购' in company_line:
                    #         if '总额' in company_line or '全部' in company_line or '合计' in company_line:
                    #             if '占比' in company_line or '比' in company_line or '占' in company_line:
                    #                 analysis_data['five_customers_sale_all'] = 1

                    # 2前五名客户销售额中关联方销售额合计占年度销售总额的比例
                    if '客户' in company_line :
                        if "关联" in company_line or "关" in company_line or "联" in company_line:
                            if '占比' in company_line or'比' in company_line or '占' in company_line:
                                analysis_data['five_relevance_customers_sale'] = 1
                                relevance_check = i

                    # 3前五名客户分别与自己的关联关系
                    if analysis_data['five_relevance_customers_sale'] == 1:
                        if i in scale_list or i + 1 in scale_list or i + 2 in scale_list :
                            analysis_data['five_relevance_customers_check'] = -1
                        else:
                            for j in range(10):
                                if relevance_check-j in relevance_list or relevance_check+j in relevance_list:
                                    analysis_data['five_relevance_customers_check'] = 1
                    else:
                        analysis_data['five_relevance_customers_check'] = 0

                    # 4前五名客户具体名称和5前五名客户的具体销售额
                    if '前五' in company_line or '前5' in company_line or '主要' in company_line:
                        if '客户情况' in company_line or '客户资料' in company_line  or '客户明细' in company_line or '客户的情况' in company_line or '客户的资料' in company_line or '营业收入情况' in company_line or '客户名称' in company_line:
                            check_customer = 1
                            print('存在',i)
                            if five_customer_name:
                                for j in five_customer_name:
                                    if abs(j-i)<25:
                                        analysis_data['five_customers_name'] = 0
                                        analysis_data['five_customers_sale'] = 1
                                        break
                            if five_company_name:
                                for m in five_company_name:
                                    print('应该有值',i,m)
                                    if abs (m - i) < 25:
                                        analysis_data['five_customers_name'] = 1
                                        analysis_data['five_customers_sale'] = 1
                                        break

                        if '供应商情况' in company_line or '供应商资料' in company_line or '供应商明细' in company_line or '供应商的资料' in company_line or '供应商的情况' in company_line or '供应商名称' in company_line:
                            check_customer = 2
                            if five_supplier_name:
                                for j in five_supplier_name:
                                    if abs(j-i)<25:
                                        analysis_data['five_supplier_name'] = 0
                                        analysis_data['five_supplier_buy'] = 1
                                        break
                            if five_company_name:
                                for m in five_company_name:
                                    if abs (m - i) < 25:
                                        analysis_data['five_supplier_name'] = 1
                                        analysis_data['five_supplier_buy'] = 1
                                        break

                    if check_customer == 1 or check_customer == 2:
                        if '第一名' in company_line or '第1名' in company_line or '客户1' in company_line or '供应商1' in company_line or '客户一' in company_line or '供应商一' in company_line:
                            analysis_data['five_customers_name'] = 0
                            analysis_data['five_customers_sale'] = 1
                            analysis_data['five_supplier_name'] = 0
                            analysis_data['five_supplier_buy'] = 1

                    # 6前五名供应商合计采购金额占年度采购总额比例
                    if '前五' in company_line or '前5' in company_line:
                        if '供应商' in company_line or '供货商' in company_line:
                            if '采购' in company_line and '总额' in company_line:
                                supplier = 1
                                supplier_total_scale = i
                                if '占' in company_line or '比' in company_line or '占比' in company_line:
                                    analysis_data['five_supplier_buy_all'] = 1
                            elif '采购' in company_line and '合计' in company_line:
                                supplier = 1
                                supplier_total_scale = i
                                if '占' in company_line or '比' in company_line or '占比' in company_line:
                                    analysis_data['five_supplier_buy_all'] = 1

                    if supplier == 1 and abs(i - supplier_total_scale) < 5 and  '比' in company_line:
                        analysis_data['five_supplier_buy_all'] = 1

                    # 7前五名供应商采购额中关联方采购额占年度采购总额比例
                    if '供应商' in company_line and "关联" in company_line and'比' in company_line:
                        analysis_data['five_relevance_supplier_buy'] = 1
                    elif '供应商' in company_line and "关" in company_line and'比' in company_line:
                        analysis_data['five_relevance_supplier_buy'] = 1
                    elif '供应商' in company_line and "联" in company_line and'比' in company_line:
                        analysis_data['five_relevance_supplier_buy'] = 1

                    # 8前五名供应商分别与自己的关联关系
                    if analysis_data['five_relevance_supplier_buy'] == 1:

                        if i in scale_list or i + 1 in scale_list or i + 2 in scale_list :
                            analysis_data['five_relevance_customers_check'] = -1
                        else:
                            for j in range(10):
                                if relevance_check-j in relevance_list or relevance_check+j in relevance_list:
                                    analysis_data['five_relevance_customers_check'] = 1
                    else:
                        analysis_data['five_relevance_customers_check'] = 0

    analysis_data['classify'] = '深市'
    analysis_data['ID'] = file_name.split('_')[2]
    analysis_data['name'] = file_name.split('_')[1]
    analysis_data['time'] = file_name.split('_')[0]
    analysis_data['total_information'] = int(analysis_data['five_customers_sale_all'])+int(analysis_data['five_relevance_customers_sale'])+int(analysis_data['five_relevance_customers_check'])+int(analysis_data['five_customers_name'])+int(analysis_data['five_customers_sale'])+int(analysis_data['five_supplier_buy_all']) +int(analysis_data['five_relevance_supplier_buy'])+int(analysis_data['five_relevance_supplier_check'])+int(analysis_data['five_supplier_name'])+int(analysis_data['five_supplier_buy'])
    print(analysis_data)
    df = df.append (analysis_data, ignore_index=True)
    return df

def save_info(contents, name):
    df = pd.DataFrame()
    df = df.append(contents.copy())
    df.to_csv('D:\\financial_reports\\sz_financial_reports\\{}.csv'.format(name+'_5'), encoding='gbk')

if __name__ == '__main__':
    analysis_path = 'D:\\financial_reports\\sz_financial_reports\\test_txt'
    all_file = os.listdir(analysis_path)
    results = []
    for one in all_file:
        path = os.path.join(analysis_path,one)
        file_name = os.path.splitext(one)[0]
        print(path)
        scale_list, relevance_list, five_company_name, five_customer_name, five_supplier_name = get_scale_list(file_name,path)
        table = create_reports_table(file_name, path, scale_list, relevance_list, five_company_name, five_customer_name, five_supplier_name)
        results.append(table)
    save_info(results,analysis_path.split('\\')[-1])
