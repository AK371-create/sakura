# Google Search Console セットアップ手順

## 1. プロパティ追加

1. https://search.google.com/search-console にアクセス
2. **「プロパティを追加」** をクリック
3. **ドメインプロパティ** を選択 (推奨。`http://` `https://` 両方カバー)
4. `sakuraballpark.com` を入力 → 続行

## 2. DNS TXT レコードで認証 (推奨)

ドメインプロパティの場合、Google が TXT レコード値を表示します:

```
google-site-verification=abcdef1234567890...
```

CloudflareダッシュボードでDNSレコード追加:
- Type: `TXT`
- Name: `@` (apex)
- Content: `google-site-verification=...` (Googleが提示する値そのまま)
- Proxy status: DNS only (TXTは proxy 不可)

数分後、Search Console で「確認」をクリック。

## 3. (代替案) HTMLメタタグで認証

URLプレフィックスプロパティ(https://sakuraballpark.com/) を選んだ場合:

1. Google が `<meta name="google-site-verification" content="xxx" />` の値 `xxx` を表示
2. Cloudflare Pages のプロジェクト設定 → Environment variables に追加:
   ```
   PUBLIC_GOOGLE_SITE_VERIFICATION = xxx
   ```
3. 再デプロイ → `<head>` に自動的にメタタグが入る (`Layout.astro` の条件分岐)
4. Search Console で「確認」

## 4. Sitemap 提出

確認完了後:
1. Search Console 左メニュー → **「サイトマップ」**
2. 「新しいサイトマップの追加」に `sitemap-index.xml` を入力 → 送信
3. ステータスが「成功しました」になるか確認 (通常数分〜1日)

## 5. 確認: インデックス進捗

- 「カバレッジ」レポート: インデックス済み/未対象/エラーを集計
- 「URL検査」: 個別URLでインデックス状況確認

## 6. (推奨) Bing Webmaster Tools も同時設定

`https://www.bing.com/webmasters` で同じ流れ。
- 同じ TXT レコードでマルチ認証可能 (BingMate)
- または `PUBLIC_BING_SITE_VERIFICATION` 環境変数で `<meta name="msvalidate.01">` が入る

## 注意

- **インデックス反映**: 新サイトはGoogleのクロールに数日〜数週間かかる場合あり
- **構造化データ**: Search Console の「拡張」レポートで Article/BreadcrumbList の検出を確認
- **Core Web Vitals**: 「ウェブに関する主な指標」レポートで LCP/CLS を継続監視
