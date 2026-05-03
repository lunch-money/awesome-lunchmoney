# Awesome Lunch Money 
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Discord](https://img.shields.io/discord/842337014556262411?label=Discord&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://lunchmoney.app/discord)


A curated list of [Lunch Money Developer](https://lunchmoney.dev) resources and generally cool apps, inspired by [awesome-go](https://github.com/avelino/awesome-go) and [awesome-python](https://github.com/vinta/awesome-python). This collection is primarily for open source applications, but also includes some well-loved closed source resources.

### Contributing

Please take a quick gander at the [Contribution guidelines](./contributing.md) first. Thanks to all contributors; you are awesome!

If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. If you have created an awesome tool for Lunch Money that isn't on here, please submit a pull request to add it. Thank you!

> **Note:** The catalog below is generated from [`data/tools.yml`](./data/tools.yml). To add or update a tool, edit that file — not the README directly.

### Contents

DISCLAIMER: The projects listed here are built and maintained by members of the Lunch Money community. Lunchbag Labs does not make any commitments about the resources listed in this document, nor the accuracy of the third party resources and any content accessible via the links below.

- [Client SDKs & API Wrappers](#client-sdks--api-wrappers)
  - [V2 API](#v2-api)
  - [V1 API](#v1-api)
- [Open Source Mobile Apps](#open-source-mobile-apps)
- [Transaction Import Tools](#transaction-import-tools)
  - [Bookmarklets](#bookmarklets)
- [Transaction Update Tools](#transaction-update-tools)
- [Notifications, Widgets & Bots](#notifications-widgets--bots)
- [Asset Value & Balance Tools](#asset-value--balance-tools)
- [Visualization Tools](#visualization-tools)
- [Extensions & Keyboard Shortcuts](#extensions--keyboard-shortcuts)
- [MCP Servers](#mcp-servers)
- [Other Notable Tools](#other-notable-tools)

<!-- GENERATED:CATALOG:START -->
## MCP Servers

Connect AI assistants like Claude to your Lunch Money data using the Model Context Protocol. Chat with AI about your spending and budget habits. [Join the AI Tools channel on Discord](https://discord.com/channels/842337014556262411/1425305869813547030).

* [lunchmoney-mcp-server](https://github.com/leafeye/lunchmoney-mcp-v2) - A Model Context Protocol server that connects Claude Desktop to your Lunch Money data. Now based on the v2 API. - (by Levi Pols)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-05-01-community-newsletter)
* [lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp) - A Model Context Protocol server that covers 100% of the Lunch Money API functionality with easy install and logging. - (by akutishevsky)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-10-09-community-newsletter)
* [lunchmoney-mcp-v2](https://github.com/ConnorDBurge/lunchmoney-mcp-v2) - MCP server built on the official Lunch Money v2 SDK. - (by Conner Burge)

## Client SDKs & API Wrappers

Official and community-built libraries to interact with the Lunch Money API in your language of choice. Looking to generate your own? Install the [Lunch Money v2 OpenAPI Spec](https://www.npmjs.com/package/@lunch-money/v2-api-spec).

### V2 API

* [Lunch Money JavaScript SDK](https://github.com/lunch-money/lunch-money-js-v2) - Official JS SDK from the Lunch Money team with full TypeScript support. - (by Lunch Money)
  * [NPM](https://www.npmjs.com/package/@lunch-money/lunch-money-js-v2)
* [lunchmoney-clients](https://github.com/juftin/lunchmoney-clients) - A framework for generating language specific SDKs for the Lunch Money API. Includes a generated Python SDK for the v2 API by Justin Flannery, author of the popular lunchable client. - (by Justin Flannery)

### V1 API

A quick note: V1 is still fully supported, but we recommend the [V2 API](https://lunchmoney.dev) for new projects — it's where all new features and improvements are happening.

* [lunchmoney_dart](https://github.com/V3ntus/lunchmoney_dart) - A Lunch Money API wrapper written in Dart, perfect for building Flutter apps. - (by Ventus)
* [lunchmoney (Go)](https://github.com/icco/lunchmoney) - Golang API wrapper for the Lunch Money API. - (by Nat Welch)
* [lunch-money-js](https://github.com/lunch-money/lunch-money-js) - JavaScript client for the Lunch Money API with TypeScript type definitions available via NPM. - (by Lunch Money)
* [lunchmoney (Kotlin)](https://github.com/smaugfm/lunchmoney) - Non-blocking JVM client for the Lunch Money developer API, built for Java and Kotlin developers. - (by Dmytro Marchuk)
* [lunchable](https://github.com/juftin/lunchable) - Full-featured Python client for the Lunch Money Developer API. - (by Justin Flannery)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-02-28-community-newsletter)
* [lunchmoney (Ruby)](https://github.com/mmenanno/lunchmoney) - A Ruby gem API client library for the Lunch Money API. - (by Michael Menanno)

## Open Source Mobile Apps

Access and manage your Lunch Money data on the go with these open source mobile apps. Or try [the official Lunch Money Mobile App](https://lunchmoney.app/download).

* [BBudget](https://github.com/cleansoftlv/bbudget) - A fast, mobile-first companion web app. Provides simple UI for manual transaction input and review, perfect for less advanced users. - (by Alex Shakhov)
  * [Try it](https://www.bbudget.com)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-06-30-community-newsletter)
* [Lunch Money Companion](https://github.com/Rodrigolmti/lunch_money_companion) - A companion Android application for Lunch Money, available on the Google Play Store. - (by Rodrigo Lopes)
  * [Google Play](https://play.google.com/store/apps/details?id=com.rodrigolmti.lunch.money.companion)
  * [Discord](https://discord.com/channels/842337014556262411/1257168913968529478)
  * [Spotlight Blog](https://lunchmoney.app/blog/community-spotlight-android-companion-app)
* [Bento Cash](https://github.com/chintans1/bento-cash) - An iOS application for Lunch Money with support for importing transactions via SimpleFin. - (by Chintan Shah)
  * [Request TestFlight](https://discord.com/channels/842337014556262411/1248167168877662348)
* [Lunch Money Shortcuts](https://github.com/patrontheo/Lunch-Money-Shortcuts) - iOS Shortcuts to import transactions and interact with Lunch Money from your iPhone. - (by Theo Patron)
* [LunchSync](https://github.com/milanave/LunchSync) - Sync Apple Card and Apple Cash transactions to Lunch Money. Available on TestFlight. - (by LittleBlueBug)
  * [TestFlight](https://testflight.apple.com/join/mF8JEHqk)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-03-31-community-newsletter)
  * [Discord](https://discord.com/channels/842337014556262411/1423505146029019257)
* [lunch-buddy](https://github.com/astiskala/lunch-buddy) - Track your Lunch Money budget progress at a glance with this Progressive Web App. - (by Adam Stiskala)
  * [Try it](https://lunch-buddy.app/)
  * [Spotlight Blog](https://lunchmoney.app/blog/2026-02-10-community-newsletter)
  * [Discord](https://discord.com/channels/842337014556262411/1470488793391038485)

## Transaction Import Tools

Import transactions from banks and services that aren't natively supported by Lunch Money.

* [RBC-LunchMoney](https://github.com/MykalMachon/RBC-LunchMoney) - Import RBC (Royal Bank of Canada) transactions into Lunch Money. - (by Mykal Machon)
* [lunchmoney-fintoc-sync](https://github.com/agucova/lunchmoney-fintoc-sync) - Rust CLI to sync Fintoc-aggregated transactions with Lunch Money, designed for the Chilean bank system. - (by Agustín Covarrubias)
* [lunchable-splitlunch](https://github.com/juftin/lunchable-splitlunch) - Import transactions from Splitwise into Lunch Money seamlessly. - (by Justin Flannery)
  * [Spotlight Blog](https://lunchmoney.app/blog/2026-01-12-community-newsletter)
* [td-lunchmoney-importer](https://github.com/thehedgefrog/td-lunchmoney-importer) - Import a TD Bank QFX multi-account file directly to Lunch Money. - (by Max)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-03-31-community-newsletter)
* [LunchSync](https://github.com/milanave/LunchSync) - Sync Apple Card and Apple Cash transactions to Lunch Money. Available on TestFlight. - (by LittleBlueBug)
  * [TestFlight](https://testflight.apple.com/join/mF8JEHqk)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-03-31-community-newsletter)
  * [Discord](https://discord.com/channels/842337014556262411/1423505146029019257)
* [lunchsimple](https://sr.ht/~colbyhub/lunchsimple/) - Import Wealthsimple activity into your Lunch Money budgets. - (by Colby Hubscher)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-02-28-community-newsletter)
  * [Discord](https://discord.com/channels/842337014556262411/1344360183597629460)
* [LunchSync SG](https://github.com/shyamsundar2007/lunchsync-sg) - Sync bank transactions from Singapore banks to Lunch Money. - (by Shyam)
* [assorted-to-lunchmoney](https://github.com/n3v3rf411/assorted-to-lunchmoney) - Import transactions from Japanese banks via Money Forward. - (by Willie Loyd Tandingan)

### Bookmarklets

Browser bookmarks that run JavaScript to import transactions after logging in to your bank's website. Don't see your bank? [Join the Bookmarklets channel](https://discord.com/channels/842337014556262411/1480708918391996588) on Discord.

* [ICS Credit Card → Lunch Money](https://getbookmarklets.com/scripts/add?source_url=https%3A%2F%2Fraw.githubusercontent.com%2FH1D%2Fics_lunchmoney_sync%2Fmain%2Fbookmarklet%2Fsrc%2Fbookmarklet.js) - Import ICS (Netherlands) credit card transactions directly to Lunch Money. - (by Artem S)
  * [Spotlight Blog](https://lunchmoney.app/blog/2026-03-10-community-newsletter)
* [CFNA Credit Card → Lunch Money](https://github.com/jpjpjp/cfna-to-lunchmoney) - Import CFNA (Firestone-branded credit card) transactions to Lunch Money. - (by JP@LunchMoney.app)
  * [Spotlight Blog](https://lunchmoney.app/blog/2026-03-10-community-newsletter)

## Transaction Update Tools

Automatically categorize, enrich, and manage your existing Lunch Money transactions.

* [lunchmoney-amazon](https://github.com/iloveitaly/lunchmoney-amazon) - Categorize and add order numbers to Amazon transactions in Lunch Money. - (by Michael Bianco)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-05-01-community-newsletter)
* [lunchable-primelunch](https://github.com/juftin/lunchable-primelunch) - Amazon transaction updater for Lunch Money, built in Python. - (by Justin Flannery)
  * [Spotlight Blog](https://lunchmoney.app/blog/2026-01-12-community-newsletter)
* [email-to-lunch-money](https://github.com/evanpurkhiser/email-to-lunchmoney/) - Track email receipts for Amazon, Lyft and others to update Lunch Money transactions. - (by Evan)
  * [Spotlight Blog](https://lunchmoney.app/blog/2026-04-14-community-newsletter)

## Notifiers & Bots

* [LunchMoneyBudgetNotifier](https://github.com/jameshansen/LunchMoneyBudgetNotifier) - Retrieve current credit card balances and send push notifications on balance changes. - (by James Hansen)
* [lonchera](https://github.com/casidiablo/lonchera) - A Telegram bot that notifies users of new transactions with tools to view and manage budgets. Includes optional AI-powered transaction categorization. - (by Cristian Knur)
  * [Spotlight Blog](https://lunchmoney.app/blog/2024-11-29-community-newsletter)
  * [Discord](https://discord.com/channels/842337014556262411/1311765488140816484)

## Asset Value & Balance Tools

* [lunchmoney-t212](https://github.com/alinalihassan/lunchmoney-t212) - Synchronize Trading212 investment values with Lunch Money automatically. - (by Alin Ali Hassan)
* [lunchmoney-assets](https://github.com/iloveitaly/lunchmoney-assets) - Update real estate and car values in Lunch Money with current market data. - (by Michael Bianco)

## Visualization Tools

* [lunch-sankey](https://github.com/aneeshd16/lunch-sankey) - Generate beautiful Sankey diagrams from your Lunch Money transactions. - (by Aneesh Devasthale)
  * [Try it](https://lunch-sankey.vercel.app/)
  * [Spotlight Blog](https://lunchmoney.app/blog/2024-12-27-community-newsletter)
* [TRMNL Plugin](https://github.com/usetrmnl/plugins/tree/master) - Lunch Money plugin for TRMNL, an e-ink dashboard. See your budget on a beautiful ambient display. - (by Ryan Kulp)
  * [Docs](https://help.usetrmnl.com/en/articles/9613508-lunch-money)
  * [Spotlight Blog](https://lunchmoney.app/blog/community-spotlight-trmnl)
* [lunchtui](https://github.com/Rshep3087/lunchtui) - A beautiful command-line interface for managing your Lunch Money data right from the terminal. - (by Ryan Sheppard)
  * [Spotlight Blog](https://lunchmoney.app/blog/2025-06-30-community-newsletter)
* [Kids Companion App](https://github.com/H1D/lunch-money-kids-companion) - Help kids learn to be better savers with this companion app for Lunch Money.
  * [Try it](https://lunch-money-kids.netlify.app/)
  * [Spotlight Blog](https://lunchmoney.app/blog/2026-03-10-community-newsletter)
  * [Discord](https://discord.com/channels/842337014556262411/1480708810443329666)

## Extensions & Keyboard Shortcuts

* [MoneyMover](https://github.com/adamtaylor13/moneymover) - A Chrome extension that gives superpowers to Lunch Money with keyboard shortcuts and productivity features. - (by Adam Taylor)
  * [Spotlight Blog](https://lunchmoney.app/blog/community-spotlight-toronto-recap-money-mover)
* [Toolkit for Lunch Money](https://github.com/tj-tee/toolkit-for-lunch-money) - A Chrome extension that enhances the Lunch Money web app. Currently facilitates splitting transactions by auto-populating amounts. - (by tj-tee)
* [Lunch Money Raycast Extension](https://www.raycast.com/oppenheimer/lunchmoney) - An open source extension for Raycast to quickly access your Lunch Money data. - (by Maxime Cattet & Zeb Pykosz)

## Other Notable Tools

These projects aren't open source, but many Lunch Money users find them helpful.

* [LunchFlow](https://www.lunchflow.app/) - Effortlessly connect your EU and UK bank accounts to Lunch Money. Subscription-based service for automatic transaction imports. - (by Amr Awad)
  * [Spotlight Blog](https://lunchmoney.app/blog/2024-12-27-community-newsletter)
  * [Discord](https://discord.com/channels/842337014556262411/1283135769933905971)
* [Lunch Money × ProjectionLab](https://chromewebstore.google.com/detail/lunch-money-to-projection/olmhamhfelfcccahmjkolgompiaijkhd) - Chrome extension to import your account balances from Lunch Money into ProjectionLab for retirement planning. - (by Lunch Money)
  * [Spotlight Blog](https://lunchmoney.app/blog/2026-01-12-community-newsletter)
* [Lunch Money × Zapier](https://zapier.com/apps/lunch-money/integrations) - Connect Lunch Money to 8,000+ apps without writing any code. Automate transaction workflows using triggers and actions across transactions, categories, tags, accounts, budgets, and recurring items. - (by Lunch Money)
  * [Spotlight Blog](https://lunchmoney.app/blog/lunch-money-is-now-on-zapier)
<!-- GENERATED:CATALOG:END -->
