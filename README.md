# 合租订阅指南

[阅读网站：Netflix奈飞、Spotify、Disney+、YouTube合租拼车指南](https://hezu-guide-netflix.github.io/subscription-guide/)

无需构建工具的静态资料站，覆盖Netflix奈飞、Spotify、Disney+、YouTube会员的合租拼车、账号交付、家庭资格、地区条件及故障处理。规则引用官方资料，成本例子为教学假设，不代售商品或受理商家订单与售后。

## 按问题阅读

- [共享、独享与额外成员有什么区别？](https://hezu-guide-netflix.github.io/subscription-guide/rules.html)
- [Netflix电视无法播放，怎样排查？](https://hezu-guide-netflix.github.io/subscription-guide/tv-playback.html)
- [高级套餐为什么看不到4K？](https://hezu-guide-netflix.github.io/subscription-guide/netflix-4k.html)
- [26天月卡与年卡费用怎样比较？](https://hezu-guide-netflix.github.io/subscription-guide/subscription-cost.html)
- [购买前六项核对清单](https://hezu-guide-netflix.github.io/subscription-guide/checklist.html)
- [浏览全部专题](https://hezu-guide-netflix.github.io/subscription-guide/guides.html)

## 页面与维护

首页是单栏会员入门指南，含官方开通步骤、套餐功能对照及常见问题；guides.html保留专题目录；ihezu.html是商品说明核对示例；about.html说明来源与责任范围。详细步骤分别放在对应专题，避免首页重复铺陈。正文直接包含在HTML中，没有构建和前端依赖。

本地预览：`python -m http.server 8000`。GitHub Pages使用main分支根目录发布。

发布前运行：

```sh
python scripts/check_site.py
git diff --check
```

检查桌面、手机布局；表格可在自身容器横向滚动。样式更新时统一更换CSS版本；正文实际修改时更新对应的结构化数据日期与站点地图lastmod，不为显得“新”而每天改日期。

## 平台信息

首页记录当前入口及条件，优惠以结算页为准，本站未测试结算效果。

- 奈飞小铺：入口已移除跳转，灰显并标记“平台有风险”，不再展示优惠。
- 环球巴士：`http://cn.goingbus.com?s=326BOCN3JD`，代码`mr23hey`，限新注册且未下过订单的用户。
- 银河录像局：`https://nf.video/8fDZl`，邀请码`8fDZl`，限新注册且未下过订单的用户，优惠以结算页为准。

外链只列在首页，HTML保留适当的链接属性。资料页不写催促购买、推荐排名、安全背书或未经验证的体验。

## 搜索上线

九页均有唯一标题摘要、自引用canonical、Open Graph、WebPage/WebSite标记；子页含可见面包屑和对应JSON-LD。站点地图列出九个规范URL，专题可从首页、导航和目录到达。

Search Console的网址前缀资源已验证；九页站点地图已提交，但Google仍报告无法抓取，详见[SEO上线与维护](docs/SEO_OPERATIONS.md)。首页及三个专题页已确认收录，其余页面需继续核查。收录不代表排名提升。

## 本地实用工具

`subscription-cost.html#calculator`提供双方案费用计算器，价格、天数、支付比例与附加费用只在浏览器内计算，无服务器传输。JavaScript禁用时保留静态公式和算例。计算逻辑检查：`node scripts/test_calculator.cjs`。

`tv-playback.html#quick`按屏幕现象跳转至步骤；`netflix-4k.html#check`提供本次检查可勾选的五项清单，勾选不代表系统验证成功，也不保存到服务器。
