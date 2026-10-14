# 合租订阅指南

一个无需构建工具的静态网站。内容聚焦数字订阅合租购买前的判断；推广入口使用站点所有者提供的专属链接。

## 页面

- `index.html`：首页与商家入口
- `checklist.html`：六项购买前核对清单
- `ihezu.html`：奈飞小铺购买前须知与推广入口
- `rules.html`：Netflix 官方共享规则摘要
- `about.html`：信息来源与推广披露

## 本地预览

在仓库根目录运行 `python3 -m http.server 8000`，打开 `http://localhost:8000/`。

## 发布与维护

目标地址为 `https://ppwjpp.github.io/subscription-guide/`。GitHub Pages 使用 `main` 分支根目录发布。

推广入口目前为 `https://ihezu.zone/cM5eHW`。更换链接时，请同步检查 `index.html`、`checklist.html` 与 `ihezu.html`。短链接在 2026-10-14 跳转至 `https://www.ihezu.cn/?sid=cM5eHW`。

平台政策或正文修改后，更新对应页面的最后核对日期，以及 `sitemap.xml` 的 `lastmod`。不要添加未经验证的价格、使用体验或收益承诺。

网站上线并不自动产生搜索流量或佣金。应在 GitHub Pages 生效后检查页面可用性，再通过搜索引擎站长工具提交站点地图，并观察搜索曝光、出站点击和商家后台成交数据。
