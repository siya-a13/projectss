---
title: Deep notes setup
tags:
---
Obsidian and Quartz are two different tools that can help you convert Markdown files into HTML and serve them as websites, but they operate in different ways and have distinct purposes.

### Obsedian

**Obsedian** is primarily a knowledge management and note-taking app that stores notes in Markdown format. While Obsidian itself does not directly serve HTML from Markdown files, you can use plugins and external tools to publish your Obsidian notes as a website.

### Quartz

**Quartz** is a different type of tool, specifically designed to convert Markdown files into a static site, typically using Jekyll or a similar static site generator.

For quartz setup and installation follow the [link](https://quartz.jzhao.xyz/)

Follow 👉 video for setup and publish the document [link](https://youtu.be/6s6DT1yN4dw)

### Commands
Below are the commands we use frequently for deploying the latest documents.

**Run application locally**

```
npx quartz build --serve
```

**Sync the document with GitHub pages**

```
npx quartz sync
```