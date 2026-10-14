# 合租订阅指南

[阅读网站：Netflix订阅与账号使用指南](https://hezu-guide-netflix.github.io/subscription-guide/)

无需构建工具的静态资料站，解释账号区别、观看条件、订阅费用和核对方法。规则引用官方资料，成本例子为教学假设，不代售商品或受理商家订单与售后。

## 按问题阅读

- [共享、独享与额外成员有什么区别？](https://hezu-guide-netflix.github.io/subscription-guide/rules.html)
- [Netflix电视无法播放，怎样排查？](https://hezu-guide-netflix.github.io/subscription-guide/tv-playback.html)
- [高级套餐为什么看不到4K？](https://hezu-guide-netflix.github.io/subscription-guide/netflix-4k.html)
- [26天月卡与年卡费用怎样比较？](https://hezu-guide-netflix.github.io/subscription-guide/subscription-cost.html)
- [购买前六项核对清单](https://hezu-guide-netflix.github.io/subscription-guide/checklist.html)
- [浏览全部专题](https://hezu-guide-netflix.github.io/subscription-guide/guides.html)

## 页面与维护

首页为总览；guides.html为专题目录；ihezu.html是商品说明核对示例；about.html说明来源与责任范围。其余专题按文件名对应独立问题。正文直接包含在HTML中，没有构建和前端依赖。

本地预览：`python -m http.server 8000`。GitHub Pages使用main分支根目录发布。

发布前运行：

```sh
python scripts/check_site.py
git diff --check
```

检查桌面、手机布局；表格可在自身容器横向滚动。样式更新时统一更换CSS版本，正文实际修改时更新对应lastmod和内容核对日期。

## 平台信息

首页保留三个平台按钮，只显示平台名称。mr23hey为记录信息，当前优惠与条件以结算页为准，本站未测试结算效果。

- 奈飞小铺：`https://ihezu.zone/cM5eHW`，标称9折。
- 环球巴士：`https://cn.goingbus.com/?s=326BOCN3JD`，限新注册且未下过订单的用户，折扣以结算页为准。
- 银河录像局：`https://nf.video/5cy27`，标称95折，限新注册且未下过订单的用户。

外链只列在首页，HTML保留适当的链接属性。资料页不写催促购买、推荐排名、安全背书或未经验证的体验。

## 搜索上线

九页均有唯一标题摘要、自引用canonical、Open Graph、WebPage/WebSite标记；子页含可见面包屑和对应JSON-LD。站点地图列出九个规范URL，专题可从首页、导航和目录到达。

还需使用真实Google账号完成Search Console验证和站点地图提交，见[SEO上线与维护](docs/SEO_OPERATIONS.md)。没有账号验证或数据时，不宣称已收录、已提交或排名已提升。
