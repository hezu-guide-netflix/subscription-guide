"""Validate crawlable static pages, metadata, structured data and navigation."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://hezu-guide-netflix.github.io/subscription-guide/"
VOID = set("area base br col embed hr img input link meta param source track wbr".split())


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.stack, self.ids, self.links, self.meta, self.canonicals = [], [], [], {}, []
        self.counts = Counter()
        self.heading_levels = []
        self.feed(text)
        assert not self.stack, f"Unclosed tags: {self.stack}"

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.counts[tag] += 1
        if re.fullmatch(r"h[1-6]", tag):
            self.heading_levels.append(int(tag[1]))
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag in ("a", "link") and "href" in attrs:
            self.links.append(attrs["href"])
        if tag in ("img", "script") and "src" in attrs:
            self.links.append(attrs["src"])
        if tag == "meta":
            self.meta[attrs.get("name", attrs.get("property"))] = attrs.get("content", "")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f"Invalid nesting: {tag}, {self.stack}"
        self.stack.pop()


def main():
    pages, titles, descriptions, modified = {}, [], [], {}
    for path in sorted(ROOT.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        page = Page(text)
        assert page.counts["h1"] == 1, f"{path.name}: expected one H1"
        assert all(b <= a + 1 for a, b in zip(page.heading_levels, page.heading_levels[1:])), f"{path.name}: skipped heading level"
        assert len(page.ids) == len(set(page.ids)), f"{path.name}: duplicate IDs"
        title = re.search(r"<title>(.*?)</title>", text, re.S)
        assert title and title.group(1).strip(), f"{path.name}: missing title"
        page_title = title.group(1)
        titles.append(page_title)
        description = page.meta.get("description")
        assert description, f"{path.name}: missing description"
        descriptions.append(description)
        expected = BASE + ("" if path.name == "index.html" else path.name)
        assert page.canonicals == [expected], f"{path.name}: incorrect canonical"
        assert "noindex" not in page.meta.get("robots", "").lower(), f"{path.name}: noindex"
        assert page.meta.get("og:url") == expected, f"{path.name}: missing Open Graph URL"
        assert page.meta.get("og:title") == page.meta.get("twitter:title") == page_title, f"{path.name}: title metadata mismatch"
        assert page.meta.get("og:description") == page.meta.get("twitter:description") == description, f"{path.name}: description metadata mismatch"
        schemas = [json.loads(s) for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)]
        assert schemas, f"{path.name}: missing structured data"
        graph = schemas[0]["@graph"]
        matching = [x for x in graph if x.get("@type") in ("WebPage", "AboutPage", "CollectionPage") and x.get("url") == expected]
        assert len(matching) == 1, f"{path.name}: missing or duplicate page schema"
        schema_page = matching[0]
        assert schema_page.get("name") == page_title and schema_page.get("description") == description, f"{path.name}: page schema metadata mismatch"
        modified[expected] = schema_page.get("dateModified")
        if path.name != "index.html":
            crumb = next(x for x in graph if x.get("@type") == "BreadcrumbList")
            assert [x["position"] for x in crumb["itemListElement"]] == [1, 2]
            assert crumb["itemListElement"][-1]["item"] == expected
        assert not re.search("推广|佣金|返佣|分销", text), f"{path.name}: unwanted visible wording"
        pages[path.name] = page
    assert len(set(titles)) == len(titles), "Duplicate titles"
    assert len(set(descriptions)) == len(descriptions), "Duplicate descriptions"
    inbound = Counter()
    for name, page in pages.items():
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            relative = unquote(parsed.path)
            target = "index.html" if relative in (".", "./") else relative or name
            assert (ROOT / target).exists(), f"{name}: broken local link {link}"
            if parsed.fragment:
                assert target in pages and parsed.fragment in pages[target].ids, f"{name}: broken anchor {link}"
            if target in pages and target != name:
                inbound[target] += 1
    assert all(inbound[name] for name in pages), "Orphan page"
    entries = ET.parse(ROOT / "sitemap.xml").findall(".//{*}url")
    urls = {x.findtext("{*}loc") for x in entries}
    assert len(entries) == len(urls), "Duplicate sitemap URL"
    assert urls == {BASE + ("" if name == "index.html" else name) for name in pages}, "Sitemap does not match pages"
    if (ROOT / "sitemap.txt").exists():
        text_urls = (ROOT / "sitemap.txt").read_text(encoding="utf-8").splitlines()
        assert len(text_urls) == len(urls) and set(text_urls) == urls, "Text and XML sitemaps differ"
    for entry in entries:
        url, date = entry.findtext("{*}loc"), entry.findtext("{*}lastmod")
        assert date and re.fullmatch(r"\d{4}-\d{2}-\d{2}", date), "Invalid sitemap date"
        assert modified[url] == date, f"{url}: sitemap and page dates differ"
    homepage = (ROOT / "index.html").read_text(encoding="utf-8")
    assert len(re.findall(r'guide-platform-actions"><a class="button"', homepage)) == 3
    assert homepage.count('<code>mr23hey</code>') == 3
    labels = re.findall(r'guide-platform-actions"><a class="button"[^>]*>(.*?)</a>', homepage)
    assert labels == ["奈飞小铺", "环球巴士", "银河录像局"], "Incorrect platform button labels"
    assert homepage.count("限新注册且未下过订单的用户。") == 2, "Missing coupon eligibility"
    for url in ("ihezu.zone", "cn.goingbus.com", "nf.video"):
        link = re.search(r'<a[^>]+href="https://' + re.escape(url) + r'[^>]+>', homepage)
        assert link and 'sponsored noopener noreferrer' in link.group(0)
    print(f"PASS: {len(pages)} pages; unique metadata, canonical URLs, JSON-LD, sitemap, HTML nesting, links, anchors, and platform controls")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, KeyError, StopIteration) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
