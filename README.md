# 合租订阅指南

一个无需构建工具的静态网站。内容聚焦数字订阅合租购买前的判断。

## 页面

- `index.html`：Netflix 新手指南、账号术语、电视与4K条件、假设成本算例、客服问题模板和平台入口
- `checklist.html`：六项购买前核对清单
- `ihezu.html`：奈飞小铺购买前须知与商品入口
- `rules.html`：Netflix 官方共享规则摘要
- `about.html`：本站说明与信息来源

## 本地预览

在仓库根目录运行 `python3 -m http.server 8000`，打开 `http://localhost:8000/`。

## 发布与维护

目标地址为 `https://hezu-guide-netflix.github.io/subscription-guide/`。GitHub Pages 使用 `main` 分支根目录发布。

奈飞小铺商品入口目前为 `https://ihezu.zone/cM5eHW`，优惠码为 `mr23hey`，9折（优惠10%），适用商品及实际优惠以结算页为准。外链和优惠码只在 `index.html` 的平台信息示例中展示，统一标注推广关系；其他资料页仅通过站内链接引用。

环球巴士商品入口目前为 `https://cn.goingbus.com/?s=326BOCN3JD`，优惠码为 `mr23hey`，限新注册且未下过订单的用户，均位于 `index.html`。

平台政策或正文修改后，更新 `sitemap.xml` 的 `lastmod`。不要添加未经验证的价格、使用体验或收益承诺。

网站上线并不自动产生搜索流量。应在 GitHub Pages 生效后检查页面可用性，再通过搜索引擎站长工具提交站点地图，并观察搜索曝光和出站点击。

银河录像局商品入口为 `https://nf.video/5cy27`，优惠码为 `mr23hey`，95折（优惠5%），仅限新注册且未下过订单的用户。优惠条件根据用户提供的推广后台截图整理，结算页为准，位于 `index.html`。

文案原则：资料解释优先，不使用推荐排名、催促购买、商家背书或商品可用性承诺。优惠信息按来源记录，不写为本站验证过的优惠；不承诺受理商家的订单、交付、退款或售后。
