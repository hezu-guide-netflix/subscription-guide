# Google 搜索上线与维护

更新：2026-10-14。本文是站点维护记录，不承诺排名。代码优化已在仓库实现；Search Console状态以用户账号中的实际结果为准。

## 页面主题

| 页面 | 解决的问题 |
| --- | --- |
| 首页 | Netflix会员怎么买，官方订阅、共享和独享如何比较 |
| guides.html | 按账号、设备、画质和费用问题寻找资料 |
| rules.html | 共享个人资料、独享账号与额外成员区别 |
| tv-playback.html | 电视无法播放，按提示选择排查步骤 |
| netflix-4k.html | 高级套餐画质模糊，核对4K条件 |
| subscription-cost.html | 月卡26天与30天、年卡及优惠计算 |
| checklist.html | 购买前核对什么、怎样问客服 |
| ihezu.html | 阅读奈飞小铺商品说明 |
| about.html | 来源、编辑方式与商品责任范围 |

这是内容定位，未经搜索量工具测量，不代表流量或排名预测。保留原有URL，避免无必要迁移。

## 添加 Search Console

1. 用自己的Google账号打开[Search Console](https://search.google.com/search-console)。
2. 添加“网址前缀”资源，填写 `https://hezu-guide-netflix.github.io/subscription-guide/`，包括协议、路径和末尾斜杠。不要选需要DNS验证的“网域”资源；本站没有github.io的DNS管理权。
3. 选择“HTML标签”，复制Google提供的完整google-site-verification标签。此值必须来自当前账号，不能填示例值。
4. 将真实标签加入首页index.html的head中，提交并推送。等待部署完成，确认线上首页源码存在相同标签，再点击“验证”。保留有效验证标签。
5. 验证后，在“站点地图”提交 `https://hezu-guide-netflix.github.io/subscription-guide/sitemap.xml`；若输入框已显示本站前缀，仅填写sitemap.xml。
6. 用“网址检查”检查首页及三个新专题。检查实际索引状态、Google选择的规范网址和实时测试结果；符合条件时请求编入索引。请求不保证收录或排名，不必反复提交。

2026-10-14 已通过HTML标签完成所有权验证，并提交站点地图。最新处理情况见文末记录。

## robots.txt路径限制

站点在 `/subscription-guide/` 子路径。Google读取 `https://hezu-guide-netflix.github.io/robots.txt`；本项目的子路径robots.txt不能控制整个主机抓取。

根目录robots.txt目前404，不等于禁止抓取。当前通过已验证的Search Console提交站点地图更直接，无需为开放抓取另建仓库。以后使用自有域名或已有用户主页仓库时，再将robots.txt放到主机根目录，同步核对canonical与站点地图。

## 发布前检查

```sh
python scripts/check_site.py
git diff --check
```

工具检查HTML结构、唯一标题摘要、canonical、JSON-LD、内部链接与锚点、站点地图以及平台按钮和优惠码保留；不预测收录或排名。

部署后核对HTTP状态、新内容和CSS版本。通过[富媒体结果测试](https://search.google.com/test/rich-results)查看面包屑；WebPage和WebSite标记不保证特定搜索样式。没有加入虚假评分、商品价格或FAQ富媒体承诺。

用[PageSpeed Insights](https://pagespeed.web.dev/)查看移动性能。本站为静态HTML和本地CSS，正文无需JavaScript，不加载外部字体或广告脚本；这些是实现特征，不等于已取得特定性能分数。

## 有数据后怎样优化

| 情况 | 先检查 | 下一步 |
| --- | --- | --- |
| 未收录 | 页面索引报告与网址检查原因 | 按原因处理返回状态、canonical、内容与链接 |
| 已收录但无曝光 | 查询、国家、页面与时间范围 | 明确真实问题、补充缺失答案，不批量生成相似文章 |
| 有曝光但点击少 | 查询与标题是否匹配、平均排名 | 优化与正文一致的标题摘要，避免夸大 |
| 有点击但答案难找 | 问题与答案顺序 | 直接答案放前面，补充例子和操作步骤 |

比较同样长度的时间段，如最近28天与前28天；数据少时延长观察。分别看索引页数、曝光、点击、点击率和各查询平均排名。平均排名受查询、国家和设备影响，不代表所有用户的位置。

lastmod只在正文实际修改时更新，不每天改日期。专题保持独立答案，首页负责总览；补充来源和真实观察，不虚构作者经验、实测或评价。站外发现可从仓库README与相关主题的真实引用开始，不购买链接、不群发留言。向社区发帖或联系他人需要用户明确授权。

## 官方依据

- [Google SEO入门](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [面向读者的内容](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [验证所有权](https://support.google.com/webmasters/answer/9008080)
- [提交站点地图](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [请求重新抓取](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)
- [面包屑标记](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)


## 本次发布验证结果（2026-10-14）

- 9个线上页面及sitemap均返回200，最新版标题、JSON-LD、样式引用和九页站点地图已确认。
- 手机390px宽度下九页均无整页横向溢出；首页三个入口仍为白字按钮，名称和新用户限制已验证。
- 移动端PageSpeed复测：性能99，无障碍100，最佳做法100，基础SEO100；LCP约0.9秒，TBT为0，CLS为0。这是一次实验室测量，不是搜索排名，也没有真实用户核心网页指标数据。
- [Google PageSpeed报告](https://pagespeed.web.dev/analysis/https-hezu-guide-netflix-github-io-subscription-guide/c11i7nud4i?form_factor=mobile)
- 最初未登录时无法完成Google富媒体测试和Search Console验证；用户随后登录，后续结果见下方记录。

## Search Console执行记录（2026-10-14）

- 已通过HTML标签验证本站网址前缀资源。标签已发布到首页，维护时保留。
- Google实时测试首页：允许编入索引；首页及tv-playback.html、netflix-4k.html、subscription-cost.html的收录请求均显示已加入优先抓取队列。请求不是已收录的证明；检查时这四页均尚未收录。
- tv-playback.html已通过Google富媒体测试，检测到一项有效面包屑内容：[测试结果](https://search.google.com/test/rich-results/result?id=xZq0aSyMyKIM3Ku7pm3URQ)。
- sitemap.xml已提交，并在首次显示无法读取后重试一次；报告仍显示无法抓取、发现网页0。这不是成功读取的状态。
- 已排查：公开XML返回200且解析到9个网址；根目录robots.txt为404，没有发现阻止规则；Google对sitemap.xml的实时测试明确显示允许抓取、网页抓取成功；人工处置报告未检测到问题。因此暂未定位到应修改的代码或规则，不改变规范URL、不反复提交，也不将地图报告错误宣称为已解决。
- 下一步查看Google后续地图处理和页面索引结果。若持续无法读取，依据[Google站点地图排查指南](https://support.google.com/webmasters/answer/7451001)继续检查抓取详情。小站所有页面可由首页内链到达，已提交首页收录请求；地图报告错误不等于网页被禁止抓取。
