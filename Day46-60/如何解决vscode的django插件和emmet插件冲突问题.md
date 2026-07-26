Django 的模板文件（如 `.html`）和 VS Code 的 Emmet 插件在默认情况下**会产生冲突**。当你在 Django 模板中使用 `{% %}` 或 `{{ }}` 语法时，Emmet 可能会拦截或错误解析部分 HTML 属性与快捷键，导致无法正常弹出自动补全。 [[1](https://www.reddit.com/r/djangolearning/comments/nq47tc/help_wanted_vscodes_emmet_plugin_messing_up_my/?tl=zh-hant), [2](https://www.volcengine.com/article/1560529), [3](https://www.volcengine.com/article/1568896)]

解决冲突的方法

- **开启语言关联**：打开 VS Code 的 `settings.json` 设置，添加 `emmet.includeLanguages` 配置，把 Django 模板语言（如 `django-html`）和 `html` 关联起来。
- **修改配置文件**：在设置中加入 `"emmet.includeLanguages": {"django-html": "html"}`，让 Emmet 在编写 Django 页面时能正确识别标签