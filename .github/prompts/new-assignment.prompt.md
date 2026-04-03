---
agent: agent
description: 创建新的编程作业
argument-hint: 提供作业详情
---

# 创建新的编程作业

你的目标是为 Mergington 高中的学生生成一个新的作业。

## 第 1 步：收集作业信息

如果用户尚未提供，询问作业的主题、目标受众、预计难度和截止日期等信息。

## 第 2 步：创建作业结构

1. 在 `assignments` 文件夹中基于作业主题创建一个唯一名称的新目录。
2. 在该目录中创建一个名为 `README.md` 的文件，使用 [assignment-template.md](../../templates/assignment-template.md) 中的结构。
3. 在 `README.md` 中填写作业详细信息（标题、目标、任务、要求等）。
4. （可选）如作业需要，添加入门代码或附件文件，并将这些文件放入同一作业文件夹中。

## 第 3 步：更新网站配置

将新作业添加到网站配置文件 [config.json](../../config.json) 的作业列表中。对于 `dueDate` 字段，若未另行指定，则使用当前日期加 7 天作为默认截止日期。