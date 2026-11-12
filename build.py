#!/usr/bin/env python3
"""Build index.html (English) and zh/index.html (Chinese) from src_page.html.

Edit copy in STRINGS below, then run: python3 build.py
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
COMPANY_EN = "Qingdao Zhilian Intelligent Catering Equipment Co., Ltd."
COMPANY_ZH = "青岛智链智能餐饮设备有限公司"

STRINGS = {
 "en": {
  "lang": "en", "root": "", "brand": "ZHILIAN", "other_href": "zh/", "other_lang": "zh-CN", "other_label": "中文",
  "title": "Zhilian | Smart cooking equipment manufacturer, OEM and ODM",
  "alt_hero": "Two white countertop ramen cookers, each with a bowl of noodles on its induction plate",
  "f1_h": "Certified for global markets", "f1_p": "Depending on the model, our equipment holds ETL, FCC, CE, CB and CCC certifications for markets from North America and Europe to China.",
  "phone_row": "",
  "desc": "Zhilian designs and manufactures induction-heated, connected cooking equipment, with OEM and ODM production for brands worldwide.",
  "home_label": "Zhilian home", "nav_label": "Main",
  "nav_factory": "Factory", "nav_make": "What we make", "nav_oem": "OEM and ODM", "nav_quality": "Quality", "nav_contact": "Contact",
  "h1": "Smart cooking equipment, engineered and built in-house.",
  "hero_p": "We design and manufacture induction-heated, connected appliances for commercial kitchens and for brands that sell around the world.",
  "hero_btn": "Email our team", "mail_subject": "Project%20inquiry", "coil_label": "Copper induction coil",
  "alt_exterior": "Two-storey white factory building with long rows of windows under a clear sky",
  "factory_h2": "Our factory",
  "factory_lede": "Engineering, assembly, testing and export packing happen under one roof in Jimo District, Qingdao. We design the heating and control systems ourselves and build them into finished equipment on our own lines.",
  "kv_loc": "Location", "kv_loc_v": "Jimo District, Qingdao, Shandong, China",
  "kv_inhouse": "In-house", "kv_inhouse_v": "Hardware and firmware engineering, assembly, safety and burn-in testing",
  "kv_sw": "Software", "kv_sw_v": "Six registered software copyrights",
  "kv_ship": "Shipping", "kv_ship_v": "Export packing for customers worldwide",
  "make_h2": "What we make",
  "make_lede": "Our core is precise, efficient induction heating paired with control software we write ourselves. We build it into finished equipment, or into components for your product.",
  "a1_h": "Induction heating systems", "a1_p": "Coils, power boards and control logic tuned for fast, even heat and stable output under continuous use.",
  "a2_h": "Smart controls", "a2_p": "Touchscreen and one-touch interfaces, barcode and QR scanning, connected IoT controls and the embedded firmware behind them. We hold six registered software copyrights.",
  "a3_h": "Commercial cooking appliances", "a3_p": "Countertop equipment for convenience stores, restaurants and self-service venues, designed for long shifts and easy cleaning.",
  "a4_h": "Custom smart appliances", "a4_p": "New categories built on the same heating and control platform, from first concept to mass production.",
  "eq_h2": "Equipment and consumables", "eq_lede": "Two machines from our lines, plus the induction paper bowls made to work with them.",
  "alt_bowls": "Stack of orange patterned paper bowls with one bowl in front", "p3_h": "Induction paper bowls", "p3_p": "Cook and serve in the same 42 oz (1250 ml) bowl, with no pot to wash. Also fits other compatible induction ramen cookers. Food-contact tested to US FDA 21 CFR 175.300, EU 1935/2004 and LFGB. 300 bowls per case.",
  "clients_h": "Our equipment is in use at",
  "alt_pro": "White countertop ramen cooker with a touchscreen, hot water spout and a bowl of noodles on its induction plate",
  "p1_h": "Commercial induction ramen cooker", "p1_p": "Touchscreen, barcode scanner and built-in hot water. Cooks noodles right in their paper bowl with induction heat, for stores and self-service counters.",
  "alt_studio": "Compact white ramen cooker with a top control panel, blue water tank and a bowl of noodles on its induction plate",
  "p2_h": "Compact ramen cooker and hot water dispenser", "p2_p": "Two appliances in one: an induction ramen cooker and an instant hot water dispenser, run from a one-touch top panel.",
  "prod_h2": "Inside our production", "prod_lede": "Every machine is assembled, wired and tested by our own team before it is packed.",
  "g1": "Assembly line", "alt_g1": "Workers seated along a long assembly line building white appliance housings",
  "g2": "Induction module assembly", "alt_g2": "Technician fitting an induction coil and cooling fan onto a power board",
  "g3": "Wiring and water system", "alt_g3": "Technician connecting wiring and water lines inside an open machine",
  "g4": "Burn-in test line", "alt_g4": "Rows of finished machines on a burn-in test line with an inspector holding a checklist",
  "oem_h2": "OEM and ODM manufacturing",
  "oem_lede": "Bring a finished design for us to produce, or bring an idea and we develop it with you. One team handles engineering, certification support and production.",
  "s1_h": "Brief", "s1_p": "You share the product, target market and price point.",
  "s2_h": "Engineering", "s2_p": "We design or adapt the hardware, firmware and housing.",
  "s3_h": "Prototypes", "s3_p": "Working samples for your testing and feedback.",
  "s4_h": "Certification", "s4_p": "We prepare the product and documents for your market's requirements.",
  "s5_h": "Production", "s5_p": "Assembly, testing and export packing on our own lines.",
  "note_a": "Minimum order, lead time and pricing depend on the project.", "note_link": "Tell us about yours", "note_b": " and we will reply with a proposal.",
  "oem_subject": "OEM%2FODM%20inquiry",
  "q_h2": "Quality and compliance", "q_lede": "We are the manufacturer of record for the equipment we produce, and we stand behind it in every market we ship to.",
  "alt_q": "Technician running an electrical safety test on a finished machine", "q_cap": "Electrical safety testing on a finished machine",
  "f2_h": "Tested before it ships", "f2_p": "Finished machines go through electrical safety testing and run on our burn-in test line before packing.",
  "f3_h": "Product safety contact", "f3_p": "For safety questions or market surveillance requests, write to", "f3_end": ".",
  "c_h2": "Contact", "c_lede": "Tell us what you want to build, or ask about our equipment.",
  "c_email": "Email", "c_phone": "Phone", "c_addr": "Address", "c_co": "Company",
  "phone": "+86 137 3091 9077", "phone_tel": "+8613730919077",
  "addr": "No. 1-005, 188 Chenjia Village, Daxin Town<br>Jimo District, Qingdao, Shandong, China",
  "company": COMPANY_EN,
 },
 "zh": {
  "lang": "zh-CN", "root": "../", "brand": "智链智能", "other_href": "../", "other_lang": "en", "other_label": "EN",
  "title": "智链 | 智能烹饪设备制造，OEM 与 ODM",
  "alt_hero": "两台白色台式煮面机，加热盘上各放着一碗面",
  "f1_h": "面向全球市场的认证", "f1_p": "不同型号的设备已分别取得 ETL、FCC、CE、CB 和 CCC 等认证，覆盖北美、欧洲和中国等市场。",
  "phone_row": "        <dt>电话</dt><dd><a href=\"tel:4006376618\">400-637-6618</a></dd>\n",
  "desc": "智链研发制造电磁加热的智能烹饪设备，为全球品牌提供 OEM 与 ODM 代工服务。",
  "home_label": "智链智能首页", "nav_label": "主导航",
  "nav_factory": "工厂", "nav_make": "产品与技术", "nav_oem": "OEM 与 ODM", "nav_quality": "质量", "nav_contact": "联系我们",
  "h1": "智能烹饪设备，自主研发制造。",
  "hero_p": "我们设计并制造电磁加热的智能联网设备，服务商用厨房，也为面向全球销售的品牌代工生产。",
  "hero_btn": "发邮件联系我们", "mail_subject": "%E9%A1%B9%E7%9B%AE%E5%92%A8%E8%AF%A2", "coil_label": "铜质电磁线圈",
  "alt_exterior": "晴天下的两层白色厂房，外墙有长排窗户",
  "factory_h2": "我们的工厂",
  "factory_lede": "研发、装配、测试和出口包装都在青岛即墨的同一座厂区内完成。加热和控制系统由我们自主设计，并在自有产线上装配成整机。",
  "kv_loc": "地址", "kv_loc_v": "山东省青岛市即墨区",
  "kv_inhouse": "自有能力", "kv_inhouse_v": "硬件与固件研发、整机装配、安规测试与老化测试",
  "kv_sw": "软件", "kv_sw_v": "6 项软件著作权",
  "kv_ship": "发货", "kv_ship_v": "出口包装，发往全球客户",
  "make_h2": "产品与技术",
  "make_lede": "我们的核心是精准高效的电磁加热，加上自主编写的控制软件。既可以做成整机，也可以作为部件用于您的产品。",
  "a1_h": "电磁加热系统", "a1_p": "线圈、功率板和控制逻辑，加热快而均匀，长时间连续使用输出稳定。",
  "a2_h": "智能控制", "a2_p": "触摸屏和一键操作界面、条码和二维码扫描、物联网联网控制，以及背后的嵌入式固件。拥有 6 项软件著作权。",
  "a3_h": "商用烹饪设备", "a3_p": "面向便利店、餐厅和自助场景的台式设备，适合长时间营业，清洁方便。",
  "a4_h": "定制智能设备", "a4_p": "基于同一套加热和控制平台开发新品类，从概念到量产。",
  "eq_h2": "设备与耗材", "eq_lede": "我们产线上生产的两款设备，以及与之配套的电磁加热纸碗。",
  "alt_bowls": "一摞橙色图案纸碗，前面单独放着一只", "p3_h": "电磁加热专用纸碗", "p3_p": "煮和吃用同一只碗，容量 42 oz（1250 ml），不用洗锅。也适用于其他兼容的电磁煮面机。已按美国 FDA 21 CFR 175.300、欧盟 1935/2004 和 LFGB 完成食品接触检测。每箱 300 只。",
  "clients_h": "我们的设备正在这些地方使用",
  "alt_pro": "白色台式煮面机，带触摸屏和出水口，加热盘上放着一碗面",
  "p1_h": "商用电磁煮面机", "p1_p": "触摸屏、扫码和内置热水。用电磁加热直接在纸碗里煮面，适合门店和自助柜台。",
  "alt_studio": "小巧的白色煮面机，顶部是操作面板，侧面是蓝色水箱，加热盘上放着一碗面",
  "p2_h": "小型煮面机兼即热饮水机", "p2_p": "两用一体：电磁煮面机加即热饮水机，顶部一键操作。",
  "prod_h2": "生产现场", "prod_lede": "每台设备都由我们自己的团队装配、接线和测试，然后再包装出厂。",
  "g1": "装配线", "alt_g1": "工人坐在长条装配线两侧组装白色机身",
  "g2": "电磁加热模块装配", "alt_g2": "技术人员在功率板上安装电磁线圈和散热风扇",
  "g3": "接线与水路系统", "alt_g3": "技术人员在打开的机身内部连接线路和水管",
  "g4": "老化测试线", "alt_g4": "老化测试线上成排的整机，质检员手持记录板巡检",
  "oem_h2": "OEM 与 ODM 代工",
  "oem_lede": "您可以带着成熟的设计来生产，也可以带着想法来和我们一起开发。研发、认证支持和生产由同一个团队负责。",
  "s1_h": "需求", "s1_p": "您提供产品、目标市场和目标价位。",
  "s2_h": "研发", "s2_p": "我们设计或调整硬件、固件和外壳。",
  "s3_h": "样机", "s3_p": "提供可用样机，供您测试和反馈。",
  "s4_h": "认证", "s4_p": "按目标市场的要求准备产品和文件。",
  "s5_h": "量产", "s5_p": "在自有产线上完成装配、测试和出口包装。",
  "note_a": "起订量、交期和价格视项目而定。", "note_link": "告诉我们您的项目", "note_b": "，我们会给您方案。",
  "oem_subject": "OEM%2FODM%20%E5%92%A8%E8%AF%A2",
  "q_h2": "质量与合规", "q_lede": "我们是所生产设备的法定制造商，对销往每个市场的产品负责。",
  "alt_q": "技术人员对整机进行电气安规测试", "q_cap": "整机电气安规测试",
  "f2_h": "出厂前测试", "f2_p": "整机出厂前经过电气安规测试，并在老化测试线上运行后再包装。",
  "f3_h": "产品安全联系", "f3_p": "产品安全问题或市场监管问询，请发邮件至", "f3_end": "。",
  "c_h2": "联系我们", "c_lede": "告诉我们您想做的产品，或咨询我们的设备。",
  "c_email": "邮箱", "c_phone": "电话", "c_addr": "地址", "c_co": "公司",
  "phone": "400-637-6618", "phone_tel": "4006376618",
  "addr": "山东省青岛市即墨区大信镇陈家村188号1-005",
  "company": COMPANY_ZH,
 },
}

def build():
    page = open(os.path.join(HERE, "src_page.html"), encoding="utf-8").read()
    css = open(os.path.join(HERE, "src_style.css"), encoding="utf-8").read()
    for code, s in STRINGS.items():
        vals = dict(s, css=css.replace("{{root}}", s["root"]))
        out = re.sub(r"\{\{(\w+)\}\}", lambda m: vals[m.group(1)], page)
        out = out.replace("{{root}}", s["root"])
        left = re.findall(r"\{\{\w+\}\}", out)
        assert not left, left
        path = os.path.join(HERE, "index.html" if code == "en" else "zh/index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(out)
        print("wrote", path)

if __name__ == "__main__":
    build()
